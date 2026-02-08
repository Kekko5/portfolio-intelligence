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
$$R = \frac{P_{end} - P_{start}}{P_{start}}$$

**Intuizione**: "Quanto ho guadagnato (o perso) rispetto all'investimento iniziale?"
- Se compro a 100€ e vendo a 110€ → R = (110-100)/100 = 0.10 = 10%
- Facile da capire, ma **non è additivo**: se guadagno +10% poi -10%, non torno a 0
- Esempio: 100€ +10% = 110€, poi 110€ -10% = 99€ (non 100€!)

*Formula rendimento logaritmico:*
$$R_{log} = \ln\left(\frac{P_{end}}{P_{start}}\right)$$

**Quando usarlo:**
- Quando hai una serie temporale lunga e vuoi sommare i rendimenti
- È **additivo**: ln(110/100) + ln(99/110) = ln(99/100) ✓
- Più accurato per analisi statistiche (distribuzione normale)
- Usato nei modelli quantitativi professionali

**Implementazione pratica:**
```python
def simple_return(price_start: float, price_end: float) -> float:
    """R = (P_end - P_start) / P_start"""
    if price_start <= 0:
        raise ValueError("price_start deve essere maggiore di zero")
    return (price_end - price_start) / price_start

def log_return(price_start: float, price_end: float) -> float:
    """R = ln(P_end / P_start)"""
    if price_start <= 0 or price_end <= 0:
        raise ValueError("I prezzi devono essere maggiori di zero")
    return math.log(price_end / price_start)
```

*CAGR - intuizione:*
**Compound Annual Growth Rate** = "Tasso di crescita annuale composto"

$$CAGR = \left(\frac{P_{end}}{P_{start}}\right)^{\frac{1}{years}} - 1$$

**Come spiegarlo a qualcuno:**
"Se avessi avuto un rendimento costante ogni anno, quale sarebbe stato per arrivare da P_start a P_end?"

Esempio:
- Investito 10,000€ nel 2020
- Nel 2025 hai 15,000€
- CAGR = (15,000/10,000)^(1/5) - 1 = 0.0845 = 8.45% annuo
- Significa: "È come se avessi guadagnato esattamente 8.45% ogni anno per 5 anni"

**Perché è utile:**
- Confrontare investimenti con durate diverse
- "Ho guadagnato 50% in 5 anni" → CAGR ~8.45%/anno
- "Ho guadagnato 20% in 1 anno" → CAGR 20%/anno → meglio!

### Volatilità
*Varianza - formula implementata:*
```python
def variance(values: list[float]) -> float:
    """
    Calcola la varianza campionaria.
    
    Formula: σ² = Σ(x - media)² / (n - 1)
    """
    if len(values) < 2:
        raise ValueError("Serve almeno 2 valori")
    
    # Step 1: calcola la media
    mean = sum(values) / len(values)
    
    # Step 2: calcola gli scarti al quadrato
    squared_diffs = [(x - mean) ** 2 for x in values]
    
    # Step 3: dividi per (n-1) non n!
    variance = sum(squared_diffs) / (len(values) - 1)
    return variance

def std_dev(values: list[float]) -> float:
    """Deviazione standard = √varianza"""
    return math.sqrt(variance(values))
```

*Perché (n-1) e non n?*
**Differenza sample vs population:**

- **Population (n)**: hai TUTTI i dati possibili dell'universo
  - Esempio: rendimenti di TUTTI gli ETF esistenti
  - Dividi per n
  
- **Sample (n-1)**: hai solo un campione dei dati
  - Esempio: rendimenti degli ultimi 252 giorni di un ETF
  - Dividi per (n-1) → **Bessel's correction**
  - Compensa il bias: il campione tende a sottostimare la varianza vera

**Nel nostro caso:**
- Usiamo sempre (n-1) perché analizziamo dati storici (un campione)
- I 252 giorni passati sono un campione, non "tutto il futuro"

