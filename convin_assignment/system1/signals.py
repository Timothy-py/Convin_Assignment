from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import File
from . import encryptor
import os


@receiver(post_save, sender=File)
def save_file(sender, instance, created, update_fields, **kwargs):
    if created:
        encryptor.write_key()
        key = encryptor.load_key()
        encrypted_file = encryptor.encrypt(os.path.join('media', instance.file_object.__str__()), key=key)
        instance.encrypted_file = encrypted_file
        File.save(instance)
        print(f"A new model {instance} created successfully")


@receiver(pre_save, sender=File)
def checker(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.description != instance.description:
            print(f"description field changed from {obj.description} to {instance.description}")
        elif obj.file_object != instance.file_object:
            print(f"file field changed from {obj.file_object} to {instance.file_object}")
        elif obj.encrypted_file != instance.encrypted_file:
            print(f"encrypted file field changed from {obj.encrypted_file} to {instance.encrypted_file}")
