from .flags import *


@construct_114001
class TrackDefault:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("byteStreamTrackID", "get_byteStreamTrackID", None, 0, 1, 0, 0, 0, 0, 1),
        ("language", "get_language", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", None, 0, 1, 0, 0, 0, 0, 1),
        ("kinds", "get_kinds", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_track_default.py -> TrackDefault.type -> get attr')

    def get_byteStreamTrackID(self):
        val = self._attr.get('byteStreamTrackID')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_track_default.py -> TrackDefault.byteStreamTrackID -> get attr')

    def get_language(self):
        val = self._attr.get('language')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_track_default.py -> TrackDefault.language -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_track_default.py -> TrackDefault.label -> get attr')

    def get_kinds(self):
        val = self._attr.get('kinds')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_track_default.py -> TrackDefault.kinds -> get attr')
