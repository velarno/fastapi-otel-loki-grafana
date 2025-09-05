import logging
import logging.config
import yaml
from pathlib import Path

app_dir = Path(__file__).parent
root_dir = app_dir.parent
config_dir = root_dir / 'config'

def setup_logging():
    """
    Set up logging configuration from YAML file
    """
    config_path = config_dir / 'logging_config.yaml'
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    logging.config.dictConfig(config)


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger configured from YAML
    """
    return logging.getLogger(name)

setup_logging()