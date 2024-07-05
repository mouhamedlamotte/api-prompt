from app import app
from constant import DEBUG
from flask import render_template



from app.lib._flask_mail import get_confirm_email_template



if __name__ == "__main__":
    app.run(debug=DEBUG)
