from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User

@receiver(post_save, sender=User)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.isProfessor:
            group = Group.objects.get(name='Professor')
        else:
            group = Group.objects.get(name='Student')
        instance.groups.add(group)