from .flags import *
from .v8_css_condition_rule import CSSConditionRule


@construct_100001
class CSSMediaRule(CSSConditionRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSMediaRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("media", "get_media", "set_media", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_media_rule.py -> CSSMediaRule.media -> get attr')

    def set_media(self, val):
        self._attr['media'] = val
