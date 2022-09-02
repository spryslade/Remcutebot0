import os
import re
import random
from platform import python_version as kontol
from telethon import events
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/354c77ca7f1f7b03d87e7.jpg",
    "https://te.legra.ph/file/2187067613c1902b4c3ad.jpg",
    "https://telegra.ph/file/ccbf8c17e2852672ec9e3.jpg", 
    "https://te.legra.ph/file/d72ce40646cd693bfb235.jpg", 
    "https://telegra.ph/file/4d514f2289956b69c5e77.jpg", 
    "https://telegra.ph/file/3d5c8066614a917ed9041.jpg", 
    "https://te.legra.ph/file/84837f9323db81be5be4e.jpg" 
]


@register(pattern=("/cosplay"))
async def awake(event):
    TEXT = "Cosplay"   
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT)


__mod_name__ = "Cosplay"
