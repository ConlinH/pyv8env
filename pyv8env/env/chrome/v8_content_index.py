from .flags import *


@construct_100001
class ContentIndex:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 1, 0, 1, 0, 1, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 1, 0, 0),
        ("getAll", "fn_getAll", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_content_index.py -> ContentIndex.add{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_content_index.py -> ContentIndex.delete{tuple(args)} -> method')

    def fn_getAll(self, *args):
        logger.debug(f'patch -> v8_content_index.py -> ContentIndex.getAll{tuple(args)} -> method')
