from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLTemplateElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLTemplateElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("content", "get_content", None, 0, 1, 0, 0, 0, 0, 1),
        ("shadowRootMode", "get_shadowRootMode", "set_shadowRootMode", 0, 1, 0, 0, 0, 0, 1),
        ("shadowRootDelegatesFocus", "get_shadowRootDelegatesFocus", "set_shadowRootDelegatesFocus", 0, 1, 0, 0, 0, 0, 1),
        ("shadowRootClonable", "get_shadowRootClonable", "set_shadowRootClonable", 0, 1, 0, 0, 0, 0, 1),
        ("shadowRootSerializable", "get_shadowRootSerializable", "set_shadowRootSerializable", 0, 1, 0, 0, 0, 0, 1),
        ("parseparts", "get_parseparts", "set_parseparts", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_content(self):
        val = self._attr.get('content')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_template_element.py -> HTMLTemplateElement.content -> get attr')

    def get_shadowRootMode(self):
        val = self._attr.get('shadowRootMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_template_element.py -> HTMLTemplateElement.shadowRootMode -> get attr')

    def set_shadowRootMode(self, val):
        self._attr['shadowRootMode'] = val

    def get_shadowRootDelegatesFocus(self):
        val = self._attr.get('shadowRootDelegatesFocus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_template_element.py -> HTMLTemplateElement.shadowRootDelegatesFocus -> get attr')

    def set_shadowRootDelegatesFocus(self, val):
        self._attr['shadowRootDelegatesFocus'] = val

    def get_shadowRootClonable(self):
        val = self._attr.get('shadowRootClonable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_template_element.py -> HTMLTemplateElement.shadowRootClonable -> get attr')

    def set_shadowRootClonable(self, val):
        self._attr['shadowRootClonable'] = val

    def get_shadowRootSerializable(self):
        val = self._attr.get('shadowRootSerializable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_template_element.py -> HTMLTemplateElement.shadowRootSerializable -> get attr')

    def set_shadowRootSerializable(self, val):
        self._attr['shadowRootSerializable'] = val

    def get_parseparts(self):
        val = self._attr.get('parseparts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_template_element.py -> HTMLTemplateElement.parseparts -> get attr')

    def set_parseparts(self, val):
        self._attr['parseparts'] = val
