from .flags import *


@construct_100001
class AnimationEffect:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getComputedTiming", "fn_getComputedTiming", 0, 0, 1, 0, 0, 0, 0),
        ("getTiming", "fn_getTiming", 0, 0, 1, 0, 0, 0, 0),
        ("updateTiming", "fn_updateTiming", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_getComputedTiming(self, *args):
        logger.debug(f'patch -> v8_animation_effect.py -> AnimationEffect.getComputedTiming{tuple(args)} -> method')

    def fn_getTiming(self, *args):
        logger.debug(f'patch -> v8_animation_effect.py -> AnimationEffect.getTiming{tuple(args)} -> method')

    def fn_updateTiming(self, *args):
        logger.debug(f'patch -> v8_animation_effect.py -> AnimationEffect.updateTiming{tuple(args)} -> method')
