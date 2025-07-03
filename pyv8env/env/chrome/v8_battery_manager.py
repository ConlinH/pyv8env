from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class BatteryManager(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BatteryManager, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("charging", "get_charging", None, 0, 1, 0, 0, 0, 0, 1),
        ("chargingTime", "get_chargingTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("dischargingTime", "get_dischargingTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("level", "get_level", None, 0, 1, 0, 0, 0, 0, 1),
        ("onchargingchange", "get_onchargingchange", "set_onchargingchange", 0, 1, 0, 0, 0, 0, 1),
        ("onchargingtimechange", "get_onchargingtimechange", "set_onchargingtimechange", 0, 1, 0, 0, 0, 0, 1),
        ("ondischargingtimechange", "get_ondischargingtimechange", "set_ondischargingtimechange", 0, 1, 0, 0, 0, 0, 1),
        ("onlevelchange", "get_onlevelchange", "set_onlevelchange", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_charging(self):
        val = self._attr.get('charging')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_battery_manager.py -> BatteryManager.charging -> get attr')

    def get_chargingTime(self):
        val = self._attr.get('chargingTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_battery_manager.py -> BatteryManager.chargingTime -> get attr')

    def get_dischargingTime(self):
        val = self._attr.get('dischargingTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_battery_manager.py -> BatteryManager.dischargingTime -> get attr')

    def get_level(self):
        val = self._attr.get('level')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_battery_manager.py -> BatteryManager.level -> get attr')

    def get_onchargingchange(self):
        val = self._attr.get('onchargingchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_battery_manager.py -> BatteryManager.onchargingchange -> get attr')

    def set_onchargingchange(self, val):
        self._attr['onchargingchange'] = val

    def get_onchargingtimechange(self):
        val = self._attr.get('onchargingtimechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_battery_manager.py -> BatteryManager.onchargingtimechange -> get attr')

    def set_onchargingtimechange(self, val):
        self._attr['onchargingtimechange'] = val

    def get_ondischargingtimechange(self):
        val = self._attr.get('ondischargingtimechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_battery_manager.py -> BatteryManager.ondischargingtimechange -> get attr')

    def set_ondischargingtimechange(self, val):
        self._attr['ondischargingtimechange'] = val

    def get_onlevelchange(self):
        val = self._attr.get('onlevelchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_battery_manager.py -> BatteryManager.onlevelchange -> get attr')

    def set_onlevelchange(self, val):
        self._attr['onlevelchange'] = val
