from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class NetworkInformation(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(NetworkInformation, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),
        ("effectiveType", "get_effectiveType", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtt", "get_rtt", None, 0, 1, 0, 0, 0, 0, 1),
        ("downlink", "get_downlink", None, 0, 1, 0, 0, 0, 0, 1),
        ("saveData", "get_saveData", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("downlinkMax", "get_downlinkMax", None, 0, 1, 0, 0, 0, 0, 1),
        ("ontypechange", "get_ontypechange", "set_ontypechange", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_network_information.py -> NetworkInformation.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def get_effectiveType(self):
        val = self._attr.get('effectiveType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_network_information.py -> NetworkInformation.effectiveType -> get attr')

    def get_rtt(self):
        val = self._attr.get('rtt')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_network_information.py -> NetworkInformation.rtt -> get attr')

    def get_downlink(self):
        val = self._attr.get('downlink')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_network_information.py -> NetworkInformation.downlink -> get attr')

    def get_saveData(self):
        val = self._attr.get('saveData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_network_information.py -> NetworkInformation.saveData -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_network_information.py -> NetworkInformation.type -> get attr')

    def get_downlinkMax(self):
        val = self._attr.get('downlinkMax')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_network_information.py -> NetworkInformation.downlinkMax -> get attr')

    def get_ontypechange(self):
        val = self._attr.get('ontypechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_network_information.py -> NetworkInformation.ontypechange -> get attr')

    def set_ontypechange(self, val):
        self._attr['ontypechange'] = val
