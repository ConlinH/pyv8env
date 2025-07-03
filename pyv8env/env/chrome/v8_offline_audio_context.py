from .flags import *
from .v8_base_audio_context import BaseAudioContext


@construct_111001
class OfflineAudioContext(BaseAudioContext):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(OfflineAudioContext, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("oncomplete", "get_oncomplete", "set_oncomplete", 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("resume", "fn_resume", 0, 0, 1, 0, 1, 0, 0),
        ("startRendering", "fn_startRendering", 0, 0, 1, 0, 1, 0, 0),
        ("suspend", "fn_suspend", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_oncomplete(self):
        val = self._attr.get('oncomplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_offline_audio_context.py -> OfflineAudioContext.oncomplete -> get attr')

    def set_oncomplete(self, val):
        self._attr['oncomplete'] = val

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_offline_audio_context.py -> OfflineAudioContext.length -> get attr')

    def fn_resume(self, *args):
        logger.debug(f'patch -> v8_offline_audio_context.py -> OfflineAudioContext.resume{tuple(args)} -> method')

    def fn_startRendering(self, *args):
        logger.debug(f'patch -> v8_offline_audio_context.py -> OfflineAudioContext.startRendering{tuple(args)} -> method')

    def fn_suspend(self, *args):
        logger.debug(f'patch -> v8_offline_audio_context.py -> OfflineAudioContext.suspend{tuple(args)} -> method')
