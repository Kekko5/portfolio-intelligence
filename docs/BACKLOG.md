# Portfolio Intelligence System — Product Backlog

## Legenda

| Label | Significato |
|-------|-------------|
| 🟢 | Ready to start |
| 🟡 | In progress |
| 🔵 | Done |
| 🔴 | Blocked |
| 📚 | Learning focus |
| 💻 | Coding focus |
| 🧪 | Testing focus |

---

# 🏃 SPRINT 1: Foundations
> **Goal**: Setup ambiente, struttura progetto, primi modelli dati
> **Durata**: ~3-4 ore totali

## Epic 1.1: Environment Setup

### US-1.1.1: Come sviluppatore, voglio un ambiente Python configurato correttamente
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-001 | Installare Python 3.12+ e verificare `python --version` | 15min | 💻 | 🟢 |
| T-002 | Creare repository GitHub `portfolio-intelligence` | 10min | 💻 | 🟢 |
| T-003 | Clonare repo e creare virtual environment | 15min | 💻 | 🟢 |
| T-004 | Creare `.gitignore` per Python | 10min | 💻 | 🟢 |
| T-005 | Creare `requirements.txt` iniziale (vuoto) | 5min | 💻 | 🟢 |

### US-1.1.2: Come sviluppatore, voglio una struttura cartelle professionale
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-006 | Creare struttura cartelle `src/` con tutti i package | 20min | 💻 | 🟢 |
| T-007 | Creare tutti i file `__init__.py` | 10min | 💻 | 🟢 |
| T-008 | Creare cartella `tests/` con struttura mirror | 15min | 💻 | 🟢 |
| T-009 | Creare `docs/` e copiare PROJECT_CHARTER e BACKLOG | 10min | 💻 | 🟢 |

## Epic 1.2: First Data Models

### US-1.2.1: Come sviluppatore, voglio modellare un asset finanziario
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-010 | 📚 Studiare dataclasses Python (15min lettura) | 15min | 📚 | 🟢 |
| T-011 | Creare `src/data/models/asset.py` con dataclass Asset | 30min | 💻 | 🟢 |
| T-012 | Aggiungere type hints e docstring | 15min | 💻 | 🟢 |
| T-013 | Creare primo test `tests/data/test_asset.py` | 30min | 🧪 | 🟢 |

### US-1.2.2: Come sviluppatore, voglio modellare un portafoglio
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-014 | Creare `src/data/models/portfolio.py` con dataclass Portfolio | 30min | 💻 | 🟢 |
| T-015 | Implementare metodo per calcolare peso % di ogni asset | 20min | 💻 | 🟢 |
| T-016 | Test per Portfolio | 30min | 🧪 | 🟢 |

**📝 Sprint 1 Deliverables:**
- [ ] Repo GitHub funzionante
- [ ] Struttura cartelle completa
- [ ] Modelli Asset e Portfolio con test
- [ ] Primo commit "Sprint 1 complete"

---

# 🏃 SPRINT 2: Data Layer
> **Goal**: Recuperare dati reali da Yahoo Finance
> **Durata**: ~4 ore totali

## Epic 2.1: External Data Fetching

### US-2.1.1: Come utente, voglio recuperare prezzi storici di un ETF
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-017 | 📚 Studiare yfinance library (docs + esempi) | 20min | 📚 | 🟢 |
| T-018 | Aggiungere `yfinance` a requirements.txt | 5min | 💻 | 🟢 |
| T-019 | Creare `src/data/fetchers/yahoo_fetcher.py` | 45min | 💻 | 🟢 |
| T-020 | Implementare `fetch_historical_prices(ticker, period)` | 30min | 💻 | 🟢 |
| T-021 | Gestire errori (ticker non valido, network error) | 30min | 💻 | 🟢 |

### US-2.1.2: Come sviluppatore, voglio dati strutturati e tipizzati
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-022 | Creare dataclass `PriceData` per prezzi storici | 20min | 💻 | 🟢 |
| T-023 | Creare dataclass `AssetInfo` per metadata (nome, currency, etc) | 20min | 💻 | 🟢 |
| T-024 | Convertire output yfinance in dataclass custom | 30min | 💻 | 🟢 |

## Epic 2.2: Error Handling Pattern

### US-2.2.1: Come sviluppatore, voglio gestione errori consistente
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-025 | 📚 Studiare custom exceptions in Python | 15min | 📚 | 🟢 |
| T-026 | Creare `src/data/exceptions.py` con eccezioni custom | 20min | 💻 | 🟢 |
| T-027 | Refactoring fetcher per usare eccezioni custom | 20min | 💻 | 🟢 |
| T-028 | Test per casi di errore | 30min | 🧪 | 🟢 |