*Annualizzazione - perché √252?*
**Formula annualizzazione volatilità:**
$$\sigma_{annual} = \sigma_{daily} \times \sqrt{252}$$

**Spiegazione matematica:**
- La volatilità scala con la **radice quadrata del tempo**
- Varianza è additiva: Var(total) = Var(day1) + Var(day2) + ...
- Std dev = √Var, quindi std_annual = √(252 × var_daily) = √252 × std_daily

**Perché 252 e non 365?**
- 252 = giorni di trading medi in un anno (esclude weekend e festivi)
- Più accurato per asset finanziari
- Per crypto (24/7) useresti 365

**Implementazione:**
```python
def annualized_volatility(daily_returns: list[float], trading_days: int = 252) -> float:
    """σ_annual = σ_daily × √252"""
    daily_vol = std_dev(daily_returns)
    return daily_vol * math.sqrt(trading_days)
```

**Esempio pratico:**
- Volatilità giornaliera = 1.2%
- Volatilità annualizzata = 1.2% × √252 ≈ 1.2% × 15.87 ≈ 19%
- Significa: "Mi aspetto oscillazioni annuali del ±19%"

---

## Sprint 4: Algorithms Part 2 + SOLID

### Correlazione
*Covarianza - intuizione:*
La covarianza misura se due serie si muovono **insieme** o in modo opposto.

- Se i rendimenti di due asset crescono e calano insieme → covarianza **positiva**
- Se uno sale quando l'altro scende → covarianza **negativa**
- Se non c'è relazione → covarianza ~ 0

Formula (campionaria):
$$\text{cov}(x,y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n-1}$$

**Intuizione pratica:**
"Quanto spesso i due asset si allontanano dalla loro media nella stessa direzione?"

*Pearson correlation - range e interpretazione:*
La correlazione di Pearson **normalizza** la covarianza, rendendola comparabile tra asset.

$$\rho_{x,y} = \frac{\text{cov}(x,y)}{\sigma_x \cdot \sigma_y}$$

**Range:** da **-1** a **+1**
- **+1** → perfettamente correlati (si muovono insieme)
- **0** → non correlati
- **-1** → perfettamente inversi

**Perché è utile:**
- Diversificazione: asset con bassa correlazione riducono il rischio complessivo
- Se correlazione ≈ 1 → portafoglio poco diversificato

**Implementazione nel codice:**
```python
def pearson_correlation(x: list[float], y: list[float]) -> float:
    cov = covariance(x, y)
    std_x = std_dev(x)
    std_y = std_dev(y)
    return cov / (std_x * std_y)
```

### Sharpe Ratio
*Formula:*
$$\text{Sharpe} = \frac{R_{medio} - R_{risk\_free}}{\sigma}$$

**Significato:**
"Quanto rendimento extra ottengo per ogni unità di rischio?"

*Interpretazione valori:*
- **< 1** → rischio elevato per il rendimento (poco interessante)
- **1 - 2** → buono
- **> 2** → eccellente (rendimento alto rispetto al rischio)

**Nota:** lo Sharpe è più affidabile su serie lunghe e rendimenti coerenti.

### SOLID Principles
*S - Single Responsibility:*
Ogni modulo ha una sola responsabilità:
- `src/domain/metrics/returns.py` calcola **solo rendimenti**
- `src/domain/metrics/volatility.py` calcola **solo volatilità**
- `src/data/fetchers/yahoo_fetcher.py` gestisce **solo il fetch dati**

Risultato: codice più chiaro e testabile.

*O - Open/Closed:*
Il codice è **aperto all'estensione** ma **chiuso alla modifica**.

Esempio:
- Posso aggiungere nuove metriche (es. `sortino_ratio`) creando un nuovo file in `metrics/`
- Non devo modificare le funzioni esistenti, solo aggiungere nuove

Inoltre, posso aggiungere un nuovo fetcher (es. `alpha_vantage_fetcher.py`) senza toccare la logica di dominio.

