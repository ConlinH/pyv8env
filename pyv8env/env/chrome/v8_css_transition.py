from .flags import *
from .v8_animation import Animation


@construct_100001
class CSSTransition(Animation):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSTransition, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("transitionProperty", "get_transitionProperty", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_transitionProperty(self):
        val = self._attr.get('transitionProperty')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_transition.py -> CSSTransition.transitionProperty -> get attr')
