from datetime import date

from django.core.mail import send_mail

from SkyChampService import settings
from mailing_service.models import Customer, MessageSender, Attempt


def send_email(*args):
    print('servise is raning')
    list_customer: list = Customer.objects.filter(is_active=True)


    list_message_sender: list = []
    list_message_sender.extend(MessageSender.objects.filter(status='CREATED',
                                                            start_date__lte=date.today().strftime("%Y-%m-%d"),
                                                            end_date__gte=date.today().strftime("%Y-%m-%d")))

    if args != ():
        list_message_sender.extend(MessageSender.objects.filter(status='LAUNCHED',
                                                                start_date__lte=date.today().strftime("%Y-%m-%d"),
                                                                end_date__gte=date.today().strftime("%Y-%m-%d"),
                                                                frequency=str(*args)))

    for send in list_message_sender:
        for customer in list_customer:
            try:
                response = send_mail(subject=send.subject,
                                     message=send.body,
                                     from_email=settings.EMAIL_HOST_USER,
                                     recipient_list=[customer.email,],)
            except Exception as e:
                response = e

            if response == 1:
                status = 'DELIVERED'
            else:
                status = 'NOT_DELIVERED'

            res_serv = Attempt.objects.create(message_sender=send,
                                customer=customer,
                                status=status,
                                response=response)
            res_serv.save()

        if send.frequency == 'ONCE':
            send.status = 'COMPLETED'
        else:
            send.status = 'LAUNCHED'
        send.save()