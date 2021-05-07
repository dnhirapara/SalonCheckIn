from django.conf import settings
from django.core.mail import send_mail


def send_email():
    subject = 'Welcome to Salon Check In'
    message = f'Hi TempUser, thank you for registering in Salon Check In.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['darshikhirapara@gmail.com']
    send_mail(subject, message, email_from, recipient_list)


def send_email_with(subject, message, recipient):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
