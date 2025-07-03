from .flags import *


@construct_111001
class Touch:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("identifier", "get_identifier", None, 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", None, 0, 1, 0, 0, 0, 0, 1),
        ("screenX", "get_screenX", None, 0, 1, 0, 0, 0, 0, 1),
        ("screenY", "get_screenY", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientX", "get_clientX", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientY", "get_clientY", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageX", "get_pageX", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageY", "get_pageY", None, 0, 1, 0, 0, 0, 0, 1),
        ("radiusX", "get_radiusX", None, 0, 1, 0, 0, 0, 0, 1),
        ("radiusY", "get_radiusY", None, 0, 1, 0, 0, 0, 0, 1),
        ("rotationAngle", "get_rotationAngle", None, 0, 1, 0, 0, 0, 0, 1),
        ("force", "get_force", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_identifier(self):
        val = self._attr.get('identifier')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.identifier -> get attr')

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.target -> get attr')

    def get_screenX(self):
        val = self._attr.get('screenX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.screenX -> get attr')

    def get_screenY(self):
        val = self._attr.get('screenY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.screenY -> get attr')

    def get_clientX(self):
        val = self._attr.get('clientX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.clientX -> get attr')

    def get_clientY(self):
        val = self._attr.get('clientY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.clientY -> get attr')

    def get_pageX(self):
        val = self._attr.get('pageX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.pageX -> get attr')

    def get_pageY(self):
        val = self._attr.get('pageY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.pageY -> get attr')

    def get_radiusX(self):
        val = self._attr.get('radiusX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.radiusX -> get attr')

    def get_radiusY(self):
        val = self._attr.get('radiusY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.radiusY -> get attr')

    def get_rotationAngle(self):
        val = self._attr.get('rotationAngle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.rotationAngle -> get attr')

    def get_force(self):
        val = self._attr.get('force')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch.py -> Touch.force -> get attr')
