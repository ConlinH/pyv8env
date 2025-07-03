from .flags import *
from .v8_event import Event


@construct_111001
class UIEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(UIEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("view", "get_view", None, 0, 1, 0, 0, 0, 0, 1),
        ("detail", "get_detail", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceCapabilities", "get_sourceCapabilities", None, 0, 1, 0, 0, 0, 0, 1),
        ("which", "get_which", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("initUIEvent", "fn_initUIEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_view(self):
        val = self._attr.get('view')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ui_event.py -> UIEvent.view -> get attr')

    def get_detail(self):
        val = self._attr.get('detail')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ui_event.py -> UIEvent.detail -> get attr')

    def get_sourceCapabilities(self):
        val = self._attr.get('sourceCapabilities')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ui_event.py -> UIEvent.sourceCapabilities -> get attr')

    def get_which(self):
        val = self._attr.get('which')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ui_event.py -> UIEvent.which -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ui_event.py -> UIEvent.isTrusted -> get attr')

    def fn_initUIEvent(self, *args):
        logger.debug(f'patch -> v8_ui_event.py -> UIEvent.initUIEvent{tuple(args)} -> method')
