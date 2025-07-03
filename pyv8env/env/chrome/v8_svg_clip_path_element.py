from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGClipPathElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGClipPathElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("clipPathUnits", "get_clipPathUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("transform", "get_transform", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_clipPathUnits(self):
        val = self._attr.get('clipPathUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_clip_path_element.py -> SVGClipPathElement.clipPathUnits -> get attr')

    def get_transform(self):
        val = self._attr.get('transform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_clip_path_element.py -> SVGClipPathElement.transform -> get attr')
