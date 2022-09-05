import random
import asyncio
from pyrogram import filters, __version__ as pver
from sys import version_info
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tver
from telegram import __version__ as lver
from FallenRobot import OWNER_USERNAME, SUPPORT_CHAT, pbot

PHOTO = [
    "https://telegra.ph/file/b246220f29d39c1e63576.jpg",
    "https://telegra.ph/file/77dcc39dfd9cf8d2db16f.jpg",
]

KIRITO = [
    [
        InlineKeyboardButton(text="Hᴇʟᴘ", url=f"https://t.me/KazuhaXRobot?start=help"),
        InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(text="Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ", url=f"http://t.me/KazuhaXRobot?startgroup=true"),
    ],
]

@pbot.on_message(filters.command("Kazuha alive"))
async def restart(client, m: Message):
    accha = await m.reply("⚡")
    await asyncio.sleep(3)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("Aʟɪᴠɪɴɢ....")
    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker("CAACAgIAAxkBAAEFwhZjFXVAiqWCLwxZTennbhUbeS8x-wACJwwAAtQqwEkOqPXXOoTv5ikE")
    await asyncio.sleep(2)
    await umm.delete()
    await asyncio.sleep(0.1)
    await m.reply_photo(
        random.choice(PHOTO),
        caption=f"""**Hᴇʏ​ I Aᴍ Kᴀᴇᴅᴇʜᴀʀᴀ Kᴀᴢᴜʜᴀ ʙᴏᴛ​**
        ━━━━━━━━━━━━━━━━━━━
        » **Mʏ Oᴡɴᴇʀ :** [Jᴇᴀɴ](https://t.me/{OWNER_USERNAME})
        » **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{lver}`
        » **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{tver}`
        » **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pver}`
        » **Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
        ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(KIRITO)
    )
