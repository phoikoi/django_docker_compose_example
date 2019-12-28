from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from uuid import uuid4
from django.dispatch import receiver
from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Member(BaseModel, AbstractUser):
    pass

    def __str__(self):
        sa = self.socialaccount_set.first()
        if sa is not None:
            return f"{self.username} ({sa.get_provider_account().to_str()} from {sa.provider})"
        return self.username


User = get_user_model()


class UserProfile(BaseModel):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.deletion.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(models.signals.post_save, sender=User, dispatch_uid='create_user_profile')
def maybe_create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = UserProfile(user=user)
        profile.save()
    else:
        user.profile.modified_at = datetime.now()
        user.profile.save()

