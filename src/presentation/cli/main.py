"""
CLI per Portfolio Intelligence.
"""
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import Optional

from src.data.models.asset import Asset
from src.data.models.portfolio import Portfolio
from src.application.services.analysis_service import AnalysisService

# Inizializza Typer e Rich
app = typer.Typer(help="Portfolio Intelligence - Analizza il tuo portafoglio")
console = Console()


@app.command()
def analyze(
    period: str = typer.Option("1y", "--period", "-p", help="Periodo di analisi (es. 3mo, 1y, 2y)"),
    no_ai: bool = typer.Option(False, "--no-ai", help="Disabilita insight AI"),
):
    """
    Analizza il portafoglio e mostra le metriche.
    """
    console.print("\n[bold blue]📊 Portfolio Intelligence[/bold blue]\n")
    
    # Portfolio di esempio (dopo lo caricheremo da YAML)
    assets = [
        Asset(ticker="VWCE.MI", name="Vanguard All-World", asset_type="ETF", weight=0.6),
        Asset(ticker="AGGH.MI", name="iShares Global Bond", asset_type="ETF", weight=0.4),
    ]
    portfolio = Portfolio(name="My Portfolio", assets=assets)
    
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
        # Colora in base al valore
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


if __name__ == "__main__":
    app()