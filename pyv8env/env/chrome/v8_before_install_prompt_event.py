from .flags import *
from .v8_event import Event


@construct_111001
class BeforeInstallPromptEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BeforeInstallPromptEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("platforms", "get_platforms", None, 0, 1, 0, 0, 0, 0, 1),
        ("userChoice", "get_userChoice", None, 0, 1, 0, 1, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("prompt", "fn_prompt", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_platforms(self):
        val = self._attr.get('platforms')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_before_install_prompt_event.py -> BeforeInstallPromptEvent.platforms -> get attr')

    def get_userChoice(self):
        val = self._attr.get('userChoice')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_before_install_prompt_event.py -> BeforeInstallPromptEvent.userChoice -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_before_install_prompt_event.py -> BeforeInstallPromptEvent.isTrusted -> get attr')

    def fn_prompt(self, *args):
        logger.debug(f'patch -> v8_before_install_prompt_event.py -> BeforeInstallPromptEvent.prompt{tuple(args)} -> method')
