from .flags import *
from .v8_html_element import HTMLElement


@construct_100001
class HTMLUnknownElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLUnknownElement, self).__init__(*args, **kw)
