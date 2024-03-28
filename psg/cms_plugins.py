from ast import If
from pyexpat import model
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from .models import Main_page_window_model, Resolution_model, Page_header, Iframe, Three_mini_windows, Two_mini_windows, One_mini_windows, Image_one, Image_two, Image_three

@plugin_pool.register_plugin
class HeaderPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Baner strony")
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

@plugin_pool.register_plugin
class PageHeader(CMSPluginBase):
    model = Page_header
    name = "Nagłowek strony"
    render_template = "page_header.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class Iframe(CMSPluginBase):
    model = Iframe
    name = "Iframe"
    render_template = "iframe.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ThreeMiniWindows(CMSPluginBase):
    model = Three_mini_windows
    name = "Trzy małe okna"
    render_template = "three_mini_windows.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ImageOne(CMSPluginBase):
    model = Image_one
    name = "Jedno małe zdjęcie"
    render_template = "image_one.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ImageTwo(CMSPluginBase):
    model = Image_two
    name = "Dwa małe zdjęcia"
    render_template = "image_two.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ImageThree(CMSPluginBase):
    model = Image_three
    name = "Trzy małe zdjęcia"
    render_template = "image_three.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class TwoMiniWindows(CMSPluginBase):
    model = Two_mini_windows
    name = "Dwa małe okna"
    render_template = "two_mini_windows.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class OneMiniWindows(CMSPluginBase):
    model = One_mini_windows
    name = "Jedno małe okno"
    render_template = "one_mini_window.html"
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context