from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class CookieStore(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CookieStore, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("delete", "fn_delete", 1, 0, 1, 0, 1, 0, 0),
        ("get", "fn_get", 0, 0, 1, 0, 1, 0, 0),
        ("getAll", "fn_getAll", 0, 0, 1, 0, 1, 0, 0),
        ("set", "fn_set", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_cookie_store.py -> CookieStore.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_cookie_store.py -> CookieStore.delete{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_cookie_store.py -> CookieStore.get{tuple(args)} -> method')

    def fn_getAll(self, *args):
        logger.debug(f'patch -> v8_cookie_store.py -> CookieStore.getAll{tuple(args)} -> method')

    def fn_set(self, *args):
        logger.debug(f'patch -> v8_cookie_store.py -> CookieStore.set{tuple(args)} -> method')
