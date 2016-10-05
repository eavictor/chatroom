from channels import Group, Channel
from channels.sessions import channel_session


@channel_session
def ws_add(message):
    Group('chat').add(message.reply_channel)
    Group('chat').send({'text': 'Hello'})


@channel_session
def ws_echo(message):
    Group('chat').send({'text': message.content['text']})
    Channel('chat').send({'text': message.content['text']})


@channel_session
def ws_remove(message):
    Group('chat').discard(message.reply_channel)
