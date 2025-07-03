from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class CloseWatcher(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CloseWatcher, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("oncancel", "get_oncancel", "set_oncancel", 0, 1, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("destroy", "fn_destroy", 0, 0, 1, 0, 0, 0, 0),
        ("requestClose", "fn_requestClose", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_oncancel(self):
        val = self._attr.get('oncancel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_close_watcher.py -> CloseWatcher.oncancel -> get attr')

    def set_oncancel(self, val):
        self._attr['oncancel'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_close_watcher.py -> CloseWatcher.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_close_watcher.py -> CloseWatcher.close{tuple(args)} -> method')

    def fn_destroy(self, *args):
        logger.debug(f'patch -> v8_close_watcher.py -> CloseWatcher.destroy{tuple(args)} -> method')

    def fn_requestClose(self, *args):
        logger.debug(f'patch -> v8_close_watcher.py -> CloseWatcher.requestClose{tuple(args)} -> method')
