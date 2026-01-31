from dataclasses import dataclass
from .asset import Asset

@dataclass
class Portfolio:
    """
    Rappresenta un portafoglio finanziario composto da più asset.
    
    Attributes:
        name: Nome del portafoglio
        assets: Lista degli asset che compongono il portafoglio
    """
    name: str
    assets: list[Asset]

    def total_weight(self) -> float:
        """
        Calcola il peso totale degli asset nel portafoglio.
    
        Returns:
        La somma dei pesi di tutti gli asset.
        """
        return sum(asset.weight for asset in self.assets)

    def is_valid(self) -> bool:
        """
        Verifica se il portafoglio è valido, ovvero se il peso totale degli asset è pari a 1.0 (100%).
    
        Returns:
            True se il portafoglio è valido, False altrimenti.
        """
        return abs(self.total_weight() - 1.0) < 1e-6

    def get_asset(self, ticker: str) -> Asset | None:
        """
        Recupera un asset dal portafoglio in base al suo ticker.
        
        Args:
            ticker: Il simbolo identificativo dell'asset da cercare.
        Returns:
            L'asset corrispondente al ticker, o None se non trovato.
        """
        for asset in self.assets:
            if asset.ticker == ticker:
                return asset
        return None