from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLOptGroupElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLOptGroupElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_opt_group_element.py -> HTMLOptGroupElement.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_opt_group_element.py -> HTMLOptGroupElement.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val
