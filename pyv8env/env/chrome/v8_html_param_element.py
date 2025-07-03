from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLParamElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLParamElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("valueType", "get_valueType", "set_valueType", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_param_element.py -> HTMLParamElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_param_element.py -> HTMLParamElement.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_param_element.py -> HTMLParamElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_valueType(self):
        val = self._attr.get('valueType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_param_element.py -> HTMLParamElement.valueType -> get attr')

    def set_valueType(self, val):
        self._attr['valueType'] = val