**📝 Sprint 2 Deliverables:**
- [ ] Fetcher Yahoo Finance funzionante
- [ ] Dataclass per price data
- [ ] Gestione errori robusta
- [ ] Test coverage data layer

---

# 🏃 SPRINT 3: Core Algorithms (Part 1)
> **Goal**: Implementare metriche finanziarie base da zero
> **Durata**: ~4-5 ore totali

## Epic 3.1: Returns Calculation

### US-3.1.1: Come utente, voglio calcolare il rendimento di un asset
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-029 | 📚 Teoria: rendimento semplice vs logaritmico | 20min | 📚 | 🟢 |
| T-030 | Creare `src/domain/metrics/returns.py` | 15min | 💻 | 🟢 |
| T-031 | Implementare `simple_return(price_start, price_end)` | 20min | 💻 | 🟢 |
| T-032 | Implementare `log_return(price_start, price_end)` | 20min | 💻 | 🟢 |
| T-033 | Implementare `returns_series(prices)` per lista prezzi | 30min | 💻 | 🟢 |
| T-034 | Test con casi noti (calcoli manuali) | 30min | 🧪 | 🟢 |

### US-3.1.2: Come utente, voglio calcolare rendimento composto
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-035 | 📚 Teoria: compound annual growth rate (CAGR) | 15min | 📚 | 🟢 |
| T-036 | Implementare `cagr(price_start, price_end, years)` | 30min | 💻 | 🟢 |
| T-037 | Implementare `total_return(prices)` | 20min | 💻 | 🟢 |
| T-038 | Test CAGR con dati reali verificabili | 30min | 🧪 | 🟢 |

## Epic 3.2: Volatility Calculation

### US-3.2.1: Come utente, voglio misurare la volatilità di un asset
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-039 | 📚 Teoria: deviazione standard e varianza | 20min | 📚 | 🟢 |
| T-040 | Creare `src/domain/metrics/volatility.py` | 15min | 💻 | 🟢 |
| T-041 | Implementare `variance(values)` DA ZERO (no numpy) | 30min | 💻 | 🟢 |
| T-042 | Implementare `std_dev(values)` DA ZERO | 20min | 💻 | 🟢 |
| T-043 | Implementare `annualized_volatility(daily_returns)` | 30min | 💻 | 🟢 |
| T-044 | Test e confronto con numpy per validazione | 30min | 🧪 | 🟢 |

**📝 Sprint 3 Deliverables:**
- [ ] Modulo returns completo e testato
- [ ] Modulo volatility completo e testato
- [ ] Comprensione profonda degli algoritmi
- [ ] LEARNINGS.md aggiornato con formule e intuizioni

---

# 🏃 SPRINT 4: Core Algorithms (Part 2) + Clean Code
> **Goal**: Metriche avanzate + refactoring SOLID
> **Durata**: ~5 ore totali

## Epic 4.1: Advanced Metrics

### US-4.1.1: Come utente, voglio vedere la correlazione tra asset
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-045 | 📚 Teoria: correlazione di Pearson | 20min | 📚 | 🟢 |
| T-046 | Creare `src/domain/metrics/correlation.py` | 15min | 💻 | 🟢 |
| T-047 | Implementare `covariance(x, y)` DA ZERO | 30min | 💻 | 🟢 |
| T-048 | Implementare `pearson_correlation(x, y)` DA ZERO | 30min | 💻 | 🟢 |
| T-049 | Test con dataset dove correlazione è nota | 30min | 🧪 | 🟢 |

### US-4.1.2: Come utente, voglio valutare il risk-adjusted return
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-050 | 📚 Teoria: Sharpe Ratio e risk-free rate | 20min | 📚 | 🟢 |
| T-051 | Creare `src/domain/metrics/ratios.py` | 15min | 💻 | 🟢 |
| T-052 | Implementare `sharpe_ratio(returns, risk_free_rate)` | 30min | 💻 | 🟢 |
| T-053 | Implementare `max_drawdown(prices)` | 40min | 💻 | 🟢 |
| T-054 | Test ratios | 30min | 🧪 | 🟢 |

## Epic 4.2: SOLID Refactoring

### US-4.2.1: Come sviluppatore, voglio codice che rispetti SOLID
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-055 | 📚 Studiare SOLID principles con esempi Python | 30min | 📚 | 🟢 |
| T-056 | Refactoring: Single Responsibility sui moduli metrics | 30min | 💻 | 🟢 |
| T-057 | Creare interfaccia `MetricCalculator` (Protocol) | 30min | 💻 | 🟢 |
| T-058 | Applicare Dependency Inversion al fetcher | 30min | 💻 | 🟢 |
| T-059 | Code review con Claude e fix | 30min | 💻 | 🟢 |

