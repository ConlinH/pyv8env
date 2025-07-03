from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLPermissionElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLPermissionElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("onresolve", "get_onresolve", "set_onresolve", 0, 1, 0, 0, 0, 0, 1),
        ("ondismiss", "get_ondismiss", "set_ondismiss", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_permission_element.py -> HTMLPermissionElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_onresolve(self):
        val = self._attr.get('onresolve')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_permission_element.py -> HTMLPermissionElement.onresolve -> get attr')

    def set_onresolve(self, val):
        self._attr['onresolve'] = val

    def get_ondismiss(self):
        val = self._attr.get('ondismiss')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_permission_element.py -> HTMLPermissionElement.ondismiss -> get attr')

    def set_ondismiss(self, val):
        self._attr['ondismiss'] = val
