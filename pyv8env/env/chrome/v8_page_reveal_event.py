from .flags import *
from .v8_event import Event


@construct_100001
class PageRevealEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PageRevealEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),
        ("viewTransition", "get_viewTransition", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_page_reveal_event.py -> PageRevealEvent.isTrusted -> get attr')

    def get_viewTransition(self):
        val = self._attr.get('viewTransition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_page_reveal_event.py -> PageRevealEvent.viewTransition -> get attr')
