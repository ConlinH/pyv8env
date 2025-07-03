from .flags import *


@construct_100001
class MimeType:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("suffixes", "get_suffixes", None, 0, 1, 0, 0, 0, 0, 1),
        ("description", "get_description", None, 0, 1, 0, 0, 0, 0, 1),
        ("enabledPlugin", "get_enabledPlugin", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mime_type.py -> MimeType.type -> get attr')

    def get_suffixes(self):
        val = self._attr.get('suffixes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mime_type.py -> MimeType.suffixes -> get attr')

    def get_description(self):
        val = self._attr.get('description')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mime_type.py -> MimeType.description -> get attr')

    def get_enabledPlugin(self):
        val = self._attr.get('enabledPlugin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mime_type.py -> MimeType.enabledPlugin -> get attr')
