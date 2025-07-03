from .flags import *
from .v8_background_fetch_event import BackgroundFetchEvent


@construct_112001
class BackgroundFetchUpdateUIEvent(BackgroundFetchEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BackgroundFetchUpdateUIEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("updateUI", "fn_updateUI", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_update_ui_event.py -> BackgroundFetchUpdateUIEvent.isTrusted -> get attr')

    def fn_updateUI(self, *args):
        logger.debug(f'patch -> v8_background_fetch_update_ui_event.py -> BackgroundFetchUpdateUIEvent.updateUI{tuple(args)} -> method')
