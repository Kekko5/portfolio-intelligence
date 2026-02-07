"""
Service per l'analisi del portafoglio.
"""
from dataclasses import dataclass
from datetime import datetime
from src.data.fetchers.yahoo_fetcher import YahooFetcher
from src.data.models.portfolio import Portfolio
from src.domain.analysis.portfolio_analyzer import PortfolioAnalyzer, AssetAnalysis


@dataclass
class PortfolioReport:
    """
    Report completo dell'analisi di un portafoglio.
    
    Attributes:
        portfolio_name: Nome del portafoglio
        analysis_date: Data dell'analisi
        period: Periodo analizzato
        assets: Analisi per ogni asset
        portfolio_return: Rendimento totale del portafoglio
        portfolio_cagr: CAGR del portafoglio
        portfolio_volatility: Volatilità del portafoglio
    """
    portfolio_name: str
    analysis_date: datetime
    period: str
    assets: dict[str, AssetAnalysis]
    portfolio_return: float
    portfolio_cagr: float
    portfolio_volatility: float


class AnalysisService:
    """
    Service che coordina il fetch dei dati e l'analisi del portafoglio.
    """
    
    def __init__(self, fetcher: YahooFetcher = None, risk_free_rate: float = 0.02):
        """
        Args:
            fetcher: Fetcher per i dati (default: YahooFetcher)
            risk_free_rate: Tasso risk-free per Sharpe ratio
        """
        self.fetcher = fetcher or YahooFetcher()
        self.analyzer = PortfolioAnalyzer(risk_free_rate)
    
    def analyze_portfolio(self, portfolio: Portfolio, period: str = "1y") -> PortfolioReport:
        """
        Analizza un portafoglio completo.
        
        Args:
            portfolio: Portfolio da analizzare
            period: Periodo di analisi (es. "1y", "2y", "5y")
        
        Returns:
            PortfolioReport con tutte le metriche
        """
        # 1. Converti period in years (es. "1y" → 1.0, "6mo" → 0.5)
        years = self._period_to_years(period)
        
        # 2. Per ogni asset, fetch prezzi e estrai i close
        assets_data: dict[str, list[float]] = {}
        weights: dict[str, float] = {}
        
        for asset in portfolio.assets:
            price_data = self.fetcher.fetch_prices(asset.ticker, period)
            close_prices = [price.close for price in price_data]
            assets_data[asset.ticker] = close_prices
            weights[asset.ticker] = asset.weight
        
        # 3. Analizza il portafoglio
        result = self.analyzer.analyze_portfolio(assets_data, weights, years)
        
        # 4. Crea e ritorna il report
        return PortfolioReport(
            portfolio_name=portfolio.name,
            analysis_date=datetime.now(),
            period=period,
            assets=result["assets"],
            portfolio_return=result["portfolio"]["total_return"],
            portfolio_cagr=result["portfolio"]["cagr"],
            portfolio_volatility=result["portfolio"]["volatility"],
        )
    
    @staticmethod
    def _period_to_years(period: str) -> float:
        """
        Converte una stringa periodo in numero di anni.
        
        Args:
            period: Stringa periodo (es. "1y", "6mo", "3mo")
        
        Returns:
            Numero di anni come float
        
        Raises:
            ValueError: Se il formato non è riconosciuto
        """
        period = period.lower().strip()
        
        if period.endswith("y"):
            return float(period[:-1])
        elif period.endswith("mo"):
            months = float(period[:-2])
            return months / 12.0
        else:
            raise ValueError(f"Formato periodo non riconosciuto: {period}")