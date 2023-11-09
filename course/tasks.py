from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_course_update_notification(list_emails, course_name):

    send_mail(subject=f'Обновление курса {course_name}',
              message=f'Курс {course_name} обновлен',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=list_emails,)
