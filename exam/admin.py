from django.contrib import admin
from .models import Questions,Student_info,Result

# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display = ('username', 'subject', 'score')

admin.site.register(Questions)
admin.site.register(Student_info)
admin.site.register(Result)