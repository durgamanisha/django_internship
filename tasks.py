from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(pk=user_id)
    send_mail(
        "Welcome!",
        f"Hello {user.username}, thanks for registering!",
        "from@example.com",
        [user.email],
    )
