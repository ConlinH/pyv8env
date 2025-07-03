from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLModElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLModElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("cite", "get_cite", "set_cite", 0, 1, 0, 0, 0, 0, 1),
        ("dateTime", "get_dateTime", "set_dateTime", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_cite(self):
        val = self._attr.get('cite')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_mod_element.py -> HTMLModElement.cite -> get attr')

    def set_cite(self, val):
        self._attr['cite'] = val

    def get_dateTime(self):
        val = self._attr.get('dateTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_mod_element.py -> HTMLModElement.dateTime -> get attr')

    def set_dateTime(self, val):
        self._attr['dateTime'] = val
