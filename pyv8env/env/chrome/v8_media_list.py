from .flags import *


@construct_100101
class MediaList:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_media_list.py -> MediaList.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_media_list.py -> MediaList.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_media_list.py -> MediaList.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_media_list.py -> MediaList.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_media_list.py -> MediaList.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_media_list.py -> MediaList.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaText", "get_mediaText", "set_mediaText", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("appendMedium", "fn_appendMedium", 1, 0, 1, 0, 0, 0, 0),
        ("deleteMedium", "fn_deleteMedium", 1, 0, 1, 0, 0, 0, 0),
        ("item", "fn_item", 1, 0, 1, 0, 0, 0, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_list.py -> MediaList.length -> get attr')

    def get_mediaText(self):
        val = self._attr.get('mediaText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_list.py -> MediaList.mediaText -> get attr')

    def set_mediaText(self, val):
        self._attr['mediaText'] = val

    def fn_appendMedium(self, *args):
        logger.debug(f'patch -> v8_media_list.py -> MediaList.appendMedium{tuple(args)} -> method')

    def fn_deleteMedium(self, *args):
        logger.debug(f'patch -> v8_media_list.py -> MediaList.deleteMedium{tuple(args)} -> method')

    def fn_item(self, *args):
        logger.debug(f'patch -> v8_media_list.py -> MediaList.item{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_media_list.py -> MediaList.toString{tuple(args)} -> method')
