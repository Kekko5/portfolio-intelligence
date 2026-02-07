import pytest
from src.domain.metrics.ratios import sharpe_ratio, max_drawdown


class TestSharpeRatio:
    
    def test_positive_sharpe(self):
        """Rendimenti buoni con bassa volatilità = Sharpe alto"""
        returns = [0.10, 0.12, 0.08, 0.11, 0.09]  # Media ~10%
        result = sharpe_ratio(returns, risk_free_rate=0.02)
        assert result > 0
    
    def test_negative_sharpe(self):
        """Rendimenti sotto risk-free = Sharpe negativo"""
        returns = [0.01, 0.015, 0.005, 0.01, 0.02]  # Media ~1.2%
        result = sharpe_ratio(returns, risk_free_rate=0.05)
        assert result < 0
    
    def test_zero_risk_free(self):
        """Con risk-free=0, Sharpe = media/std_dev"""
        returns = [0.10, 0.10, 0.10, 0.10]  # Volatilità quasi zero
        # Con rendimenti identici, std_dev è 0 → divisione per zero
        # Usiamo rendimenti leggermente diversi
        returns = [0.08, 0.10, 0.12, 0.10]
        result = sharpe_ratio(returns, risk_free_rate=0.0)
        assert result > 0


class TestMaxDrawdown:
    
    def test_basic_drawdown(self):
        """Drawdown semplice: 100 → 120 → 90"""
        prices = [100, 120, 90]
        result = max_drawdown(prices)
        # Da 120 a 90 = -25%
        assert result == pytest.approx(-0.25, rel=1e-10)
    
    def test_drawdown_with_recovery(self):
        """Drawdown con recupero parziale"""
        prices = [100, 120, 90, 110, 85, 100]
        result = max_drawdown(prices)
        # Da 120 a 85 = -29.17%
        expected = (85 - 120) / 120
        assert result == pytest.approx(expected, rel=1e-10)
    
    def test_no_drawdown(self):
        """Prezzi sempre in crescita = drawdown 0"""
        prices = [100, 110, 120, 130, 140]
        result = max_drawdown(prices)
        assert result == 0.0
    
    def test_continuous_decline(self):
        """Declino continuo"""
        prices = [100, 90, 80, 70]
        result = max_drawdown(prices)
        # Da 100 a 70 = -30%
        assert result == pytest.approx(-0.30, rel=1e-10)