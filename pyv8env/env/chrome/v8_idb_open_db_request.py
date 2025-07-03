from .flags import *
from .v8_idb_request import IDBRequest


@construct_100001
class IDBOpenDBRequest(IDBRequest):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(IDBOpenDBRequest, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onblocked", "get_onblocked", "set_onblocked", 0, 1, 0, 0, 0, 0, 1),
        ("onupgradeneeded", "get_onupgradeneeded", "set_onupgradeneeded", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_onblocked(self):
        val = self._attr.get('onblocked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_open_db_request.py -> IDBOpenDBRequest.onblocked -> get attr')

    def set_onblocked(self, val):
        self._attr['onblocked'] = val

    def get_onupgradeneeded(self):
        val = self._attr.get('onupgradeneeded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_open_db_request.py -> IDBOpenDBRequest.onupgradeneeded -> get attr')

    def set_onupgradeneeded(self, val):
        self._attr['onupgradeneeded'] = val
