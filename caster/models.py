"""caster/model.py
"""
from django.db import models
from django.contrib.auth.models import User


class Caster(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, default=None, unique=True, on_delete=models.CASCADE
    )
    twitch_channel = models.CharField(
        max_length=128, default=None, null=True, blank=True, db_index=True, unique=True
    )
    url_path = models.CharField(max_length=128, default=None, null=True, db_index=True, unique=True)
    stream_delay = models.FloatField(default=0, null=False, blank=True, verbose_name='Your Stream Delay (in seconds)')
    youtube_url = models.CharField(default=None, blank=True, null=True, max_length=1024)
    youtube_time = models.FloatField(default=None, null=True, blank=True)
    irl_time = models.FloatField(default=None, null=True, blank=True)

    def __str__(self):
        return f"Caster - {self.twitch_channel}"
