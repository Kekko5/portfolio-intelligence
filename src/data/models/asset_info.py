from dataclasses import dataclass

@dataclass
class AssetInfo:
    """
    Metadati di un asset finanziario.
    
    Attributes:
        ticker: Simbolo dell'asset
        name: Nome completo
        currency: Valuta (es. "EUR", "USD")
        exchange: Borsa di riferimento (es. "MIL", "NYSE")
    """
    ticker: str
    name: str
    currency: str
    exchange: str