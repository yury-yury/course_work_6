from mailing_service.services import send_email


def my_scheduled_job(*args):

    send_email(*args)