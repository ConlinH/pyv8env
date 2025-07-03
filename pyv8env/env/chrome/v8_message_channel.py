from .flags import *


@construct_110001
class MessageChannel:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("port1", "get_port1", None, 0, 1, 0, 0, 0, 0, 1),
        ("port2", "get_port2", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_port1(self):
        val = self._attr.get('port1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_channel.py -> MessageChannel.port1 -> get attr')

    def get_port2(self):
        val = self._attr.get('port2')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_message_channel.py -> MessageChannel.port2 -> get attr')
