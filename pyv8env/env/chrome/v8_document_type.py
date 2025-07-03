from .flags import *
from .v8_node import Node


@construct_100001
class DocumentType(Node):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DocumentType, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("publicId", "get_publicId", None, 0, 1, 0, 0, 0, 0, 1),
        ("systemId", "get_systemId", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("after", "fn_after", 0, 0, 1, 0, 0, 0, 0),
        ("before", "fn_before", 0, 0, 1, 0, 0, 0, 0),
        ("remove", "fn_remove", 0, 0, 1, 0, 0, 0, 0),
        ("replaceWith", "fn_replaceWith", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_type.py -> DocumentType.name -> get attr')

    def get_publicId(self):
        val = self._attr.get('publicId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_type.py -> DocumentType.publicId -> get attr')

    def get_systemId(self):
        val = self._attr.get('systemId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_type.py -> DocumentType.systemId -> get attr')

    def fn_after(self, *args):
        logger.debug(f'patch -> v8_document_type.py -> DocumentType.after{tuple(args)} -> method')

    def fn_before(self, *args):
        logger.debug(f'patch -> v8_document_type.py -> DocumentType.before{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_document_type.py -> DocumentType.remove{tuple(args)} -> method')

    def fn_replaceWith(self, *args):
        logger.debug(f'patch -> v8_document_type.py -> DocumentType.replaceWith{tuple(args)} -> method')
