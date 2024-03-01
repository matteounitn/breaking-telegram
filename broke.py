from pyrogram.raw.types import (
    UpdateNewMessage,
    MessageMediaPhoto,
    MessageMediaDocument,
    PeerUser,
    MessageService,
)
from pyrogram import Client
import os.path

with open("config.ini", "r") as f:
    # we read the second and third line and split = to get the api_id and api_hash
    file = f.readlines()
    api_id = file[1].split("=")[1].strip()
    api_hash = file[2].split("=")[1].strip()

client = Client(name="default", api_id=api_id, api_hash=api_hash)


@client.on_raw_update(group=-100)
def handler(client, update, users, chats):
    if isinstance(update, UpdateNewMessage) and not isinstance(
        update.message, MessageService
    ):
        # print(update) # debug
        if (
            (
                isinstance(update.message.media, MessageMediaDocument)
                or isinstance(update.message.media, MessageMediaPhoto)
            )
            and isinstance(update.message.peer_id, PeerUser)
            and update.message.out is False
            and update.message.media.ttl_seconds is not None
        ):
            message = client.get_messages(
                update.message.peer_id.user_id, update.message.id
            )
            print(
                f"Message Received from userID {update.message.peer_id.user_id}. Saving!"
            )
            text = (
                f"__New Secret__\n__From__ {message.from_user.first_name} -"
                f" [{message.from_user.id}](tg://user?id={message.from_user.id}) \n\n"
                f"[Go to message](tg://openmessage?user_id={str(message.chat.id)}"
                f"&message_id={message.id})\n"
            )
            path = message.download()
            if os.path.exists(path):
                client.send_document("me", path, caption=text)
                os.remove(path)


print("Started! waiting for message...Press CTRL+C to stop.")
client.run()
