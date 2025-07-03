from .flags import *
from .v8_mouse_event import MouseEvent


@construct_111001
class DragEvent(MouseEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DragEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("dataTransfer", "get_dataTransfer", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_dataTransfer(self):
        val = self._attr.get('dataTransfer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_drag_event.py -> DragEvent.dataTransfer -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_drag_event.py -> DragEvent.isTrusted -> get attr')
