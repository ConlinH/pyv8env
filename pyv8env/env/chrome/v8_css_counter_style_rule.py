from .flags import *
from .v8_css_rule import CSSRule


@construct_100001
class CSSCounterStyleRule(CSSRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSCounterStyleRule, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("system", "get_system", "set_system", 0, 1, 0, 0, 0, 0, 1),
        ("symbols", "get_symbols", "set_symbols", 0, 1, 0, 0, 0, 0, 1),
        ("additiveSymbols", "get_additiveSymbols", "set_additiveSymbols", 0, 1, 0, 0, 0, 0, 1),
        ("negative", "get_negative", "set_negative", 0, 1, 0, 0, 0, 0, 1),
        ("prefix", "get_prefix", "set_prefix", 0, 1, 0, 0, 0, 0, 1),
        ("suffix", "get_suffix", "set_suffix", 0, 1, 0, 0, 0, 0, 1),
        ("range", "get_range", "set_range", 0, 1, 0, 0, 0, 0, 1),
        ("pad", "get_pad", "set_pad", 0, 1, 0, 0, 0, 0, 1),
        ("speakAs", "get_speakAs", "set_speakAs", 0, 1, 0, 0, 0, 0, 1),
        ("fallback", "get_fallback", "set_fallback", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_system(self):
        val = self._attr.get('system')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.system -> get attr')

    def set_system(self, val):
        self._attr['system'] = val

    def get_symbols(self):
        val = self._attr.get('symbols')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.symbols -> get attr')

    def set_symbols(self, val):
        self._attr['symbols'] = val

    def get_additiveSymbols(self):
        val = self._attr.get('additiveSymbols')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.additiveSymbols -> get attr')

    def set_additiveSymbols(self, val):
        self._attr['additiveSymbols'] = val

    def get_negative(self):
        val = self._attr.get('negative')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.negative -> get attr')

    def set_negative(self, val):
        self._attr['negative'] = val

    def get_prefix(self):
        val = self._attr.get('prefix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.prefix -> get attr')

    def set_prefix(self, val):
        self._attr['prefix'] = val

    def get_suffix(self):
        val = self._attr.get('suffix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.suffix -> get attr')

    def set_suffix(self, val):
        self._attr['suffix'] = val

    def get_range(self):
        val = self._attr.get('range')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.range -> get attr')

    def set_range(self, val):
        self._attr['range'] = val

    def get_pad(self):
        val = self._attr.get('pad')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.pad -> get attr')

    def set_pad(self, val):
        self._attr['pad'] = val

    def get_speakAs(self):
        val = self._attr.get('speakAs')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.speakAs -> get attr')

    def set_speakAs(self, val):
        self._attr['speakAs'] = val

    def get_fallback(self):
        val = self._attr.get('fallback')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_counter_style_rule.py -> CSSCounterStyleRule.fallback -> get attr')

    def set_fallback(self, val):
        self._attr['fallback'] = val
