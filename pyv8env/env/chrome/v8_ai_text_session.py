from .flags import *


@construct_100001
class AITextSession:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("destroy", "fn_destroy", 0, 0, 1, 0, 0, 0, 0),
        ("execute", "fn_execute", 1, 0, 1, 0, 1, 0, 0),
        ("executeStreaming", "fn_executeStreaming", 1, 0, 1, 0, 1, 0, 0),
        ("prompt", "fn_prompt", 1, 0, 1, 0, 1, 0, 0),
        ("promptStreaming", "fn_promptStreaming", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_destroy(self, *args):
        logger.debug(f'patch -> v8_ai_text_session.py -> AITextSession.destroy{tuple(args)} -> method')

    def fn_execute(self, *args):
        logger.debug(f'patch -> v8_ai_text_session.py -> AITextSession.execute{tuple(args)} -> method')

    def fn_executeStreaming(self, *args):
        logger.debug(f'patch -> v8_ai_text_session.py -> AITextSession.executeStreaming{tuple(args)} -> method')

    def fn_prompt(self, *args):
        logger.debug(f'patch -> v8_ai_text_session.py -> AITextSession.prompt{tuple(args)} -> method')

    def fn_promptStreaming(self, *args):
        logger.debug(f'patch -> v8_ai_text_session.py -> AITextSession.promptStreaming{tuple(args)} -> method')
