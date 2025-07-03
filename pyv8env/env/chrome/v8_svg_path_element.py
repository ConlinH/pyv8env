from .flags import *
from .v8_svg_geometry_element import SVGGeometryElement


@construct_100001
class SVGPathElement(SVGGeometryElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGPathElement, self).__init__(*args, **kw)
