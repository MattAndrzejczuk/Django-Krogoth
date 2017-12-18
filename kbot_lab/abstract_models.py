# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from django.db import models
from polymorphic.models import PolymorphicModel
import os

from jawn.settings import MEDIA_ROOT


class KBNanolatheAbstractBlueprint(PolymorphicModel):
    """Generates dynamic ajax forms within the krogoth_gantry.

    Should be treated as a Java/C# abstract class. KBNanolatheAbstractBlueprints are
    compiled into AngularJS code as MVCs and include user activity tracking.
    """
    _HELPDOC_TITLE = 'The display title for development and documentation.'
    class Meta:
        app_label = 'kbot_lab'
        verbose_name = "nanolathing blueprint"
        verbose_name_plural = 'nanolathing blueprints'
        abstract = True

    doc_title = models.CharField(max_length=140,
                                 default='Untitled Nanolathe Construct',
                                 help_text=_HELPDOC_TITLE)

class KBNanolatheUploadAbstract(KBNanolatheAbstractBlueprint):
    """Subclass this in order to make an easy uploader.

    Note:
        Should be treated as a Java/C# abstract class.
    """
    _HELPDOC_UPLOADPATH = 'The directory name of the upload destination i.e. /media/{kb_path_name}'
    class Meta:
        app_label = 'kbot_lab'
        verbose_name = "nanolathed upload"
        verbose_name_plural = 'nanolathed uploads'

    kb_path_slug = models.SlugField(max_length=50,
                                    unique=True,
                                    help_text=_HELPDOC_UPLOADPATH)
    kb_file = models.FileField()

    @classmethod
    def nanolathe_upload(cls, named: str) -> KBNanolatheAbstractBlueprint:
        """Any and all uploads need an upload destination.

        When a new KBNanolatheUploadAbstract is created, an upload destination path must be
        generated if it does not exist.

        Args:
            named: The upload destination, i.e. /usr/src/persistent/media/{named}

        Returns:
            The freshly initialized KBNanolatheUploadAbstract.
        """
        nano_construct = cls(kb_path_slug=named)
        if not os.path.exists(nano_construct.destination_path):
            os.makedirs(nano_construct.destination_path)
            nano_construct.save()
            return nano_construct
        else:
            return KBNanolatheUploadAbstract.objects.get(kb_path_slug=named)

    @property
    def destination_path(self) -> str:
        """:str: full OS file system path to the upload destination."""
        return MEDIA_ROOT + self.kb_path_slug

    @property
    def filename_full(self) -> str:
        """:str: the full file name i.e. 'filename.txt'."""
        return os.path.basename(self.kb_file.name)

    @property
    def filename_no_ext(self) -> str:
        """:str: the full file name without the extension i.e. 'filename'."""
        return os.path.basename(self.kb_file.name)[:-4]

    @property
    def file_ext(self) -> str:
        """:str: the file extention i.e. '.txt', '.png'."""
        return os.path.basename(self.kb_file.name)[-4:]


class KBNanolatheThreadAbstract(KBNanolatheAbstractBlueprint):
    kb_parent = models.ForeignKey('KBNanolatheThreadAbstract',
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True)

    @property
    def is_root_thread(self) -> bool:
        if self.kb_parent is None:
            return True
        else:
            return False# coding=utf-8
