from .flags import *
from .v8_svg_graphics_element import SVGGraphicsElement


@construct_100001
class SVGAElement(SVGGraphicsElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGAElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("target", "get_target", None, 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),
        ("interestTargetElement", "get_interestTargetElement", "set_interestTargetElement", 0, 1, 0, 0, 0, 0, 1),
        ("interestAction", "get_interestAction", "set_interestAction", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_a_element.py -> SVGAElement.target -> get attr')

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_a_element.py -> SVGAElement.href -> get attr')

    def get_interestTargetElement(self):
        val = self._attr.get('interestTargetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_a_element.py -> SVGAElement.interestTargetElement -> get attr')

    def set_interestTargetElement(self, val):
        self._attr['interestTargetElement'] = val

    def get_interestAction(self):
        val = self._attr.get('interestAction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_a_element.py -> SVGAElement.interestAction -> get attr')

    def set_interestAction(self, val):
        self._attr['interestAction'] = val
