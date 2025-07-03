from .flags import *
from .v8_event import Event


@construct_111001
class MediaEncryptedEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaEncryptedEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("initDataType", "get_initDataType", None, 0, 1, 0, 0, 0, 0, 1),
        ("initData", "get_initData", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_initDataType(self):
        val = self._attr.get('initDataType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_encrypted_event.py -> MediaEncryptedEvent.initDataType -> get attr')

    def get_initData(self):
        val = self._attr.get('initData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_encrypted_event.py -> MediaEncryptedEvent.initData -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_encrypted_event.py -> MediaEncryptedEvent.isTrusted -> get attr')
