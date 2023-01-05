from django.conf.urls import url
from book.views import *


urlpatterns = [
    url('^index/$', index),
    url('^bookList/$', bookList),
    url(r'^testproject/$', testproject),
    url(r'^testmodel/$', testmodel)
]
