from .flags import *
from .v8_event import Event


@construct_112001
class AudioProcessingEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AudioProcessingEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("playbackTime", "get_playbackTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputBuffer", "get_inputBuffer", None, 0, 1, 0, 0, 0, 0, 1),
        ("outputBuffer", "get_outputBuffer", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_playbackTime(self):
        val = self._attr.get('playbackTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_processing_event.py -> AudioProcessingEvent.playbackTime -> get attr')

    def get_inputBuffer(self):
        val = self._attr.get('inputBuffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_processing_event.py -> AudioProcessingEvent.inputBuffer -> get attr')

    def get_outputBuffer(self):
        val = self._attr.get('outputBuffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_processing_event.py -> AudioProcessingEvent.outputBuffer -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_processing_event.py -> AudioProcessingEvent.isTrusted -> get attr')
