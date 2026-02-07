import pytest
from src.data.models.asset import Asset
from src.data.models.portfolio import Portfolio
from src.application.services.analysis_service import AnalysisService, PortfolioReport


class TestAnalysisService:
    
    def test_period_to_years(self):
        """Test conversione periodo in anni"""
        assert AnalysisService._period_to_years("1y") == 1.0
        assert AnalysisService._period_to_years("2y") == 2.0
        assert AnalysisService._period_to_years("6mo") == 0.5
        assert AnalysisService._period_to_years("3mo") == 0.25
    
    def test_period_to_years_invalid(self):
        """Formato non valido solleva errore"""
        with pytest.raises(ValueError):
            AnalysisService._period_to_years("invalid")
    
    def test_analyze_portfolio_real_data(self):
        """Test con dati reali (richiede connessione internet)"""
        # Crea un portfolio semplice
        assets = [
            Asset(ticker="VWCE.MI", name="Vanguard All-World", asset_type="ETF", weight=0.6),
            Asset(ticker="AGGH.MI", name="iShares Global Aggregate Bond", asset_type="ETF", weight=0.4),
        ]
        portfolio = Portfolio(name="Test Portfolio", assets=assets)
        
        # Analizza
        service = AnalysisService()
        report = service.analyze_portfolio(portfolio, period="3mo")
        
        # Verifica struttura report
        assert isinstance(report, PortfolioReport)
        assert report.portfolio_name == "Test Portfolio"
        assert report.period == "3mo"
        assert len(report.assets) == 2
        assert "VWCE.MI" in report.assets
        assert "AGGH.MI" in report.assets
        
        # Verifica che le metriche siano numeri ragionevoli
        assert -1 < report.portfolio_return < 1  # Tra -100% e +100%
        assert -1 < report.portfolio_cagr < 1
        assert report.portfolio_volatility > 0