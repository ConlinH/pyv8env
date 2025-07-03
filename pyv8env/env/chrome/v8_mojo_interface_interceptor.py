from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class MojoInterfaceInterceptor(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MojoInterfaceInterceptor, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("oninterfacerequest", "get_oninterfacerequest", "set_oninterfacerequest", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("start", "fn_start", 0, 0, 1, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_oninterfacerequest(self):
        val = self._attr.get('oninterfacerequest')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mojo_interface_interceptor.py -> MojoInterfaceInterceptor.oninterfacerequest -> get attr')

    def set_oninterfacerequest(self, val):
        self._attr['oninterfacerequest'] = val

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_mojo_interface_interceptor.py -> MojoInterfaceInterceptor.start{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_mojo_interface_interceptor.py -> MojoInterfaceInterceptor.stop{tuple(args)} -> method')
