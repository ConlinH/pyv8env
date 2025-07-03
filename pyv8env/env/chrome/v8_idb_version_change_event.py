from .flags import *
from .v8_event import Event


@construct_111001
class IDBVersionChangeEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(IDBVersionChangeEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("oldVersion", "get_oldVersion", None, 0, 1, 0, 0, 0, 0, 1),
        ("newVersion", "get_newVersion", None, 0, 1, 0, 0, 0, 0, 1),
        ("dataLoss", "get_dataLoss", None, 0, 1, 0, 0, 0, 0, 1),
        ("dataLossMessage", "get_dataLossMessage", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_oldVersion(self):
        val = self._attr.get('oldVersion')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_version_change_event.py -> IDBVersionChangeEvent.oldVersion -> get attr')

    def get_newVersion(self):
        val = self._attr.get('newVersion')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_version_change_event.py -> IDBVersionChangeEvent.newVersion -> get attr')

    def get_dataLoss(self):
        val = self._attr.get('dataLoss')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_version_change_event.py -> IDBVersionChangeEvent.dataLoss -> get attr')

    def get_dataLossMessage(self):
        val = self._attr.get('dataLossMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_version_change_event.py -> IDBVersionChangeEvent.dataLossMessage -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idb_version_change_event.py -> IDBVersionChangeEvent.isTrusted -> get attr')
