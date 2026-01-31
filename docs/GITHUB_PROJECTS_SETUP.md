# 🛠️ Setup GitHub Projects

Guida per configurare il tracking visuale del progetto.

---

## Step 1: Crea il Repository

1. Vai su github.com → "New repository"
2. Nome: `portfolio-intelligence`
3. Descrizione: "Portfolio analysis system with AI insights"
4. ✅ Public (così puoi mostrarlo come portfolio)
5. ✅ Add README
6. ✅ Add .gitignore → Python
7. License: MIT
8. Create repository

---

## Step 2: Crea il Project Board

1. Nel repo, vai su tab **Projects**
2. Click **"New project"**
3. Scegli **"Board"** (Kanban style)
4. Nome: "Portfolio Intelligence Development"

---

## Step 3: Configura le Colonne

Crea queste colonne (in ordine da sinistra a destra):

| Colonna | Descrizione |
|---------|-------------|
| 📋 **Backlog** | Task futuri, non ancora nel sprint corrente |
| 🎯 **Sprint Backlog** | Task pianificati per lo sprint attuale |
| 🏃 **In Progress** | Cosa stai facendo ORA (max 1-2 issue) |
| 👀 **Review** | Completato, da verificare/testare |
| ✅ **Done** | Completato e verificato |

---

## Step 4: Crea le Labels

Vai in **Issues** → **Labels** → **New label**

### Labels essenziali per iniziare

| Nome | Colore | Descrizione |
|------|--------|-------------|
| `sprint-1` | `#0E8A16` | Sprint 1 - Foundations |
| `sprint-2` | `#1D76DB` | Sprint 2 - Data Layer |
| `sprint-3` | `#5319E7` | Sprint 3 - Algorithms P1 |
| `sprint-4` | `#D93F0B` | Sprint 4 - Algorithms P2 |
| `epic:setup` | `#B60205` | Epic: Environment Setup |
| `epic:data` | `#B60205` | Epic: Data Layer |
| `epic:algorithms` | `#B60205` | Epic: Algorithms |
| `📚 learning` | `#D4C5F9` | Study/theory task |
| `💻 coding` | `#0366D6` | Implementation task |
| `🧪 testing` | `#FBCA04` | Testing task |

---

## Step 5: Struttura Epic → User Story → Task

### Come funziona in GitHub

| Concetto | In GitHub | Come si crea |
|----------|-----------|--------------|
| **Epic** | Label | Es: `epic:setup` |
| **User Story** | Issue | Una issue per funzionalità |
| **Task** | Checkbox | Lista dentro la issue |

### Vantaggi di questo approccio
- Meno issue da gestire
- Visione chiara del progresso per funzionalità
- I checkbox si spuntano man mano che completi

---

## Step 6: Crea le Issue per Sprint 1

Crea **4 Issue** in questo ordine. Per ogni issue:
1. Click **Issues** → **New issue**
2. Copia il **Title**
3. Copia il **Body** 
4. Aggiungi le **Labels**
5. Click **Create**
6. Aggiungi la issue al **Project** (sidebar destra → Projects)

---

### Issue 1 di 4

**Title:**
```
[US-1.1.1] Ambiente Python configurato
```

**Body:**
```markdown
## User Story
Come sviluppatore, voglio un ambiente Python configurato correttamente per poter iniziare lo sviluppo del progetto.

## Tasks
- [ ] **T-001** (~15min): Installare Python 3.12+ e verificare con `python --version`
- [ ] **T-002** (~10min): Creare repository GitHub `portfolio-intelligence`
- [ ] **T-003** (~15min): Clonare repo in locale e creare virtual environment
- [ ] **T-004** (~10min): Creare `.gitignore` per Python
- [ ] **T-005** (~5min): Creare `requirements.txt` iniziale (vuoto per ora)

## Acceptance Criteria
- [ ] `python --version` mostra 3.12 o superiore
- [ ] Repository GitHub esiste ed è clonato in locale
- [ ] Virtual environment creato e attivabile
- [ ] `.gitignore` presente con esclusioni Python standard
- [ ] Primo commit effettuato

## Notes
Tempo totale stimato: ~55 minuti

Comandi utili:
- `python -m venv venv`
- `source venv/bin/activate` (Mac/Linux) o `venv\Scripts\activate` (Windows)
```

