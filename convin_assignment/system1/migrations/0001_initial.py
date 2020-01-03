# Generated by Django 3.0.1 on 2020-01-03 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('file_object', models.FileField(unique=True, upload_to='files/%Y/%m/%d')),
                ('encrypted_file', models.CharField(blank=True, default='xxxx', max_length=500, null=True)),
            ],
        ),
    ]
