from .flags import *


@construct_100101
class ImageTrackList:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_image_track_list.py -> ImageTrackList.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_image_track_list.py -> ImageTrackList.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_image_track_list.py -> ImageTrackList.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_image_track_list.py -> ImageTrackList.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_image_track_list.py -> ImageTrackList.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_image_track_list.py -> ImageTrackList.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectedIndex", "get_selectedIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectedTrack", "get_selectedTrack", None, 0, 1, 0, 0, 0, 0, 1),
        ("ready", "get_ready", None, 0, 1, 0, 1, 0, 0, 1),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_track_list.py -> ImageTrackList.length -> get attr')

    def get_selectedIndex(self):
        val = self._attr.get('selectedIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_track_list.py -> ImageTrackList.selectedIndex -> get attr')

    def get_selectedTrack(self):
        val = self._attr.get('selectedTrack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_track_list.py -> ImageTrackList.selectedTrack -> get attr')

    def get_ready(self):
        val = self._attr.get('ready')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_track_list.py -> ImageTrackList.ready -> get attr')
