from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTrackElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTrackElement, self).__init__(*args, **kw)
    NONE = 0
    LOADING = 1
    LOADED = 2
    ERROR = 3

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("kind", "get_kind", "set_kind", 0, 1, 0, 0, 0, 0, 1),
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("srclang", "get_srclang", "set_srclang", 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),
        ("default", "get_default", "set_default", 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("track", "get_track", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_kind(self):
        val = self._attr.get('kind')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_track_element.py -> HTMLTrackElement.kind -> get attr')

    def set_kind(self, val):
        self._attr['kind'] = val

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_track_element.py -> HTMLTrackElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_srclang(self):
        val = self._attr.get('srclang')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_track_element.py -> HTMLTrackElement.srclang -> get attr')

    def set_srclang(self, val):
        self._attr['srclang'] = val

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_track_element.py -> HTMLTrackElement.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def get_default(self):
        val = self._attr.get('default')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_track_element.py -> HTMLTrackElement.default -> get attr')

    def set_default(self, val):
        self._attr['default'] = val

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_track_element.py -> HTMLTrackElement.readyState -> get attr')

    def get_track(self):
        val = self._attr.get('track')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_track_element.py -> HTMLTrackElement.track -> get attr')
