from .flags import *


@construct_100001
class DocumentPartRoot:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("rootContainer", "get_rootContainer", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clone", "fn_clone", 0, 0, 1, 0, 0, 0, 0),
        ("getPartNode", "fn_getPartNode", 1, 0, 1, 0, 0, 0, 0),
        ("getParts", "fn_getParts", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_rootContainer(self):
        val = self._attr.get('rootContainer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_part_root.py -> DocumentPartRoot.rootContainer -> get attr')

    def fn_clone(self, *args):
        logger.debug(f'patch -> v8_document_part_root.py -> DocumentPartRoot.clone{tuple(args)} -> method')

    def fn_getPartNode(self, *args):
        logger.debug(f'patch -> v8_document_part_root.py -> DocumentPartRoot.getPartNode{tuple(args)} -> method')

    def fn_getParts(self, *args):
        logger.debug(f'patch -> v8_document_part_root.py -> DocumentPartRoot.getParts{tuple(args)} -> method')
