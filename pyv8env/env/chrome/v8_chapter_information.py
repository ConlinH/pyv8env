from .flags import *


@construct_100001
class ChapterInformation:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("title", "get_title", None, 0, 1, 0, 0, 0, 0, 1),
        ("startTime", "get_startTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("artwork", "get_artwork", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_title(self):
        val = self._attr.get('title')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_chapter_information.py -> ChapterInformation.title -> get attr')

    def get_startTime(self):
        val = self._attr.get('startTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_chapter_information.py -> ChapterInformation.startTime -> get attr')

    def get_artwork(self):
        val = self._attr.get('artwork')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_chapter_information.py -> ChapterInformation.artwork -> get attr')
