import os
import resend

resend.api_key = os.environ["RESEND_API_KEY"]

params: resend.Emails.SendParams = {
    "from": "Prompt Master <instagramsecurepw@gmail.com>",
    "to": ["lamottelymouhamed@gmail.com"],
    "subject": "hello world",
    "html": "<strong>it works!</strong>",
}

email = resend.Emails.send(params)
print(email)
