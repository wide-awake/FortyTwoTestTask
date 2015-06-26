from .models import ChangeLog
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


IGNORED_MODELS = ['HttpRequest', 'ChangeLog', 'LogEntry', 'ContentType']


@receiver(post_save, dispatch_uid='nope')
def post_save_signal(sender, created, **kwargs):
    if sender.__name__ in IGNORED_MODELS:
        return
    if created:
        ChangeLog.objects.create(model_name=sender.__name__, action='create')
    else:
        ChangeLog.objects.create(model_name=sender.__name__, action='update')


@receiver(post_delete, dispatch_uid='nope')
def post_delete_signal(sender, **kwargs):
    if sender.__name__ in IGNORED_MODELS:
        return
    ChangeLog.objects.create(model_name=sender.__name__, action='delete')
