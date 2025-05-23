# import requests
from curl_cffi import requests
from .config import logger


class Handler:

    def __init__(self, url=None, cookies=None, headers=None, proxies=None):
        self.s = None
        self.cookies = cookies or {}
        self.headers = headers or {}
        self.url = url
        self.proxies = proxies
        self.xhr = []
        self.audio_event = []   # 存储AudioContext事件 方便触发
        self.offline_audio_context = []   # 存储OfflineAudioContext事件 方便触发
        self.rtc = []   # 存储RTCPeerConnection事件 方便触发

        self.setup()

    def setup(self):
        self.s = requests.Session()
        self.cookies and self.s.cookies.update(self.cookies)
        self.cookies = dict(self.s.cookies)

    def get_iframe_handler(self, src):
        return Handler(src, cookies=self.cookies, headers=self.headers, proxies=self.proxies)

    def update_document_cookie(self):
        self.cookies.update(dict(self.s.cookies))

    def update_session_cookie(self):
        self.s.cookies.update(self.cookies)

    def on_html(self, url=None, headers=None):
        """ 处理html页面的下载 """
        url = url or self.url
        if not url or url == 'http://127.0.0.1':
            return
            # raise Exception("参数错误，请设置url")
        headers = headers or self.headers
        res = self.s.get(url, headers=headers, proxies=self.proxies)
        return res.text

    def on_script_text(self, js_text):
        """ 拦截并处理判断是否执行该script内的js代码 """
        return js_text

    def on_script_src(self, src, referer=None):
        """ 处理js的下载 """
        headers = self.headers
        logger.debug(f"download js: {src}")
        if referer:
            headers = self.headers.copy()
            headers.update({'Referer': referer})
        return self.s.get(src, headers=headers, proxies=self.proxies).text

    def on_fetch(self, *args):
        """ 处理fetch请求的下载 """
        logger.debug(f"need fetch: {args}")

    def on_xhr_send(self, xhr):
        """ 处理xhr的send请求 """
        pass

    def on_xhr_new(self, xhr):
        """ 处理xhr的send请求 """
        self.xhr.append(xhr)

    def on_done(self, win):
        """ 当所有js代码执行完后 处理一些setTimeout事件及触发鼠标点击等事件 """
        pass

    def on_performance_observer_observe(self, performance_obj, types):
        """处理PerformanceObserver.observe函数， 根据types的类型向window.performance._items中增加对应的值"""
        pass
