import yfinance as yf
import pandas as pd
from ..models.price_data import PriceData
from ..models.asset_info import AssetInfo
from ..exceptions import TickerNotFoundError, DataFetchError


def fetch_historical_prices(ticker: str, period: str = "1y") -> list[PriceData]:
    """
    Recupera i prezzi storici di un asset da Yahoo Finance.
    
    Args:
        ticker: Simbolo dell'asset (es. "VWCE.MI")
        period: Periodo di tempo (es. "1mo", "3mo", "1y", "5y")
    
    Returns:
        Lista di PriceData, uno per ogni giorno
    
    Raises:
        TickerNotFoundError: Se il ticker non esiste o non ha dati
    """
    asset = yf.Ticker(ticker)
    hist = asset.history(period=period)
    
    if hist.empty:
        raise TickerNotFoundError(ticker)
    
    price_data_list = []
    for date, row in hist.iterrows():
        price_data = PriceData(
            date=date.to_pydatetime(),
            open=row['Open'],
            high=row['High'],
            low=row['Low'],
            close=row['Close'],
            volume=row['Volume']
        )
        price_data_list.append(price_data)
    return price_data_list


def fetch_asset_info(ticker: str) -> AssetInfo:
    """
    Recupera i metadati di un asset da Yahoo Finance.
    
    Args:
        ticker: Simbolo dell'asset
    
    Returns:
        AssetInfo con i metadati dell'asset
    
    Raises:
        TickerNotFoundError: Se il ticker non esiste
    """

    asset = yf.Ticker(ticker)
    info = asset.info
    
    # Verifica che ci siano dati reali, non solo il dizionario vuoto di yfinance
    if not info or info.get('longName') is None:
        raise TickerNotFoundError(ticker)
    
    asset_info = AssetInfo(
        ticker=ticker,
        name=info.get('longName', 'N/A'),
        currency=info.get('currency', 'N/A'),
        exchange=info.get('exchange', 'N/A')
    )
    return asset_info