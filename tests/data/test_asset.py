from src.data.models.asset import Asset

def test_asset_creation():
    asset = Asset(
        ticker="VWCE.MI",
        name="Vanguard FTSE All-World UCITS ETF",
        asset_type="ETF",
        weight=0.30
    )
    
    assert asset.ticker == "VWCE.MI"
    assert asset.name == "Vanguard FTSE All-World UCITS ETF"
    assert asset.asset_type == "ETF"
    assert asset.weight == 0.30

def test_assets_with_same_values_are_equal():
    asset1 = Asset(ticker="AAPL", name="Apple Inc.", asset_type="Stock", weight=0.15)
    asset2 = Asset(ticker="AAPL", name="Apple Inc.", asset_type="Stock", weight=0.15)
    
    assert asset1 == asset2

def test_assets_with_different_ticker_are_not_equal():
    asset1 = Asset(ticker="AAPL", name="Apple Inc.", asset_type="Stock", weight=0.15)
    asset2 = Asset(ticker="MSFT", name="Microsoft", asset_type="Stock", weight=0.15)
    
    assert asset1 != asset2