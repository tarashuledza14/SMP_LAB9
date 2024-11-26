import requests
from requests.exceptions import RequestException


class APIClient:
    """Client for interacting with the JSONPlaceholder API."""

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        """Initialize the API client."""
        pass

    def _get(self, endpoint: str):
        """Helper method to send a GET request to the API."""
        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Error while fetching data from {endpoint}: {e}")
            return None

    def get_data(self, endpoint: str):
        """Get data from a specified endpoint."""
        return self._get(endpoint)

    def get_data_by_id(self, endpoint: str, item_id: int):
        """Get data from a specified endpoint by ID."""
        return self._get(f"{endpoint}/{item_id}")

    def get_all_users(self):
        """Get all users."""
        return self.get_data("users")

    def get_user_by_id(self, user_id: int):
        """Get a user by their ID."""
        return self.get_data_by_id("users", user_id)

    def get_all_comments(self):
        """Get all comments."""
        return self.get_data("comments")

    def get_comment_by_id(self, comment_id: int):
        """Get a comment by its ID."""
        return self.get_data_by_id("comments", comment_id)
