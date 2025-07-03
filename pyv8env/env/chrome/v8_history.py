from .flags import *


@construct_100001
class History:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollRestoration", "get_scrollRestoration", "set_scrollRestoration", 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("back", "fn_back", 0, 0, 1, 0, 0, 0, 0),
        ("forward", "fn_forward", 0, 0, 1, 0, 0, 0, 0),
        ("go", "fn_go", 0, 0, 1, 0, 0, 0, 0),
        ("pushState", "fn_pushState", 2, 0, 1, 0, 0, 0, 0),
        ("replaceState", "fn_replaceState", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_history.py -> History.length -> get attr')

    def get_scrollRestoration(self):
        val = self._attr.get('scrollRestoration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_history.py -> History.scrollRestoration -> get attr')

    def set_scrollRestoration(self, val):
        self._attr['scrollRestoration'] = val

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_history.py -> History.state -> get attr')

    def fn_back(self, *args):
        logger.debug(f'patch -> v8_history.py -> History.back{tuple(args)} -> method')

    def fn_forward(self, *args):
        logger.debug(f'patch -> v8_history.py -> History.forward{tuple(args)} -> method')

    def fn_go(self, *args):
        logger.debug(f'patch -> v8_history.py -> History.go{tuple(args)} -> method')

    def fn_pushState(self, *args):
        logger.debug(f'patch -> v8_history.py -> History.pushState{tuple(args)} -> method')

    def fn_replaceState(self, *args):
        logger.debug(f'patch -> v8_history.py -> History.replaceState{tuple(args)} -> method')
