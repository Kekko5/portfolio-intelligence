from src.data.models.asset import Asset
from src.data.models.portfolio import Portfolio

def test_total_weight():
    assets = [
        Asset(ticker="AAPL", name="Apple Inc.", asset_type="Stock", weight=0.5),
        Asset(ticker="MSFT", name="Microsoft Corp.", asset_type="Stock", weight=0.3),
    ]
    portfolio = Portfolio(name="Tech Portfolio", assets=assets)
    
    assert abs(portfolio.total_weight() - 0.8) < 1e-6  # 0.5 + 0.3 = 0.8

def test_is_valid_with_valid_portfolio():
    assets = [
        Asset(ticker="AAPL", name="Apple Inc.", asset_type="Stock", weight=0.6),
        Asset(ticker="MSFT", name="Microsoft Corp.", asset_type="Stock", weight=0.4)
    ]
    portfolio = Portfolio(name="Valid Portfolio", assets=assets)
    
    assert portfolio.is_valid() is True

def test_is_valid_with_invalid_portfolio():
    assets = [
        Asset(ticker="AAPL", name="Apple Inc.", asset_type="Stock", weight=0.7),
        Asset(ticker="MSFT", name="Microsoft Corp.", asset_type="Stock", weight=0.4)
    ]
    portfolio = Portfolio(name="Invalid Portfolio", assets=assets)

    assert portfolio.is_valid() is False
    

def test_get_asset_found():
    assets = [
        Asset(ticker="AAPL", name="Apple Inc.", asset_type="Stock", weight=0.5),
        Asset(ticker="MSFT", name="Microsoft Corp.", asset_type="Stock", weight=0.5)
    ]
    portfolio = Portfolio(name="Tech Portfolio", assets=assets)
    asset = portfolio.get_asset("AAPL")
    assert asset is not None
    assert asset.ticker == "AAPL"


def test_get_asset_not_found():
    assets = [
        Asset(ticker="AAPL", name="Apple Inc.", asset_type="Stock", weight=0.5),
        Asset(ticker="MSFT", name="Microsoft Corp.", asset_type="Stock", weight=0.5)
    ]
    portfolio = Portfolio(name="Tech Portfolio", assets=assets)
    asset = portfolio.get_asset("GOOGL")
    assert asset is None
    