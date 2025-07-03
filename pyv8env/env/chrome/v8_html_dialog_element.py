from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLDialogElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLDialogElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("open", "get_open", "set_open", 0, 1, 0, 0, 0, 0, 1),
        ("returnValue", "get_returnValue", "set_returnValue", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("show", "fn_show", 0, 0, 1, 0, 0, 0, 0),
        ("showModal", "fn_showModal", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_open(self):
        val = self._attr.get('open')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_dialog_element.py -> HTMLDialogElement.open -> get attr')

    def set_open(self, val):
        self._attr['open'] = val

    def get_returnValue(self):
        val = self._attr.get('returnValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_dialog_element.py -> HTMLDialogElement.returnValue -> get attr')

    def set_returnValue(self, val):
        self._attr['returnValue'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_html_dialog_element.py -> HTMLDialogElement.close{tuple(args)} -> method')

    def fn_show(self, *args):
        logger.debug(f'patch -> v8_html_dialog_element.py -> HTMLDialogElement.show{tuple(args)} -> method')

    def fn_showModal(self, *args):
        logger.debug(f'patch -> v8_html_dialog_element.py -> HTMLDialogElement.showModal{tuple(args)} -> method')
