from pyv8env import Null, Undefined
from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_touch_list import TouchList as V8TouchList
from pyv8env.env.impl.error import V8TypeError


@impl_warp
class TouchList(V8TouchList):

    def __v8_index_get__(self, index):
        ret = self.fn_item(index)
        if ret is not Null:
            return ret

    def __v8_index_set__(self, *args):
        return Undefined

    def __v8_index_enum__(self, *args):
        return len(self._bs_tags)

    def __v8_index_del__(self, *args):
        return False

    def get_length(self):
        return len(self._items)

    def fn_item(self, *args):
        if len(args) == 0:
            raise V8TypeError(
                "Failed to execute 'item' on 'TouchList': 1 argument required, but only 0 present."
            )
        try:
            return self._items[int(args[0])]
        except Exception:
            return Null

    def __init__(self, items=None):
        self._items = items or []
