import pytest
import math
from src.domain.metrics.returns import simple_return, log_return, returns_series
from src.domain.metrics.returns import simple_return, log_return, returns_series, total_return, cagr


class TestSimpleReturn:
    
    def test_positive_return(self):
        """Da 100 a 110 = +10%"""
        result = simple_return(100, 110)
        assert result == 0.10
    
    def test_negative_return(self):
        """Da 100 a 90 = -10%"""
        result = simple_return(100, 90)
        assert result == -0.10
    
    def test_zero_return(self):
        """Da 100 a 100 = 0%"""
        result = simple_return(100, 100)
        assert result == 0.0
    
    def test_invalid_start_price(self):
        """Prezzo iniziale zero solleva errore"""
        with pytest.raises(ValueError):
            simple_return(0, 100)


class TestLogReturn:
    
    def test_positive_return(self):
        """Da 100 a 110 = ln(1.1)"""
        result = log_return(100, 110)
        expected = math.log(1.1)
        assert abs(result - expected) < 1e-10
    
    def test_invalid_prices(self):
        """Prezzi negativi sollevano errore"""
        with pytest.raises(ValueError):
            log_return(-100, 110)


class TestReturnsSeries:
    
    def test_basic_series(self):
        """Serie di 4 prezzi produce 3 rendimenti"""
        prices = [100, 110, 105, 108]
        returns = returns_series(prices)
        
        assert len(returns) == 3
        assert returns[0] == pytest.approx(0.10)      # 100 → 110
        assert returns[1] == pytest.approx(-0.0454545, rel=1e-4)  # 110 → 105
        assert returns[2] == pytest.approx(0.0285714, rel=1e-4)   # 105 → 108
    
    def test_insufficient_prices(self):
        """Meno di 2 prezzi solleva errore"""
        with pytest.raises(ValueError):
            returns_series([100])

class TestTotalReturn:
    
    def test_basic_total_return(self):
        """Da 100 a 150 = +50%"""
        prices = [100, 110, 120, 150]
        result = total_return(prices)
        assert result == 0.50
    
    def test_negative_total_return(self):
        """Da 100 a 80 = -20%"""
        prices = [100, 90, 85, 80]
        result = total_return(prices)
        assert result == -0.20


class TestCAGR:
    
    def test_cagr_basic(self):
        """1000 → 1331 in 3 anni = 10% annuo"""
        result = cagr(1000, 1331, 3)
        assert result == pytest.approx(0.10, rel=1e-4)
        
    def test_cagr_double_in_7_years(self):
        """Raddoppio in ~7 anni ≈ 10% annuo (regola del 72)"""
        result = cagr(1000, 2000, 7.2)
        assert result == pytest.approx(0.10, rel=0.02)  # 2% di tolleranza
    
    def test_cagr_invalid_years(self):
        """Years <= 0 solleva errore"""
        with pytest.raises(ValueError):
            cagr(100, 150, 0)