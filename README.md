![CI](https://github.com/ernestoalbarez/playwright-python-automation-skeleton/actions/workflows/ci.yml/badge.svg)
![Lint](https://img.shields.io/badge/lint-ruff-blue?logo=ruff)
![Python](https://img.shields.io/badge/python-3.11+-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/playwright-e2e-45ba63?logo=playwright)
![License](https://img.shields.io/badge/license-MIT-green)

# Playwright Python Automation Skeleton

## Overview

This repository provides a **professional, enterprise-ready skeleton** for building end-to-end automation projects using **Playwright with Python**.

It is designed as a **reusable template** that prioritizes scalability, type safety, and developer experience. Unlike basic scripts, this skeleton implements a robust Page Object Model (POM), centralized configuration, and professional reporting.

## Key Features

- **Scalable Architecture**: Separation of concerns between tests, pages, and locators.
- **Robust Configuration**: Environment-based settings (Local, Staging, Prod) with validation.
- **Professional Reporting**: Integrated **Allure Results** and automatic **screenshots on failure**.
- **Static Type Safety**: Fully typed codebase with **mypy** strict mode.
- **CI/CD Ready**: Pre-configured **GitHub Actions** with browser caching.
- **Standard Tooling**: Uses **Pytest**, **Ruff** (linting), and **Black** (formatting).

---

## Project Structure

```text
.
├── .github/workflows/  # CI/CD pipeline definitions
├── config/             # Environment & browser settings
├── locators/           # Isolated UI selectors
├── pages/              # Page Object definitions (behavior & assertions)
├── tests/              # Test suites (Smoke, Regression, etc.)
├── utils/              # Shared browser & utility helpers
├── pyproject.toml      # Dependency & tool configuration
└── pytest.ini          # Pytest execution settings
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- uv (Python package manager)
- [Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline) (for reporting)

### Installation

1. **Clone the template**:
   ```bash
   git clone git@github.com:ernestoalbarez/playwright-python-automation-skeleton.git
   cd playwright-python-automation-skeleton
   ```

2. **Install uv**:
   ```bash
   curl -Ls https://astral.sh/uv/install.sh | sh
   ```

3. **Set up virtual environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate  # Windows
   ```

4. **Install dependencies**:
   ```bash
   uv sync
   uv run playwright install --with-deps
   ```

5. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

---

## Running Tests

### Execute all tests
```bash
uv run pytest
```

### Run with different environment
```bash
ENV=staging uv run pytest
```

### Run in a specific browser
```bash
BROWSER=firefox uv run pytest
```

### Generate and View Allure Report
```bash
allure serve allure-results
```

---

## CI Status

This project runs:

- Lint (Ruff)
- Format check (Black)
- Type checking (mypy)
- Playwright E2E tests

---

## Configuration

Settings are managed in `config/settings.py` and can be overridden via environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `ENV` | Environment (local, staging, prod) | `local` |
| `BROWSER` | chromium, firefox, webkit | `chromium` |
| `HEADLESS` | Run in headless mode | `true` |
| `TIMEOUT_MS` | Global timeout in ms | `30000` |

---

## Design Philosophy

- **Typed Everything**: Use type hints for better IDE support and fewer runtime errors.
- **Native Assertions**: Favor Playwright's `expect` for its built-in polling/retry logic.
- **Locator Isolation**: Keep selectors out of Page Objects to handle UI changes easier.
- **Clean Fixtures**: Use `conftest.py` for standard lifecycle management without bloating tests.

---

## License

This project is licensed under the **MIT License**.
