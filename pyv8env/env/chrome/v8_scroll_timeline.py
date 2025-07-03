from .flags import *
from .v8_animation_timeline import AnimationTimeline


@construct_110001
class ScrollTimeline(AnimationTimeline):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ScrollTimeline, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("source", "get_source", None, 0, 1, 0, 0, 0, 0, 1),
        ("axis", "get_axis", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_source(self):
        val = self._attr.get('source')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_scroll_timeline.py -> ScrollTimeline.source -> get attr')

    def get_axis(self):
        val = self._attr.get('axis')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_scroll_timeline.py -> ScrollTimeline.axis -> get attr')
