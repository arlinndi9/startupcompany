from django.contrib import admin
from .models import Contact,Jobs,Stories,apply_job,Team

# Register your models here.
admin.site.register(Contact)
admin.site.register(Jobs)
admin.site.register(Stories)
@admin.register(apply_job)
class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ('name','lastname','email','positionjob')
    fields = ('name', 'lastname', 'email', 'positionjob', 'about', 'resume', 'coverletter')
admin.site.register(Team)