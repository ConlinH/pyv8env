import pyv8env

from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_idb_version_change_event import IDBVersionChangeEvent as V8IDBVersionChangeEvent
from pyv8env.env.impl.error import V8TypeError


@impl_warp
class IDBVersionChangeEvent(V8IDBVersionChangeEvent):

    def __init__(self, name, **kw):
        kw.setdefault("oldVersion", 0)
        kw.setdefault("newVersion", 1)
        super(IDBVersionChangeEvent, self).__init__(name, **kw)
