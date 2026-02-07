"""
Funzioni per il calcolo di ratio finanziari.
"""
from .volatility import std_dev


def sharpe_ratio(returns: list[float], risk_free_rate: float = 0.02) -> float:
    """
    Calcola lo Sharpe Ratio.
    
    Formula: Sharpe = (R_medio - R_risk_free) / σ
    
    Args:
        returns: Lista di rendimenti (es. giornalieri o annuali)
        risk_free_rate: Tasso risk-free (default 2% = 0.02)
    
    Returns:
        Sharpe Ratio
    
    Raises:
        ValueError: Se la lista ha meno di 2 elementi
    """
    if len(returns) < 2:
        raise ValueError("La lista deve contenere almeno 2 elementi")
    
    mean_return = sum(returns) / len(returns)
    excess_return = mean_return - risk_free_rate
    volatility = std_dev(returns)
    
    return excess_return / volatility


def max_drawdown(prices: list[float]) -> float:
    """
    Calcola il Maximum Drawdown di una serie di prezzi.
    
    Il drawdown misura la perdita percentuale dal picco precedente.
    Il Max Drawdown è il drawdown più grande (più negativo) della serie.
    
    Args:
        prices: Lista di prezzi in ordine cronologico
    
    Returns:
        Max Drawdown come decimale negativo (es. -0.25 = -25%)
    
    Raises:
        ValueError: Se la lista ha meno di 2 prezzi
    """
    if len(prices) < 2:
        raise ValueError("La lista deve contenere almeno 2 prezzi")
    
    max_drawdown = 0.0
    peak = prices[0]
    
    for price in prices:
        if price > peak:
            peak = price
        drawdown = (price - peak) / peak
        if drawdown < max_drawdown:
            max_drawdown = drawdown
    
    return max_drawdown