from .flags import *
from .v8_event import Event


@construct_100001
class PageSwapEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PageSwapEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("activation", "get_activation", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),
        ("viewTransition", "get_viewTransition", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_activation(self):
        val = self._attr.get('activation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_page_swap_event.py -> PageSwapEvent.activation -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_page_swap_event.py -> PageSwapEvent.isTrusted -> get attr')

    def get_viewTransition(self):
        val = self._attr.get('viewTransition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_page_swap_event.py -> PageSwapEvent.viewTransition -> get attr')