**📝 Sprint 4 Deliverables:**
- [ ] Correlazione e Sharpe Ratio implementati
- [ ] Max Drawdown implementato
- [ ] Codice refactored secondo SOLID
- [ ] Test coverage domain layer > 80%

---

# 🏃 SPRINT 5: Application Layer + Portfolio Analysis
> **Goal**: Orchestrare tutto in un servizio coeso
> **Durata**: ~4 ore totali

## Epic 5.1: Portfolio Analyzer Service

### US-5.1.1: Come utente, voglio analizzare il mio intero portafoglio
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-060 | Creare `src/domain/analysis/portfolio_analyzer.py` | 30min | 💻 | 🟢 |
| T-061 | Implementare aggregazione metriche per portafoglio | 45min | 💻 | 🟢 |
| T-062 | Calcolare rendimento portafoglio pesato | 30min | 💻 | 🟢 |
| T-063 | Calcolare volatilità portafoglio (con correlazioni) | 45min | 💻 | 🟢 |

### US-5.1.2: Come sviluppatore, voglio un service layer pulito
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-064 | Creare `src/application/services/analysis_service.py` | 30min | 💻 | 🟢 |
| T-065 | Implementare `AnalysisService.analyze_portfolio()` | 45min | 💻 | 🟢 |
| T-066 | Creare dataclass `PortfolioReport` per output | 30min | 💻 | 🟢 |
| T-067 | Integration test del service | 30min | 🧪 | 🟢 |

**📝 Sprint 5 Deliverables:**
- [ ] PortfolioAnalyzer funzionante
- [ ] AnalysisService che orchestra tutto
- [ ] PortfolioReport strutturato
- [ ] Integration test

---

# 🏃 SPRINT 6: AI Integration
> **Goal**: Integrare Claude per insight qualitativi
> **Durata**: ~4-5 ore totali

## Epic 6.1: Claude API Integration

### US-6.1.1: Come utente, voglio insight AI sul mio portafoglio
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-068 | 📚 Studiare Anthropic API docs | 30min | 📚 | 🟢 |
| T-069 | Creare account Anthropic e ottenere API key | 15min | 💻 | 🟢 |
| T-070 | Aggiungere `anthropic` a requirements.txt | 5min | 💻 | 🟢 |
| T-071 | Creare `src/data/fetchers/ai_client.py` | 30min | 💻 | 🟢 |
| T-072 | Implementare wrapper base per Claude API | 30min | 💻 | 🟢 |

### US-6.1.2: Come sviluppatore, voglio prompt engineering efficace
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-073 | Creare `config/prompts/` per system prompts | 20min | 💻 | 🟢 |
| T-074 | Scrivere system prompt per analista finanziario | 45min | 💻 | 🟢 |
| T-075 | Creare template prompt per portfolio analysis | 30min | 💻 | 🟢 |
| T-076 | Iterare e testare qualità risposte | 45min | 💻 | 🟢 |
| T-077 | Implementare parsing output strutturato | 30min | 💻 | 🟢 |

## Epic 6.2: AI-Enhanced Analysis Service

### US-6.2.1: Come utente, voglio report con insight AI integrati
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-078 | Estendere AnalysisService con AI insights | 30min | 💻 | 🟢 |
| T-079 | Creare `AIInsight` dataclass | 20min | 💻 | 🟢 |
| T-080 | Integrare insight in PortfolioReport | 30min | 💻 | 🟢 |
| T-081 | Gestire fallback se AI non disponibile | 20min | 💻 | 🟢 |

**📝 Sprint 6 Deliverables:**
- [ ] Integrazione Claude API funzionante
- [ ] System prompt ottimizzato
- [ ] Insight AI nel report
- [ ] Gestione errori/fallback

---

# 🏃 SPRINT 7: CLI + Reports
> **Goal**: Interfaccia utente da terminale e export
> **Durata**: ~4 ore totali

## Epic 7.1: Command Line Interface

### US-7.1.1: Come utente, voglio usare il tool da terminale
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-082 | 📚 Studiare Typer library | 20min | 📚 | 🟢 |
| T-083 | Aggiungere `typer` e `rich` a requirements | 5min | 💻 | 🟢 |
| T-084 | Creare `src/presentation/cli/main.py` | 30min | 💻 | 🟢 |
| T-085 | Implementare comando `analyze` | 45min | 💻 | 🟢 |
| T-086 | Aggiungere opzioni (--period, --format, etc) | 30min | 💻 | 🟢 |
| T-087 | Output formattato con Rich | 30min | 💻 | 🟢 |

