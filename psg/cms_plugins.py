from pyexpat import model
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from .models import Main_page_window_model, Resolution_model

@plugin_pool.register_plugin
class HeaderPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Nagłówek")
    render_template = "header_template.html"
    cache = False

@plugin_pool.register_plugin
class WindowPlugin(CMSPluginBase):
    model = Main_page_window_model
    name = "Okna na stronie głównej"
    render_template = "main_page_window.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ResolutionPlugin(CMSPluginBase):
    model = Resolution_model
    name = "Uchwała"
    render_template = "resolution_template.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
