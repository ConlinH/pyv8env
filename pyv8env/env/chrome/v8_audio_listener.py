from .flags import *


@construct_100001
class AudioListener:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("positionX", "get_positionX", None, 0, 1, 0, 0, 0, 0, 1),
        ("positionY", "get_positionY", None, 0, 1, 0, 0, 0, 0, 1),
        ("positionZ", "get_positionZ", None, 0, 1, 0, 0, 0, 0, 1),
        ("forwardX", "get_forwardX", None, 0, 1, 0, 0, 0, 0, 1),
        ("forwardY", "get_forwardY", None, 0, 1, 0, 0, 0, 0, 1),
        ("forwardZ", "get_forwardZ", None, 0, 1, 0, 0, 0, 0, 1),
        ("upX", "get_upX", None, 0, 1, 0, 0, 0, 0, 1),
        ("upY", "get_upY", None, 0, 1, 0, 0, 0, 0, 1),
        ("upZ", "get_upZ", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setOrientation", "fn_setOrientation", 6, 0, 1, 0, 0, 0, 0),
        ("setPosition", "fn_setPosition", 3, 0, 1, 0, 0, 0, 0),

    )

    def get_positionX(self):
        val = self._attr.get('positionX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.positionX -> get attr')

    def get_positionY(self):
        val = self._attr.get('positionY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.positionY -> get attr')

    def get_positionZ(self):
        val = self._attr.get('positionZ')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.positionZ -> get attr')

    def get_forwardX(self):
        val = self._attr.get('forwardX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.forwardX -> get attr')

    def get_forwardY(self):
        val = self._attr.get('forwardY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.forwardY -> get attr')

    def get_forwardZ(self):
        val = self._attr.get('forwardZ')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.forwardZ -> get attr')

    def get_upX(self):
        val = self._attr.get('upX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.upX -> get attr')

    def get_upY(self):
        val = self._attr.get('upY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.upY -> get attr')

    def get_upZ(self):
        val = self._attr.get('upZ')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.upZ -> get attr')

    def fn_setOrientation(self, *args):
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.setOrientation{tuple(args)} -> method')

    def fn_setPosition(self, *args):
        logger.debug(f'patch -> v8_audio_listener.py -> AudioListener.setPosition{tuple(args)} -> method')
