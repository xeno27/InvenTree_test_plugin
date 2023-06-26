"""Sample plugin which renders custom panels on certain pages."""

from part.views import PartDetail
from plugin import InvenTreePlugin
from plugin.mixins import PanelMixin, SettingsMixin, UrlsMixin
from stock.views import StockLocationDetail

from django.conf.urls import url
from django.http import HttpResponse


class StockListing(PanelMixin, SettingsMixin, InvenTreePlugin, UrlsMixin):
    """A sample plugin which renders some custom panels."""
    value=0
    NAME = "Stock listing"
    SLUG = "stocky"
    TITLE = "Stock Listing plugin"
    DESCRIPTION = "List all items of a stock location"
    VERSION = "0.1"
    #URLS = [url(r'stocklist/(?P<location>\d+)/', self.createList, name='creator'),]
    SETTINGS = {
        'ENABLE_HELLO_WORLD': {
            'name': 'Enable Hello World',
            'description': 'Enable a custom hello world panel on every page',
            'default': False,
            'validator': bool,
        },
        'ENABLE_BROKEN_PANEL': {
            'name': 'Enable Broken Panel',
            'description': 'Enable a panel with rendering issues',
            'default': False,
            'validator': bool,
        }
    }

    def get_panel_context(self, view, request, context):
        """Returns enriched context."""
        ctx = super().get_panel_context(view, request, context)

        # If we are looking at a StockLocationDetail view, add location context object
        if isinstance(view, StockLocationDetail):
            ctx['location'] = view.get_object()

        return ctx


    def setup_urls(self):
        return [
            url(r'stocklist/(?P<location>\d+)/', self.createList, name='creator'),
        ]

    def get_custom_panels(self, view, request):
        """You can decide at run-time which custom panels you want to display!

        - Display on every page
        - Only on a single page or set of pages
        - Only for a specific instance (e.g. part)
        - Based on the user viewing the page!
        """
        panels = []

        self.value=self.value+1
        
        # This panel will *only* display on the PartDetail view
        if isinstance(view, StockLocationDetail):
            panels.append({
                'title': 'Stock listing',
                'icon': 'fas fa-book',
                'content_template': 'stocky/stocklistpanel.html',
            })

        return panels

    def createList(self, request, location):
        print('User:', request.user)
        self.value = self.value + 1
        return HttpResponse('OK')
    
