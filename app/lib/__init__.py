from .postgres import Postgres
from ._flask_mail import _send_confirm_email, mail, send_mail
from ._paytech import Paytech

paytech = Paytech()
db = Postgres()

