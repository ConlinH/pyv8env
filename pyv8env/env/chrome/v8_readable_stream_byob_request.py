from .flags import *


@construct_100001
class ReadableStreamBYOBRequest:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("view", "get_view", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("respond", "fn_respond", 1, 0, 1, 0, 0, 0, 0),
        ("respondWithNewView", "fn_respondWithNewView", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_view(self):
        val = self._attr.get('view')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_readable_stream_byob_request.py -> ReadableStreamBYOBRequest.view -> get attr')

    def fn_respond(self, *args):
        logger.debug(f'patch -> v8_readable_stream_byob_request.py -> ReadableStreamBYOBRequest.respond{tuple(args)} -> method')

    def fn_respondWithNewView(self, *args):
        logger.debug(f'patch -> v8_readable_stream_byob_request.py -> ReadableStreamBYOBRequest.respondWithNewView{tuple(args)} -> method')
