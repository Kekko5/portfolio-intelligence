# 📚 Learning Journal

Documenta qui cosa impari in ogni sprint. Questo file è per te, scrivilo come ti è più utile.

---

## Sprint 1: Foundations

### Dataclasses
*Cosa sono e quando usarle:*
Le dataclasses sono una feature di Python (dal 3.7+) che semplifica la creazione di classi utilizzate principalmente per contenere dati. Con il decorator `@dataclass`, Python genera automaticamente metodi come `__init__()`, `__repr__()`, `__eq__()` senza doverli scrivere manualmente.

**Quando usarle:**
- Per modellare entità di dominio (Asset, Portfolio, PriceData)
- Quando hai una classe con molti attributi ma poca logica
- Quando vuoi immutabilità (usando `frozen=True`)
- Per avere type hints puliti e autocomplete nell'IDE

*Esempio pratico:*
```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Asset:
    """Rappresenta un asset finanziario nel portafoglio"""
    ticker: str          # es. "VWCE.MI"
    quantity: float      # numero di quote possedute
    avg_price: float     # prezzo medio di carico
    currency: str = "EUR"  # default value
    
    def total_value(self) -> float:
        """Calcola il valore totale investito"""
        return self.quantity * self.avg_price

# Vantaggi: __init__, __repr__, __eq__ generati automaticamente
asset = Asset("VWCE.MI", 100, 85.50)
print(asset)  # Asset(ticker='VWCE.MI', quantity=100, avg_price=85.5, currency='EUR')
```

### Virtual Environment
*Perché è importante:*
Il virtual environment isola le dipendenze del progetto dall'installazione globale di Python. Questo previene conflitti tra versioni di librerie diverse per progetti diversi e rende il progetto riproducibile su altre macchine.

**Benefici chiave:**
- Ogni progetto ha le sue dipendenze indipendenti
- `requirements.txt` documenta esattamente cosa serve
- Evita "funziona sul mio PC" - riproducibilità garantita
- Puoi testare diverse versioni di librerie senza rompe re altri progetti

*Comandi chiave:*
```bash
# Creare il virtual environment
python3 -m venv venv

# Attivare (macOS/Linux)
source venv/bin/activate

# Attivare (Windows)
venv\Scripts\activate

# Installare dipendenze
pip install -r requirements.txt

# Salvare dipendenze correnti
pip freeze > requirements.txt

# Disattivare
deactivate
```

### Git Workflow
*Cosa ho imparato:*
**Workflow base per questo progetto:**
1. Creare repo su GitHub e clonarlo localmente
2. Lavorare su feature/fix in locale
3. Commit frequenti con messaggi descrittivi
4. Push al termine di ogni sprint

**Best practices applicate:**
- `.gitignore` per escludere `venv/`, `__pycache__/`, file IDE
- Messaggi di commit descrittivi: "Add Asset dataclass with tests"
- Commit atomici: ogni commit rappresenta un'unità logica completa
- File `__init__.py` in ogni package per struttura Python corretta

**Comandi essenziali usati:**
```bash
git init
git add .
git commit -m "Sprint 1 complete: setup + data models"
git push origin main
```

---

## Sprint 2: Data Layer

### API Integration
*Pattern usati:*
**yfinance library** per interfacciarsi con Yahoo Finance.

**Pattern implementato:**
1. **Fetcher separato**: `yahoo_fetcher.py` contiene tutte le funzioni per recuperare dati esterni
2. **Conversione immediata**: output di yfinance (DataFrame pandas) → convertito subito in dataclass custom
3. **Type hints espliciti**: ogni funzione dichiara input/output precisi
4. **Separazione responsabilità**: `fetch_historical_prices()` per dati storici, `fetch_asset_info()` per metadati

*Esempio pratico:*
```python
import yfinance as yf
from ..models.price_data import PriceData

def fetch_historical_prices(ticker: str, period: str = "1y") -> list[PriceData]:
    """Recupera prezzi storici da Yahoo Finance"""
    asset = yf.Ticker(ticker)
    hist = asset.history(period=period)
    
    if hist.empty:
        raise TickerNotFoundError(ticker)
    
    # Conversione DataFrame → list[PriceData]
    price_data_list = []
    for date, row in hist.iterrows():
        price_data = PriceData(
            date=date.to_pydatetime(),
            open=row['Open'],
            close=row['Close'],
            # ... altri campi
        )
        price_data_list.append(price_data)
    return price_data_list
```

**Vantaggi:**
- Disaccoppiamento: il resto del codice non dipende da pandas/yfinance
- Testabilità: posso mockare facilmente il fetcher
- Type safety: IDE può controllare i tipi

