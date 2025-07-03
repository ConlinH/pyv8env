from .flags import *


@construct_110001
class TextFormat:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("rangeStart", "get_rangeStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("rangeEnd", "get_rangeEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("underlineStyle", "get_underlineStyle", None, 0, 1, 0, 0, 0, 0, 1),
        ("underlineThickness", "get_underlineThickness", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_rangeStart(self):
        val = self._attr.get('rangeStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_format.py -> TextFormat.rangeStart -> get attr')

    def get_rangeEnd(self):
        val = self._attr.get('rangeEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_format.py -> TextFormat.rangeEnd -> get attr')

    def get_underlineStyle(self):
        val = self._attr.get('underlineStyle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_format.py -> TextFormat.underlineStyle -> get attr')

    def get_underlineThickness(self):
        val = self._attr.get('underlineThickness')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_format.py -> TextFormat.underlineThickness -> get attr')
