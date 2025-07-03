from .event import Event
from .idb_version_change_event import IDBVersionChangeEvent
from .before_unload_event import BeforeUnloadEvent
from .mouse_event import MouseEvent
from .pointer_event import PointerEvent
from .touch_event import TouchEvent
from .device_motion_event import DeviceMotionEvent
from .progress_event import ProgressEvent
from .message_event import MessageEvent
from .input_event import InputEvent
from .audio_processing_event import AudioProcessingEvent
from .offline_audio_completion_event import OfflineAudioCompletionEvent
from .focus_event import FocusEvent
from .custom_event import CustomEvent

from .device_orientation_event import DeviceOrientationEvent
from .device_motion_event_acceleration import DeviceMotionEventAcceleration
from .device_motion_event_rotation_rate import DeviceMotionEventRotationRate
from .rtc_peer_connection_ice_event import RTCPeerConnectionIceEvent

from .media_key_message_event import MediaKeyMessageEvent


Event_Mapper = {
    'TouchEvent': TouchEvent,
    'Event': Event,
    'MouseEvent': MouseEvent,
}
