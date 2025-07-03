from .flags import *


@construct_100001
class IdleDeadline:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("didTimeout", "get_didTimeout", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("timeRemaining", "fn_timeRemaining", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_didTimeout(self):
        val = self._attr.get('didTimeout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idle_deadline.py -> IdleDeadline.didTimeout -> get attr')

    def fn_timeRemaining(self, *args):
        logger.debug(f'patch -> v8_idle_deadline.py -> IdleDeadline.timeRemaining{tuple(args)} -> method')
