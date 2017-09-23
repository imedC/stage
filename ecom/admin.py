from django.contrib import admin
from .models import Produit



class ProdAdmin(admin.ModelAdmin):
	pass
admin.site.register(Produit, ProdAdmin)