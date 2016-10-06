from channels import Group, Channel
from channels.sessions import channel_session


def ws_add(message):
    message.reply_channel.send({'accept': True})
    Group('chat').add(message.reply_channel)


def ws_echo(message):
    print(message.content['text'])
    # OK
    message.reply_channel.send({'text': message.content['text']})
    # Fail
    Channel('chat').send({'text': message.content['text']})
    # Fail
    Group('chat').send({'text': message.content['text']})


def ws_remove(message):
    Group('chat').discard(message.reply_channel)
