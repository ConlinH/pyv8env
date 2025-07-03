from .flags import *


@construct_000000
class AsyncIterator_SharedStorage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("next", "fn_next", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_next(self, *args):
        logger.debug(f'patch -> v8_async_iterator_shared_storage.py -> AsyncIterator_SharedStorage.next{tuple(args)} -> method')
