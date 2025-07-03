from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLMeterElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLMeterElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("min", "get_min", "set_min", 0, 1, 0, 0, 0, 0, 1),
        ("max", "get_max", "set_max", 0, 1, 0, 0, 0, 0, 1),
        ("low", "get_low", "set_low", 0, 1, 0, 0, 0, 0, 1),
        ("high", "get_high", "set_high", 0, 1, 0, 0, 0, 0, 1),
        ("optimum", "get_optimum", "set_optimum", 0, 1, 0, 0, 0, 0, 1),
        ("labels", "get_labels", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meter_element.py -> HTMLMeterElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_min(self):
        val = self._attr.get('min')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meter_element.py -> HTMLMeterElement.min -> get attr')

    def set_min(self, val):
        self._attr['min'] = val

    def get_max(self):
        val = self._attr.get('max')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meter_element.py -> HTMLMeterElement.max -> get attr')

    def set_max(self, val):
        self._attr['max'] = val

    def get_low(self):
        val = self._attr.get('low')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meter_element.py -> HTMLMeterElement.low -> get attr')

    def set_low(self, val):
        self._attr['low'] = val

    def get_high(self):
        val = self._attr.get('high')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meter_element.py -> HTMLMeterElement.high -> get attr')

    def set_high(self, val):
        self._attr['high'] = val

    def get_optimum(self):
        val = self._attr.get('optimum')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meter_element.py -> HTMLMeterElement.optimum -> get attr')

    def set_optimum(self, val):
        self._attr['optimum'] = val

    def get_labels(self):
        val = self._attr.get('labels')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_meter_element.py -> HTMLMeterElement.labels -> get attr')
