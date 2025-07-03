from .flags import *
from .v8_event import Event


@construct_111001
class ContentVisibilityAutoStateChangeEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ContentVisibilityAutoStateChangeEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("skipped", "get_skipped", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_skipped(self):
        val = self._attr.get('skipped')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_content_visibility_auto_state_change_event.py -> ContentVisibilityAutoStateChangeEvent.skipped -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_content_visibility_auto_state_change_event.py -> ContentVisibilityAutoStateChangeEvent.isTrusted -> get attr')
