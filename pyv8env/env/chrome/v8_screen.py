from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class Screen(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Screen, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("availWidth", "get_availWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("availHeight", "get_availHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("colorDepth", "get_colorDepth", None, 0, 1, 0, 0, 0, 0, 1),
        ("pixelDepth", "get_pixelDepth", None, 0, 1, 0, 0, 0, 0, 1),
        ("availLeft", "get_availLeft", None, 0, 1, 0, 0, 0, 0, 1),
        ("availTop", "get_availTop", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientation", "get_orientation", None, 0, 1, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),
        ("isExtended", "get_isExtended", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_availWidth(self):
        val = self._attr.get('availWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.availWidth -> get attr')

    def get_availHeight(self):
        val = self._attr.get('availHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.availHeight -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.height -> get attr')

    def get_colorDepth(self):
        val = self._attr.get('colorDepth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.colorDepth -> get attr')

    def get_pixelDepth(self):
        val = self._attr.get('pixelDepth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.pixelDepth -> get attr')

    def get_availLeft(self):
        val = self._attr.get('availLeft')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.availLeft -> get attr')

    def get_availTop(self):
        val = self._attr.get('availTop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.availTop -> get attr')

    def get_orientation(self):
        val = self._attr.get('orientation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.orientation -> get attr')

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def get_isExtended(self):
        val = self._attr.get('isExtended')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_screen.py -> Screen.isExtended -> get attr')
