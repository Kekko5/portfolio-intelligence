import pytest
from src.data.fetchers.yahoo_fetcher import fetch_historical_prices, fetch_asset_info
from src.data.exceptions import TickerNotFoundError


def test_fetch_historical_prices_valid_ticker():
    """Test che un ticker valido ritorni dati."""
    prices = fetch_historical_prices("VWCE.MI", "5d")
    
    assert len(prices) > 0
    assert prices[0].close > 0


def test_fetch_historical_prices_invalid_ticker():
    """Test che un ticker invalido sollevi TickerNotFoundError."""
    with pytest.raises(TickerNotFoundError) as exc_info:
        fetch_historical_prices("TICKERFALSO123", "5d")
    
    assert exc_info.value.ticker == "TICKERFALSO123"


def test_fetch_asset_info_valid_ticker():
    """Test che un ticker valido ritorni info."""
    info = fetch_asset_info("VWCE.MI")
    
    assert info.ticker == "VWCE.MI"
    assert info.currency == "EUR"
    assert len(info.name) > 0


def test_fetch_asset_info_invalid_ticker():
    """Test che un ticker invalido sollevi TickerNotFoundError."""
    with pytest.raises(TickerNotFoundError) as exc_info:
        fetch_asset_info("TICKERFALSO123")
    
    assert exc_info.value.ticker == "TICKERFALSO123"