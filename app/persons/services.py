"""
Service layer for Person API calls.
Implements CQRS pattern: Commands → MySQL (port 3000), Queries → MongoDB (port 3001)
"""
import requests
from django.conf import settings
from typing import Optional


class PersonService:
    """Service for managing Person CRUD operations."""
    
    def __init__(self):
        self.command_url = f"{settings.API_COMMAND_URL}/persons"
        self.query_url = f"{settings.API_QUERY_URL}/persons"
    
    def list(self) -> list[dict]:
        """List all persons (QUERY → MongoDB)."""
        try:
            response = requests.get(self.query_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching persons: {e}")
            return []
    
    def get(self, person_id: str) -> Optional[dict]:
        """Get a person by ID (QUERY → MongoDB)."""
        try:
            response = requests.get(f"{self.query_url}/{person_id}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching person {person_id}: {e}")
            return None
    
    def create(self, data: dict) -> Optional[dict]:
        """Create a new person (COMMAND → MySQL)."""
        try:
            response = requests.post(
                self.command_url,
                json=data,
                timeout=10,
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error creating person: {e}")
            return None
    
    def update(self, person_id: str, data: dict) -> Optional[dict]:
        """Update an existing person (COMMAND → MySQL)."""
        try:
            response = requests.patch(
                f"{self.command_url}/{person_id}",
                json=data,
                timeout=10,
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error updating person {person_id}: {e}")
            return None
    
    def delete(self, person_id: str) -> bool:
        """Delete a person (COMMAND → MySQL)."""
        try:
            response = requests.delete(f"{self.command_url}/{person_id}", timeout=10)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Error deleting person {person_id}: {e}")
            return False


# Singleton instance
person_service = PersonService()
