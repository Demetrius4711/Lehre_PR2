"""Hilfsfunktionen für das Projekt."""


def format_string(text):
    """Formatiert einen String."""
    return text.strip().lower()


def validate_email(email):
    """Validiert eine E-Mail-Adresse."""
    return "@" in email and "." in email
