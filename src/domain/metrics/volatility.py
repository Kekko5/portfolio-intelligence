"""
Funzioni per il calcolo della volatilità.
"""
import math


def variance(values: list[float]) -> float:
    """
    Calcola la varianza campionaria di una lista di valori.
    
    Formula: σ² = Σ(x - media)² / (n - 1)
    
    Args:
        values: Lista di valori numerici
    
    Returns:
        Varianza campionaria
    
    Raises:
        ValueError: Se la lista ha meno di 2 elementi
    """
    if len(values) < 2:
        raise ValueError("La lista deve contenere almeno 2 elementi")
    mean = sum(values) / len(values)
    squared_diffs = [(x - mean) ** 2 for x in values]
    variance = sum(squared_diffs) / (len(values) - 1)
    return variance


def std_dev(values: list[float]) -> float:
    """
    Calcola la deviazione standard campionaria.
    
    Formula: σ = √varianza
    
    Args:
        values: Lista di valori numerici
    
    Returns:
        Deviazione standard
    
    Raises:
        ValueError: Se la lista ha meno di 2 elementi
    """
    if len(values) < 2:
        raise ValueError("La lista deve contenere almeno 2 elementi")
    var = variance(values)
    return math.sqrt(var)

def annualized_volatility(daily_returns: list[float], trading_days: int = 252) -> float:
    """
    Calcola la volatilità annualizzata dai rendimenti giornalieri.
    
    Formula: σ_annual = σ_daily × √trading_days
    
    Args:
        daily_returns: Lista di rendimenti giornalieri
        trading_days: Giorni di trading in un anno (default 252)
    
    Returns:
        Volatilità annualizzata come decimale
    
    Raises:
        ValueError: Se la lista ha meno di 2 elementi
    """
    if len(daily_returns) < 2:
        raise ValueError("La lista deve contenere almeno 2 elementi")
    daily_vol = std_dev(daily_returns)
    return daily_vol * math.sqrt(trading_days)