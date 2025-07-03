from .flags import *
from .v8_event import Event


@construct_100001
class SnapEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SnapEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("snapTargetBlock", "get_snapTargetBlock", None, 0, 1, 0, 0, 0, 0, 1),
        ("snapTargetInline", "get_snapTargetInline", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_snapTargetBlock(self):
        val = self._attr.get('snapTargetBlock')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_snap_event.py -> SnapEvent.snapTargetBlock -> get attr')

    def get_snapTargetInline(self):
        val = self._attr.get('snapTargetInline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_snap_event.py -> SnapEvent.snapTargetInline -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_snap_event.py -> SnapEvent.isTrusted -> get attr')
