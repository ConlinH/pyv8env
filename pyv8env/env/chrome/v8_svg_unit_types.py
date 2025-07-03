from .flags import *


@construct_100001
class SVGUnitTypes:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    SVG_UNIT_TYPE_UNKNOWN = 0
    SVG_UNIT_TYPE_USERSPACEONUSE = 1
    SVG_UNIT_TYPE_OBJECTBOUNDINGBOX = 2
