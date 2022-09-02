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
    "https://telegra.ph/file/646a1752358324aa2ae24.jpg" 
]


@register(pattern=("/cosplay"))
async def awake(event):
    TEXT = "🥵Cosplay🥵"   
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT)


__mod_name__ = "Cosplay"
