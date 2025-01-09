from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client():
    subject = 'This email is from Django server'
    message = 'This ia a test email from Django server'
    from_email = 'Django Server'
    recipient_list = ['shahzaibdev404@gmail.com', 'sg03056924122@gmail.com', 'dani.q441@gmail.com']
    send_mail(subject, message, from_email, recipient_list)