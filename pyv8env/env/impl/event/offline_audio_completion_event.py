from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_offline_audio_completion_event import OfflineAudioCompletionEvent as V8OfflineAudioCompletionEvent


@impl_warp
class OfflineAudioCompletionEvent(V8OfflineAudioCompletionEvent):
    def __init__(self, *args, **kw):
        kw.setdefault('isTrusted', True)
        super(OfflineAudioCompletionEvent, self).__init__(*args, **kw)