**Labels:** `sprint-1`, `epic:setup`, `💻 coding`

---

### Issue 2 di 4

**Title:**
```
[US-1.1.2] Struttura cartelle professionale
```

**Body:**
```markdown
## User Story
Come sviluppatore, voglio una struttura di cartelle organizzata secondo best practice per mantenere il codice pulito e scalabile.

## Tasks
- [ ] **T-006** (~20min): Creare struttura cartelle `src/` con tutti i package (data, domain, application, presentation)
- [ ] **T-007** (~10min): Creare tutti i file `__init__.py` necessari
- [ ] **T-008** (~15min): Creare cartella `tests/` con struttura che rispecchia `src/`
- [ ] **T-009** (~10min): Creare cartella `docs/` e aggiungere documentazione progetto

## Acceptance Criteria
- [ ] Struttura cartelle corrisponde al design in PROJECT_CHARTER.md
- [ ] Tutti i package hanno `__init__.py`
- [ ] Cartella `tests/` pronta per i test
- [ ] Documentazione (PROJECT_CHARTER, BACKLOG, LEARNINGS) nella cartella `docs/`

## Struttura target
```
portfolio-intelligence/
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── fetchers/
│   │   │   └── __init__.py
│   │   └── models/
│   │       └── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── metrics/
│   │   │   └── __init__.py
│   │   └── analysis/
│   │       └── __init__.py
│   ├── application/
│   │   ├── __init__.py
│   │   └── services/
│   │       └── __init__.py
│   └── presentation/
│       ├── __init__.py
│       ├── cli/
│       │   └── __init__.py
│       └── reports/
│           └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── data/
│   ├── domain/
│   └── application/
├── config/
├── docs/
└── requirements.txt
```

## Notes
Tempo totale stimato: ~55 minuti
```

**Labels:** `sprint-1`, `epic:setup`, `💻 coding`

---

### Issue 3 di 4

**Title:**
```
[US-1.2.1] Modellare un asset finanziario
```

**Body:**
```markdown
## User Story
Come sviluppatore, voglio una struttura dati per rappresentare un singolo asset finanziario (ETF, azione, etc.) con tutte le sue proprietà.

## Tasks
- [ ] **T-010** (~15min): 📚 Studiare dataclasses Python - leggere documentazione ufficiale
- [ ] **T-011** (~30min): Creare `src/data/models/asset.py` con dataclass `Asset`
- [ ] **T-012** (~15min): Aggiungere type hints completi e docstring descrittiva
- [ ] **T-013** (~30min): Creare primo test `tests/data/test_asset.py`

## Acceptance Criteria
- [ ] Dataclass `Asset` creata con campi: `ticker`, `name`, `asset_type`, `weight`
- [ ] Type hints presenti su tutti i campi
- [ ] Docstring che spiega lo scopo della classe
- [ ] Almeno 3 test che verificano creazione e validazione
- [ ] Test passano con `pytest`

## Campi Asset (proposta)
```python
@dataclass
class Asset:
    ticker: str          # Es: "VWCE.MI"
    name: str            # Es: "Vanguard FTSE All-World"
    asset_type: str      # Es: "ETF", "Stock", "Bond"
    weight: float        # Es: 0.25 (25% del portafoglio)
```

## Notes
Tempo totale stimato: ~1 ora 30 minuti

Risorse:
- https://docs.python.org/3/library/dataclasses.html
- Installare pytest: `pip install pytest`
```

**Labels:** `sprint-1`, `epic:setup`, `💻 coding`, `📚 learning`

