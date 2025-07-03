from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLMapElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLMapElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("areas", "get_areas", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_map_element.py -> HTMLMapElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_areas(self):
        val = self._attr.get('areas')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_map_element.py -> HTMLMapElement.areas -> get attr')
