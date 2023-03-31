from django.contrib import admin
from .views import *
from .models import *

admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
#admin.site.register(Project)
admin.site.register(ContactForm)

# Register your models here.
