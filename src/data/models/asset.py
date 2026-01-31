from dataclasses import dataclass

@dataclass
class Asset:
    """
    Rappresenta un singolo asset all'interno di un portafoglio finanziario.
    
    Attributes:
        ticker: Simbolo identificativo dell'asset (es. "VWCE.MI")
        name: Denominazione completa dell'asset
        asset_type: Categoria dell'asset (es. "ETF", "Stock", "Bond")
        weight: Peso percentuale nel portafoglio (es. 0.25 = 25%)
    """
    ticker: str
    name: str
    asset_type: str
    weight: float