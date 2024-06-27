from django.contrib import admin
from .models import (
    Education,
    Project,
    History,
    ContactUs
)
# Register your models here.


admin.site.register(Education)
admin.site.register(Project)
admin.site.register(History)
admin.site.register(ContactUs)