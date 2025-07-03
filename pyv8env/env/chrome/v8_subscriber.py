from .flags import *


@construct_100001
class Subscriber:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("active", "get_active", None, 0, 1, 0, 0, 0, 0, 1),
        ("signal", "get_signal", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addTeardown", "fn_addTeardown", 1, 0, 1, 0, 0, 0, 0),
        ("complete", "fn_complete", 0, 0, 1, 0, 0, 0, 0),
        ("error", "fn_error", 1, 0, 1, 0, 0, 0, 0),
        ("next", "fn_next", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_active(self):
        val = self._attr.get('active')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_subscriber.py -> Subscriber.active -> get attr')

    def get_signal(self):
        val = self._attr.get('signal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_subscriber.py -> Subscriber.signal -> get attr')

    def fn_addTeardown(self, *args):
        logger.debug(f'patch -> v8_subscriber.py -> Subscriber.addTeardown{tuple(args)} -> method')

    def fn_complete(self, *args):
        logger.debug(f'patch -> v8_subscriber.py -> Subscriber.complete{tuple(args)} -> method')

    def fn_error(self, *args):
        logger.debug(f'patch -> v8_subscriber.py -> Subscriber.error{tuple(args)} -> method')

    def fn_next(self, *args):
        logger.debug(f'patch -> v8_subscriber.py -> Subscriber.next{tuple(args)} -> method')
