from django.db import models
from krogoth_chat.models import JawnUser
# Create your models here.
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantrySlaveViewController, \
    KrogothGantryService, KrogothGantryDirective
from krogoth_gantry.management.commands.installdjangular import bcolors
from polymorphic.models import PolymorphicModel


# from conn


def more_than_zero(length: int):
    if length > 0:
        return True
    else:
        return False


class UncommitedSQL(models.Model):
    """When saving code using web IDE, keep track of saved modules.

    This model keeps track of code which has been saved to SQL, but has still never been backed up
    to be saved as a file to the filesystem. They must be saved to the file system in order to
    allow developers to commit their HTML, JS or CSS code.

    Developers should avoid changing the 'name' property for all models in the Gantry app.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    krogoth_class = models.CharField(max_length=125)
    edited_by = models.ForeignKey(JawnUser, on_delete=models.CASCADE)
    has_error = models.BooleanField(default=False)
    status = models.CharField(max_length=255, null=True, blank=True)

    @classmethod
    def does_exist(cls, name: str, krogoth_class: str) -> bool:
        if krogoth_class == "KrogothGantryMasterViewController":
            return more_than_zero(len(cls.objects.filter(name=name)))
        elif krogoth_class == "KrogothGantrySlaveViewController":
            return more_than_zero(len(cls.objects.filter(name=name)))
        elif krogoth_class == "KrogothGantryService":
            return more_than_zero(len(cls.objects.filter(name=name)))
        elif krogoth_class == "KrogothGantryDirective":
            return more_than_zero(len(cls.objects.filter(name=name)))
        elif krogoth_class == "IncludedHtmlMaster":
            return more_than_zero(len(cls.objects.filter(name=name)))
        elif krogoth_class == "IncludedJsMaster":
            return more_than_zero(len(cls.objects.filter(name=name)))
        elif krogoth_class == "AKFoundation":
            return more_than_zero(len(cls.objects.filter(name=name)))
        else:
            print(bcolors.red + " ! ! ! WARNING ! ! ! " + bcolors.ENDC)
            print(bcolors.red + " ! UNKNOWN GANTRY  ! " + bcolors.ENDC)
            print(bcolors.orange + " ! Gantry: " + krogoth_class + " " + bcolors.ENDC)
            print(bcolors.orange + " ! Name: " + name + " " + bcolors.ENDC)
            return False

    @classmethod
    def finish_and_remove(cls, name: str):
        destroy = cls.objects.get(name=name)
        destroy.delete()

    @classmethod
    def report_failure(cls, for_record_named: str, error_info: str):
        broken = cls.objects.get(name=for_record_named)
        broken.has_error = True
        broken.status = error_info
        broken.save()

    def save(self, *args, **kwargs):
        pre_existing = UncommitedSQL.objects.filter(name=self.name)
        if len(pre_existing) > 0:
            pre_existing.first().delete()
        super(UncommitedSQL, self).save(*args, **kwargs)


INSTANCE_TYPES = (
    ('view', 'View'),
    ('url', 'URL'),
    ('model', 'Model'),
)


class KrogothAppTrace(models.Model):
    instance_class = models.CharField(max_length=45,
                                      choices=INSTANCE_TYPES,
                                      help_text="Keep track of all Krogoth Python functions and classes being used.")
    name = models.CharField(max_length=65)
    date_created = models.DateTimeField(auto_now_add=True)


CONSOLE_LEVELS = (
    ('log', 'Log'),
    ('info', 'Info'),
    ('debug', 'Debug'),
    ('warn', 'Warn'),
    ('error', 'Error'),
)


class KrogothServerConsole(PolymorphicModel):
    console_type = models.CharField(max_length=125, choices=CONSOLE_LEVELS)
    date_created = models.DateTimeField(auto_now_add=True)


# class KrogothServerLoggedJSON(KrogothServerConsole):
#     content = models.J
class KrogothServerLoggedText(KrogothServerConsole):
    content = models.TextField()