---

### Issue 4 di 4

**Title:**
```
[US-1.2.2] Modellare un portafoglio
```

**Body:**
```markdown
## User Story
Come sviluppatore, voglio una struttura dati per rappresentare un portafoglio composto da più asset, con metodi per calcolare informazioni aggregate.

## Tasks
- [ ] **T-014** (~30min): Creare `src/data/models/portfolio.py` con dataclass `Portfolio`
- [ ] **T-015** (~20min): Implementare metodo per calcolare/verificare peso % totale
- [ ] **T-016** (~30min): Creare test `tests/data/test_portfolio.py`

## Acceptance Criteria
- [ ] Dataclass `Portfolio` creata con lista di `Asset`
- [ ] Metodo `total_weight()` che somma i pesi
- [ ] Metodo `validate()` che verifica che i pesi sommino a ~1.0
- [ ] Metodo per ottenere un asset by ticker
- [ ] Test coprono tutti i metodi

## Struttura Portfolio (proposta)
```python
@dataclass
class Portfolio:
    name: str
    assets: list[Asset]
    
    def total_weight(self) -> float:
        """Ritorna la somma dei pesi di tutti gli asset"""
        pass
    
    def is_valid(self) -> bool:
        """Verifica che i pesi sommino a 1.0 (con tolleranza)"""
        pass
    
    def get_asset(self, ticker: str) -> Asset | None:
        """Trova un asset per ticker"""
        pass
```

## Notes
Tempo totale stimato: ~1 ora 20 minuti

Dipende da: US-1.2.1 (Asset deve esistere)
```

**Labels:** `sprint-1`, `epic:setup`, `💻 coding`, `🧪 testing`

---

## Step 7: Organizza nel Project Board

Dopo aver creato le 4 issue:

1. Vai nel **Project Board**
2. Trascina tutte e 4 le issue nella colonna **📋 Backlog**
3. Quando sei pronto a iniziare, sposta **[US-1.1.1]** in **🎯 Sprint Backlog**

### Ordine di esecuzione Sprint 1

```
1. [US-1.1.1] Ambiente Python       ← Inizia da qui
2. [US-1.1.2] Struttura cartelle    ← Poi questa
3. [US-1.2.1] Asset dataclass       ← Poi questa
4. [US-1.2.2] Portfolio dataclass   ← Infine questa
```

---

## Step 8: Workflow Quotidiano

### Inizio sessione
1. Apri il Project Board
2. Prendi la prima issue da "Sprint Backlog"
3. Spostala in "In Progress"
4. Lavora sui task (spunta i checkbox man mano)

### Durante il lavoro
Commit frequenti con riferimento alla issue:
```bash
git commit -m "feat: add Asset dataclass #3"
```
Il `#3` (numero issue) crea un link automatico.

### Fine issue
1. Tutti i checkbox spuntati
2. Sposta issue in "Review" 
3. Verifica acceptance criteria
4. Se tutto ok → "Done"
5. Passa alla issue successiva

### Fine sprint
1. Tutte le issue in "Done"
2. Crea tag: `git tag -a v0.1.0 -m "Sprint 1 complete"`
3. Crea le issue per Sprint 2

---

## Comandi Git Utili

```bash
# Inizio giornata
git pull origin main

# Commit con riferimento issue
git commit -m "feat: implement Asset dataclass

- Add ticker, name, asset_type, weight fields
- Add type hints and validation

Refs #3"

# Push
git push origin main

# Tag fine sprint
git tag -a v0.1.0 -m "Sprint 1: Foundations complete"
git push origin --tags
```

---

## 🎯 Ricorda

Non serve creare TUTTE le issue subito. Crea solo quelle dello sprint corrente:
- Ora: Issue Sprint 1 (queste 4)
- Fine Sprint 1: Crea Issue Sprint 2
- E così via...

L'obiettivo è **imparare**, non avere il board perfetto.
