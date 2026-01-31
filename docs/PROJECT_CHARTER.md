# Portfolio Intelligence System — Project Charter

## 🎯 Vision
Costruire un sistema di analisi portafoglio ETF che fornisca metriche quantitative e insight AI-driven, imparando Python, algoritmi, clean code, architettura software e cloud deployment.

---

## 📋 Informazioni progetto

| Campo | Valore |
|-------|--------|
| **Owner** | Francesco |
| **Inizio** | Gennaio 2026 |
| **Durata stimata** | 8-10 settimane (2-4h/settimana) |
| **Repository** | github.com/[username]/portfolio-intelligence |
| **Stack** | Python 3.12+, Claude API, Yahoo Finance API |

---

## 🎓 Obiettivi di apprendimento

### Python Fundamentals
- [ ] Virtual environments e dependency management
- [ ] Type hints e dataclasses
- [ ] Error handling strutturato
- [ ] Moduli e package

### Algoritmi
- [ ] Rendimento semplice e composto
- [ ] Volatilità (deviazione standard)
- [ ] Correlazione tra asset
- [ ] Sharpe Ratio
- [ ] Maximum Drawdown
- [ ] Media mobile (SMA, EMA)

### Clean Code & Architettura
- [ ] SOLID principles (almeno S, O, D)
- [ ] Layered architecture
- [ ] Unit testing con pytest
- [ ] Refactoring incrementale

### AI & Prompt Engineering
- [ ] Integrazione API Claude
- [ ] System prompt design
- [ ] Context management
- [ ] Output parsing strutturato

### Cloud & DevOps
- [ ] GitHub Actions (linting, testing)
- [ ] Deploy su Railway/Render
- [ ] Secrets management
- [ ] Scheduling job

---

## 📊 Criteri di successo

### MVP (Minimum Viable Product) — Sprint 1-4
- [ ] CLI funzionante che analizza una lista di ticker
- [ ] Calcolo metriche base (rendimento, volatilità)
- [ ] Output formattato su terminale
- [ ] Test coverage > 60% sul domain layer

### V1.0 — Sprint 5-6
- [ ] Integrazione AI per insight
- [ ] Report Markdown esportabile
- [ ] Configurazione portafoglio da file YAML

### V1.1 — Sprint 7-8
- [ ] Deploy cloud con scheduling settimanale
- [ ] GitHub Actions CI/CD
- [ ] Documentazione completa

---

## 🚫 Out of scope (per ora)
- Web UI / Dashboard
- Database persistente
- Backtesting strategie
- Trading automatico
- Multi-utente

*Questi possono diventare future evoluzioni dopo V1.1*

---

## 📁 Struttura repository target

```
portfolio-intelligence/
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── fetchers/
│   │   │   ├── __init__.py
│   │   │   └── yahoo_fetcher.py
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── asset.py
│   │       └── portfolio.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── metrics/
│   │   │   ├── __init__.py
│   │   │   ├── returns.py
│   │   │   ├── volatility.py
│   │   │   ├── correlation.py
│   │   │   └── ratios.py
│   │   └── analysis/
│   │       ├── __init__.py
│   │       └── portfolio_analyzer.py
│   ├── application/
│   │   ├── __init__.py
│   │   └── services/
│   │       ├── __init__.py
│   │       └── analysis_service.py
│   └── presentation/
│       ├── __init__.py
│       ├── cli/
│       │   ├── __init__.py
│       │   └── main.py
│       └── reports/
│           ├── __init__.py
│           └── markdown_report.py
├── tests/
│   ├── __init__.py
│   ├── data/
│   ├── domain/
│   │   └── metrics/
│   │       ├── test_returns.py
│   │       ├── test_volatility.py
│   │       └── test_correlation.py
│   └── application/
├── config/
│   ├── settings.py
│   └── portfolio.yaml
├── docs/
│   ├── PROJECT_CHARTER.md
│   ├── BACKLOG.md
│   ├── LEARNINGS.md
│   └── ARCHITECTURE.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

## 🔄 Workflow di sviluppo

1. **Prima di ogni sessione**: check backlog, scegli task
2. **Durante**: sviluppo + test + commit frequenti
3. **Dopo**: aggiorna task status, scrivi in LEARNINGS.md
4. **Fine sprint**: review con Claude, planning prossimo sprint

---

## 📝 Note
- Ogni modulo corrisponde a uno sprint di ~1 settimana
- I task sono dimensionati per sessioni da 30-60 minuti
- Meglio completare poco ma bene che avanzare senza capire
