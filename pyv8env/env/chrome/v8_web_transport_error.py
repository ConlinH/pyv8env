from .flags import *
from .v8_dom_exception import DOMException


@construct_110001
class WebTransportError(DOMException):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WebTransportError, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("streamErrorCode", "get_streamErrorCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("source", "get_source", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_streamErrorCode(self):
        val = self._attr.get('streamErrorCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_error.py -> WebTransportError.streamErrorCode -> get attr')

    def get_source(self):
        val = self._attr.get('source')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_transport_error.py -> WebTransportError.source -> get attr')
