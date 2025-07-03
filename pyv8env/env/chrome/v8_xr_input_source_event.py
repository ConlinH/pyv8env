from .flags import *
from .v8_event import Event


@construct_112001
class XRInputSourceEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRInputSourceEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("frame", "get_frame", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputSource", "get_inputSource", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_frame(self):
        val = self._attr.get('frame')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source_event.py -> XRInputSourceEvent.frame -> get attr')

    def get_inputSource(self):
        val = self._attr.get('inputSource')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source_event.py -> XRInputSourceEvent.inputSource -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_input_source_event.py -> XRInputSourceEvent.isTrusted -> get attr')
