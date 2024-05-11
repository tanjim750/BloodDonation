# email sending packages 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from django.conf import settings
from django.core.mail import send_mail

#For Send html template to email
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string


def send(smtp_server,port,password,from_email,recipient_list,subject,template,data):
    subject = subject
    settings.EMAIL_HOST_USER = from_email
    settings.EMAIL_PORT = port
    settings.EMAIL_HOST = smtp_server
    settings.EMAIL_HOST_PASSWORD = password

    email_from = settings.EMAIL_HOST_USER
    # send_mail(subject, message, email_from, recipient_list)

    html_template = render_to_string(template,data)
    message = strip_tags(html_template)

    email = EmailMultiAlternatives(
            subject,
            message,
            email_from,
            recipient_list
    )
    email.attach_alternative(html_template, 'text/html')
    email.send()