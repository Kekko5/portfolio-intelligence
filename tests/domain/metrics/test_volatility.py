import pytest
import math
from src.domain.metrics.volatility import variance, std_dev, annualized_volatility


class TestVariance:
    
    def test_basic_variance(self):
        """Varianza di [2, 4, 6] = 4"""
        values = [2, 4, 6]  # media = 4
        # (2-4)² + (4-4)² + (6-4)² = 4 + 0 + 4 = 8
        # 8 / (3-1) = 4
        result = variance(values)
        assert result == 4.0
    
    def test_zero_variance(self):
        """Valori uguali hanno varianza 0"""
        values = [5, 5, 5, 5]
        result = variance(values)
        assert result == 0.0
    
    def test_insufficient_values(self):
        """Meno di 2 valori solleva errore"""
        with pytest.raises(ValueError):
            variance([1])


class TestStdDev:
    
    def test_basic_std_dev(self):
        """Std dev di [2, 4, 6] = 2"""
        values = [2, 4, 6]
        result = std_dev(values)
        assert result == 2.0
    
    def test_compare_with_manual(self):
        """Confronto con calcolo manuale"""
        values = [10, 12, 14, 16, 18]  # media = 14
        # Differenze: -4, -2, 0, 2, 4
        # Quadrati: 16, 4, 0, 4, 16 = 40
        # Varianza: 40 / 4 = 10
        # Std dev: √10 ≈ 3.162
        result = std_dev(values)
        assert result == pytest.approx(math.sqrt(10), rel=1e-10)


class TestAnnualizedVolatility:
    
    def test_annualization(self):
        """Volatilità giornaliera × √252"""
        # Creiamo rendimenti con std_dev nota
        daily_returns = [0.01, -0.01, 0.01, -0.01, 0.01]
        daily_vol = std_dev(daily_returns)
        
        result = annualized_volatility(daily_returns)
        expected = daily_vol * math.sqrt(252)
        
        assert result == pytest.approx(expected, rel=1e-10)
    
    def test_custom_trading_days(self):
        """Test con numero custom di trading days"""
        daily_returns = [0.01, -0.01, 0.02, -0.02]
        
        result_252 = annualized_volatility(daily_returns, 252)
        result_365 = annualized_volatility(daily_returns, 365)
        
        # Con più giorni, volatilità annualizzata maggiore
        assert result_365 > result_252