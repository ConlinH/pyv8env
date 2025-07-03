from .flags import *
from .v8_dom_exception import DOMException


@construct_110001
class WebSocketError(DOMException):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WebSocketError, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("closeCode", "get_closeCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("reason", "get_reason", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_closeCode(self):
        val = self._attr.get('closeCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket_error.py -> WebSocketError.closeCode -> get attr')

    def get_reason(self):
        val = self._attr.get('reason')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_websocket_error.py -> WebSocketError.reason -> get attr')
