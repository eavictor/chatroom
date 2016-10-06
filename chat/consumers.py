from channels import Group, Channel
from channels.auth import channel_session_user_from_http, channel_session_user


@channel_session_user_from_http
def ws_add(message):
    # OK
    message.reply_channel.send({'text': 'Hello Browser from django-channels'})
    print(message.reply_channel)
    Group('chat').add(message.reply_channel)


@channel_session_user
def ws_echo(message):
    print("ws_echo: " + message.content['text'])
    # OK
    # message.reply_channel.send({'text': message.content['text']})
    # OK
    # Channel('chat').send({'text': message.content['text']})
    # OK
    Group('chat').send({'text': message.content['text']})


@channel_session_user
def ws_remove(message):
    Group('chat').discard(message.reply_channel)