### Error Handling
*Strategia scelta:*
**Custom exceptions** specifiche per il data layer, organizzate in gerarchia.

**Principi applicati:**
1. **Gerarchia**: tutte le eccezioni ereditano da `DataError` base
2. **Semantica chiara**: nome dell'eccezione descrive il problema (`TickerNotFoundError`, `DataFetchError`)
3. **Informazioni contestuali**: ogni eccezione porta dati utili (ticker, messaggio, eccezione originale)
4. **Fail-fast**: validazione immediata (es. `hist.empty` → raise subito)

*Custom exceptions create:*
```python
# src/data/exceptions.py

class DataError(Exception):
    """Classe base per errori del data layer"""
    pass

class TickerNotFoundError(DataError):
    """Ticker non esiste o non ha dati"""
    def __init__(self, ticker: str):
        self.ticker = ticker
        super().__init__(f"Ticker non trovato: {ticker}")

class DataFetchError(DataError):
    """Errore nel recupero dati (rete, API, etc)"""
    def __init__(self, message: str, original_error: Exception | None = None):
        self.message = message
        self.original_error = original_error
        super().__init__(message)
```

**Perché custom exceptions:**
- Catch selettivo: posso gestire `TickerNotFoundError` diversamente da errori generici
- Debugging: stack trace più chiaro
- Documentazione: il tipo di eccezione comunica l'errore
- Testabilità: posso verificare che il codice sollevi l'eccezione giusta

**Uso pratico:**
```python
try:
    prices = fetch_historical_prices("INVALID_TICKER")
except TickerNotFoundError as e:
    print(f"Ticker {e.ticker} non valido")
except DataFetchError as e:
    print(f"Errore rete: {e.message}")
```

---

## Sprint 3: Algorithms Part 1

### Rendimento
*Formula rendimento semplice:*
<!-- Formula matematica + intuizione -->

*Formula rendimento logaritmico:*
<!-- Formula + quando usarlo -->

*CAGR - intuizione:*
<!-- Spiega come se lo spiegassi a qualcuno -->

### Volatilità
*Varianza - formula implementata:*
```python
# Il tuo codice con commenti
```

*Perché (n-1) e non n?*
<!-- Spiega la differenza sample vs population -->

*Annualizzazione - perché √252?*
<!-- Scrivi qui -->

---

## Sprint 4: Algorithms Part 2 + SOLID

### Correlazione
*Covarianza - intuizione:*
<!-- Scrivi qui -->

*Pearson correlation - range e interpretazione:*
<!-- Scrivi qui -->

### Sharpe Ratio
*Formula:*
<!-- Scrivi qui -->

*Interpretazione valori:*
<!-- < 1, 1-2, > 2 cosa significano -->

### SOLID Principles
*S - Single Responsibility:*
<!-- Esempio dal tuo codice -->

*O - Open/Closed:*
<!-- Esempio dal tuo codice -->

*D - Dependency Inversion:*
<!-- Esempio dal tuo codice -->

---

## Sprint 5: Application Layer

### Service Layer Pattern
*Perché separare domain da application:*
<!-- Scrivi qui -->

### Portfolio Metrics
*Rendimento pesato - formula:*
<!-- Scrivi qui -->

*Volatilità portafoglio - perché non è la media delle volatilità:*
<!-- Scrivi qui, è importante! -->

---

## Sprint 6: AI Integration

### Prompt Engineering
*Cosa funziona bene:*
<!-- Pattern che hai scoperto -->

*Cosa non funziona:*
<!-- Errori da evitare -->

*System prompt finale:*
```
<!-- Il tuo prompt ottimizzato -->
```

### API Best Practices
*Rate limiting:*
<!-- Come lo gestisci -->

*Error handling:*
<!-- Pattern usato -->

---

## Sprint 7: CLI + Reports

### Typer
*Pattern utili:*
<!-- Scrivi qui -->

### Rich
*Formattazione che uso:*
<!-- Scrivi qui -->

---

## Sprint 8: Cloud + CI/CD

### GitHub Actions
*Workflow configurato:*
<!-- Descrivi -->

### Deploy
*Piattaforma scelta e perché:*
<!-- Scrivi qui -->

*Problemi incontrati:*
<!-- Scrivi qui -->

---

## 💡 Insights Generali

### Pattern che riuserò
1. 
2. 
3. 

### Errori da non ripetere
1. 
2. 
3. 

### Risorse utili trovate
- 
- 
- 

---

## 🎯 Prossimi passi dopo V1.1
- [ ] 
- [ ] 
- [ ] 
