from .flags import *
from .v8_extendable_event import ExtendableEvent


@construct_111001
class ExtendableMessageEvent(ExtendableEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ExtendableMessageEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("origin", "get_origin", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastEventId", "get_lastEventId", None, 0, 1, 0, 0, 0, 0, 1),
        ("source", "get_source", None, 0, 1, 0, 0, 0, 0, 1),
        ("ports", "get_ports", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_extendable_message_event.py -> ExtendableMessageEvent.data -> get attr')

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_extendable_message_event.py -> ExtendableMessageEvent.origin -> get attr')

    def get_lastEventId(self):
        val = self._attr.get('lastEventId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_extendable_message_event.py -> ExtendableMessageEvent.lastEventId -> get attr')

    def get_source(self):
        val = self._attr.get('source')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_extendable_message_event.py -> ExtendableMessageEvent.source -> get attr')

    def get_ports(self):
        val = self._attr.get('ports')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_extendable_message_event.py -> ExtendableMessageEvent.ports -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_extendable_message_event.py -> ExtendableMessageEvent.isTrusted -> get attr')
