from django.contrib import admin

from .models.logs import Group, Level, Log
from .models.users import User

# Register your models here.
admin.site.register(Log)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Level)
