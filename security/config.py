"""Configuration module for the Personal Finance API.

This module defines security settings and global constants, such as
CORS (Cross-Origin Resource Sharing) permissions.

Attributes:
    ALLOWED_ORIGINS (list): A list of strings containing the authorized
        URLs that can interact with the API.
"""

ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
]
