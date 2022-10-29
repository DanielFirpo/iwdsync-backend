from rest_framework import serializers
from caster.models import Caster


class CasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caster
        fields = [
            'user',
            'twitch_channel',
            'url_path',
            'stream_delay',
            'youtube_url',
            'youtube_time',
            'irl_time'
        ]
