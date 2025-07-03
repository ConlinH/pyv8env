from .flags import *


@construct_100001
class CropTarget:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("fromElement", "fn_fromElement", 1, 0, 2, 0, 1, 1, 0),

    )

    @classmethod
    def fn_fromElement(cls, *args):
        logger.debug(f'patch -> v8_crop_target.py -> CropTarget.fromElement{tuple(args)} -> method')
