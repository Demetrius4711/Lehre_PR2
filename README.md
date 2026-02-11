# MRT-Projekt2-Lehre 

## Beschreibung
Die Dokumentation und Sammlung von Skripten für das Verständnis der zu benutzenden Hardware
- Realsense D435   
- Orbbec Femtobolt

## Verwendung

Starten Sie die Anwendung:
```bash
python src/main.py
```

## Tests ausführen

```bash
pytest tests/
```

## Projektstruktur
my_python_project/
│
├── .venv/                      # Virtuelle Umgebung (nicht in Git)
│
├── src/                        # Hauptquellcode
│   ├── __init__.py
│   ├── main.py                 # Einstiegspunkt der Anwendung
│   ├── config.py               # Konfigurationsdateien
│   │
│   ├── Pipeline/               # Zusammenfassende Funktionen
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── services/               # Business Logic
│   │   ├── __init__.py
│   │   └── user_service.py
│   │
│   └── utils/                  # Hilfsfunktionen
│       ├── __init__.py
│       └── helpers.py
│
├── tests/                      # Unit- und Integrationstests
│   ├── __init__.py
│   ├── test_main.py
│   └── test_user_service.py
│
├── docs/                       # Dokumentation
│   ├── README.md
│   └── api_documentation.md
│
├── data/                       # Datendateien
│   ├── raw/                    # Rohdaten
│   └── processed/              # Verarbeitete Daten
│
├── scripts/                    # Skripte für Automatisierung
│   └── setup.py
│
├── .gitignore                  # Git-Ignorierung
├── .env.example                # Beispiel-Umgebungsvariablen
├── requirements.txt            # Projekt-Abhängigkeiten
├── setup.py                    # Package-Installation
├── README.md                   # Projektdokumentation
└── LICENSE                     # Lizenz


## Installation

1. Klonen Sie das Repository:
```bash
git clone https://github.com/username/my_python_project.git
cd my_python_project
```

2. Erstellen Sie eine virtuelle Umgebung:
```bash
python -m venv .venv
```

3. Aktivieren Sie die virtuelle Umgebung:
- Windows: `.venv\Scripts\activate`
- Linux/Mac: `source .venv/bin/activate`

4. Installieren Sie die Abhängigkeiten:
```bash
pip install -r requirements.txt
```

## Lizenz
MIT License
