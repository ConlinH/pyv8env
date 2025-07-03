from .flags import *


@construct_100001
class WorkletAnimationEffect:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("localTime", "get_localTime", "set_localTime", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getComputedTiming", "fn_getComputedTiming", 0, 0, 1, 0, 0, 0, 0),
        ("getTiming", "fn_getTiming", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_localTime(self):
        val = self._attr.get('localTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_worklet_animation_effect.py -> WorkletAnimationEffect.localTime -> get attr')

    def set_localTime(self, val):
        self._attr['localTime'] = val

    def fn_getComputedTiming(self, *args):
        logger.debug(f'patch -> v8_worklet_animation_effect.py -> WorkletAnimationEffect.getComputedTiming{tuple(args)} -> method')

    def fn_getTiming(self, *args):
        logger.debug(f'patch -> v8_worklet_animation_effect.py -> WorkletAnimationEffect.getTiming{tuple(args)} -> method')
