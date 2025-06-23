import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AloneX import LOGGER, app, userbot
from AloneX.core.call import Alone
from AloneX.misc import sudo
from AloneX.plugins import ALL_MODULES
from AloneX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AloneX.plugins" + all_module)
    LOGGER("AloneX.plugins").info("sabu kichi lod heigala modul jaka miss queen kai")
    await userbot.start()
    await Alone.start()
    try:
        await Alone.stream_call("https://files.catbox.moe/sfr91g.mp4")
    except NoActiveGroupCall:
        LOGGER("AloneX").error(
            "ʙsᴅᴋ ᴠᴄ ᴛᴏ ᴏɴ ᴋᴀʀʟᴇ  ʟᴏɢ ɢʀᴏᴜᴘ\ᴄʜᴀɴɴᴇʟ ᴋɪ.\n\n ᴏɴ ᴋᴀʀᴋᴇ ᴀᴀ ᴛᴀʙ ᴛᴀᴋ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ ʜᴏᴏɴ..."
        )
        exit()
    except:
        pass
    await Alone.decorators()
    LOGGER("AloneX").info(
        "ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ebe miss queen ra number ana nahele auu thare bot band karidebi"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AloneX").info("ᴍᴀᴀ ᴄʜᴜᴅᴀ ᴍᴀɪɴ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ hun miss queen number kai delani..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
