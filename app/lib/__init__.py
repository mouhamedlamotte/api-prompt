from .postgres import Postgres
from ._flask_mail import send_email, mail

db = Postgres()

