from .flags import *


@construct_111001
class VideoFrame:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("format", "get_format", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestamp", "get_timestamp", None, 0, 1, 0, 0, 0, 0, 1),
        ("duration", "get_duration", None, 0, 1, 0, 0, 0, 0, 1),
        ("codedWidth", "get_codedWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("codedHeight", "get_codedHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("codedRect", "get_codedRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("visibleRect", "get_visibleRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("displayWidth", "get_displayWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("displayHeight", "get_displayHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("colorSpace", "get_colorSpace", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("allocationSize", "fn_allocationSize", 0, 0, 1, 0, 0, 0, 0),
        ("clone", "fn_clone", 0, 0, 1, 0, 0, 0, 0),
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("copyTo", "fn_copyTo", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_format(self):
        val = self._attr.get('format')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.format -> get attr')

    def get_timestamp(self):
        val = self._attr.get('timestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.timestamp -> get attr')

    def get_duration(self):
        val = self._attr.get('duration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.duration -> get attr')

    def get_codedWidth(self):
        val = self._attr.get('codedWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.codedWidth -> get attr')

    def get_codedHeight(self):
        val = self._attr.get('codedHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.codedHeight -> get attr')

    def get_codedRect(self):
        val = self._attr.get('codedRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.codedRect -> get attr')

    def get_visibleRect(self):
        val = self._attr.get('visibleRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.visibleRect -> get attr')

    def get_displayWidth(self):
        val = self._attr.get('displayWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.displayWidth -> get attr')

    def get_displayHeight(self):
        val = self._attr.get('displayHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.displayHeight -> get attr')

    def get_colorSpace(self):
        val = self._attr.get('colorSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.colorSpace -> get attr')

    def fn_allocationSize(self, *args):
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.allocationSize{tuple(args)} -> method')

    def fn_clone(self, *args):
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.clone{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.close{tuple(args)} -> method')

    def fn_copyTo(self, *args):
        logger.debug(f'patch -> v8_video_frame.py -> VideoFrame.copyTo{tuple(args)} -> method')
