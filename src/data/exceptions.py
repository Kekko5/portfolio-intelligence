"""
Eccezioni custom per il data layer.
"""


class DataError(Exception):
    """Classe base per errori del data layer."""
    pass


class TickerNotFoundError(DataError):
    """
    Sollevata quando un ticker non esiste o non ha dati.
    
    Attributes:
        ticker: Il ticker che non è stato trovato
    """
    def __init__(self, ticker: str):
        self.ticker = ticker
        super().__init__(f"Ticker non trovato: {ticker}")


class DataFetchError(DataError):
    """
    Sollevata quando c'è un errore nel recupero dati (rete, API, ecc).
    
    Attributes:
        message: Descrizione dell'errore
        original_error: L'eccezione originale (se presente)
    """
    def __init__(self, message: str, original_error: Exception | None = None):
        self.message = message
        self.original_error = original_error
        super().__init__(message)