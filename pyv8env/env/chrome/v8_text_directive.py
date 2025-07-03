from .flags import *
from .v8_selector_directive import SelectorDirective


@construct_110001
class TextDirective(SelectorDirective):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TextDirective, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("prefix", "get_prefix", None, 0, 1, 0, 0, 0, 0, 1),
        ("textStart", "get_textStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("textEnd", "get_textEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("suffix", "get_suffix", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_prefix(self):
        val = self._attr.get('prefix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_directive.py -> TextDirective.prefix -> get attr')

    def get_textStart(self):
        val = self._attr.get('textStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_directive.py -> TextDirective.textStart -> get attr')

    def get_textEnd(self):
        val = self._attr.get('textEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_directive.py -> TextDirective.textEnd -> get attr')

    def get_suffix(self):
        val = self._attr.get('suffix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_directive.py -> TextDirective.suffix -> get attr')
