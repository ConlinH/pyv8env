
from pyv8env.env.chrome.flags import *


@attr_warp(__v8_constructor_behavior__=False)
def getDetails(*args):
    logger.debug(f'patch -> chrome.py -> chrome.app.getDetails{tuple(args)} -> method')


@attr_warp(__v8_constructor_behavior__=False)
def getIsInstalled(*args):
    logger.debug(f'patch -> chrome.py -> chrome.app.getIsInstalled{tuple(args)} -> method')


@attr_warp(__v8_constructor_behavior__=False)
def installState(*args):
    logger.debug(f'patch -> chrome.py -> chrome.app.installState{tuple(args)} -> method')


@attr_warp(__v8_constructor_behavior__=False)
def runningState(*args):
    logger.debug(f'patch -> chrome.py -> chrome.app.runningState{tuple(args)} -> method')


@attr_warp(__v8_name__='')
def csi(*args):
    logger.debug(f'patch -> chrome.py -> chrome.csi{tuple(args)} -> method')


@attr_warp(__v8_name__='')
def loadTimes(*args):
    logger.debug(f'patch -> chrome.py -> chrome.loadTimes{tuple(args)} -> method')


chrome = {
    'loadTimes': loadTimes,
    'csi': csi,
    'app': {
        "isInstalled": False,
        "getDetails": getDetails,
        "getIsInstalled": getIsInstalled,
        "installState": installState,
        "runningState": runningState,
        "InstallState": {
            "DISABLED": "disabled",
            "INSTALLED": "installed",
            "NOT_INSTALLED": "not_installed"
        },
        "RunningState": {
            "CANNOT_RUN": "cannot_run",
            "READY_TO_RUN": "ready_to_run",
            "RUNNING": "running"
        },
    },
}


exposed_constructs['chrome'] = chrome


@attr_warp(__v8_name__='Option')
def Option(*args):
    logger.debug(f'patch -> window.Option{tuple(args)} -> method')


@attr_warp(__v8_name__='webkitURL')
def webkitURL(*args):
    logger.debug(f'patch -> window.webkitURL{tuple(args)} -> method')


@attr_warp(__v8_name__='webkitMediaStream')
def webkitMediaStream(*args):
    logger.debug(f'patch -> window.webkitMediaStream{tuple(args)} -> method')


@attr_warp(__v8_name__='WebKitMutationObserver')
def WebKitMutationObserver(*args):
    logger.debug(f'patch -> window.WebKitMutationObserver{tuple(args)} -> method')


@attr_warp(__v8_name__='WebKitCSSMatrix')
def WebKitCSSMatrix(*args):
    logger.debug(f'patch -> window.WebKitCSSMatrix{tuple(args)} -> method')


@attr_warp(__v8_constructor_behavior__=False)
def CSSNestedDeclarations(*args):
    logger.debug(f'patch -> window.CSSNestedDeclarations{tuple(args)} -> method')


@attr_warp(__v8_constructor_behavior__=False)
def when(*args):
    logger.debug(f'patch -> window.when{tuple(args)} -> method')


@attr_warp()
def Image(*args):
    logger.debug(f'patch -> window.Image{tuple(args)} -> method')


@attr_warp()
def Audio(*args):
    logger.debug(f'patch -> window.Audio{tuple(args)} -> method')


exposed_constructs['Option'] = Option
exposed_constructs['webkitURL'] = webkitURL
exposed_constructs['webkitMediaStream'] = webkitMediaStream
exposed_constructs['WebKitMutationObserver'] = WebKitMutationObserver
exposed_constructs['CSSNestedDeclarations'] = CSSNestedDeclarations
exposed_constructs['when'] = when
exposed_constructs['Image'] = Image
exposed_constructs['Audio'] = Audio
