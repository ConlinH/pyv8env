from .flags import *
from .v8_css_style_value import CSSStyleValue


@construct_100001
class CSSImageValue(CSSStyleValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSImageValue, self).__init__(*args, **kw)
