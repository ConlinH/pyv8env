from .flags import *
from .v8_event import Event


@construct_111001
class ErrorEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ErrorEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),
        ("filename", "get_filename", None, 0, 1, 0, 0, 0, 0, 1),
        ("lineno", "get_lineno", None, 0, 1, 0, 0, 0, 0, 1),
        ("colno", "get_colno", None, 0, 1, 0, 0, 0, 0, 1),
        ("error", "get_error", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_error_event.py -> ErrorEvent.message -> get attr')

    def get_filename(self):
        val = self._attr.get('filename')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_error_event.py -> ErrorEvent.filename -> get attr')

    def get_lineno(self):
        val = self._attr.get('lineno')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_error_event.py -> ErrorEvent.lineno -> get attr')

    def get_colno(self):
        val = self._attr.get('colno')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_error_event.py -> ErrorEvent.colno -> get attr')

    def get_error(self):
        val = self._attr.get('error')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_error_event.py -> ErrorEvent.error -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_error_event.py -> ErrorEvent.isTrusted -> get attr')
