from django.contrib import admin
from .models import Job
from .models import PersonalJob


class JobAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

# Register your models here.
admin.site.register(Job, JobAdmin)
admin.site.register(PersonalJob, JobAdmin)
