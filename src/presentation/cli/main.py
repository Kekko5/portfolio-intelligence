"""
CLI per Portfolio Intelligence.
"""
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from pathlib import Path

from src.application.services.analysis_service import AnalysisService
from src.presentation.cli.config_loader import load_portfolio

# Inizializza Typer e Rich
app = typer.Typer(help="Portfolio Intelligence - Analizza il tuo portafoglio")
console = Console()


@app.command()
def analyze(
    period: str = typer.Option("1y", "--period", "-p", help="Periodo di analisi (es. 3mo, 1y, 2y)"),
    config: str = typer.Option("config/portfolio.yaml", "--config", "-c", help="File di configurazione"),
    no_ai: bool = typer.Option(False, "--no-ai", help="Disabilita insight AI"),
    export: str = typer.Option(None, "--export", "-e", help="Esporta report in Markdown"),
):
    """
    Analizza il portafoglio e mostra le metriche.
    """
    console.print("\n[bold blue]📊 Portfolio Intelligence[/bold blue]\n")
    
    # Carica portfolio da YAML
    try:
        portfolio = load_portfolio(config)
    except FileNotFoundError:
        console.print(f"[red]Errore: File non trovato: {config}[/red]")
        raise typer.Exit(1)
    except ValueError as e:
        console.print(f"[red]Errore configurazione: {e}[/red]")
        raise typer.Exit(1)
    
    # Analizza
    with console.status("[bold green]Recupero dati e calcolo metriche..."):
        service = AnalysisService()
        report = service.analyze_portfolio(
            portfolio, 
            period=period, 
            include_ai_insight=not no_ai
        )
    
    # Mostra risultati
    _print_summary(report)
    _print_assets_table(report)
    
    if report.ai_insight and not no_ai:
        _print_ai_insight(report)
    
    # Export se richiesto
    if export:
        _export_markdown(report, export)
    
    console.print("\n[dim]Analisi completata.[/dim]\n")


def _print_summary(report):
    """Stampa il riepilogo del portafoglio."""
    summary = f"""[bold]{report.portfolio_name}[/bold]
Periodo: {report.period}

📈 Rendimento: [green]{report.portfolio_return:+.2%}[/green]
📊 CAGR: [green]{report.portfolio_cagr:+.2%}[/green]
📉 Volatilità: [yellow]{report.portfolio_volatility:.2%}[/yellow]
"""
    console.print(Panel(summary, title="Riepilogo", border_style="blue"))


def _print_assets_table(report):
    """Stampa la tabella degli asset."""
    table = Table(title="Dettaglio Asset")
    
    table.add_column("Ticker", style="cyan")
    table.add_column("Rendimento", justify="right")
    table.add_column("Volatilità", justify="right")
    table.add_column("Sharpe", justify="right")
    table.add_column("Max DD", justify="right")
    
    for ticker, analysis in report.assets.items():
        ret_color = "green" if analysis.total_return >= 0 else "red"
        sharpe_color = "green" if analysis.sharpe_ratio >= 1 else "yellow" if analysis.sharpe_ratio >= 0 else "red"
        
        table.add_row(
            ticker,
            f"[{ret_color}]{analysis.total_return:+.2%}[/{ret_color}]",
            f"{analysis.volatility:.2%}",
            f"[{sharpe_color}]{analysis.sharpe_ratio:.2f}[/{sharpe_color}]",
            f"[red]{analysis.max_drawdown:.2%}[/red]",
        )
    
    console.print(table)


def _print_ai_insight(report):
    """Stampa l'insight AI."""
    console.print(Panel(
        report.ai_insight.full_analysis,
        title="🤖 AI Insight",
        border_style="green"
    ))


def _export_markdown(report, filepath: str):
    """Esporta il report in Markdown."""
    md_content = f"""# Report Portafoglio: {report.portfolio_name}

**Data analisi:** {report.analysis_date.strftime('%Y-%m-%d %H:%M')}
**Periodo:** {report.period}

## Riepilogo

| Metrica | Valore |
|---------|--------|
| Rendimento | {report.portfolio_return:+.2%} |
| CAGR | {report.portfolio_cagr:+.2%} |
| Volatilità | {report.portfolio_volatility:.2%} |

## Dettaglio Asset

| Ticker | Rendimento | Volatilità | Sharpe | Max DD |
|--------|------------|------------|--------|--------|
"""
    
    for ticker, analysis in report.assets.items():
        md_content += f"| {ticker} | {analysis.total_return:+.2%} | {analysis.volatility:.2%} | {analysis.sharpe_ratio:.2f} | {analysis.max_drawdown:.2%} |\n"
    
    if report.ai_insight:
        md_content += f"\n## AI Insight\n\n{report.ai_insight.full_analysis}\n"
    
    Path(filepath).write_text(md_content)
    console.print(f"\n[green]✅ Report esportato in: {filepath}[/green]")


if __name__ == "__main__":
    app()