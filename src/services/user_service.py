"""User service module."""


class UserService:
    """Service für User-Business-Logic."""

    def __init__(self):
        """Initialisiert den User-Service."""
        pass

    def get_user(self, user_id):
        """Holt einen User anhand der ID."""
        return {"id": user_id, "name": "Beispiel User"}

    def create_user(self, user_data):
        """Erstellt einen neuen User."""
        return user_data
