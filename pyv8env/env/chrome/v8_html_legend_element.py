from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLLegendElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLLegendElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_legend_element.py -> HTMLLegendElement.form -> get attr')

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_legend_element.py -> HTMLLegendElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val
