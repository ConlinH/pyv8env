import base64
import binascii
import time
from copy import deepcopy

from pyv8env import Null, Undefined, Context
from pyv8env import Null, Undefined
from pyv8env.env.impl import *
from pyv8env.env.impl.error import V8TypeError
from pyv8env.env.impl.error import DOMException
# from .window_depen.dom_file_system import DOMFileSystem
from ..chrome.flags import *
from .event.message_event import MessageEvent
from ..chrome.v8_window import Window as V8Window
from ..handler import Handler


@impl_warp
class Window(V8Window):
    __v8_global_this__ = True

    def __v8__cross_origin_check__(self, interviewee):
        # origin = interviewee.origin
        # if origin == "about://":
        #     return True
        #
        # if origin == self.get_origin():
        #     return True
        #
        # return False
        return True

    def __v8_name_get__(self, name):
        if name in exposed_constructs and name not in self._modify_exposed_constructs:
            return exposed_constructs[name]

    def __v8_name_set__(self, name, val):
        if name in exposed_constructs and name not in self._modify_exposed_constructs:
            self._modify_exposed_constructs.add(name)

    def __v8_name_enum__(self, *args):
        return exposed_names

    def __v8_name_query__(self, name):
        # 0： 'writable': True, 'enumerable': True, 'configurable': True
        # 1： 'writable': False, 'enumerable': True, 'configurable': True
        # 2： 'writable': True, 'enumerable': False, 'configurable': True
        # 3： 'writable': False, 'enumerable': False, 'configurable': True
        # 4： 'writable': True, 'enumerable': True, 'configurable': False
        if name == "chrome":
            return 4
        if name in exposed_names:
            return 2

    def __v8_index_get__(self, *args):
        pass

    def __v8_index_set__(self, *args):
        return Undefined

    def __v8_index_del__(self, *args):
        pass

    def __v8_index_enum__(self, *args):
        return 0

    def fn_structuredClone(self, *args):
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'structuredClone' on 'Window': 1 arguments required, but only 0 present.")
        return self.ctx.faker.structuredClone(args[0])

    def postMessage_impl(self, e):
        if on_message := self.get_onmessage():
            on_message(e)
        self.fn_dispatchEvent(e)

    def fn_postMessage(self, *args, win=None):
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'postMessage' on 'Window': 1 arguments required, but only 0 present.")

        data = args[0]
        logger.debug(f"fn_postMessage target: {self.get_origin()}")
        logger.debug(f"fn_postMessage source: {win.get_origin()}")
        # val = {k: data[k] for k in dir(data)}
        # logger.debug(f"fn_postMessage data: {val}")
        e = MessageEvent("message", isTrusted=True, data=data, source=win, target=self, origin=win.get_origin(), eventPhase=2)
        # 使用v8的Promise 使得postMessage稍后执行
        self.ctx.Promise.resolve(e).then(self.postMessage_impl)

    def fn_requestAnimationFrame(self, *args, delay=False):
        if len(args) == 0:
            raise V8TypeError(
                "Failed to execute 'requestAnimationFrame' on 'Window': 1 arguments required, but only 0 present.")
        # i = getattr(self, '_requestAnimationFrame', 1)
        # setattr(self, '_requestAnimationFrame', i + 1)
        # if delay:
        #     self._on_finish_tasks.push(self.fn_requestAnimationFrame, args)
        # else:
        #     args[0]()
        # return i

    def fn_matchMedia(self, *args):
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'matchMedia' on 'Window': 1 arguments required, but only 0 present.")
        # return MediaQueryList(args[0])

    def fn_fetch(self, *args):
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'fetch' on 'Window': 1 argument required, but only 0 present.")

        # url = self.get_document().deal_url(args[0])
        # with self.get_performance().add_resource_entry() as item:
        #     item['name'] = url
        #     item['initiatorType'] = 'fetch'
        #     ret = self.handler.on_fetch(url)
        #
        # status = (ret and ret.status_code) or 200
        # ok = status < 300
        # logger.debug(f'v8_window.py -> Window.fetch{tuple(args)} -> method {url}')
        # kw_response = dict(ok=ok, status=status)
        # if ret:
        #     kw_response.update(dict(content=ret.content, kw_headers=dict(ret.headers)))
        # return self._ctx.Promise.resolve(Response(**kw_response))

    def fn_atob(self, *args):
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'atob' on 'Window': 1 argument required, but only 0 present.")
        # logger.debug(f'window.py -> Window.atob{tuple(args)} -> method')
        s = str(args[0])
        try:
            return base64.b64decode(s + '=' * (4 - len(s) % 4)).decode('latin-1')
        except binascii.Error:
            raise InvalidCharacterError(
                "Failed to execute 'atob' on 'Window': The string to be decoded is not correctly encoded.")

    def fn_btoa(self, *args):
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'btoa' on 'Window': 1 argument required, but only 0 present.")
        # logger.debug(f'v8_window.py -> Window.btoa{tuple(args)} -> method')
        return base64.b64encode(str(args[0]).encode('latin-1')).decode('latin-1')

    def fn_webkitRequestFileSystem(self, *args, delay=True):
        # 文件存储系统 类似缓存 非标准接口
        if len(args) < 3:
            raise V8TypeError(
                f"Failed to execute 'webkitRequestFileSystem' on 'Window': 3 arguments required, but only {len(args)} present.")
        if args[0] not in (0, 1):
            if len(args) >= 3:
                failed_cb = args[3]
                failed_cb(DOMException(
                    "It was determined that certain files are unsafe for access within a Web application, or that "
                    "too many calls are being made on file resources.", "SecurityError", 18))
        # logger.debug(args)

        success_cb = args[3]
        # success_cb(
        #     DOMFileSystem())
        # logger.debug(f"fn_webkitRequestFileSystem {success_cb}")

    def fn_getComputedStyle(self, *args):
        if len(args) == 0:
            raise V8TypeError(
                "Failed to execute 'getComputedStyle' on 'Window': 1 argument required, but only 0 present.")
        # ele = args[0]
        # if not isinstance(ele, HTMLElement):
        #     raise V8TypeError("Failed to execute 'getComputedStyle' on 'Window': parameter 1 is not of type 'Element'.")
        # background_color = GetComputedStyle_Mapper.get(ele._bs_tag.get("style"), "")
        # if not background_color:
        #     logger.debug(
        #         f'patch -> 请hook获取具体的CSSStyleDeclaration值 -> Window.getComputedStyle{tuple(args)} -> method')
        # logger.debug(f'Window.getComputedStyle{tuple(args)} -> {ele._bs_tag.get("style")} -> {background_color}')
        # return CSSStyleDeclaration(backgroundColor=background_color)

    def fn_clearTimeout(self, *args):
        if len(args) >= 1 and args[0] in self._timers:
            del self._timers[args[0]]

    def fn_clearInterval(self, *args):
        if len(args) >= 1 and args[0] in self._timers:
            del self._timers[args[0]]

    def fn_setTimeout(self, *args, worker=False):
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'setTimeout' on 'Window': 1 argument required, but only 0 present.")
        self._timer_index += 1
        delay = 0
        arguments = []
        if len(args) >= 2:
            delay = args[1]
            if str(delay) == 'nan':
                delay = 0
        if len(args) >= 3:
            arguments = args[2:]
        self._timers[self._timer_index] = {
            "delay": delay, "type": 'Timeout', "start": int(time.time() * 1000), "func": args[0],
            "arguments": arguments, "worker": worker
        }
        # logger.debug(f"setTimeout: {self._timer_index} {self.get_origin()} {self._timers[self._timer_index]}")
        return self._timer_index

    def fn_setInterval(self, *args):
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'setInterval' on 'Window': 1 argument required, but only 0 present.")
        self._timer_index += 1
        delay = 0
        arguments = []
        if len(args) >= 2:
            delay = args[1]
        if len(args) >= 3:
            arguments = args[2:]
        self._timers[self._timer_index] = {
            "delay": delay, "type": 'Interval', "start": int(time.time() * 1000), "func": args[0],
            "arguments": arguments
        }
        logger.debug(f"setInterval: {self._timer_index} {self._timers[self._timer_index]}")
        return self._timer_index

    def exec_timeout(self, timeout=True, interval=True, worker=False, skip_time=0, delay=float('inf')):
        flag = True
        while flag:
            flag = False
            for index, _ in sorted(self._timers.items(), key=lambda item: item[1]['delay'] + item[1]['start']):
                now = int(time.time() * 1000) + skip_time
                task = self._timers.get(index)

                if task["delay"] > delay:
                    logger.debug(f"----{index} pass -> {task}")
                    continue

                if task["start"] + task["delay"] > now:
                    logger.debug(f"----{index} pass -> {task}")
                    continue

                if timeout and task["type"] == "Timeout" and task["worker"] == worker:
                    logger.debug(f"----{index} do -> {task}")
                    flag = True
                    if isinstance(task["func"], str):
                        self._ctx.exec_js(task["func"])
                    else:
                        logger.info(task["func"])
                        logger.info(task["arguments"])
                        task["func"].call(task["func"], *task["arguments"])
                    if index in self._timers:
                        del self._timers[index]
                    break
                elif interval and task["type"] == "Interval" and task["worker"] == worker:
                    logger.debug(f"----{index} do -> {task}")
                    flag = True
                    if isinstance(task["func"], str):
                        self._ctx.exec_js(task["func"])
                    else:
                        task["func"](*task["arguments"])
                    task["start"] = now
                    task["times"] = task.get("times", 0) + 1
                    break
                else:
                    logger.debug(f"----{index} pass -> {task}")

    def exec_timer_one(self, timeout=True, interval=True, worker=False, delay=float('inf')):
        for index in list(self._timers.keys()):
            task = self._timers[index]

            if task["delay"] != delay:
                logger.debug(f"----{index} pass -> {task}")
                continue

            if timeout and task["type"] == "Timeout" and task["worker"] == worker:
                logger.debug(f"----{index} do -> {task}")
                if isinstance(task["func"], str):
                    self._ctx.exec_js(task["func"])
                else:
                    logger.info(task["func"])
                    logger.info(task["arguments"])
                    task["func"].call(task["func"], *task["arguments"])
                if index in self._timers:
                    del self._timers[index]
            elif interval and task["type"] == "Interval" and task["worker"] == worker:
                logger.debug(f"----{index} do -> {task}")
                if isinstance(task["func"], str):
                    self._ctx.exec_js(task["func"])
                else:
                    task["func"](*task["arguments"])
                task["start"] = int(time.time() * 1000)
                task["times"] = task.get("times", 0) + 1
            else:
                logger.debug(f"----{index} pass -> {task}")

    def dispatch_event(self, target, ev):
        nodes = []
        ev._attr['bubbles'] = True
        ev._attr['cancelable'] = True
        ev._attr['isTrusted'] = True
        ev._attr['target'] = target
        ev._attr['srcElement'] = target
        ev._attr['view'] = self
        ev._attr['which'] = 1

        self._attr['event'] = ev

        # 找出所有element对象
        point = target
        while point and point != self:
            nodes.append(point)
            point = point.get_parentNode()
        nodes.append(self)

        # 触发捕获事件
        for node in nodes[::-1]:
            if ev._attr.get("cancelBubble"):
                break
            ev._attr['eventPhase'] = 1
            if node == target:
                ev._attr['eventPhase'] = 2
            ev._attr['currentTarget'] = node
            onevent = node._attr.get('on' + ev.get_type())
            if onevent:
                onevent.call(node, ev)
            node.fn_dispatchEvent(ev, capture=True)

        # 触发冒泡事件
        ev._attr["cancelBubble"] = False
        for node in nodes:
            if ev._attr.get("cancelBubble"):
                break
            ev._attr['eventPhase'] = 3
            if node == target:
                ev._attr['eventPhase'] = 2
            ev._attr['currentTarget'] = node
            onevent = node._attr.get('on' + ev.get_type())
            if onevent:
                onevent.call(node, ev)
            node.fn_dispatchEvent(ev, capture=False)

        self._attr['event'] = Undefined

    def done(self):
        if self.handler:
            self.handler.on_done(self)

    def debugger(self):
        self._ctx.exec_js('debugger;')

    def exec_js(self, *args, **kwargs):
        return self._ctx.exec_js(*args, **kwargs)
    
    @property
    def ctx(self):
        return self._ctx

    def release(self):
        self._ctx = None

    def start(self, devtool=False, callback=None):
        code = """
            Object.defineProperty(globalThis, "chrome", {
                value: globalThis.chrome, writable: true, enumerable: true, configurable: false
            });
            Object.setPrototypeOf(Image.prototype, HTMLImageElement.prototype);
            Object.setPrototypeOf(Audio.prototype, HTMLAudioElement.prototype);
            
            webkitRTCPeerConnection = RTCPeerConnection;
            window.gc = undefined;
            delete SharedArrayBuffer;
        """
        if self._wasm:
            code += """
            WebAssembly.compile = function compile(bufferSource) {
                try {
                  let module = new WebAssembly.Module(bufferSource);
                  return Promise.resolve(module);
                } catch (err) {
                  return Promise.reject(err);
                }
            }

            WebAssembly.instantiate= function instantiate(buffer_or_module, importObject){
                try {
                    if (ArrayBuffer.isView(buffer_or_module) || buffer_or_module instanceof ArrayBuffer ) {
                        let module = new WebAssembly.Module(buffer_or_module);
                        let instance = new WebAssembly.Instance(module, importObject);
                        return Promise.resolve({module:module, instance:instance});
                    }else if (buffer_or_module instanceof WebAssembly.Module) {
                        let instance = new WebAssembly.Instance(buffer_or_module, importObject);
                        return Promise.resolve(instance);
                    } else {
                        throw TypeError("WebAssembly.instantiate(): Argument 0 must be a buffer source");
                    }
                } catch (err) {
                  return Promise.reject(err);
                }
            };
            """
        if self._hook:
            code += "faker.hook=true;"
        self._ctx.exec_js(code)

        if devtool:
            from pyv8env import start_devtools
            # start_devtools(self._ctx, self, callback=callback if callback else self.get_document().parse_html)
            start_devtools(self._ctx, self, callback=callback)
        else:
            if callback:
                # for _ in self.get_document()._bs_tag.iter_tags():
                #     pass
                callback(self._ctx, self)
            else:
                # self.get_document().parse_html(self._ctx)
                pass

    def __init__(
            self,
            hook: bool = False,
            url: str = None,
            cookies: dict = None,
            headers: dict = None,
            handler: Handler = None,
            wasm: bool = False,
            proxies=None,
            top=None,
            parent=None,
            origin=None,
            ctx_type="[Top]",
            **kw
    ):
        self._hook = hook
        self._wasm = wasm
        if not url:
            url = "http://127.0.0.1"  # raise Exception("Set url Please!")

        if handler is None:
            handler = Handler(url=url, cookies=cookies or {}, headers=headers, proxies=proxies)
        self.handler = handler

        self._kw = deepcopy(kw)

        # self._location = Location(url, **kw.pop('kw_location', {}))
        # self._navigator = Navigator(window=self, **kw.pop('kw_navigator', {}))
        default = {
            # "location": self._location, "origin": origin or self._location.get_origin(),
            # "document": HTMLDocument(location=self._location, win=self, **kw.pop('kw_document', {})),
            # "navigator": self._navigator, "customElements": CustomElementRegistry(),
            # "history": History(location=self._location, **kw.pop('kw_history', {})),
            # "navigation": Navigation(**kw.pop('kw_navigation', {})),
            # "indexedDB": IDBFactory(self, **kw.pop('kw_indexedDB', {})),
            # "sessionStorage": Storage(**kw.pop('kw_sessionStorage', {})),
            # "localStorage": Storage(**kw.pop('kw_localStorage', {})), "screen": Screen(**kw.pop('kw_screen', {})),

            "outerWidth": 2560, "outerHeight": 1040, "innerWidth": 2560, "innerHeight": 919, "scrollX": 0,
            "pageXOffset": 0, "scrollY": 0, "pageYOffset": 0, "length": 0, "screenX": 0, "screenY": 0, "screenLeft": 0,
            # "screenTop": 0, "devicePixelRatio": 1, "locationbar": BarProp(), "menubar": BarProp(),
            # "personalbar": BarProp(), "scrollbars": BarProp(), "statusbar": BarProp(), "toolbar": BarProp(),
            # "status": "", "name": "", "closed": False, "opener": Null, "frameElement": Null, "external": External(),
            # "visualViewport": VisualViewport(), "clientInformation": self._navigator, "styleMedia": StyleMedia(),
            # "isSecureContext": True, "trustedTypes": TrustedTypePolicyFactory(),
            # "performance": Performance(self._location.get_href(), **kw.pop('kw_performance', {})),
            # "crypto": Crypto(win=self), "launchQueue": LaunchQueue(), "sharedStorage": SharedStorage(),
            # "documentPictureInPicture": DocumentPictureInPicture(), "originAgentCluster": True,
            # "offscreenBuffering": True, "credentialless": False, "speechSynthesis": SpeechSynthesis(),
            # "crossOriginIsolated": False, "scheduler": Scheduler(), "caches": CacheStorage(),
            # "cookieStore": CookieStore(), "onbeforeinstallprompt": Null, "onbeforexrselect": Null, "onabort": Null,
            "onbeforeinput": Null, "onbeforetoggle": Null, "onblur": Null, "oncancel": Null, "oncanplay": Null,
            "oncanplaythrough": Null, "onchange": Null, "onclick": Null, "onclose": Null, "oncontextlost": Null,
            "oncontextmenu": Null, "ondblclick": Null, "ondrag": Null, "ondragend": Null, "ondragenter": Null,
            "ondragleave": Null, "ondragover": Null, "ondragstart": Null, "ondrop": Null, "ondurationchange": Null,
            "onemptied": Null, "onended": Null, "onerror": Null, "onfocus": Null, "onformdata": Null, "oninput": Null,
            "oninvalid": Null, "onkeydown": Null, "onkeypress": Null, "onkeyup": Null, "onload": Null,
            "onloadeddata": Null, "onloadedmetadata": Null, "onloadstart": Null, "onmousedown": Null,
            "onmouseenter": Null, "onsearch": Null, "onmouseleave": Null, "onmousemove": Null, "onmouseout": Null,
            "onmouseover": Null, "onmouseup": Null, "onmousewheel": Null, "onpause": Null, "onplay": Null,
            "onplaying": Null, "onprogress": Null, "onratechange": Null, "onreset": Null, "onresize": Null,
            "onscroll": Null, "onappinstalled": Null, "onsecuritypolicyviolation": Null, "onseeked": Null,
            "onseeking": Null, "onselect": Null, "onslotchange": Null, "onstalled": Null, "onsubmit": Null,
            "onsuspend": Null, "ontimeupdate": Null, "ontoggle": Null, "onvolumechange": Null, "onwaiting": Null,
            "onwebkitanimationend": Null, "onwebkitanimationiteration": Null, "onwebkitanimationstart": Null,
            "onwebkittransitionend": Null, "onwheel": Null, "onauxclick": Null, "ongotpointercapture": Null,
            "onlostpointercapture": Null, "onpointerdown": Null, "onpointermove": Null, "onpointerrawupdate": Null,
            "onpointerup": Null, "onpointercancel": Null, "onpointerover": Null, "onpointerout": Null,
            "onpointerenter": Null, "onpointerleave": Null, "onselectstart": Null, "onselectionchange": Null,
            "onanimationend": Null, "onanimationiteration": Null, "onanimationstart": Null, "ontransitionrun": Null,
            "ontransitionstart": Null, "ontransitionend": Null, "ontransitioncancel": Null, "onafterprint": Null,
            "onbeforeprint": Null, "onbeforeunload": Null, "onhashchange": Null, "onlanguagechange": Null,
            "onmessage": Null, "onmessageerror": Null, "onoffline": Null, "onpagehide": Null, "onpageshow": Null,
            "onscrollend": Null, "onpopstate": Null, "onrejectionhandled": Null, "onstorage": Null,
            "onunhandledrejection": Null, "onunload": Null, "onpageswap": Null, "onpagereveal": Null, "fence": Null,
            "onbeforematch": Null, "ondevicemotion": Null, "ondeviceorientation": Null,
            "ondeviceorientationabsolute": Null, "ononline": Null, "oncontentvisibilityautostatechange": Null,
            "oncuechange": Null, "oncontextrestored": Null, "onscrollsnapchange": Null, "onscrollsnapchanging": Null,
            "event": Undefined,
        }
        for key, val in default.items():
            kw.setdefault(key, val)
        super(Window, self).__init__(**kw)
        self._attr.update({
            "window": self, "frames": self, "self": self, 
            "top": self if top is None else top,
            "parent": self if parent is None else parent
        })

        self._timers = {}
        self._timer_index = 0
        self._timer_index_worker = 0

        self._blob_cache = {}

        self._modify_exposed_constructs = set()
        self._ctx = Context(global_this=self, hook=hook, ctx_type=ctx_type)
