from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLHeadElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLHeadElement, self).__init__(*args, **kw)
