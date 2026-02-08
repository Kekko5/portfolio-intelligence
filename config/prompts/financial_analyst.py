"""
Prompt templates per l'analisi finanziaria.
"""

SYSTEM_PROMPT = """Sei un analista finanziario esperto e consulente per investitori individuali.

Il tuo compito è analizzare i dati di portafoglio e fornire insight chiari, utili e personalizzati.

Linee guida:
- Usa un linguaggio semplice, evita gergo tecnico non necessario
- Sii conciso ma completo
- Evidenzia sia aspetti positivi che aree di miglioramento
- Non dare consigli di investimento specifici ("compra X"), ma suggerisci considerazioni
- Contestualizza i numeri (es. "una volatilità del 15% è nella media per un portafoglio azionario")
- Se i dati mostrano rischi, segnalali con chiarezza ma senza allarmismo

Formato risposta:
- Inizia con un riassunto di 1-2 frasi
- Poi analizza i punti chiave
- Concludi con 1-2 suggerimenti pratici
"""

PORTFOLIO_ANALYSIS_TEMPLATE = """Analizza questo portafoglio:

**Nome portafoglio:** {portfolio_name}
**Periodo analizzato:** {period}

**Metriche aggregate:**
- Rendimento totale: {total_return:.2%}
- CAGR: {cagr:.2%}
- Volatilità annualizzata: {volatility:.2%}

**Dettaglio per asset:**
{assets_detail}

Fornisci un'analisi del portafoglio considerando:
1. Performance complessiva
2. Livello di rischio (volatilità e drawdown)
3. Rapporto rischio/rendimento (Sharpe ratio)
4. Eventuali suggerimenti per migliorare la diversificazione
"""


def format_portfolio_prompt(report) -> str:
    """
    Formatta il prompt per l'analisi del portafoglio.
    
    Args:
        report: PortfolioReport con i dati da analizzare
    
    Returns:
        Prompt formattato
    """
    # Formatta dettaglio asset
    assets_lines = []
    for ticker, analysis in report.assets.items():
        line = (
            f"- {ticker}: rendimento {analysis.total_return:.2%}, "
            f"volatilità {analysis.volatility:.2%}, "
            f"Sharpe {analysis.sharpe_ratio:.2f}, "
            f"max drawdown {analysis.max_drawdown:.2%}"
        )
        assets_lines.append(line)
    
    assets_detail = "\n".join(assets_lines)
    
    return PORTFOLIO_ANALYSIS_TEMPLATE.format(
        portfolio_name=report.portfolio_name,
        period=report.period,
        total_return=report.portfolio_return,
        cagr=report.portfolio_cagr,
        volatility=report.portfolio_volatility,
        assets_detail=assets_detail,
    )