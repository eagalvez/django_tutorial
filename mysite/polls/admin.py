from django.contrib import admin
from .models import Question, Choice
# tell the admin Question table has an admin interface
admin.site.register(Question)
admin.site.register(Choice)