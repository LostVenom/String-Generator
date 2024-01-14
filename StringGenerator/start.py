from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝐻𝑒𝑦 {msg.from_user.mention} 🫧🖤,

๏ Ｍʏsᴇʟғ {me2}!,

⧉  𝖠 𝖲ᴛʀɪɴɢ 𝖲ᴇssɪᴏɴ 𝖡ᴏᴛ ᴛᴏ 𝖧ᴇʟᴘ ᴜ 𝖢ʀᴇᴀᴛᴇ 𝖠ɴʏ 𝖳ʏᴘᴇ ᴏғ 𝖲ᴛʀɪɴɢ 𝖤ᴀsɪʟʏ.

⧉ 𝖥ᴜʟʟʏ 𝖳ʀᴜsᴛᴇᴅ, 𝖲ᴀғᴇ & 𝖲ᴇᴄᴜʀᴇ 𝖡ᴏᴛ ᴛᴏ 𝖦ᴇɴᴇʀᴀᴛᴇ 𝖸ᴏᴜʀ 𝖲ᴛʀɪɴɢ 𝖲ᴇssɪᴏɴs.

⧉ 𝖳ᴀᴘ ᴏɴ 𝖦ᴇɴᴇʀᴀᴛᴇ 𝖲ᴇssɪᴏɴ 𝖡ᴜᴛᴛᴏɴ ᴛᴏ 𝖦ᴇɴᴇʀᴀᴛᴇ 𝖸ᴏᴜʀ 𝖲ᴇssɪᴏɴ📄.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="👻 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐒ᴇssɪᴏɴ 👻", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔎 sᴜᴘᴘᴏʀᴛ 🔍", url="https://t.me/TitanXSupport"),
                    InlineKeyboardButton("🏴‍☠ ɴᴇᴛᴡᴏʀᴋ 🏴‍☠", url="https://t.me/TitanNetwrk")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
