from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class SourceBuffer(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SourceBuffer, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("mode", "get_mode", "set_mode", 0, 1, 0, 0, 0, 0, 1),
        ("updating", "get_updating", None, 0, 1, 0, 0, 0, 0, 1),
        ("buffered", "get_buffered", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestampOffset", "get_timestampOffset", "set_timestampOffset", 0, 1, 0, 0, 0, 0, 1),
        ("appendWindowStart", "get_appendWindowStart", "set_appendWindowStart", 0, 1, 0, 0, 0, 0, 1),
        ("appendWindowEnd", "get_appendWindowEnd", "set_appendWindowEnd", 0, 1, 0, 0, 0, 0, 1),
        ("onupdatestart", "get_onupdatestart", "set_onupdatestart", 0, 1, 0, 0, 0, 0, 1),
        ("onupdate", "get_onupdate", "set_onupdate", 0, 1, 0, 0, 0, 0, 1),
        ("onupdateend", "get_onupdateend", "set_onupdateend", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 1, 0, 0, 0, 0, 1),
        ("audioTracks", "get_audioTracks", None, 0, 1, 0, 0, 0, 0, 1),
        ("videoTracks", "get_videoTracks", None, 0, 1, 0, 0, 0, 0, 1),
        ("trackDefaults", "get_trackDefaults", "set_trackDefaults", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 0, 0, 0),
        ("appendBuffer", "fn_appendBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("changeType", "fn_changeType", 1, 0, 1, 0, 0, 0, 0),
        ("remove", "fn_remove", 2, 0, 1, 0, 0, 0, 0),
        ("appendEncodedChunks", "fn_appendEncodedChunks", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_mode(self):
        val = self._attr.get('mode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.mode -> get attr')

    def set_mode(self, val):
        self._attr['mode'] = val

    def get_updating(self):
        val = self._attr.get('updating')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.updating -> get attr')

    def get_buffered(self):
        val = self._attr.get('buffered')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.buffered -> get attr')

    def get_timestampOffset(self):
        val = self._attr.get('timestampOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.timestampOffset -> get attr')

    def set_timestampOffset(self, val):
        self._attr['timestampOffset'] = val

    def get_appendWindowStart(self):
        val = self._attr.get('appendWindowStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.appendWindowStart -> get attr')

    def set_appendWindowStart(self, val):
        self._attr['appendWindowStart'] = val

    def get_appendWindowEnd(self):
        val = self._attr.get('appendWindowEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.appendWindowEnd -> get attr')

    def set_appendWindowEnd(self, val):
        self._attr['appendWindowEnd'] = val

    def get_onupdatestart(self):
        val = self._attr.get('onupdatestart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.onupdatestart -> get attr')

    def set_onupdatestart(self, val):
        self._attr['onupdatestart'] = val

    def get_onupdate(self):
        val = self._attr.get('onupdate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.onupdate -> get attr')

    def set_onupdate(self, val):
        self._attr['onupdate'] = val

    def get_onupdateend(self):
        val = self._attr.get('onupdateend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.onupdateend -> get attr')

    def set_onupdateend(self, val):
        self._attr['onupdateend'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_audioTracks(self):
        val = self._attr.get('audioTracks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.audioTracks -> get attr')

    def get_videoTracks(self):
        val = self._attr.get('videoTracks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.videoTracks -> get attr')

    def get_trackDefaults(self):
        val = self._attr.get('trackDefaults')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.trackDefaults -> get attr')

    def set_trackDefaults(self, val):
        self._attr['trackDefaults'] = val

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.abort{tuple(args)} -> method')

    def fn_appendBuffer(self, *args):
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.appendBuffer{tuple(args)} -> method')

    def fn_changeType(self, *args):
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.changeType{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.remove{tuple(args)} -> method')

    def fn_appendEncodedChunks(self, *args):
        logger.debug(f'patch -> v8_source_buffer.py -> SourceBuffer.appendEncodedChunks{tuple(args)} -> method')