*D - Dependency Inversion:*
Il dominio non dipende da implementazioni concrete ma da **astrazioni**.

Esempio:
- In `src/data/fetchers/base.py` ci sono i `Protocol` (`PriceFetcher`, `AssetInfoFetcher`)
- Le parti alte del sistema possono dipendere da queste interfacce
- Questo permette di sostituire il fetcher Yahoo con un mock o un altro provider senza cambiare il dominio

---

## Sprint 5: Application Layer

### Service Layer Pattern
*Perché separare domain da application:*
Il **domain layer** contiene la logica pura (calcoli, formule) senza sapere da dove arrivano i dati.
Il **application layer** (service) **coordina** il flusso: fetch dati → trasformazione → analisi → output.

**Vantaggi della separazione:**
- Il domain è **testabile** senza rete, senza mock, con semplici liste di numeri
- Il service è il punto di ingresso unico: nasconde la complessità al chiamante
- Posso cambiare la sorgente dati (Yahoo → API diversa) senza toccare il domain

**Struttura nel progetto:**
```
domain/                        ← Logica pura (no dipendenze esterne)
├── metrics/                   ← Calcoli: returns, volatility, correlation, ratios
└── analysis/portfolio_analyzer.py  ← Orchestrazione metriche

application/                   ← Coordinamento (dipende da data + domain)
└── services/analysis_service.py    ← Fetch → Analisi → Report
```

**Il flow di `AnalysisService.analyze_portfolio()`:**
```python
# 1. Converti period → years
years = self._period_to_years(period)  # "1y" → 1.0, "6mo" → 0.5

# 2. Fetch dati e estrai prezzi di chiusura
for asset in portfolio.assets:
    price_data = self.fetcher.fetch_prices(asset.ticker, period)
    close_prices = [price.close for price in price_data]

# 3. Delega l'analisi al domain layer
result = self.analyzer.analyze_portfolio(assets_data, weights, years)

# 4. Impacchetta il risultato in un PortfolioReport
return PortfolioReport(...)
```

**Lezione chiave:** il service non calcola nulla direttamente, **coordina e delega**.

### Portfolio Metrics
*Rendimento pesato - formula:*
Il rendimento del portafoglio è la **media pesata** dei rendimenti individuali:

$$R_{portfolio} = \sum_{i=1}^{n} w_i \cdot R_i$$

Dove $w_i$ è il peso dell'asset $i$ e $R_i$ il suo rendimento.

**Esempio:**
- VWCE (60%): rendimento +12% → contributo = 0.60 × 0.12 = 0.072
- AGGH (40%): rendimento +3% → contributo = 0.40 × 0.03 = 0.012
- Rendimento portafoglio = 0.072 + 0.012 = 0.084 = **8.4%**

Lo stesso principio si applica al CAGR del portafoglio.

*Volatilità portafoglio - perché non è la media delle volatilità:*
**Questo è un concetto fondamentale!**

La volatilità del portafoglio **NON** è la media pesata delle volatilità individuali.
La formula corretta include le **correlazioni** tra gli asset:

$$\sigma_p = \sqrt{\sum_{i}\sum_{j} w_i \cdot w_j \cdot \sigma_i \cdot \sigma_j \cdot \rho_{ij}}$$

**Perché?**
- Se due asset sono **poco correlati** ($\rho \approx 0$), la volatilità del portafoglio è **inferiore** alla media pesata
- Questo è il principio della **diversificazione**: combinare asset non correlati riduce il rischio
- È il motivo per cui un portafoglio 60/40 (azioni/obbligazioni) ha rischio minore di quanto ci si aspetterebbe

**Nel nostro codice (semplificato):**
```python
# Approssimazione: media pesata delle volatilità
portfolio_volatility = sum(
    asset_analyses[ticker].volatility * weights[ticker]
    for ticker in assets_data.keys()
)
# Nota: questa è una SOVRASTIMA del rischio reale
# La versione corretta richiederebbe la matrice di correlazione
```

