from .flags import *


@construct_100001
class AbstractRange:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("startContainer", "get_startContainer", None, 0, 1, 0, 0, 0, 0, 1),
        ("startOffset", "get_startOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("endContainer", "get_endContainer", None, 0, 1, 0, 0, 0, 0, 1),
        ("endOffset", "get_endOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("collapsed", "get_collapsed", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_startContainer(self):
        val = self._attr.get('startContainer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abstract_range.py -> AbstractRange.startContainer -> get attr')

    def get_startOffset(self):
        val = self._attr.get('startOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abstract_range.py -> AbstractRange.startOffset -> get attr')

    def get_endContainer(self):
        val = self._attr.get('endContainer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abstract_range.py -> AbstractRange.endContainer -> get attr')

    def get_endOffset(self):
        val = self._attr.get('endOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abstract_range.py -> AbstractRange.endOffset -> get attr')

    def get_collapsed(self):
        val = self._attr.get('collapsed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abstract_range.py -> AbstractRange.collapsed -> get attr')
