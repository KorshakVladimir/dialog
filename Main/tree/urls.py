from django.conf.urls import include, url
from . views import index


urlpatterns = [
    url(r'^(?P<answer_id>.*)$', index, name='share'),
]
