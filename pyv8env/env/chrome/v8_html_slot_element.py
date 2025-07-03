from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLSlotElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLSlotElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("assign", "fn_assign", 0, 0, 1, 0, 0, 0, 0),
        ("assignedElements", "fn_assignedElements", 0, 0, 1, 0, 0, 0, 0),
        ("assignedNodes", "fn_assignedNodes", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_slot_element.py -> HTMLSlotElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def fn_assign(self, *args):
        logger.debug(f'patch -> v8_html_slot_element.py -> HTMLSlotElement.assign{tuple(args)} -> method')

    def fn_assignedElements(self, *args):
        logger.debug(f'patch -> v8_html_slot_element.py -> HTMLSlotElement.assignedElements{tuple(args)} -> method')

    def fn_assignedNodes(self, *args):
        logger.debug(f'patch -> v8_html_slot_element.py -> HTMLSlotElement.assignedNodes{tuple(args)} -> method')
