"""Konfigurationsdateien für das Projekt."""
import os
from pathlib import Path

# Basis-Verzeichnis
BASE_DIR = Path(__file__).resolve().parent.parent

# Datenverzeichnisse
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Weitere Konfigurationen hier
