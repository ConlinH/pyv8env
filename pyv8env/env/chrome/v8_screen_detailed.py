from .flags import *
from .v8_screen import Screen


@construct_100001
class ScreenDetailed(Screen):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ScreenDetailed, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("left", "get_left", None, 0, 1, 0, 0, 0, 0, 1),
        ("top", "get_top", None, 0, 1, 0, 0, 0, 0, 1),
        ("isPrimary", "get_isPrimary", None, 0, 1, 0, 0, 0, 0, 1),
        ("isInternal", "get_isInternal", None, 0, 1, 0, 0, 0, 0, 1),
        ("devicePixelRatio", "get_devicePixelRatio", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", None, 0, 1, 0, 0, 0, 0, 1),
        ("highDynamicRangeHeadroom", "get_highDynamicRangeHeadroom", None, 0, 1, 0, 0, 0, 0, 1),
        ("redPrimaryX", "get_redPrimaryX", None, 0, 1, 0, 0, 0, 0, 1),
        ("redPrimaryY", "get_redPrimaryY", None, 0, 1, 0, 0, 0, 0, 1),
        ("greenPrimaryX", "get_greenPrimaryX", None, 0, 1, 0, 0, 0, 0, 1),
        ("greenPrimaryY", "get_greenPrimaryY", None, 0, 1, 0, 0, 0, 0, 1),
        ("bluePrimaryX", "get_bluePrimaryX", None, 0, 1, 0, 0, 0, 0, 1),
        ("bluePrimaryY", "get_bluePrimaryY", None, 0, 1, 0, 0, 0, 0, 1),
        ("whitePointX", "get_whitePointX", None, 0, 1, 0, 0, 0, 0, 1),
        ("whitePointY", "get_whitePointY", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_left(self):
        val = self._attr.get('left')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.left -> get attr')

    def get_top(self):
        val = self._attr.get('top')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.top -> get attr')

    def get_isPrimary(self):
        val = self._attr.get('isPrimary')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.isPrimary -> get attr')

    def get_isInternal(self):
        val = self._attr.get('isInternal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.isInternal -> get attr')

    def get_devicePixelRatio(self):
        val = self._attr.get('devicePixelRatio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.devicePixelRatio -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.label -> get attr')

    def get_highDynamicRangeHeadroom(self):
        val = self._attr.get('highDynamicRangeHeadroom')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.highDynamicRangeHeadroom -> get attr')

    def get_redPrimaryX(self):
        val = self._attr.get('redPrimaryX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.redPrimaryX -> get attr')

    def get_redPrimaryY(self):
        val = self._attr.get('redPrimaryY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.redPrimaryY -> get attr')

    def get_greenPrimaryX(self):
        val = self._attr.get('greenPrimaryX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.greenPrimaryX -> get attr')

    def get_greenPrimaryY(self):
        val = self._attr.get('greenPrimaryY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.greenPrimaryY -> get attr')

    def get_bluePrimaryX(self):
        val = self._attr.get('bluePrimaryX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.bluePrimaryX -> get attr')

    def get_bluePrimaryY(self):
        val = self._attr.get('bluePrimaryY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.bluePrimaryY -> get attr')

    def get_whitePointX(self):
        val = self._attr.get('whitePointX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.whitePointX -> get attr')

    def get_whitePointY(self):
        val = self._attr.get('whitePointY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen_detailed.py -> ScreenDetailed.whitePointY -> get attr')
