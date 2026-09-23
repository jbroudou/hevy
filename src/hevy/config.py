"""Configuration management for the project."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class ConfigError(RuntimeError):
    """Raised when required configuration is missing or invalid."""


class Config:
    """Application configuration loaded from environment variables."""

    # Project settings
    PROJECT_NAME = os.getenv("PROJECT_NAME", "hevy")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    # The CLI prints its own user-facing errors, so the console handler stays
    # quiet by default; raise it to DEBUG/INFO when troubleshooting.
    LOG_CONSOLE_LEVEL = os.getenv("LOG_CONSOLE_LEVEL", "CRITICAL")
    LOG_DIR = Path(__file__).parent.parent.parent / "log"

    # Hevy API settings
    HEVY_API_KEY = os.getenv("HEVY_API_KEY", "")
    HEVY_API_BASE_URL = os.getenv("HEVY_API_BASE_URL", "https://api.hevyapp.com")

    # The Hevy API caps pageSize at 10 on every paginated endpoint.
    HEVY_MAX_PAGE_SIZE = 10

    @classmethod
    def validate(cls):
        """Validate required configuration values."""
        cls.LOG_DIR.mkdir(exist_ok=True)
        if not cls.HEVY_API_KEY:
            raise ConfigError(
                "HEVY_API_KEY is not set. Add it to your .env file "
                "(get a key at https://hevy.com/settings?developer)."
            )


config = Config()
