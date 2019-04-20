from django.contrib import admin
from post import models

@admin.register(models.Post)
class AdminPost(admin.ModelAdmin):
	model = models.Post
	list_display = ['id','title','user_add','date_add']
	list_display_links = ('title',)
	list_filter = ('user_add', 'date_add')
	date_hierarchy = 'date_add'
	actions_on_top = True
	ordering = ('-date_add',)

# Register your models here.
