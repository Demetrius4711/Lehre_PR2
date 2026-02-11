"""Tests für user_service.py."""
import pytest
from src.services.user_service import UserService


def test_get_user():
    """Testet die get_user Funktion."""
    service = UserService()
    user = service.get_user(1)
    assert user["id"] == 1


def test_create_user():
    """Testet die create_user Funktion."""
    service = UserService()
    user_data = {"name": "Test User", "email": "test@example.com"}
    result = service.create_user(user_data)
    assert result == user_data
