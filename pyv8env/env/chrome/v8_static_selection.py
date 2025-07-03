from .flags import *


@construct_000001
class StaticSelection:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("anchorNode", "get_anchorNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("anchorOffset", "get_anchorOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("focusNode", "get_focusNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("focusOffset", "get_focusOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("isCollapsed", "get_isCollapsed", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_anchorNode(self):
        val = self._attr.get('anchorNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_static_selection.py -> StaticSelection.anchorNode -> get attr')

    def get_anchorOffset(self):
        val = self._attr.get('anchorOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_static_selection.py -> StaticSelection.anchorOffset -> get attr')

    def get_focusNode(self):
        val = self._attr.get('focusNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_static_selection.py -> StaticSelection.focusNode -> get attr')

    def get_focusOffset(self):
        val = self._attr.get('focusOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_static_selection.py -> StaticSelection.focusOffset -> get attr')

    def get_isCollapsed(self):
        val = self._attr.get('isCollapsed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_static_selection.py -> StaticSelection.isCollapsed -> get attr')
