from .flags import *


@construct_100001
class ImageTrack:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("frameCount", "get_frameCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("animated", "get_animated", None, 0, 1, 0, 0, 0, 0, 1),
        ("repetitionCount", "get_repetitionCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("selected", "get_selected", "set_selected", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_frameCount(self):
        val = self._attr.get('frameCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_track.py -> ImageTrack.frameCount -> get attr')

    def get_animated(self):
        val = self._attr.get('animated')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_track.py -> ImageTrack.animated -> get attr')

    def get_repetitionCount(self):
        val = self._attr.get('repetitionCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_track.py -> ImageTrack.repetitionCount -> get attr')

    def get_selected(self):
        val = self._attr.get('selected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_track.py -> ImageTrack.selected -> get attr')

    def set_selected(self, val):
        self._attr['selected'] = val
