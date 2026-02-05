"""
Global pytest configuration and fixtures.

This module defines shared fixtures used across the test suite, including:
- Playwright lifecycle management
- Browser, context, and page setup/teardown
- Centralized configuration via settings

Design goals:
- Single Playwright instance per session
- Single browser per session
- Isolated browser context per test
- Clean, explicit lifecycle management
- CI-friendly and locally debuggable
"""

import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)

from config import settings
from utils.browser import launch_browser


@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    """
    Starts a single Playwright instance for the entire test session.

    Session scope avoids unnecessary startup overhead and mirrors
    Playwright's intended lifecycle usage.
    """
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    """
    Launches a single browser for the entire test session.

    Browser type, headless mode, and slow motion are fully driven
    by environment-based settings.
    """
    browser = launch_browser(
        playwright=playwright_instance,
        browser_name=settings.BROWSER,
        headless=settings.HEADLESS,
        slow_mo=settings.SLOW_MO,
    )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    """
    Creates a fresh browser context per test.

    This guarantees full test isolation (cookies, storage, cache),
    while still reusing the same browser process for performance.
    """
    context = browser.new_context(
        base_url=settings.BASE_URL,
        viewport=settings.VIEWPORT,
    )

    # Apply timeouts at the context level
    context.set_default_timeout(settings.TIMEOUT)
    context.set_default_navigation_timeout(settings.NAVIGATION_TIMEOUT)

    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """
    Provides a clean Page instance for each test.

    Page-level default timeout is aligned with context settings
    to ensure consistent behavior across all interactions.
    """
    page = context.new_page()

    # Explicitly set page timeout for clarity and future overrides
    page.set_default_timeout(settings.TIMEOUT)

    yield page
    page.close()
