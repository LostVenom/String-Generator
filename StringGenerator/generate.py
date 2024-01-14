from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "**☞ 𝐂𝗁𝗈𝗈𝗌𝖾 𝐓𝗒𝗉𝖾 𝗈𝖿 𝐒𝗍𝗋𝗂𝗇𝗀 𝐘𝗈𝗎 𝐖𝖺𝗇𝗍 𝗍𝗈 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝖾 :**"
buttons_ques = [
    [
        InlineKeyboardButton("🕷 𝐏ʏʀᴏɢʀᴀᴍ 𝘃1 🕷", callback_data="pyrogram1"),
        InlineKeyboardButton("🕷 𝐏ʏʀᴏɢʀᴀᴍ 𝘃2 🕷", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("☠️ 𝐓ᴇʟᴇᴛʜᴏи ☠️", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("👀 𝐏ʏʀᴏɢʀᴀᴍ 𝐁ᴏᴛ 👀", callback_data="pyrogram_bot"),
        InlineKeyboardButton("👀 𝐓ᴇʟᴇᴛʜᴏи 𝐁ᴏᴛ 👀", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text="👻 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐒ᴛʀɪɴɢ 👻", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "☠️ 𝐓ᴇʟᴇᴛʜᴏи ☠️"
    else:
        ty = "🕷 𝐏ʏʀᴏɢʀᴀᴍ 🕷"
        if not old_pyro:
            ty += "𝘃2"
    if is_bot:
        ty += "𝐁ᴏᴛ"
    await msg.reply(f"☞ 𝐒ᴛᴀʀᴛɪɴɢ {ty} 𝐒ᴇssɪᴏɴ 𝐆ᴇɴᴇʀᴀᴛᴏʀ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝐏𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗇𝖽 ʏ𝗈𝗎𝗋 𝐴𝑃𝐼 𝐼𝐷 ᴛᴏ ᴘʀᴏᴄᴇss :\n\n𝐂𝗅𝗂𝖼𝗄 𝗈𝗇 /𝗌𝗄𝗂𝗉 𝗍𝗈 𝗎𝗌𝖾 𝐁𝗈𝗍 𝖠𝖯𝖨.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("☞ 𝐴𝑃𝐼 𝐼𝐷 𝖬ᴜs𝗍 𝖻𝖾 𝖺𝗇 𝐈𝗇𝗍𝖾𝗀𝖾𝗋, 𝐍𝗈𝗐 𝖲𝗍𝖺𝗋𝗍 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝐒𝗍𝗋𝗂𝗇𝗀 𝐀𝗀𝖺𝗂𝗇.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "☞ 𝐍𝗈𝗐 𝐏𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗇𝖽 ʏ𝗈𝗎𝗋 𝐴𝑃𝐼 𝐻𝐴𝑆𝐻 ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ :", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "☞ 𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝖾𝗇𝖽 ʏ𝗈𝗎𝗋 𝐏𝗁𝗈𝗇𝖾 𝐍𝗎𝗆𝖻𝖾𝗋 𝗐𝗂𝗍𝗁 𝐂𝗈𝗎𝗇𝗍𝗋𝗒 𝐂𝗈𝖽𝖾 𝗍𝗈 𝐂𝗈𝗇𝗍𝗂𝗇𝗎𝖾 :\n\n𝐄𝗑𝖺𝗆𝗉𝗅𝖾 : +91𝖷𝖷𝖷𝖷𝖷𝖷𝖷𝖷𝖷𝖷"
    else:
        t = "☞ 𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝖾𝗇𝖽 ʏ𝗈𝗎𝗋 𝐵𝑂𝑇 𝑇𝑂𝐾𝐸𝑁 𝗍𝗈 𝐂𝗈𝗇𝗍𝗂𝗇𝗎𝖾 :"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("☞ 𝐓𝗋𝗒𝗂𝗇𝗀 𝗍𝗈 𝐒𝖾𝗇𝖽 𝑂𝑇𝑃 𝖺𝗍 𝗍𝗁𝖾 𝐆𝗂𝗏𝖾𝗇 𝐍𝗎𝗆𝖻𝖾𝗋....")
    else:
        await msg.reply("☞ 𝐓𝗋𝗒𝗂𝗇𝗀 𝗍𝗈 𝐋𝗈𝗀𝗂𝗇 𝗏𝗂𝖺 𝐵𝑂𝑇 𝑇𝑂𝐾𝐸𝑁 ....")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("☞ 𝐘𝗈𝗎𝗋 𝐆𝗂𝗏𝖾𝗇  𝐴𝑃𝐼 𝐼𝐷 & 𝐴𝑃𝐼 𝐻𝐴𝑆𝐻 𝐂𝗈𝗆𝖻𝗂𝗇𝖺𝗍𝗂𝗈𝗇 𝐃𝗈𝖾𝗌𝗇'𝗍 𝐌𝖺𝗍𝖼𝗁 𝗐𝗂𝗍𝗁 𝐓𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝐀𝗉𝗉𝗌 𝐒𝗒𝗌𝗍𝖾𝗆.\n\n𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝐘𝗈𝗎𝗋 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇 𝐀𝗀𝖺𝗂𝗇.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("☞ 𝐓𝗁𝖾 𝑃𝐻𝑂𝑁𝐸 𝑁𝑈𝑀𝐵𝐸𝑅 𝗒𝗈𝗎 𝗌𝖾𝗇𝗍 𝐃𝗈𝖾𝗌𝗇'𝗍 𝐁𝖾𝗅𝗈𝗇𝗀 𝗍𝗈 𝖺𝗇𝗒 𝐓𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝐀𝖼𝖼𝗈𝗎𝗇𝗍.\n\n𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝐘𝗈𝗎𝗋 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇 𝐀𝗀𝖺𝗂𝗇.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "☞ 𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝖾𝗇𝖽 𝑂𝑇𝑃 𝗐𝗁𝗂𝖼𝗁 𝐘𝗈𝗎 𝐑𝖾𝖼𝖾𝗂𝗏𝖾𝖽 𝗈𝗇 𝐘𝗈𝗎𝗋 𝐓𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝐀𝖼𝖼𝗈𝗎𝗇𝗍.\n\n𝐈𝖿 𝑂𝑇𝑃 𝗂𝗌 43652, 𝐒𝖾𝗇𝖽 𝗂𝗍 𝖺𝗌 4 3 6 5 2", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("☞ 𝐓𝗂𝗆𝖾 𝐋𝗂𝗆𝗂𝗍 𝗈𝖿 10 𝐌𝗂𝗇𝗎𝗍𝖾𝗌 𝐑𝖾𝖺𝖼𝗁𝖾𝖽.\n\n𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝐘𝗈𝗎𝗋 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇 𝐀𝗀𝖺𝗂𝗇.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("☞ 𝐓𝗁𝖾 𝑂𝑇𝑃 𝐘𝗈𝗎'𝗏𝖾 𝐒𝖾𝗇𝗍 𝗂𝗌 𝐖𝗋𝗈𝗇𝗀.\n\n𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝐘𝗈𝗎𝗋 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇 𝐀𝗀𝖺𝗂𝗇.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("☞ 𝐓𝗁𝖾 𝑂𝑇𝑃 𝐘𝗈𝗎'𝗏𝖾 𝐒𝖾𝗇𝗍 𝗂𝗌 𝐄𝗑𝗉𝗂𝗋𝖾𝖽.\n\n𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝐘𝗈𝗎𝗋 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇 𝐀𝗀𝖺𝗂𝗇.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "☞ 𝐏𝗅𝖾𝖺𝗌𝖾 𝐄𝗇𝗍𝖾𝗋 𝗒𝗈𝗎𝗋 𝐓𝗐𝗈 𝐒𝗍𝖾𝗉 𝐕𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇 𝑃𝐴𝑆𝑆𝑊𝑂𝑅𝐷 𝗍𝗈 𝐂𝗈𝗇𝗍𝗂𝗇𝗎𝖾.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» 𝐓𝗂𝗆𝖾 𝐋𝗂𝗆𝗂𝗍 𝗈𝖿 5 𝐌𝗂𝗇𝗎𝗍𝖾𝗌 𝐑𝖾𝖺𝖼𝗁𝖾𝖽.\n\n𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝐘𝗈𝗎𝗋 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇 𝐀𝗀𝖺𝗂𝗇.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("☞ 𝐓𝗁𝖾 𝑃𝐴𝑆𝑆𝑊𝑂𝑅𝐷 𝐘𝗈𝗎'𝗏𝖾 𝐒𝖾𝗇𝗍 𝗂𝗌 𝐖𝗋𝗈𝗇𝗀.\n\n𝐏𝗅𝖾𝖺𝗌𝖾 𝖲𝗍𝖺𝗋𝗍 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗇𝗀 𝐘𝗈𝗎𝗋 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇 𝐀𝗀𝖺𝗂𝗇.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"☞ 𝐓𝗁𝗂𝗌 𝗂𝗌 𝐘𝗈𝗎𝗋 {ty} 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇. \n\n`{string_session}` \n\n𝐀 𝐏𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝐒𝗍𝗋𝗂𝗇𝗀 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗈𝗋 𝖻𝗒 : @𝖳𝗂𝗍𝖺𝗇𝖭𝖾𝗍𝗐𝗋𝗄"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "☞ 𝐒𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝖾𝖽 𝐘𝗈𝗎𝗋 {} 𝐒𝗍𝗋𝗂𝗇𝗀 𝐒𝖾𝗌𝗌𝗂𝗈𝗇.\n\n𝐏𝗅𝖾𝖺𝗌𝖾 𝐂𝗁𝖾𝖼𝗄 𝐘𝗈𝗎𝗋 𝐒𝖺𝗏𝖾𝖽 𝐌𝖾𝗌𝗌𝖺𝗀𝖾 𝗍𝗈 𝐆𝖾𝗍 𝗂𝗍 ! \n\n𝐀 𝐏𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝐒𝗍𝗋𝗂𝗇𝗀 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗈𝗋 𝖻𝗒 : @𝖳𝗂𝗍𝖺𝗇𝖭𝖾𝗍𝗐𝗋𝗄".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("☞ 𝐂𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽 𝗍𝗁𝖾 𝐎𝗇𝗀𝗈𝗂𝗇𝗀 𝐒𝗍𝗋𝗂𝗇𝗀 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗈𝗇 𝐏𝗋𝗈𝖼𝖾𝗌𝗌.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("☞ 𝐒𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝐑𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 𝖻𝗈𝗍..", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("☞ 𝐂𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽 𝗍𝗁𝖾 𝐎𝗇𝗀𝗈𝗂𝗇𝗀 𝐒𝗍𝗋𝗂𝗇𝗀 𝐆𝖾𝗇𝖾𝗋𝖺𝗍𝗂𝗈𝗇 𝐏𝗋𝗈𝖼𝖾𝗌𝗌.", quote=True)
        return True
    else:
        return False
