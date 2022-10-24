from django.contrib import admin
from caster.models import Caster


@admin.register(Caster)
class CasterAdmin(admin.ModelAdmin):
    list_display = ('twitch_channel', )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
