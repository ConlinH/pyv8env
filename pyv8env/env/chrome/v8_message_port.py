from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class MessagePort(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MessagePort, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),
        ("onmessageerror", "get_onmessageerror", "set_onmessageerror", 0, 1, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("postMessage", "fn_postMessage", 1, 0, 1, 0, 0, 0, 0),
        ("start", "fn_start", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_port.py -> MessagePort.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_onmessageerror(self):
        val = self._attr.get('onmessageerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_port.py -> MessagePort.onmessageerror -> get attr')

    def set_onmessageerror(self, val):
        self._attr['onmessageerror'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_port.py -> MessagePort.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_message_port.py -> MessagePort.close{tuple(args)} -> method')

    def fn_postMessage(self, *args):
        logger.debug(f'patch -> v8_message_port.py -> MessagePort.postMessage{tuple(args)} -> method')

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_message_port.py -> MessagePort.start{tuple(args)} -> method')
