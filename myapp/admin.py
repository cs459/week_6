from django.contrib import admin
from .models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Car._meta.fields]
admin.site.register(Car,CarAdmin)