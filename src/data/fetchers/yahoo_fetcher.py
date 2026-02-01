import yfinance as yf
import pandas as pd


def fetch_historical_prices(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Recupera i prezzi storici di un asset da Yahoo Finance.
    
    Args:
        ticker: Simbolo dell'asset (es. "VWCE.MI")
        period: Periodo di tempo (es. "1mo", "3mo", "1y", "5y")
    
    Returns:
        DataFrame con colonne: Open, High, Low, Close, Volume
    
    Raises:
        ValueError: Se il ticker non esiste o non ha dati
    """
    asset = yf.Ticker(ticker)
    hist = asset.history(period=period)
    
    if hist.empty:
        raise ValueError(f"Nessun dato trovato per il ticker: {ticker}")
    
    return hist