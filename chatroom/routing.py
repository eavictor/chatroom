from channels.routing import include


channel_routing = [
    include('chat.routing.channel_routing', path=r'^/chat'),
]
