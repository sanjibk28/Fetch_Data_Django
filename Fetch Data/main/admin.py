from django.contrib import admin
from .models import PlayerData

# Register your models here.

from import_export.admin import ImportExportModelAdmin

class PlayerDataAdmin(admin.ModelAdmin):
	fields = ["NAME",
			  "STATUS"]

admin.site.register(PlayerData, PlayerDataAdmin)

class ViewAdmin(ImportExportModelAdmin):
	pass