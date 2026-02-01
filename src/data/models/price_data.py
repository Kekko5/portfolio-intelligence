from dataclasses import dataclass
from datetime import datetime


@dataclass
class PriceData:
    """
    Rappresenta i dati di prezzo di un asset per una singola data.
    
    Attributes:
        date: Data del prezzo
        open: Prezzo di apertura
        high: Prezzo massimo della giornata
        low: Prezzo minimo della giornata
        close: Prezzo di chiusura
        volume: Volume scambiato
    """
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int