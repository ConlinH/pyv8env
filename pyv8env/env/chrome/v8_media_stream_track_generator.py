from .flags import *
from .v8_media_stream_track import MediaStreamTrack


@construct_111001
class MediaStreamTrackGenerator(MediaStreamTrack):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaStreamTrackGenerator, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("writable", "get_writable", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_writable(self):
        val = self._attr.get('writable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_stream_track_generator.py -> MediaStreamTrackGenerator.writable -> get attr')
