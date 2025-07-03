from .flags import *


@construct_110001
class VTTRegion:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", "set_id", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("lines", "get_lines", "set_lines", 0, 1, 0, 0, 0, 0, 1),
        ("regionAnchorX", "get_regionAnchorX", "set_regionAnchorX", 0, 1, 0, 0, 0, 0, 1),
        ("regionAnchorY", "get_regionAnchorY", "set_regionAnchorY", 0, 1, 0, 0, 0, 0, 1),
        ("viewportAnchorX", "get_viewportAnchorX", "set_viewportAnchorX", 0, 1, 0, 0, 0, 0, 1),
        ("viewportAnchorY", "get_viewportAnchorY", "set_viewportAnchorY", 0, 1, 0, 0, 0, 0, 1),
        ("scroll", "get_scroll", "set_scroll", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_region.py -> VTTRegion.id -> get attr')

    def set_id(self, val):
        self._attr['id'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_region.py -> VTTRegion.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_lines(self):
        val = self._attr.get('lines')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_region.py -> VTTRegion.lines -> get attr')

    def set_lines(self, val):
        self._attr['lines'] = val

    def get_regionAnchorX(self):
        val = self._attr.get('regionAnchorX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_region.py -> VTTRegion.regionAnchorX -> get attr')

    def set_regionAnchorX(self, val):
        self._attr['regionAnchorX'] = val

    def get_regionAnchorY(self):
        val = self._attr.get('regionAnchorY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_region.py -> VTTRegion.regionAnchorY -> get attr')

    def set_regionAnchorY(self, val):
        self._attr['regionAnchorY'] = val

    def get_viewportAnchorX(self):
        val = self._attr.get('viewportAnchorX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_region.py -> VTTRegion.viewportAnchorX -> get attr')

    def set_viewportAnchorX(self, val):
        self._attr['viewportAnchorX'] = val

    def get_viewportAnchorY(self):
        val = self._attr.get('viewportAnchorY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_region.py -> VTTRegion.viewportAnchorY -> get attr')

    def set_viewportAnchorY(self, val):
        self._attr['viewportAnchorY'] = val

    def get_scroll(self):
        val = self._attr.get('scroll')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_region.py -> VTTRegion.scroll -> get attr')

    def set_scroll(self, val):
        self._attr['scroll'] = val
