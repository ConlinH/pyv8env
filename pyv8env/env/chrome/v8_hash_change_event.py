from .flags import *
from .v8_event import Event


@construct_111001
class HashChangeEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HashChangeEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("oldURL", "get_oldURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("newURL", "get_newURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_oldURL(self):
        val = self._attr.get('oldURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hash_change_event.py -> HashChangeEvent.oldURL -> get attr')

    def get_newURL(self):
        val = self._attr.get('newURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hash_change_event.py -> HashChangeEvent.newURL -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hash_change_event.py -> HashChangeEvent.isTrusted -> get attr')
