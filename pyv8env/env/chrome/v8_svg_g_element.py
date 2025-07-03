from .flags import *
from .v8_svg_graphics_element import SVGGraphicsElement


@construct_100001
class SVGGElement(SVGGraphicsElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGGElement, self).__init__(*args, **kw)
