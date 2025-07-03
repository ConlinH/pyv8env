from .flags import *
from .v8_event_target import EventTarget


@construct_100101
class TextTrackList(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TextTrackList, self).__init__(*args, **kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_text_track_list.py -> TextTrackList.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_text_track_list.py -> TextTrackList.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_text_track_list.py -> TextTrackList.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_text_track_list.py -> TextTrackList.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_text_track_list.py -> TextTrackList.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_text_track_list.py -> TextTrackList.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),
        ("onaddtrack", "get_onaddtrack", "set_onaddtrack", 0, 1, 0, 0, 0, 0, 1),
        ("onremovetrack", "get_onremovetrack", "set_onremovetrack", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getTrackById", "fn_getTrackById", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_list.py -> TextTrackList.length -> get attr')

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_list.py -> TextTrackList.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def get_onaddtrack(self):
        val = self._attr.get('onaddtrack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_list.py -> TextTrackList.onaddtrack -> get attr')

    def set_onaddtrack(self, val):
        self._attr['onaddtrack'] = val

    def get_onremovetrack(self):
        val = self._attr.get('onremovetrack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_track_list.py -> TextTrackList.onremovetrack -> get attr')

    def set_onremovetrack(self, val):
        self._attr['onremovetrack'] = val

    def fn_getTrackById(self, *args):
        logger.debug(f'patch -> v8_text_track_list.py -> TextTrackList.getTrackById{tuple(args)} -> method')
