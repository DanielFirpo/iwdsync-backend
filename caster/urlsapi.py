"""caster/urlsapi.py
"""
from django.urls import path
from caster import viewsapi
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", viewsapi.caster),
    path("get-my-caster/", viewsapi.get_my_caster),
]

urlpatterns = format_suffix_patterns(urlpatterns)
