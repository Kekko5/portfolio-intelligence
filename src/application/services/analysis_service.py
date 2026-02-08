"""
Service per l'analisi del portafoglio.
"""
from dataclasses import dataclass
from datetime import datetime
from src.data.fetchers.yahoo_fetcher import YahooFetcher
from src.data.fetchers.ai_client import AIClient
from src.data.models.portfolio import Portfolio
from src.domain.analysis.portfolio_analyzer import PortfolioAnalyzer, AssetAnalysis
from config.prompts.financial_analyst import SYSTEM_PROMPT, format_portfolio_prompt


@dataclass
class AIInsight:
    """
    Insight generato dall'AI sul portafoglio.
    """
    summary: str
    full_analysis: str
    generated_at: datetime


@dataclass
class PortfolioReport:
    """
    Report completo dell'analisi di un portafoglio.
    """
    portfolio_name: str
    analysis_date: datetime
    period: str
    assets: dict[str, AssetAnalysis]
    portfolio_return: float
    portfolio_cagr: float
    portfolio_volatility: float
    ai_insight: AIInsight | None = None


class AnalysisService:
    """
    Service che coordina il fetch dei dati e l'analisi del portafoglio.
    """
    
    def __init__(
        self, 
        fetcher: YahooFetcher = None, 
        ai_client: AIClient = None,
        risk_free_rate: float = 0.02
    ):
        self.fetcher = fetcher or YahooFetcher()
        self.ai_client = ai_client
        self.analyzer = PortfolioAnalyzer(risk_free_rate)
    
    def analyze_portfolio(
        self, 
        portfolio: Portfolio, 
        period: str = "1y",
        include_ai_insight: bool = True
    ) -> PortfolioReport:
        """
        Analizza un portafoglio completo.
        """
        years = self._period_to_years(period)
        
        assets_data: dict[str, list[float]] = {}
        weights: dict[str, float] = {}
        
        for asset in portfolio.assets:
            price_data = self.fetcher.fetch_prices(asset.ticker, period)
            close_prices = [price.close for price in price_data]
            assets_data[asset.ticker] = close_prices
            weights[asset.ticker] = asset.weight
        
        result = self.analyzer.analyze_portfolio(assets_data, weights, years)
        
        report = PortfolioReport(
            portfolio_name=portfolio.name,
            analysis_date=datetime.now(),
            period=period,
            assets=result["assets"],
            portfolio_return=result["portfolio"]["total_return"],
            portfolio_cagr=result["portfolio"]["cagr"],
            portfolio_volatility=result["portfolio"]["volatility"],
        )
        
        if include_ai_insight:
            report.ai_insight = self._generate_ai_insight(report)
        
        return report
    
    def _generate_ai_insight(self, report: PortfolioReport) -> AIInsight | None:
        """Genera insight AI per il report."""
        if not self.ai_client:
            try:
                self.ai_client = AIClient()
            except ValueError:
                return None
        
        try:
            prompt = format_portfolio_prompt(report)
            analysis = self.ai_client.ask(prompt, system_prompt=SYSTEM_PROMPT)
            
            first_sentence = analysis.split('.')[0] + '.'
            
            return AIInsight(
                summary=first_sentence,
                full_analysis=analysis,
                generated_at=datetime.now()
            )
        except Exception:
            return None
    
    @staticmethod
    def _period_to_years(period: str) -> float:
        """Converte una stringa periodo in numero di anni."""
        period = period.lower().strip()
        
        if period.endswith("y"):
            return float(period[:-1])
        elif period.endswith("mo"):
            months = float(period[:-2])
            return months / 12.0
        else:
            raise ValueError(f"Formato periodo non riconosciuto: {period}")