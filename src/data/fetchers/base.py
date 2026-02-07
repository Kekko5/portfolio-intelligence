"""
Interfacce per i data fetcher.
"""
from typing import Protocol
from ..models.price_data import PriceData
from ..models.asset_info import AssetInfo


class PriceFetcher(Protocol):
    """Interfaccia per recuperare prezzi storici."""
    
    def fetch_prices(self, ticker: str, period: str) -> list[PriceData]:
        """Recupera i prezzi storici di un asset."""
        ...


class AssetInfoFetcher(Protocol):
    """Interfaccia per recuperare info sugli asset."""
    
    def fetch_info(self, ticker: str) -> AssetInfo:
        """Recupera i metadati di un asset."""
        ...