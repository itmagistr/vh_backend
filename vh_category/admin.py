from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
	model = Category
	readonly_fields = ['uid']

admin.site.register(Category, CategoryAdmin)
