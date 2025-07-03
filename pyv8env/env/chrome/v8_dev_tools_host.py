from .flags import *


@construct_000000
class DevToolsHost:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("copyText", "fn_copyText", 1, 0, 1, 0, 0, 0, 0),
        ("isHostedMode", "fn_isHostedMode", 0, 0, 1, 0, 0, 0, 0),
        ("platform", "fn_platform", 0, 0, 1, 0, 0, 0, 0),
        ("sendMessageToEmbedder", "fn_sendMessageToEmbedder", 1, 0, 1, 0, 0, 0, 0),
        ("showContextMenuAtPoint", "fn_showContextMenuAtPoint", 3, 0, 1, 0, 0, 0, 0),
        ("zoomFactor", "fn_zoomFactor", 0, 0, 1, 0, 0, 0, 0),
        ("isolatedFileSystem", "fn_isolatedFileSystem", 2, 0, 1, 0, 0, 0, 0),
        ("upgradeDraggedFileSystemPermissions", "fn_upgradeDraggedFileSystemPermissions", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_copyText(self, *args):
        logger.debug(f'patch -> v8_dev_tools_host.py -> DevToolsHost.copyText{tuple(args)} -> method')

    def fn_isHostedMode(self, *args):
        logger.debug(f'patch -> v8_dev_tools_host.py -> DevToolsHost.isHostedMode{tuple(args)} -> method')

    def fn_platform(self, *args):
        logger.debug(f'patch -> v8_dev_tools_host.py -> DevToolsHost.platform{tuple(args)} -> method')

    def fn_sendMessageToEmbedder(self, *args):
        logger.debug(f'patch -> v8_dev_tools_host.py -> DevToolsHost.sendMessageToEmbedder{tuple(args)} -> method')

    def fn_showContextMenuAtPoint(self, *args):
        logger.debug(f'patch -> v8_dev_tools_host.py -> DevToolsHost.showContextMenuAtPoint{tuple(args)} -> method')

    def fn_zoomFactor(self, *args):
        logger.debug(f'patch -> v8_dev_tools_host.py -> DevToolsHost.zoomFactor{tuple(args)} -> method')

    def fn_isolatedFileSystem(self, *args):
        logger.debug(f'patch -> v8_dev_tools_host.py -> DevToolsHost.isolatedFileSystem{tuple(args)} -> method')

    def fn_upgradeDraggedFileSystemPermissions(self, *args):
        logger.debug(f'patch -> v8_dev_tools_host.py -> DevToolsHost.upgradeDraggedFileSystemPermissions{tuple(args)} -> method')
