from .flags import *
from .v8_animation_effect import AnimationEffect


@construct_111001
class KeyframeEffect(AnimationEffect):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(KeyframeEffect, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("target", "get_target", "set_target", 0, 1, 0, 0, 0, 0, 1),
        ("pseudoElement", "get_pseudoElement", "set_pseudoElement", 0, 1, 0, 0, 0, 0, 1),
        ("composite", "get_composite", "set_composite", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getKeyframes", "fn_getKeyframes", 0, 0, 1, 0, 0, 0, 0),
        ("setKeyframes", "fn_setKeyframes", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyframe_effect.py -> KeyframeEffect.target -> get attr')

    def set_target(self, val):
        self._attr['target'] = val

    def get_pseudoElement(self):
        val = self._attr.get('pseudoElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyframe_effect.py -> KeyframeEffect.pseudoElement -> get attr')

    def set_pseudoElement(self, val):
        self._attr['pseudoElement'] = val

    def get_composite(self):
        val = self._attr.get('composite')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyframe_effect.py -> KeyframeEffect.composite -> get attr')

    def set_composite(self, val):
        self._attr['composite'] = val

    def fn_getKeyframes(self, *args):
        logger.debug(f'patch -> v8_keyframe_effect.py -> KeyframeEffect.getKeyframes{tuple(args)} -> method')

    def fn_setKeyframes(self, *args):
        logger.debug(f'patch -> v8_keyframe_effect.py -> KeyframeEffect.setKeyframes{tuple(args)} -> method')
