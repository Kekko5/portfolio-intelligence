"""
Funzioni per il calcolo dei rendimenti.
"""
import math


def simple_return(price_start: float, price_end: float) -> float:
    """
    Calcola il rendimento semplice tra due prezzi.
    
    Formula: R = (P_end - P_start) / P_start
    
    Args:
        price_start: Prezzo iniziale
        price_end: Prezzo finale
    
    Returns:
        Rendimento come decimale (es. 0.10 = 10%)
    
    Raises:
        ValueError: Se price_start è zero o negativo
    """
    if price_start <= 0:
        raise ValueError("price_start deve essere maggiore di zero")
    return (price_end - price_start) / price_start

def log_return(price_start: float, price_end: float) -> float:
    """
    Calcola il rendimento logaritmico tra due prezzi.
    
    Formula: R = ln(P_end / P_start)
    
    Args:
        price_start: Prezzo iniziale
        price_end: Prezzo finale
    
    Returns:
        Rendimento logaritmico
    
    Raises:
        ValueError: Se price_start o price_end sono zero o negativi
    """
    if price_start <= 0 or price_end <= 0:
        raise ValueError("price_start e price_end devono essere maggiori di zero")
    return math.log(price_end / price_start)

def returns_series(prices: list[float]) -> list[float]:
    """
    Calcola la serie di rendimenti semplici da una lista di prezzi.
    
    Args:
        prices: Lista di prezzi in ordine cronologico
    
    Returns:
        Lista di rendimenti (un elemento in meno dei prezzi)
    
    Raises:
        ValueError: Se la lista ha meno di 2 prezzi
    """
    if len(prices) < 2:
        raise ValueError("La lista deve contenere almeno 2 prezzi")
    returns = []
    for i in range(1, len(prices)):
        r = simple_return(prices[i-1], prices[i])
        returns.append(r)
    return returns

def total_return(prices: list[float]) -> float:
    """
    Calcola il rendimento totale dal primo all'ultimo prezzo.
    
    Args:
        prices: Lista di prezzi in ordine cronologico
    
    Returns:
        Rendimento totale come decimale
    
    Raises:
        ValueError: Se la lista ha meno di 2 prezzi
    """
    if len(prices) < 2:
        raise ValueError("La lista deve contenere almeno 2 prezzi")
    return simple_return(prices[0], prices[-1])


def cagr(price_start: float, price_end: float, years: float) -> float:
    """
    Calcola il Compound Annual Growth Rate.
    
    Formula: CAGR = (P_end / P_start)^(1/years) - 1
    
    Args:
        price_start: Prezzo iniziale
        price_end: Prezzo finale
        years: Numero di anni (può essere decimale, es. 2.5)
    
    Returns:
        CAGR come decimale (es. 0.10 = 10% annuo)
    
    Raises:
        ValueError: Se price_start <= 0 o years <= 0
    """
    if price_start <= 0 or years <= 0:
        raise ValueError("price_start e years devono essere maggiori di zero")
    return (price_end / price_start) ** (1 / years) - 1