## Epic 7.2: Report Generation

### US-7.2.1: Come utente, voglio esportare report in Markdown
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-088 | Creare `src/presentation/reports/markdown_report.py` | 30min | 💻 | 🟢 |
| T-089 | Implementare template Markdown | 30min | 💻 | 🟢 |
| T-090 | Aggiungere grafici ASCII per trend | 30min | 💻 | 🟢 |
| T-091 | Comando CLI `--export markdown` | 20min | 💻 | 🟢 |

## Epic 7.3: Configuration

### US-7.3.1: Come utente, voglio configurare il mio portafoglio da file
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-092 | Creare `config/portfolio.yaml` schema | 20min | 💻 | 🟢 |
| T-093 | Implementare loader YAML | 30min | 💻 | 🟢 |
| T-094 | Configurare il TUO portafoglio reale | 20min | 💻 | 🟢 |

**📝 Sprint 7 Deliverables:**
- [ ] CLI funzionante con Typer
- [ ] Export Markdown
- [ ] Configurazione YAML
- [ ] README con usage examples

---

# 🏃 SPRINT 8: Cloud Deploy + CI/CD
> **Goal**: Deploy e automazione
> **Durata**: ~4-5 ore totali

## Epic 8.1: Continuous Integration

### US-8.1.1: Come sviluppatore, voglio CI automatica
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-095 | 📚 Studiare GitHub Actions basics | 20min | 📚 | 🟢 |
| T-096 | Creare `.github/workflows/ci.yml` | 30min | 💻 | 🟢 |
| T-097 | Configurare linting (ruff) | 20min | 💻 | 🟢 |
| T-098 | Configurare test automatici | 20min | 💻 | 🟢 |
| T-099 | Configurare type checking (mypy) | 20min | 💻 | 🟢 |

## Epic 8.2: Cloud Deployment

### US-8.2.1: Come utente, voglio report automatici settimanali
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-100 | 📚 Studiare Railway/Render deployment | 20min | 📚 | 🟢 |
| T-101 | Creare account Railway/Render | 10min | 💻 | 🟢 |
| T-102 | Configurare secrets (API keys) | 20min | 💻 | 🟢 |
| T-103 | Deploy applicazione | 30min | 💻 | 🟢 |
| T-104 | Configurare cron job settimanale | 30min | 💻 | 🟢 |
| T-105 | Test end-to-end in cloud | 30min | 🧪 | 🟢 |

## Epic 8.3: Documentation

### US-8.3.1: Come sviluppatore, voglio documentazione completa
| ID | Task | Tempo | Label | Status |
|----|------|-------|-------|--------|
| T-106 | Scrivere README.md professionale | 45min | 💻 | 🟢 |
| T-107 | Documentare architettura in ARCHITECTURE.md | 30min | 💻 | 🟢 |
| T-108 | Finalizzare LEARNINGS.md | 30min | 💻 | 🟢 |
| T-109 | Aggiungere docstring mancanti | 30min | 💻 | 🟢 |

**📝 Sprint 8 Deliverables:**
- [ ] CI/CD funzionante
- [ ] Deploy cloud attivo
- [ ] Report settimanale automatico
- [ ] Documentazione completa
- [ ] 🎉 Progetto completato!

---

# 📊 Tracking Progress

## Sprint Summary

| Sprint | Focus | Status | Completion |
|--------|-------|--------|------------|
| 1 | Foundations | 🟢 Ready | 0% |
| 2 | Data Layer | ⏳ Waiting | 0% |
| 3 | Algorithms Part 1 | ⏳ Waiting | 0% |
| 4 | Algorithms Part 2 + SOLID | ⏳ Waiting | 0% |
| 5 | Application Layer | ⏳ Waiting | 0% |
| 6 | AI Integration | ⏳ Waiting | 0% |
| 7 | CLI + Reports | ⏳ Waiting | 0% |
| 8 | Cloud + CI/CD | ⏳ Waiting | 0% |

## Velocity Tracking

| Sprint | Planned Tasks | Completed | Notes |
|--------|---------------|-----------|-------|
| 1 | 16 | - | - |
| 2 | 12 | - | - |
| 3 | 16 | - | - |
| 4 | 15 | - | - |
| 5 | 8 | - | - |
| 6 | 14 | - | - |
| 7 | 13 | - | - |
| 8 | 15 | - | - |

---

*Ultimo aggiornamento: Gennaio 2026*
