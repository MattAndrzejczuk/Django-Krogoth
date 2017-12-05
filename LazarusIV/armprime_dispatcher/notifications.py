from chat.models import JawnUser
from LazarusIV.models import NotificationCenter, NotificationItem, BackgroundWorkerJob


class Notifier:

    def __init__(self, for_user: JawnUser):
        self.nc = NotificationCenter.objects.get_or_create(parent_user=for_user)


    def ping_basic_alert(self, msg: str):
        try:
            centre = NotificationCenter.objects.get(id=self.nc.id)
            ping = NotificationItem(center=centre,
                                    is_private=True,
                                    kind='RepositoryProcessor',
                                    image_url='',
                                    sfx_chime='',
                                    title='Alert',
                                    body=msg,
                                    unread=0)
            ping.save()
        except:
            print('  ⚠️ Notifications Centre has failed.', end='')
