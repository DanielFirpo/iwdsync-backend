"""caster/urlsapi.py
"""
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from caster import viewsapi
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", csrf_exempt(viewsapi.caster)),
    path("get-my-caster/", viewsapi.get_my_caster),
    path("get-csrf/", viewsapi.get_csrf),
    path("get-server-time/", viewsapi.get_server_time),
    path("auth/login/", viewsapi.login_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
