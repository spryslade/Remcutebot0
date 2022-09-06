import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as lver
from telethon import __version__ as tver
from pyrogram import __version__ as pver
from FallenRobot.events import register
from FallenRobot import telethn as tbot, SUPPORT_CHAT, OWNER_USERNAME, dispatcher


PHOTO = [
    "https://telegra.ph/file/47487d8437bd316d98feb.jpg",
    "https://telegra.ph/file/3bfc172ba4b2eaf3892dc.jpg", 
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"[{event.sender.first_name}](tg://user?id={event.sender.id}) *Kᴜɴɴ,* \n\n*❆ I Aᴍ* {dispatcher.bot.first_name}** \n\n"
    TEXT += f"*❆ I'ʟʟ Bᴇ Gɪᴠɪɴɢ Mʏ Bᴇsᴛ.* \n\n"
    TEXT += f"*❆ Mʏ Oᴡɴᴇʀ* : [Jᴇᴀɴ](https://t.me/{OWNER_USERNAME})** \n\n"
    TEXT += f"*❆ Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ* : {lver} \n\n"
    TEXT += f"*❆ Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ* : {tver} \n\n"
    TEXT += f"*❆ Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ* : {pver} \n\n"
    TEXT += f"*❆ Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ Hᴇʀᴇ.* \n\n"
    BUTTON = [
        [
            Button.url("Hᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("Sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


mod_name = "Aʟɪᴠᴇ"
