"""
Funzioni per il calcolo di covarianza e correlazione.
"""
from .volatility import std_dev


def covariance(x: list[float], y: list[float]) -> float:
    """
    Calcola la covarianza campionaria tra due serie.
    
    Formula: cov(x,y) = Σ(x - media_x)(y - media_y) / (n - 1)
    
    Args:
        x: Prima serie di valori
        y: Seconda serie di valori
    
    Returns:
        Covarianza campionaria
    
    Raises:
        ValueError: Se le serie hanno lunghezze diverse o meno di 2 elementi
    """
    if len(x) != len(y):
        raise ValueError("Le serie devono avere la stessa lunghezza")
    if len(x) < 2:
        raise ValueError("Le serie devono contenere almeno 2 elementi")
    
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    
    cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (len(x) - 1)
    return cov


def pearson_correlation(x: list[float], y: list[float]) -> float:
    """
    Calcola il coefficiente di correlazione di Pearson.
    
    Formula: corr(x,y) = cov(x,y) / (std_x × std_y)
    
    Args:
        x: Prima serie di valori
        y: Seconda serie di valori
    
    Returns:
        Correlazione tra -1 e +1
    
    Raises:
        ValueError: Se le serie hanno lunghezze diverse o meno di 2 elementi
    """
    if len(x) != len(y):
        raise ValueError("Le serie devono avere la stessa lunghezza")
    if len(x) < 2:
        raise ValueError("Le serie devono contenere almeno 2 elementi")
    
    cov = covariance(x, y)
    std_x = std_dev(x)
    std_y = std_dev(y)
    
    return cov / (std_x * std_y)