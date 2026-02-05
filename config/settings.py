"""
Global configuration settings for the Playwright Python automation framework.

This module centralizes environment-aware configuration such as base URLs,
timeouts, browser options, and execution flags.

Design goals:
- Single source of truth for configuration
- Environment-variable driven (CI friendly)
- Immutable and explicit
- Safe defaults with early validation
"""

import os
from dataclasses import dataclass
from typing import Literal


def _get_env(name: str, default: str) -> str:
    """Read environment variable with a fallback default."""
    return os.getenv(name, default)


def _get_bool(name: str, default: bool) -> bool:
    """Read boolean environment variable."""
    return os.getenv(name, str(default)).lower() in {"1", "true", "yes", "on"}


def _get_int(name: str, default: int) -> int:
    """Read integer environment variable."""
    try:
        return int(os.getenv(name, default))
    except ValueError as exc:
        raise ValueError(f"Environment variable {name} must be an integer") from exc


@dataclass(frozen=True)
class Settings:
    """
    Immutable application settings.

    Values are resolved at import time from environment variables,
    making configuration explicit, predictable, and CI-friendly.
    """

    # Execution environment
    env: str = _get_env("ENV", "local")

    # Base URLs
    base_url: str = _get_env("BASE_URL", "https://example.com")

    # Browser configuration
    browser: Literal["chromium", "webkit"] = _get_env(
        "BROWSER", "chromium"
    )  # type: ignore[assignment]
    headless: bool = _get_bool("HEADLESS", True)
    slow_mo: int = _get_int("SLOW_MO", 0)

    # Timeouts (milliseconds)
    default_timeout: int = _get_int("DEFAULT_TIMEOUT", 30_000)
    navigation_timeout: int = _get_int("NAVIGATION_TIMEOUT", 30_000)

    # Viewport
    viewport_width: int = _get_int("VIEWPORT_WIDTH", 1280)
    viewport_height: int = _get_int("VIEWPORT_HEIGHT", 720)

    # Artifacts
    screenshots_dir: str = _get_env("SCREENSHOTS_DIR", "artifacts/screenshots")
    videos_dir: str = _get_env("VIDEOS_DIR", "artifacts/videos")
    traces_dir: str = _get_env("TRACES_DIR", "artifacts/traces")

    @property
    def viewport(self) -> dict[str, int]:
        """Return Playwright-compatible viewport configuration."""
        return {"width": self.viewport_width, "height": self.viewport_height}


# Global, immutable settings instance
settings = Settings()
