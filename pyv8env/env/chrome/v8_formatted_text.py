from .flags import *


@construct_100001
class FormattedText:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("format", "fn_format", 1, 0, 2, 0, 1, 1, 0),

    )

    @classmethod
    def fn_format(cls, *args):
        logger.debug(f'patch -> v8_formatted_text.py -> FormattedText.format{tuple(args)} -> method')
