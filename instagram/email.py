from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from django.conf import settings
from sendgrid.helpers.mail import Mail


def send_welcome_email(name,email):
    message=Mail(from_email='bernardmairura@gmail.com',to_emails=email,subject='Welcome to my Istagram Clone',html_content=render_to_string('email/newsemail.html',{'name':name}))
    

    try:
        sendgrid=SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response=sendgrid.send(message)
        
        print('RESPONSE_CODE',response.status_code)
    except Exception as e:
        print('SENDGRID_API_KEY',settings.SENDGRID_API_KEY)
        print('SENDGRID ERROR',e)
