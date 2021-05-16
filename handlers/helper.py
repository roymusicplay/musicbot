from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("help") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""😊Thanks for useing this bot😊

           BOT CAMMANDS 
 
/play <song name>

/urlplay <YouTube video link>

/skip  ⏩To the next song 

/end 🚫to stop playing

/pause ⏸️to pause the song

/resume ▶️To continue The song

        💝❤️🧡💛💚💙💜🤎🖤❤️
        🤍 @MafiaBot_Support 🤍
        💝❤️🧡💛💚💙💜🤎🖤❤️""")

@Client.on_message(command("help") & other_filters)
async def ghelp(_, message: Message):
    await message.reply_text(f"**{bn} :-** Hey! DM me to get all the commands 😉")
                            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Click here to Dm me for help😏", url="http://t.me/MAFIA_MUSIC_ROBOT?start=help"
                    )
                ],[
                    InlineKeyboardButton(
                        "Support Group 🎙️", url="https://t.me/MafiaBot_Chit_Chat""
                    ),
                    )
                ]
            ]
        )
    )
