from .flags import *
from .v8_svg_text_positioning_element import SVGTextPositioningElement


@construct_100001
class SVGTextElement(SVGTextPositioningElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGTextElement, self).__init__(*args, **kw)
