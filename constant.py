import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = False if os.getenv("ENV") == "dev" else True

FLASK_SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or "secret"

POSTGRES_USER=os.getenv("POSTGRES_USER") or "postgres"
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD") or "pass"
POSTGRES_DB = os.getenv("POSTGRES_DB") or "postgres"

GMAIL_STMP_PW = os.getenv("GMAIL_STMP_PW")
GMAIL_STMP_USERNAME = os.getenv("GMAIL_STMP_USERNAME")


PAYTECH_API_URL=os.getenv("PAYTECH_API_URL")
PAYTECH_API_KEY=os.getenv("PAYTECH_API_KEY")
PAYTECH_SECRET_KEY=os.getenv("PAYTECH_SECRET_KEY")
PAYTECH_ENV=os.getenv("PAYTECH_ENV") or "test"