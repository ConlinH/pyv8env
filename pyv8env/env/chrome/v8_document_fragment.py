from .flags import *
from .v8_node import Node


@construct_110001
class DocumentFragment(Node):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DocumentFragment, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("children", "get_children", None, 0, 1, 0, 0, 0, 0, 1),
        ("firstElementChild", "get_firstElementChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastElementChild", "get_lastElementChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("childElementCount", "get_childElementCount", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("append", "fn_append", 0, 0, 1, 0, 0, 0, 0),
        ("getElementById", "fn_getElementById", 1, 0, 1, 0, 0, 0, 0),
        ("prepend", "fn_prepend", 0, 0, 1, 0, 0, 0, 0),
        ("querySelector", "fn_querySelector", 1, 0, 1, 0, 0, 0, 1),
        ("querySelectorAll", "fn_querySelectorAll", 1, 0, 1, 0, 0, 0, 1),
        ("replaceChildren", "fn_replaceChildren", 0, 0, 1, 0, 0, 0, 0),
        ("getPartRoot", "fn_getPartRoot", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_children(self):
        val = self._attr.get('children')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.children -> get attr')

    def get_firstElementChild(self):
        val = self._attr.get('firstElementChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.firstElementChild -> get attr')

    def get_lastElementChild(self):
        val = self._attr.get('lastElementChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.lastElementChild -> get attr')

    def get_childElementCount(self):
        val = self._attr.get('childElementCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.childElementCount -> get attr')

    def fn_append(self, *args):
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.append{tuple(args)} -> method')

    def fn_getElementById(self, *args):
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.getElementById{tuple(args)} -> method')

    def fn_prepend(self, *args):
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.prepend{tuple(args)} -> method')

    def fn_querySelector(self, *args):
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.querySelector{tuple(args)} -> method')

    def fn_querySelectorAll(self, *args):
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.querySelectorAll{tuple(args)} -> method')

    def fn_replaceChildren(self, *args):
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.replaceChildren{tuple(args)} -> method')

    def fn_getPartRoot(self, *args):
        logger.debug(f'patch -> v8_document_fragment.py -> DocumentFragment.getPartRoot{tuple(args)} -> method')
