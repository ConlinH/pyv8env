from .flags import *


@construct_100001
class Client:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("frameType", "get_frameType", None, 0, 1, 0, 0, 0, 0, 1),
        ("lifecycleState", "get_lifecycleState", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("postMessage", "fn_postMessage", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_client.py -> Client.url -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_client.py -> Client.id -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_client.py -> Client.type -> get attr')

    def get_frameType(self):
        val = self._attr.get('frameType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_client.py -> Client.frameType -> get attr')

    def get_lifecycleState(self):
        val = self._attr.get('lifecycleState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_client.py -> Client.lifecycleState -> get attr')

    def fn_postMessage(self, *args):
        logger.debug(f'patch -> v8_client.py -> Client.postMessage{tuple(args)} -> method')
