from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client, dispatcher, OWNER_USERNAME


JEAN = "https://te.legra.ph/file/a523094b25a3cae372c02.mp4"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_video(
        video=JEAN,
        caption=f"""**Hᴇʏ​ {message.from_user.mention()},\n\nI Aᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ​ :** [JEAN](tg://user?id=5508536618)
**» Pʏᴛʜᴏɴ vᴇʀsɪᴏɴ :** `{y()}`
**» Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{o}` 
**» Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{s}` 
**» Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{z}`

**Yᴏᴜ Cᴀɴ Bᴜʏ Tʜɪs Bᴏᴛ's Pʀɪᴠᴀᴛᴇ Rᴇᴘᴏ Aᴛ Tʜᴇ Bᴜᴛᴛᴏɴs Bᴇʟʟᴏᴡ .**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❆ Mʏ Gᴏᴅ ❆", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "• Bᴜʏ Rᴇᴘᴏ•",
                        url="https://t.me/iamjeansama/3",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
