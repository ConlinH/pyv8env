from .flags import *


@construct_100001
class CookieStoreManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getSubscriptions", "fn_getSubscriptions", 0, 0, 1, 0, 1, 0, 0),
        ("subscribe", "fn_subscribe", 1, 0, 1, 0, 1, 0, 0),
        ("unsubscribe", "fn_unsubscribe", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_getSubscriptions(self, *args):
        logger.debug(f'patch -> v8_cookie_store_manager.py -> CookieStoreManager.getSubscriptions{tuple(args)} -> method')

    def fn_subscribe(self, *args):
        logger.debug(f'patch -> v8_cookie_store_manager.py -> CookieStoreManager.subscribe{tuple(args)} -> method')

    def fn_unsubscribe(self, *args):
        logger.debug(f'patch -> v8_cookie_store_manager.py -> CookieStoreManager.unsubscribe{tuple(args)} -> method')
