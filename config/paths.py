from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Folders
CORE_DIR = ROOT / 'core'
LOG_DIR = ROOT / 'logs'
API_DIR = ROOT / 'api'
UTILS_DIR = ROOT / 'utils'
OUTPUT_DIR = ROOT / 'outputs'

# Files 
TASK_LOG_FILE = LOG_DIR / 'agent.log'
ENV_FILE = ROOT / ".env"

def ensure_dirs():
    for path in [CORE_DIR, LOG_DIR, API_DIR, UTILS_DIR, OUTPUT_DIR]:
        path.mkdir(parents=True, exist_ok=True)