from django.core.management.base import BaseCommand
from django.db.models import get_models


class Command(BaseCommand):
    """
    List of all models, known to ORM with amout of objects in them
    """
    def handle(self, *args, **options):
        """
        command's hande method
        """
        # all of the models and amount of objects in them is single dict ;)
        counted_models = {m: len(m.objects.all()) for m in get_models()}

        self.stdout.write("List of all models, known to ORM with amout of objects in them")
        for model, amount in counted_models.iteritems():
            output = "%s: %s objects" % (model._meta.module_name, amount)
            self.stdout.write(output)

        for model, amount in counted_models.iteritems():
            output = "%s: %s objects" % (model._meta.module_name, amount)
            self.stderr.write("error: " + output)