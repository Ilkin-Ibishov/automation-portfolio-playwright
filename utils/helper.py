"""
Utility functions for test data generation and common operations.
"""
import uuid
from typing import TypedDict


class APIResponse(TypedDict, total=False):
    """Typed structure for API responses from automationexercise.com."""
    responseCode: int
    message: str
    products: list
    user_id: int


def get_unique_email(prefix: str = "testuser") -> str:
    """
    Generate a unique email address for test isolation.
    
    Args:
        prefix: Email prefix before the unique identifier.
    
    Returns:
        Unique email in format: {prefix}_{uuid}@example.com
    """
    return f"{prefix}_{uuid.uuid4().hex[:8]}@example.com"


def parse_api_response(response) -> APIResponse:
    """
    Parse API response and return typed dict.
    
    Args:
        response: Playwright APIResponse object.
    
    Returns:
        Parsed response body as APIResponse TypedDict.
    
    Raises:
        ValueError: If response body is not valid JSON.
    """
    import json
    try:
        return json.loads(response.text())
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON response: {response.text()}") from e