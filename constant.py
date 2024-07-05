import os

from dotenv import load_dotenv
load_dotenv()

POSTGRES_USER=os.getenv("POSTGRES_USER") or "postgres"
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD") or "pass"
POSTGRES_DB = os.getenv("POSTGRES_DB") or "postgres"
FLASK_SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or "48e23eeb9e67e357128a847fd44cfe0d"
DEBUG = os.getenv("DEBUG") or False