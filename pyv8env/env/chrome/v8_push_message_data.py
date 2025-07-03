from .flags import *


@construct_100001
class PushMessageData:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("arrayBuffer", "fn_arrayBuffer", 0, 0, 1, 0, 0, 0, 0),
        ("blob", "fn_blob", 0, 0, 1, 0, 0, 0, 0),
        ("json", "fn_json", 0, 0, 1, 0, 0, 0, 0),
        ("text", "fn_text", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_arrayBuffer(self, *args):
        logger.debug(f'patch -> v8_push_message_data.py -> PushMessageData.arrayBuffer{tuple(args)} -> method')

    def fn_blob(self, *args):
        logger.debug(f'patch -> v8_push_message_data.py -> PushMessageData.blob{tuple(args)} -> method')

    def fn_json(self, *args):
        logger.debug(f'patch -> v8_push_message_data.py -> PushMessageData.json{tuple(args)} -> method')

    def fn_text(self, *args):
        logger.debug(f'patch -> v8_push_message_data.py -> PushMessageData.text{tuple(args)} -> method')
