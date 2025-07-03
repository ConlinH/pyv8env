from .flags import *


@construct_112001
class FontFace:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("family", "get_family", "set_family", 0, 1, 0, 0, 0, 0, 1),
        ("style", "get_style", "set_style", 0, 1, 0, 0, 0, 0, 1),
        ("weight", "get_weight", "set_weight", 0, 1, 0, 0, 0, 0, 1),
        ("stretch", "get_stretch", "set_stretch", 0, 1, 0, 0, 0, 0, 1),
        ("unicodeRange", "get_unicodeRange", "set_unicodeRange", 0, 1, 0, 0, 0, 0, 1),
        ("variant", "get_variant", "set_variant", 0, 1, 0, 0, 0, 0, 1),
        ("featureSettings", "get_featureSettings", "set_featureSettings", 0, 1, 0, 0, 0, 0, 1),
        ("display", "get_display", "set_display", 0, 1, 0, 0, 0, 0, 1),
        ("ascentOverride", "get_ascentOverride", "set_ascentOverride", 0, 1, 0, 0, 0, 0, 1),
        ("descentOverride", "get_descentOverride", "set_descentOverride", 0, 1, 0, 0, 0, 0, 1),
        ("lineGapOverride", "get_lineGapOverride", "set_lineGapOverride", 0, 1, 0, 0, 0, 0, 1),
        ("sizeAdjust", "get_sizeAdjust", "set_sizeAdjust", 0, 1, 0, 0, 0, 0, 1),
        ("status", "get_status", None, 0, 1, 0, 0, 0, 0, 1),
        ("loaded", "get_loaded", None, 0, 1, 0, 1, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("load", "fn_load", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_family(self):
        val = self._attr.get('family')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.family -> get attr')

    def set_family(self, val):
        self._attr['family'] = val

    def get_style(self):
        val = self._attr.get('style')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.style -> get attr')

    def set_style(self, val):
        self._attr['style'] = val

    def get_weight(self):
        val = self._attr.get('weight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.weight -> get attr')

    def set_weight(self, val):
        self._attr['weight'] = val

    def get_stretch(self):
        val = self._attr.get('stretch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.stretch -> get attr')

    def set_stretch(self, val):
        self._attr['stretch'] = val

    def get_unicodeRange(self):
        val = self._attr.get('unicodeRange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.unicodeRange -> get attr')

    def set_unicodeRange(self, val):
        self._attr['unicodeRange'] = val

    def get_variant(self):
        val = self._attr.get('variant')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.variant -> get attr')

    def set_variant(self, val):
        self._attr['variant'] = val

    def get_featureSettings(self):
        val = self._attr.get('featureSettings')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.featureSettings -> get attr')

    def set_featureSettings(self, val):
        self._attr['featureSettings'] = val

    def get_display(self):
        val = self._attr.get('display')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.display -> get attr')

    def set_display(self, val):
        self._attr['display'] = val

    def get_ascentOverride(self):
        val = self._attr.get('ascentOverride')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.ascentOverride -> get attr')

    def set_ascentOverride(self, val):
        self._attr['ascentOverride'] = val

    def get_descentOverride(self):
        val = self._attr.get('descentOverride')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.descentOverride -> get attr')

    def set_descentOverride(self, val):
        self._attr['descentOverride'] = val

    def get_lineGapOverride(self):
        val = self._attr.get('lineGapOverride')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.lineGapOverride -> get attr')

    def set_lineGapOverride(self, val):
        self._attr['lineGapOverride'] = val

    def get_sizeAdjust(self):
        val = self._attr.get('sizeAdjust')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.sizeAdjust -> get attr')

    def set_sizeAdjust(self, val):
        self._attr['sizeAdjust'] = val

    def get_status(self):
        val = self._attr.get('status')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.status -> get attr')

    def get_loaded(self):
        val = self._attr.get('loaded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face.py -> FontFace.loaded -> get attr')

    def fn_load(self, *args):
        logger.debug(f'patch -> v8_font_face.py -> FontFace.load{tuple(args)} -> method')
