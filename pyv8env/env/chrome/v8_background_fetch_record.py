from .flags import *


@construct_100001
class BackgroundFetchRecord:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("request", "get_request", None, 0, 1, 0, 0, 0, 0, 1),
        ("responseReady", "get_responseReady", None, 0, 1, 0, 1, 0, 0, 1),

    )

    def get_request(self):
        val = self._attr.get('request')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_record.py -> BackgroundFetchRecord.request -> get attr')

    def get_responseReady(self):
        val = self._attr.get('responseReady')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_record.py -> BackgroundFetchRecord.responseReady -> get attr')
