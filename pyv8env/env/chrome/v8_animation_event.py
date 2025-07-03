from .flags import *
from .v8_event import Event


@construct_111001
class AnimationEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AnimationEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("animationName", "get_animationName", None, 0, 1, 0, 0, 0, 0, 1),
        ("elapsedTime", "get_elapsedTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("pseudoElement", "get_pseudoElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_animationName(self):
        val = self._attr.get('animationName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_event.py -> AnimationEvent.animationName -> get attr')

    def get_elapsedTime(self):
        val = self._attr.get('elapsedTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_event.py -> AnimationEvent.elapsedTime -> get attr')

    def get_pseudoElement(self):
        val = self._attr.get('pseudoElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_event.py -> AnimationEvent.pseudoElement -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_animation_event.py -> AnimationEvent.isTrusted -> get attr')
