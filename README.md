# QA Automation Framework

This is my automation testing framework for API, Database and UI testing. Uses Python with pytest, requests for API, PostgreSQL for database and Playwright for UI testing.

## Project Structure

```
.
├── config/
│   └── settings.py
├── utils.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8 or above
- PostgreSQL
- Git

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
4. Install packages: `pip install -r requirements.txt`
5. Install Playwright browsers: `playwright install chromium`
6. Create `.env` file with these variables:

```env
API_BASE_URL=
API_TIMEOUT=30
DB_HOST=localhost
DB_PORT=5432
DB_NAME=testdb
DB_USER=postgres
DB_PASSWORD=postgres
UI_BASE_URL=
TEST_TIMEOUT=60
```

7. Create PostgreSQL database: `CREATE DATABASE testdb;`

## Testing Setup

You can test the setup by importing and using the connection functions directly in Python:

```python
from utils import get_db_connection
from config.settings import DB_CONFIG

# Test database connection
conn = get_db_connection()
print("Database connected!")
conn.close()
```

## Overview

This framework provides the setup structure for:
- **API Testing**: Configuration ready for requests library
- **Database Testing**: PostgreSQL connection setup in utils.py
- **UI Testing**: Playwright browser fixture setup in conftest.py

Connection and setup code is in `utils.py` and `conftest.py`. Configuration is in `config/settings.py` which reads from `.env` file.

## Common Issues

- **Database connection fails**: Check PostgreSQL is running and credentials in `.env` are correct
- **Playwright issues**: Run `playwright install chromium` again
- **API tests failing**: Verify API_BASE_URL in `.env` is set correctly
- **Import errors**: Make sure virtual environment is activated and packages are installed

This is my first automation framework, so feedback is welcome!
