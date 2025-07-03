from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class MediaRecorder(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaRecorder, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("stream", "get_stream", None, 0, 1, 0, 0, 0, 0, 1),
        ("mimeType", "get_mimeType", None, 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("onstart", "get_onstart", "set_onstart", 0, 1, 0, 0, 0, 0, 1),
        ("onstop", "get_onstop", "set_onstop", 0, 1, 0, 0, 0, 0, 1),
        ("ondataavailable", "get_ondataavailable", "set_ondataavailable", 0, 1, 0, 0, 0, 0, 1),
        ("onpause", "get_onpause", "set_onpause", 0, 1, 0, 0, 0, 0, 1),
        ("onresume", "get_onresume", "set_onresume", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("videoBitsPerSecond", "get_videoBitsPerSecond", None, 0, 1, 0, 0, 0, 0, 1),
        ("audioBitsPerSecond", "get_audioBitsPerSecond", None, 0, 1, 0, 0, 0, 0, 1),
        ("audioBitrateMode", "get_audioBitrateMode", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("pause", "fn_pause", 0, 0, 1, 0, 0, 0, 0),
        ("requestData", "fn_requestData", 0, 0, 1, 0, 0, 0, 0),
        ("resume", "fn_resume", 0, 0, 1, 0, 0, 0, 0),
        ("start", "fn_start", 0, 0, 1, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),
        ("isTypeSupported", "fn_isTypeSupported", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_stream(self):
        val = self._attr.get('stream')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.stream -> get attr')

    def get_mimeType(self):
        val = self._attr.get('mimeType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.mimeType -> get attr')

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.state -> get attr')

    def get_onstart(self):
        val = self._attr.get('onstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.onstart -> get attr')

    def set_onstart(self, val):
        self._attr['onstart'] = val

    def get_onstop(self):
        val = self._attr.get('onstop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.onstop -> get attr')

    def set_onstop(self, val):
        self._attr['onstop'] = val

    def get_ondataavailable(self):
        val = self._attr.get('ondataavailable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.ondataavailable -> get attr')

    def set_ondataavailable(self, val):
        self._attr['ondataavailable'] = val

    def get_onpause(self):
        val = self._attr.get('onpause')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.onpause -> get attr')

    def set_onpause(self, val):
        self._attr['onpause'] = val

    def get_onresume(self):
        val = self._attr.get('onresume')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.onresume -> get attr')

    def set_onresume(self, val):
        self._attr['onresume'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_videoBitsPerSecond(self):
        val = self._attr.get('videoBitsPerSecond')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.videoBitsPerSecond -> get attr')

    def get_audioBitsPerSecond(self):
        val = self._attr.get('audioBitsPerSecond')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.audioBitsPerSecond -> get attr')

    def get_audioBitrateMode(self):
        val = self._attr.get('audioBitrateMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.audioBitrateMode -> get attr')

    def fn_pause(self, *args):
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.pause{tuple(args)} -> method')

    def fn_requestData(self, *args):
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.requestData{tuple(args)} -> method')

    def fn_resume(self, *args):
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.resume{tuple(args)} -> method')

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.start{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.stop{tuple(args)} -> method')

    @classmethod
    def fn_isTypeSupported(cls, *args):
        logger.debug(f'patch -> v8_media_recorder.py -> MediaRecorder.isTypeSupported{tuple(args)} -> method')
