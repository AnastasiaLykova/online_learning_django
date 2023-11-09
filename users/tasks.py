import datetime
from celery import shared_task
from users.models import User


@shared_task
def deactivate_user():
    users = User.objects.all()
    for user in users:
        if user.last_login >= user.last_login+datetime.timedelta(days=30) and user.is_active:
            user.is_active = False
