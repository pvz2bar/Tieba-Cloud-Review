# -*- coding:utf-8 -*-
__all__ = ('SCRIPT_DIR', 'MODULE_DIR',
           'config')

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(sys.argv[0])
MODULE_DIR = Path(__file__).parent

config = None
try:
    with (SCRIPT_DIR.parent / 'config/config.json').open('r', encoding='utf-8') as file:
        config = json.load(file)
except Exception:
    log.critical("Unable to read config.json!")
    raise
