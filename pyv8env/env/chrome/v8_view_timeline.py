from .flags import *
from .v8_scroll_timeline import ScrollTimeline


@construct_110001
class ViewTimeline(ScrollTimeline):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ViewTimeline, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("subject", "get_subject", None, 0, 1, 0, 0, 0, 0, 1),
        ("startOffset", "get_startOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("endOffset", "get_endOffset", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_subject(self):
        val = self._attr.get('subject')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_view_timeline.py -> ViewTimeline.subject -> get attr')

    def get_startOffset(self):
        val = self._attr.get('startOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_view_timeline.py -> ViewTimeline.startOffset -> get attr')

    def get_endOffset(self):
        val = self._attr.get('endOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_view_timeline.py -> ViewTimeline.endOffset -> get attr')
