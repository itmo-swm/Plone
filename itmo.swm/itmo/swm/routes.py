# We must use BrowserView from view, not from zope.browser
from Products.Five.browser import BrowserView
import requests
import json

class RoutesView(BrowserView):

    def __init__(self, context, request):
        """ Initialize context and request as view multi adaption parameters.

        Note that the BrowserView constructor does this for you.
        This step here is just to show how view receives its context and
        request parameter. You do not need to write __init__() for your
        views.
        """
        self.context = context
        self.request = request

    def routes(self):
        r=requests.get('http://sdn.naulinux.ru:8123/test')
        j=r.json()
        return j

    # by default call will call self.index() method which is mapped
    # to ViewPageTemplateFile specified in ZCML
    #def __call__():
    #
