from .models import ChangeLog
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


@receiver(post_save)
def post_save_signal(sender, created, **kwargs):
    if created and sender.__name__ != 'ChangesLog':
        ChangeLog.objects.create(model=sender.__name__, operation='create')
    elif not created and sender.__name__ != 'ChangesLog':
        ChangeLog.objects.create(model=sender.__name__, operation='update')


@receiver(post_delete)
def post_delete_signal(sender, **kwargs):
    if sender.__name__ != 'ChangesLog':
        ChangeLog.objects.create(model=sender.__name__, operation='delete')