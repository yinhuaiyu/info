from django.contrib import admin
from book.models import PeopleInfo,BookInfo
# Register your models here.

#
admin.site.register(BookInfo)

admin.site.register(PeopleInfo)
