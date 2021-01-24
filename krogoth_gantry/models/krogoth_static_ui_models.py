from django.db import models
import uuid
import codecs
import datetime





###    //  static/web/krogoth_static_interface/stylesheets/index_loading_styles.css
class KStaticInterfaceCSSModel(models.Model):
    unique_id = models.CharField(primary_key=True, max_length=25)
    file_name = models.CharField(max_length=100, default='index_loading_styles.css')
    content = models.TextField(default='/* This CSS doc is empty */')
    is_enabled = models.BooleanField(default=True)

    pub_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.unique_id

    def make_a_backup(self):
        ktime = datetime.datetime.now()
        stamp = '_' + str(ktime.month) + '_' + str(ktime.day) + '_' + str(ktime.year) + \
                '_X_' + str(ktime.hour) + '_' + str(ktime.minute) + '_' + str(ktime.second)
        destination = 'krogoth_ui_backups/krogoth_static_css/' + self.file_name
        text_file = open(destination, "w")
        text_file.write(self.content)
        text_file.close()
        print("saved backup to ->   " + destination)

    def save_file_into_db(self):
        p = 'static/web/krogoth_static_interface/stylesheets/' + self.file_name
        contents = codecs.open(p, 'r').read()
        self.content = contents
