from .flags import *
from .v8_event import Event


@construct_111001
class MessageEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MessageEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("origin", "get_origin", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastEventId", "get_lastEventId", None, 0, 1, 0, 0, 0, 0, 1),
        ("source", "get_source", None, 0, 1, 0, 0, 0, 0, 1),
        ("ports", "get_ports", None, 0, 1, 0, 0, 0, 0, 1),
        ("userActivation", "get_userActivation", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("initMessageEvent", "fn_initMessageEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_event.py -> MessageEvent.data -> get attr')

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_event.py -> MessageEvent.origin -> get attr')

    def get_lastEventId(self):
        val = self._attr.get('lastEventId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_event.py -> MessageEvent.lastEventId -> get attr')

    def get_source(self):
        val = self._attr.get('source')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_event.py -> MessageEvent.source -> get attr')

    def get_ports(self):
        val = self._attr.get('ports')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_event.py -> MessageEvent.ports -> get attr')

    def get_userActivation(self):
        val = self._attr.get('userActivation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_event.py -> MessageEvent.userActivation -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_event.py -> MessageEvent.isTrusted -> get attr')

    def fn_initMessageEvent(self, *args):
        logger.debug(f'patch -> v8_message_event.py -> MessageEvent.initMessageEvent{tuple(args)} -> method')
