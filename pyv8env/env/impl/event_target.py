from pyv8env.env.impl.error import V8TypeError
from ..chrome.flags import *
from ..chrome.v8_event_target import EventTarget as V8EventTarget


@impl_warp
class EventTarget(V8EventTarget):

    __v8_method__ = (
        ("addEventListener", "fn_addEventListener", 2, 0, 1, 0, 0, 0, 0),
        ("dispatchEvent", "fn_dispatchEvent", 1, 0, 1, 0, 0, 0, 0),
        ("removeEventListener", "fn_removeEventListener", 2, 0, 1, 0, 0, 0, 0),
    )

    def fn_addEventListener(self, *args):
        # logger.debug(f'{self}.addEventListener{tuple(args)}')

        if len(args) < 2:
            raise V8TypeError(
                f"Failed to execute 'addEventListener' on 'EventTarget': 2 arguments required, but only {len(args)} present."
            )
        option = {"capture": False, "once": False, "passive": False}
        if len(args) >= 3:
            if isinstance(args[2], dict):
                option.update(args[2])
            else:
                option["capture"] = bool(args[2])
        type_ = args[0]
        listener = args[1]

        this_type_events = self._events.get(type_, [])
        if not this_type_events:
            self._events[type_] = this_type_events

        e = (listener, option)
        if e not in this_type_events:
            this_type_events.append(e)

    def fn_dispatchEvent(self, *args, capture=None):
        # logger.debug(f'start {self}.dispatchEvent{tuple(args)}')

        if len(args) == 0:
            raise V8TypeError(
                f"Failed to execute 'dispatchEvent' on 'EventTarget': 2 arguments required, but only 0 present."
            )

        event = args[0]
        type_ = event.get_type()
        this_type_events = self._events.get(type_, [])
        for listener, option in this_type_events:
            if option["capture"] != capture and capture is not None:
                continue
            # logger.info(f"xxxx {self.__class__.__name__}")
            if self.__class__.__name__ == "Window":
                listener(event)
            else:
                logger.info(listener)
                if isinstance(listener, dict):
                    if "handleEvent" not in listener:
                        continue
                    handle_event_func = listener["handleEvent"]
                    handle_event_func.call(listener, event)
                else:
                    listener.call(self, event)
                # logger.info(f"listener.call(self, event) 2")
            logger.debug(f'{self}.dispatchEvent{tuple(args)} -> {listener}')

    def fn_removeEventListener(self, *args):
        # logger.debug(f'{self}.removeEventListener{tuple(args)}')

        if len(args) < 2:
            raise V8TypeError(
                f"Failed to execute 'removeEventListener' on 'EventTarget': 2 arguments required, but only {len(args)} present."
            )
        type_ = args[0]
        listener = args[1]
        this_type_events = self._events.get(type_)
        if not this_type_events:
            return
        for listener_, option in this_type_events:
            if listener == listener_:
                this_type_events.remove((listener_, option))
                break

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
        self._events = {}
