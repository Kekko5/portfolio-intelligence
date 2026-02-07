import pytest
from src.domain.metrics.correlation import covariance, pearson_correlation


class TestCovariance:
    
    def test_positive_covariance(self):
        """Serie che crescono insieme = covarianza positiva"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        result = covariance(x, y)
        assert result > 0
    
    def test_negative_covariance(self):
        """Serie opposte = covarianza negativa"""
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]
        result = covariance(x, y)
        assert result < 0
    
    def test_different_lengths(self):
        """Serie di lunghezza diversa solleva errore"""
        with pytest.raises(ValueError):
            covariance([1, 2, 3], [1, 2])


class TestPearsonCorrelation:
    
    def test_perfect_positive_correlation(self):
        """Serie identiche (scalate) = correlazione +1"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]  # y = 2x
        result = pearson_correlation(x, y)
        assert result == pytest.approx(1.0, rel=1e-10)
    
    def test_perfect_negative_correlation(self):
        """Serie opposte = correlazione -1"""
        x = [1, 2, 3, 4, 5]
        y = [5, 4, 3, 2, 1]
        result = pearson_correlation(x, y)
        assert result == pytest.approx(-1.0, rel=1e-10)
    
    def test_no_correlation(self):
        """Serie indipendenti = correlazione ~0"""
        x = [1, 2, 3, 4, 5]
        y = [3, 1, 4, 2, 5]  # Nessun pattern
        result = pearson_correlation(x, y)
        assert -0.5 < result < 0.5  # Circa zero
    
    def test_correlation_range(self):
        """Correlazione sempre tra -1 e +1"""
        x = [10, 20, 15, 25, 30]
        y = [5, 15, 10, 20, 18]
        result = pearson_correlation(x, y)
        assert -1 <= result <= 1