from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGSymbolElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGSymbolElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("viewBox", "get_viewBox", None, 0, 1, 0, 0, 0, 0, 1),
        ("preserveAspectRatio", "get_preserveAspectRatio", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_viewBox(self):
        val = self._attr.get('viewBox')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_symbol_element.py -> SVGSymbolElement.viewBox -> get attr')

    def get_preserveAspectRatio(self):
        val = self._attr.get('preserveAspectRatio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_symbol_element.py -> SVGSymbolElement.preserveAspectRatio -> get attr')
