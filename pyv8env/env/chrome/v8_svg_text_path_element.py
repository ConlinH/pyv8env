from .flags import *
from .v8_svg_text_content_element import SVGTextContentElement


@construct_100001
class SVGTextPathElement(SVGTextContentElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGTextPathElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("startOffset", "get_startOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("method", "get_method", None, 0, 1, 0, 0, 0, 0, 1),
        ("spacing", "get_spacing", None, 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_startOffset(self):
        val = self._attr.get('startOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_path_element.py -> SVGTextPathElement.startOffset -> get attr')

    def get_method(self):
        val = self._attr.get('method')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_path_element.py -> SVGTextPathElement.method -> get attr')

    def get_spacing(self):
        val = self._attr.get('spacing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_path_element.py -> SVGTextPathElement.spacing -> get attr')

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_path_element.py -> SVGTextPathElement.href -> get attr')
