from .flags import *


@construct_100001
class LayoutShiftAttribution:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("node", "get_node", None, 0, 1, 0, 0, 0, 0, 1),
        ("previousRect", "get_previousRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentRect", "get_currentRect", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_node(self):
        val = self._attr.get('node')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_shift_attribution.py -> LayoutShiftAttribution.node -> get attr')

    def get_previousRect(self):
        val = self._attr.get('previousRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_shift_attribution.py -> LayoutShiftAttribution.previousRect -> get attr')

    def get_currentRect(self):
        val = self._attr.get('currentRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_shift_attribution.py -> LayoutShiftAttribution.currentRect -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_layout_shift_attribution.py -> LayoutShiftAttribution.toJSON{tuple(args)} -> method')
