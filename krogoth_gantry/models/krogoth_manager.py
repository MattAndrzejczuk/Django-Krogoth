from django.db import models
from krogoth_gantry.models.models_chat import JawnUser
# Create your models here.
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
        elif krogoth_class == "NgIncludedHtmlCore":
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






class DataVisitorTracking(models.Model):
    remote_port = models.CharField(max_length=24, default="NONE")
    http_user_agent = models.CharField(max_length=355, default='UNKNOWN')
    remote_addr = models.CharField(max_length=100, default='NO_HOST')
    date_created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, default="ANONYMOUS")



BEHAVIOR_TYPES = (
    ('user_activity', 'User Activity'),  #              KrogothViewController is loaded by user.
    ('client_input', 'User Input'),  #                  API, buttons, or easter eggs can be traced here.
    ('hacker', 'Malicious User'),  #                    Brute force password changers, KrogothFramework developer.
    ('crawler_bot', 'Web Crawlers/Non Browsers'),  #    bots and web crawlers
    ('other', 'Strange Client Activity'),  #            Random stuff here
)
"""
DataAppTrace
User behavior tracking event logging.
- KrogothViewController is loaded by user.
- API, buttons, or easter eggs can be traced here.
- Brute force password changers, KrogothFramework developer.
- bots and web crawlers
- Random/unique behaviors
"""
class DataVisitorBehavior(models.Model):
    behavior_tracked = models.CharField(max_length=45,
                                        choices=BEHAVIOR_TYPES,
                                        help_text="User behavior tracking event logging.")
    name = models.CharField(max_length=65)
    remote_port = models.CharField(max_length=24, default="NONE")
    http_user_agent = models.CharField(max_length=355, default='UNKNOWN')
    remote_addr = models.CharField(max_length=100, default='NO_HOST')
    date_created = models.DateTimeField(auto_now_add=True)


CONSOLE_LEVELS = (
    ('log', 'Log'),
    ('info', 'Info'),
    ('todo', 'TODO'),
    ('debug', 'Debug'),
    ('warn', 'Warn'),
    ('error', 'Error'),
)
import inspect
from inspect import Traceback


OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
HEADER = '\033[95m'
UNDERLINE = '\033[4m'


BGBl = "\033[47m"
BGCy = "\033[46m"
"\033[44m"
"\033[43m"
"\033[42m"
"\033[41m"





"""
DataServerEvents

Run tests:
from krogoth_gantry.models import DataServerEvents
import inspect
DataServerEvents.warn("NgIncludedHtml has been deprecated",
                                      inspect.getframeinfo(inspect.stack()[1][0]))
test1 = DataServerEvents.report("First", "log",
                                inspect.getframeinfo(inspect.stack()[1][0]))
test2 = DataServerEvents.report("Info", "info",
                                inspect.getframeinfo(inspect.stack()[1][0]))
test3 = DataServerEvents.report("FAIL", "fail",
                                inspect.getframeinfo(inspect.stack()[1][0]))



# FULL TEST
from krogoth_gantry.models import DataServerEvents
import inspect
DataServerEvents.log("log test", inspect.getframeinfo(inspect.stack()[1][0]))
DataServerEvents.info("info test", inspect.getframeinfo(inspect.stack()[1][0]))
DataServerEvents.todo("todo test", inspect.getframeinfo(inspect.stack()[1][0]))
DataServerEvents.debug("debug test", inspect.getframeinfo(inspect.stack()[1][0]))
DataServerEvents.warn("warn test", inspect.getframeinfo(inspect.stack()[1][0]))
DataServerEvents.error("error test", inspect.getframeinfo(inspect.stack()[1][0]))


"""
class DataServerEvents(models.Model):
    console_type = models.CharField(max_length=125, choices=CONSOLE_LEVELS)
    date_created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=900, default="0")

    code_file = models.CharField(max_length=125, null=True, default=None)
    code_line = models.CharField(max_length=125, null=True, default=None)
    code_func = models.CharField(max_length=125, null=True, default=None)

    @classmethod
    def log(cls, msg, trc:Traceback=None):
        cls.report(msg=msg, console_level='log', info=trc)

    @classmethod
    def info(cls, msg, trc: Traceback = None):
        cls.report(msg=msg, console_level='info', info=trc)

    @classmethod
    def todo(cls, msg, trc: Traceback=None):
        cls.report(msg=msg, console_level='todo', info=trc)

    @classmethod
    def debug(cls, msg, trc: Traceback = None):
        cls.report(msg=msg, console_level='debug', info=trc)

    @classmethod
    def warn(cls, msg, trc: Traceback = None):
        cls.report(msg=msg, console_level='warn', info=trc)

    @classmethod
    def error(cls, msg, trc: Traceback = None):
        cls.report(msg=msg, console_level='error', info=trc)

    @classmethod
    def report(cls, msg, console_level: str='log', info: Traceback=None):
        b = ' ◀︎░▒▓▒░▶︎ '
        if console_level == CONSOLE_LEVELS[0][0]: print(BOLD +b+ str(msg) + ENDC)
        if console_level == CONSOLE_LEVELS[1][0]: print(OKBLUE +b+ str(msg) + ENDC)
        if console_level == CONSOLE_LEVELS[2][0]: print(OKCYAN +b+ str(msg) + ENDC)
        if console_level == CONSOLE_LEVELS[3][0]: print(OKGREEN +b+ str(msg) + ENDC)
        if console_level == CONSOLE_LEVELS[4][0]: print(UNDERLINE + WARNING +b+ str(msg) + ENDC)
        if console_level == CONSOLE_LEVELS[5][0]: print(HEADER + FAIL +b+ str(msg) + ENDC)
        try:
            new = cls()
            new.msg=msg.__str__()
            new.console_type=console_level
            new.code_file = info.filename
            new.code_line = info.function
            new.code_func = info.lineno
            new.save()
        except Exception as e:
            print(FAIL + "DataServerEvents Fatal Error " + msg)
            print(FAIL + "[!!!]" + e.__str__())

    def fuck_her2(self, info: Traceback):
        # info: Traceback = inspect.getframeinfo(inspect.stack()[1][0])
        self.code_file = info.filename
        self.code_line = info.function
        self.code_func = info.lineno


