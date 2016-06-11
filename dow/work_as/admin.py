from django.contrib import admin
# Register your models here.
from .models import User
from .models import Note
from .models import Part,Storage

admin.site.register(User)
admin.site.register(Note)
admin.site.register(Part)
admin.site.register(Storage)
