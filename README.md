# Prerequisites
- Python 3.8 or higher
- PostgreSQL 12 or higher
- Git

# QA Automation Framework

This is an automation testing framework for API, Database and UI testing. Uses Python with pytest, requests for API, PostgreSQL for database and Playwright for UI testing.

# Requirements

- Python 3.8 or above
- PostgreSQL
- Git

# Setup

1. Clone the repository
2. Create virtual environment: python -m venv venv
3. Activate it: venv\Scripts\activate
4. Install packages: pip install -r requirements.txt
5. Install Playwright browsers: playwright install chromium
6. Create .env file
7. Create PostgreSQL database: CREATE DATABASE testdb;


All utility functions are in utils.py. Configuration is in settings.py which reads from .env file.
