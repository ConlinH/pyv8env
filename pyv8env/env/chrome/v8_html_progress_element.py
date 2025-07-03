from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLProgressElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLProgressElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("max", "get_max", "set_max", 0, 1, 0, 0, 0, 0, 1),
        ("position", "get_position", None, 0, 1, 0, 0, 0, 0, 1),
        ("labels", "get_labels", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_progress_element.py -> HTMLProgressElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_max(self):
        val = self._attr.get('max')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_progress_element.py -> HTMLProgressElement.max -> get attr')

    def set_max(self, val):
        self._attr['max'] = val

    def get_position(self):
        val = self._attr.get('position')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_progress_element.py -> HTMLProgressElement.position -> get attr')

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_progress_element.py -> HTMLProgressElement.labels -> get attr')
