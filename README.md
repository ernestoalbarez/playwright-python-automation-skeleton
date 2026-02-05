# playwright-python-automation-skeleton

## Overview

This repository provides a **clean, minimal, and opinionated skeleton**
for building end-to-end automation projects using **Playwright with Python**.

It is intentionally designed as a **starting point**, not a full framework.
The goal is to offer a solid and reusable foundation that can be cloned and
adapted for different products, teams, or domains without inheriting
application-specific assumptions.

This repository is suitable for:
- Bootstrapping new automation projects quickly
- Serving as a shared base across multiple teams or products
- Demonstrating automation design and architectural decisions

---

## Design Goals

The skeleton focuses on:

- Clear and predictable project structure
- Strong separation of concerns (tests, pages, locators, utilities)
- Minimal abstractions that stay out of the way
- Easy extensibility for future needs (API mocking, fixtures, reporting, CI)
- Readability and maintainability over cleverness

---

## High-Level Project Structure

```
.
├── tests/        # Test specifications
├── pages/        # Page Objects (behavior & assertions)
├── locators/     # UI locators isolated from logic
├── utils/        # Shared helpers and utilities
├── config/       # Playwright and environment configuration
└── README.md
```

This structure is intentionally simple and flexible, allowing each project
to evolve independently based on its real needs.

---

## What This Skeleton Does NOT Include

To avoid premature complexity, this repository deliberately excludes:

- Custom test runners or frameworks
- Opinionated reporting solutions
- CI/CD pipelines
- Data-driven or BDD abstractions
- Application-specific logic

These concerns are expected to be introduced **only when the project requires them**.

---

## Philosophy

- Start simple, scale intentionally
- Avoid premature abstractions
- Prefer clarity over cleverness
- Let each project own its evolution
- Optimize for long-term maintainability

---

## How to Use This Repository

1. Clone this repository
2. Rename it for your project
3. Adapt the structure as needed
4. Extend it responsibly
5. Own the result

This skeleton is a foundation — not a constraint.

---

## License

This project is licensed under the **MIT License**.