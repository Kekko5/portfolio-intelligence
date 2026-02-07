"""
Analizzatore di portafoglio.
"""
from dataclasses import dataclass
from ..metrics.returns import returns_series, total_return, cagr
from ..metrics.volatility import std_dev, annualized_volatility
from ..metrics.ratios import sharpe_ratio, max_drawdown


@dataclass
class AssetAnalysis:
    """
    Risultato dell'analisi di un singolo asset.
    
    Attributes:
        ticker: Simbolo dell'asset
        total_return: Rendimento totale nel periodo
        cagr: Tasso di crescita annuo composto
        volatility: Volatilità annualizzata
        sharpe_ratio: Sharpe ratio
        max_drawdown: Massimo drawdown
    """
    ticker: str
    total_return: float
    cagr: float
    volatility: float
    sharpe_ratio: float
    max_drawdown: float


class PortfolioAnalyzer:
    """Analizza singoli asset e portafogli."""
    
    def __init__(self, risk_free_rate: float = 0.02):
        """
        Args:
            risk_free_rate: Tasso risk-free per Sharpe ratio (default 2%)
        """
        self.risk_free_rate = risk_free_rate
    
    def analyze_asset(self, ticker: str, prices: list[float], years: float) -> AssetAnalysis:
        """
        Analizza un singolo asset.
        
        Args:
            ticker: Simbolo dell'asset
            prices: Lista prezzi in ordine cronologico
            years: Numero di anni del periodo
        
        Returns:
            AssetAnalysis con tutte le metriche
        """
        # Calcola rendimenti giornalieri (riusati per volatility e sharpe)
        daily_returns = returns_series(prices)
        
        # Calcola le metriche
        total_ret = total_return(prices)
        cagr_val = cagr(prices[0], prices[-1], years)
        vol = annualized_volatility(daily_returns)
        sharpe = sharpe_ratio(daily_returns, self.risk_free_rate)
        max_dd = max_drawdown(prices)
        
        return AssetAnalysis(
            ticker=ticker,
            total_return=total_ret,
            cagr=cagr_val,
            volatility=vol,
            sharpe_ratio=sharpe,
            max_drawdown=max_dd
        )
    
    def analyze_portfolio(
        self, 
        assets_data: dict[str, list[float]], 
        weights: dict[str, float],
        years: float
    ) -> dict:
        """
        Analizza un portafoglio completo.
        
        Args:
            assets_data: Dict {ticker: lista_prezzi}
            weights: Dict {ticker: peso} (i pesi devono sommare a 1)
            years: Numero di anni del periodo
        
        Returns:
            Dict con analisi per asset e metriche aggregate del portafoglio
        """
        # 1. Analizza ogni singolo asset
        asset_analyses = {}
        for ticker, prices in assets_data.items():
            asset_analyses[ticker] = self.analyze_asset(ticker, prices, years)
        
        # 2. Calcola rendimento portafoglio (media pesata)
        portfolio_return = sum(
            asset_analyses[ticker].total_return * weights[ticker]
            for ticker in assets_data.keys()
        )
        
        # 3. Calcola CAGR portafoglio (media pesata)
        portfolio_cagr = sum(
            asset_analyses[ticker].cagr * weights[ticker]
            for ticker in assets_data.keys()
        )
        
        # 4. Calcola volatilità portafoglio (semplificata: media pesata)
        # Nota: la formula corretta richiederebbe le correlazioni
        portfolio_volatility = sum(
            asset_analyses[ticker].volatility * weights[ticker]
            for ticker in assets_data.keys()
        )
        
        return {
            "assets": asset_analyses,
            "portfolio": {
                "total_return": portfolio_return,
                "cagr": portfolio_cagr,
                "volatility": portfolio_volatility,
            }
        }