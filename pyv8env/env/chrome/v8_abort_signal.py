from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class AbortSignal(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AbortSignal, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("aborted", "get_aborted", None, 0, 1, 0, 0, 0, 0, 1),
        ("reason", "get_reason", None, 0, 1, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("throwIfAborted", "fn_throwIfAborted", 0, 0, 1, 0, 0, 0, 0),
        ("abort", "fn_abort", 0, 0, 2, 0, 1, 1, 0),
        ("any", "fn_any", 1, 0, 2, 0, 1, 1, 0),
        ("timeout", "fn_timeout", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_aborted(self):
        val = self._attr.get('aborted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abort_signal.py -> AbortSignal.aborted -> get attr')

    def get_reason(self):
        val = self._attr.get('reason')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abort_signal.py -> AbortSignal.reason -> get attr')

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_abort_signal.py -> AbortSignal.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def fn_throwIfAborted(self, *args):
        logger.debug(f'patch -> v8_abort_signal.py -> AbortSignal.throwIfAborted{tuple(args)} -> method')

    @classmethod
    def fn_abort(cls, *args):
        logger.debug(f'patch -> v8_abort_signal.py -> AbortSignal.abort{tuple(args)} -> method')

    @classmethod
    def fn_any(cls, *args):
        logger.debug(f'patch -> v8_abort_signal.py -> AbortSignal.any{tuple(args)} -> method')

    @classmethod
    def fn_timeout(cls, *args):
        logger.debug(f'patch -> v8_abort_signal.py -> AbortSignal.timeout{tuple(args)} -> method')
