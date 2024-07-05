import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG") or False

FLASK_SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or "secret"

POSTGRES_USER=os.getenv("POSTGRES_USER") or "postgres"
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD") or "pass"
POSTGRES_DB = os.getenv("POSTGRES_DB") or "postgres"

GMAIL_STMP_PW = os.getenv("GMAIL_STMP_PW")
GMAIL_STMP_USERNAME = os.getenv("GMAIL_STMP_USERNAME")