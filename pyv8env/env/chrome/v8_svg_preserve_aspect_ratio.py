from .flags import *


@construct_100001
class SVGPreserveAspectRatio:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    SVG_PRESERVEASPECTRATIO_UNKNOWN = 0
    SVG_PRESERVEASPECTRATIO_NONE = 1
    SVG_PRESERVEASPECTRATIO_XMINYMIN = 2
    SVG_PRESERVEASPECTRATIO_XMIDYMIN = 3
    SVG_PRESERVEASPECTRATIO_XMAXYMIN = 4
    SVG_PRESERVEASPECTRATIO_XMINYMID = 5
    SVG_PRESERVEASPECTRATIO_XMIDYMID = 6
    SVG_PRESERVEASPECTRATIO_XMAXYMID = 7
    SVG_PRESERVEASPECTRATIO_XMINYMAX = 8
    SVG_PRESERVEASPECTRATIO_XMIDYMAX = 9
    SVG_PRESERVEASPECTRATIO_XMAXYMAX = 10
    SVG_MEETORSLICE_UNKNOWN = 0
    SVG_MEETORSLICE_MEET = 1
    SVG_MEETORSLICE_SLICE = 2

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("meetOrSlice", "get_meetOrSlice", "set_meetOrSlice", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_preserve_aspect_ratio.py -> SVGPreserveAspectRatio.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_meetOrSlice(self):
        val = self._attr.get('meetOrSlice')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_preserve_aspect_ratio.py -> SVGPreserveAspectRatio.meetOrSlice -> get attr')

    def set_meetOrSlice(self, val):
        self._attr['meetOrSlice'] = val
