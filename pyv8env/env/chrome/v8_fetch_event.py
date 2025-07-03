from .flags import *
from .v8_extendable_event import ExtendableEvent


@construct_112001
class FetchEvent(ExtendableEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FetchEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("request", "get_request", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientId", "get_clientId", None, 0, 1, 0, 0, 0, 0, 1),
        ("resultingClientId", "get_resultingClientId", None, 0, 1, 0, 0, 0, 0, 1),
        ("isReload", "get_isReload", None, 0, 1, 0, 0, 0, 0, 1),
        ("preloadResponse", "get_preloadResponse", None, 0, 1, 0, 1, 0, 0, 1),
        ("handled", "get_handled", None, 0, 1, 0, 1, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("respondWith", "fn_respondWith", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_request(self):
        val = self._attr.get('request')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fetch_event.py -> FetchEvent.request -> get attr')

    def get_clientId(self):
        val = self._attr.get('clientId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fetch_event.py -> FetchEvent.clientId -> get attr')

    def get_resultingClientId(self):
        val = self._attr.get('resultingClientId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fetch_event.py -> FetchEvent.resultingClientId -> get attr')

    def get_isReload(self):
        val = self._attr.get('isReload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fetch_event.py -> FetchEvent.isReload -> get attr')

    def get_preloadResponse(self):
        val = self._attr.get('preloadResponse')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fetch_event.py -> FetchEvent.preloadResponse -> get attr')

    def get_handled(self):
        val = self._attr.get('handled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fetch_event.py -> FetchEvent.handled -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fetch_event.py -> FetchEvent.isTrusted -> get attr')

    def fn_respondWith(self, *args):
        logger.debug(f'patch -> v8_fetch_event.py -> FetchEvent.respondWith{tuple(args)} -> method')
