import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot, SUPPORT_CHAT, OWNER_USERNAME, dispatcher


PHOTO = [
    "https://te.legra.ph/file/65e0e592613042d1a778a.jpg",
    "https://te.legra.ph/file/65e0e592613042d1a778a.jpg", 
]


@register(pattern=("Kazuha Start"))
async def awake(event):
    TEXT = f"**Hᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ {dispatcher.bot.first_name}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ​ : [𝗦𝗢𝗨𝗠𝗬𝗔:)](https://t.me/{OWNER_USERNAME})** \n\n"
    TEXT += f"» **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("Hᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("Sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "Aʟɪᴠᴇ"
