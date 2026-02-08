"""
Loader per configurazione YAML.
"""
import yaml
from pathlib import Path
from src.data.models.asset import Asset
from src.data.models.portfolio import Portfolio


def load_portfolio(config_path: str = "config/portfolio.yaml") -> Portfolio:
    """
    Carica un portafoglio da file YAML.
    
    Args:
        config_path: Percorso al file di configurazione
    
    Returns:
        Portfolio configurato
    
    Raises:
        FileNotFoundError: Se il file non esiste
        ValueError: Se il formato non è valido
    """
    path = Path(config_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File di configurazione non trovato: {config_path}")
    
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    
    if not config or 'assets' not in config:
        raise ValueError("Formato configurazione non valido")
    
    assets = []
    for asset_config in config['assets']:
        asset = Asset(
            ticker=asset_config['ticker'],
            name=asset_config['name'],
            asset_type=asset_config['type'],
            weight=asset_config['weight'],
        )
        assets.append(asset)
    
    return Portfolio(
        name=config.get('name', 'Portfolio'),
        assets=assets,
    )