from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class MediaSource(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaSource, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("sourceBuffers", "get_sourceBuffers", None, 0, 1, 0, 0, 0, 0, 1),
        ("activeSourceBuffers", "get_activeSourceBuffers", None, 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", "set_duration", 0, 1, 0, 0, 0, 0, 1),
        ("onsourceopen", "get_onsourceopen", "set_onsourceopen", 0, 1, 0, 0, 0, 0, 1),
        ("onsourceended", "get_onsourceended", "set_onsourceended", 0, 1, 0, 0, 0, 0, 1),
        ("onsourceclose", "get_onsourceclose", "set_onsourceclose", 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("canConstructInDedicatedWorker", "get_canConstructInDedicatedWorker", None, 0, 2, 0, 1, 1, 1, 1),
        ("handle", "get_handle", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addSourceBuffer", "fn_addSourceBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("clearLiveSeekableRange", "fn_clearLiveSeekableRange", 0, 0, 1, 0, 0, 0, 0),
        ("endOfStream", "fn_endOfStream", 0, 0, 1, 0, 0, 0, 0),
        ("removeSourceBuffer", "fn_removeSourceBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("setLiveSeekableRange", "fn_setLiveSeekableRange", 2, 0, 1, 0, 0, 0, 0),
        ("isTypeSupported", "fn_isTypeSupported", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_sourceBuffers(self):
        val = self._attr.get('sourceBuffers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.sourceBuffers -> get attr')

    def get_activeSourceBuffers(self):
        val = self._attr.get('activeSourceBuffers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.activeSourceBuffers -> get attr')

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.duration -> get attr')

    def set_duration(self, val):
        self._attr['duration'] = val

    def get_onsourceopen(self):
        val = self._attr.get('onsourceopen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.onsourceopen -> get attr')

    def set_onsourceopen(self, val):
        self._attr['onsourceopen'] = val

    def get_onsourceended(self):
        val = self._attr.get('onsourceended')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.onsourceended -> get attr')

    def set_onsourceended(self, val):
        self._attr['onsourceended'] = val

    def get_onsourceclose(self):
        val = self._attr.get('onsourceclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.onsourceclose -> get attr')

    def set_onsourceclose(self, val):
        self._attr['onsourceclose'] = val

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.readyState -> get attr')

    @classmethod
    def get_canConstructInDedicatedWorker(cls):
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.canConstructInDedicatedWorker -> get attr')

    def get_handle(self):
        val = self._attr.get('handle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.handle -> get attr')

    def fn_addSourceBuffer(self, *args):
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.addSourceBuffer{tuple(args)} -> method')

    def fn_clearLiveSeekableRange(self, *args):
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.clearLiveSeekableRange{tuple(args)} -> method')

    def fn_endOfStream(self, *args):
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.endOfStream{tuple(args)} -> method')

    def fn_removeSourceBuffer(self, *args):
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.removeSourceBuffer{tuple(args)} -> method')

    def fn_setLiveSeekableRange(self, *args):
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.setLiveSeekableRange{tuple(args)} -> method')

    @classmethod
    def fn_isTypeSupported(cls, *args):
        logger.debug(f'patch -> v8_media_source.py -> MediaSource.isTypeSupported{tuple(args)} -> method')
