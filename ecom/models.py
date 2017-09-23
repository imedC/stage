from django.db import models

from cms.models.pluginmodel import CMSPlugin






class Produit(CMSPlugin):
	name = models.CharField(max_length=50, default='NameProd')
	price = models.CharField(max_length=50, default='PriceProd')
	image = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	
class ProduitPluginModel(CMSPlugin):
	product = models.ForeignKey(Produit)



	def __unicode__(self):
		return self.product.name 



