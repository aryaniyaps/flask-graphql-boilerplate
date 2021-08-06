from {{ cookiecutter.project_slug }}.extensions import mail
from flask_mail import Message


def send_mail(to, subject, template, body=None):
    """
    sends an individual mail to the
    specified recipient, with the given
    subject and template.
    """
    message = Message(
        subject=subject,
        body=body,
        html=template
    )
    message.add_recipient(to)
    mail.send(message)
