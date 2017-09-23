from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from .models import ProduitPluginModel 





class HelloPlugin(CMSPluginBase):
	#model = ProduitPluginModel
	name = _("Product Plugin")
	render_template = "rpc/category.html"

	def render(self, context, instance, placeholder):
		context = super(HelloPlugin, self).render(context, instance, placeholder)
		return context

plugin_pool.register_plugin(HelloPlugin)