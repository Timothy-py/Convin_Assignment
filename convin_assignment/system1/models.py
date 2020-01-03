from django.db import models


# Create your models here.


class File(models.Model):

    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    file_object = models.FileField(upload_to='files/%Y/%m/%d', unique=True)
    encrypted_file = models.CharField(max_length=500, default='xxxx', blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.description}"
