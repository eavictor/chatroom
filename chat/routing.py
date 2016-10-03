from channels.routing import route
from . import consumers


channel_routing = [
    route('websocket.connect', consumers.ws_add, path=r'^/(?P<room>\w+)$'),
    route('websocket.receive', consumers.ws_echo),
    route('websocket.disconnect', consumers.ws_remove, path=r'^/(?P<room>\w+)$'),
]