**Lezione:** la media pesata è un'approssimazione che **sovrastima** il rischio. È conservativa ma non precisa. Un miglioramento futuro sarà usare la formula completa con le correlazioni.

---

## Sprint 6: AI Integration

### Prompt Engineering
*Cosa funziona bene:*
1. **System prompt con ruolo chiaro**: definire "Sei un analista finanziario esperto" dà un tono coerente
2. **Linee guida esplicite**: dire cosa fare E cosa non fare (es. "Non dare consigli specifici di acquisto")
3. **Formato risposta strutturato**: chiedere riassunto → punti chiave → suggerimenti mantiene le risposte organizzate
4. **Dati formattati nel prompt**: passare i numeri con `:.2%` li rende leggibili per l'AI
5. **Template con placeholders**: usare `PORTFOLIO_ANALYSIS_TEMPLATE.format(...)` rende il prompt riproducibile

```python
# Template con placeholders chiari
PORTFOLIO_ANALYSIS_TEMPLATE = """Analizza questo portafoglio:
**Nome portafoglio:** {portfolio_name}
**Metriche aggregate:**
- Rendimento totale: {total_return:.2%}
- CAGR: {cagr:.2%}
...
"""
```

*Cosa non funziona:*
- **Prompt troppo vaghi**: "analizza questo" → risposte generiche e poco utili
- **Troppo contesto**: sovraccaricare con dati non necessari confonde il modello
- **Nessun vincolo sul formato**: senza "Formato risposta:" l'output è imprevedibile
- **Chiedere previsioni**: l'AI non prevede il futuro, meglio chiedere analisi di dati storici

*System prompt finale:*
```
Sei un analista finanziario esperto e consulente per investitori individuali.

Linee guida:
- Usa linguaggio semplice, evita gergo non necessario
- Sii conciso ma completo
- Evidenzia aspetti positivi E aree di miglioramento
- Non dare consigli specifici ("compra X"), suggerisci considerazioni
- Contestualizza i numeri (es. "volatilità 15% è nella media per azionario")
- Segnala rischi con chiarezza ma senza allarmismo

Formato: riassunto 1-2 frasi → punti chiave → 1-2 suggerimenti pratici
```

### API Best Practices
*Rate limiting:*
Per ora non è un problema (uso singolo), ma le best practices applicate:
- L'`AIClient` è opzionale (`ai_client: AIClient = None`) → il sistema funziona anche senza AI
- L'insight viene generato una sola volta per report, non per asset
- Il parametro `include_ai_insight=True` permette di disattivarlo per test o batch

*Error handling:*
Pattern **graceful degradation**: se l'AI fallisce, il report esce comunque senza insight.

```python
def _generate_ai_insight(self, report: PortfolioReport) -> AIInsight | None:
    """Genera insight AI — restituisce None se fallisce."""
    if not self.ai_client:
        try:
            self.ai_client = AIClient()
        except ValueError:
            return None  # API key mancante → nessun insight
    
    try:
        prompt = format_portfolio_prompt(report)
        analysis = self.ai_client.ask(prompt, system_prompt=SYSTEM_PROMPT)
        first_sentence = analysis.split('.')[0] + '.'
        return AIInsight(
            summary=first_sentence,
            full_analysis=analysis,
            generated_at=datetime.now()
        )
    except Exception:
        return None  # Errore rete/API → nessun insight, nessun crash
```

**Pattern chiave:**
1. **Lazy initialization**: `AIClient` viene creato solo quando serve
2. **Optional dependency**: il campo `ai_insight: AIInsight | None = None` nel report
3. **No crash**: doppio try/except → il report numerico esce sempre
4. **Secrets via `.env`**: `ANTHROPIC_API_KEY` in `.env`, mai nel codice
5. **Separazione prompt/codice**: i prompt vivono in `config/prompts/`, non nel service

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
