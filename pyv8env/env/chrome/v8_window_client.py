from .flags import *
from .v8_client import Client


@construct_100001
class WindowClient(Client):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WindowClient, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("visibilityState", "get_visibilityState", None, 0, 1, 0, 0, 0, 0, 1),
        ("focused", "get_focused", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("focus", "fn_focus", 0, 0, 1, 0, 1, 0, 0),
        ("navigate", "fn_navigate", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_visibilityState(self):
        val = self._attr.get('visibilityState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_window_client.py -> WindowClient.visibilityState -> get attr')

    def get_focused(self):
        val = self._attr.get('focused')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_window_client.py -> WindowClient.focused -> get attr')

    def fn_focus(self, *args):
        logger.debug(f'patch -> v8_window_client.py -> WindowClient.focus{tuple(args)} -> method')

    def fn_navigate(self, *args):
        logger.debug(f'patch -> v8_window_client.py -> WindowClient.navigate{tuple(args)} -> method')
