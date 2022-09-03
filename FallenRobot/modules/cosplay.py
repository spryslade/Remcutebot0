import os
import re
import random
from platform import python_version as kontol
from telethon import events
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/a0875ad582a20831d3c72.jpg",
    "https://telegra.ph/file/4f815ffba1b3b4c5f4344.jpg",
    "https://telegra.ph/file/2fba3f829d1721368815f.jpg", 
    "https://telegra.ph/file/a7f76f90dabf9e86ec56f.jpg", 
    "https://telegra.ph/file/bd40d1306e102053ddb10.jpg", 
    "https://telegra.ph/file/486b06cc2b7be67581758.png", 
    "https://telegra.ph/file/42e4062137629ceb293a2.jpg", 
    "https://telegra.ph/file/34bea60a68f0363166561.jpg", 
    "https://telegra.ph/file/50f6606d72c71ab63d4e7.jpg", 
    "https://telegra.ph/file/a0dd57ac4530478d11293.jpg", 
    "https://telegra.ph/file/482c032f907d5312bb6dd.jpg",
    "https://telegra.ph/file/28ae629db5f85e1ef415c.jpg", 
    "https://telegra.ph/file/b7d035cc58e66ebe02291.png",
    "https://telegra.ph/file/c6f25c861ae9f7d423aa0.jpg",
    "https://telegra.ph/file/646a1752358324aa2ae24.jpg", 
    "https://te.legra.ph/file/b6a60f649a7068a8dcc95.jpg",
    "https://te.legra.ph/file/f5605260724f030360cdc.jpg", 
    "https://te.legra.ph/file/32e88f5e8304e83e1ea32.jpg", 
    "https://te.legra.ph/file/56a6a9ceee754a1ba87a0.jpg", 
    "https://te.legra.ph/file/30057c3267784b52a911c.jpg", 
    "https://te.legra.ph/file/9edd4ec351d243f640b20.jpg", 
    "https://te.legra.ph/file/aa4d368e6816a4853c477.jpg", 
    "https://te.legra.ph/file/ac9abe81fb07a2fc44afd.jpg", 
    "https://te.legra.ph/file/11a77988f615123ba2abd.jpg", 
    "https://te.legra.ph/file/d49f884c039f40f5b1271.jpg", 
    "https://te.legra.ph/file/1b0f096c8d6e82e91147d.jpg",
    "https://te.legra.ph/file/fb5e047dc7b5eb8f3c5bb.jpg", 
    "https://te.legra.ph/file/964536fb05b0c8b1e0cd7.jpg"
]


@register(pattern=("/cosplay"))
async def awake(event):
    TEXT = "🥵 コスプレ 🥵"   
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT)


__mod_name__ = "Cᴏsᴘʟᴀʏ"
