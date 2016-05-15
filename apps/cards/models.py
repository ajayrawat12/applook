from django.db import models
from django.utils import timezone
from apps.users.models import UserProfile
# Create your models here.

TYPE_CHOICES = (("public", "public"), ("private", "private"))


class Cards(models.Model):
    """Creating a model."""

    user = models.ForeignKey(
        UserProfile,
        default="",
        null=True,
        blank=True)

    name = models.CharField(
        max_length=200,
        blank=False,
        null=False)

    image = models.ImageField(
        upload_to='Cards',
        blank=False,
        null=False)

    desc = models.TextField(
        blank=True,
        null=True)

    v_type = models.CharField(max_length=125, choices=TYPE_CHOICES, default="public")

    likes = models.IntegerField(default=0)

    uplaod_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="time")

    def __str__(self):
        """Show on admin."""
        return self.name

    class Meta:
        """This will show on admin main page."""

        verbose_name = 'Cards'
        verbose_name_plural = "Cards"
