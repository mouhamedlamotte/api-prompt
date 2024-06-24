import os

from dotenv import load_dotenv
load_dotenv()

POSTGRES_USER=os.getenv("POSTGRES_USER") | "ktmlee"
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD") | "pass"
FLASK_SECRET_KEY=os.getenv("FLASK_SECRET_KEY") | "48e23eeb9e67e357128a847fd44cfe0d"