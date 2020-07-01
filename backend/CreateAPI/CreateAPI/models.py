from django.db import models
from django.utils import timezone

class subModel(models.Model):
    sub_id = models.CharField(max_length = 50)
    sub_name = models.CharField(max_length = 50)
    sub_teacher = models.CharField(max_length = 30)
    sub_start = models.DateTimeField(default=timezone.now)
    sub_stop = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('sub_start',)
        db_table = 'detail'
        managed = False


    