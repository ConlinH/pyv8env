from .flags import *


@construct_110001
class MediaMetadata:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("title", "get_title", "set_title", 0, 1, 0, 0, 0, 0, 1),
        ("artist", "get_artist", "set_artist", 0, 1, 0, 0, 0, 0, 1),
        ("album", "get_album", "set_album", 0, 1, 0, 0, 0, 0, 1),
        ("artwork", "get_artwork", "set_artwork", 0, 1, 0, 0, 0, 0, 1),
        ("chapterInfo", "get_chapterInfo", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_title(self):
        val = self._attr.get('title')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_metadata.py -> MediaMetadata.title -> get attr')

    def set_title(self, val):
        self._attr['title'] = val

    def get_artist(self):
        val = self._attr.get('artist')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_metadata.py -> MediaMetadata.artist -> get attr')

    def set_artist(self, val):
        self._attr['artist'] = val

    def get_album(self):
        val = self._attr.get('album')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_metadata.py -> MediaMetadata.album -> get attr')

    def set_album(self, val):
        self._attr['album'] = val

    def get_artwork(self):
        val = self._attr.get('artwork')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_metadata.py -> MediaMetadata.artwork -> get attr')

    def set_artwork(self, val):
        self._attr['artwork'] = val

    def get_chapterInfo(self):
        val = self._attr.get('chapterInfo')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_metadata.py -> MediaMetadata.chapterInfo -> get attr')
