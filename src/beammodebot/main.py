import asyncio
import time
from pathlib import Path
from dotenv import load_dotenv
from telethon.types import InputWebDocument, DocumentAttributeImageSize
from telethon.tl.custom.button import Button

import beammodebot.pseudorand as pseudorand
from .config import get_tg_config
from telethon import TelegramClient, events
import random


async def _main_async():
    load_dotenv()

    api_id, api_hash, BOT_TOKEN, dev_mode = get_tg_config()

    """Main entry point for the bot."""
    print("BeamModeBot starting...")

    userlist_file = Path("./userlist.txt")
    users = []
    if userlist_file.exists():
        with userlist_file.open('r', encoding='utf-8') as fh:
            users = [l.strip() for l in fh.readlines()]

    async with TelegramClient('bot', api_id, api_hash) as bot:
        await bot.start(bot_token=BOT_TOKEN)


        @bot.on(events.NewMessage(pattern='/start'))
        async def start_handler(event: events.NewMessage.Event):
            """Show help message, but only in direct messages."""
            await event.reply("""Hello!
      
To use this bot, simply type "@BeamModeBot " into your text box and click one of the results or click the button attached to this message.""",
buttons=[[Button.switch_inline('Share your beam mode!', query='')]])

        @bot.on(events.InlineQuery)
        async def handler(event: events.InlineQuery.Event):
            nonlocal users

            builder = event.builder
            sender_id = event.sender_id
            unix_epoch = int(time.time())
            query_text = event.text.strip() if event.text else ""

            perc = pseudorand.roll150((sender_id if query_text == "" else query_text), unix_epoch) - 50

            commentary = (
                "You are at negative beam mode and officially in beam debt." if perc < 0
                else "You are at risk of being banned." if perc < 10
                else "Dan is paying attention." if perc < 30
                else "Gotta get your beam up." if perc < 50
                else "Not bad. not good. It's time to pay attention." if perc < 70
                else "Impressive. Very nice."
            )
            thumb = InputWebDocument(
                        url='https://raw.githubusercontent.com/idkravitz/BeamModeBot-assets/master/thumb.png',
                        size=0,
                        mime_type='image/png',
                        attributes=[DocumentAttributeImageSize(w=320, h=320)]
                    )
            buttons = [[Button.switch_inline('Share your beam mode!', query='')]]
            result_text = f'I am at {perc}% beam mode' if query_text == "" else f'{query_text} is at {perc}% beam mode'
            text = f'{result_text}. {commentary}'

            articles = [
                builder.article(
                    title=('How Beam Mode I am?' if query_text == "" else f"How Beam Mode is {query_text}"), 
                    text=text,
                    description=(f"[{perc}%]" if dev_mode else "") + "Send your current Beam Mode to this chat.",
                    thumb=thumb,
                    buttons=buttons
                ),
                builder.article(
                    title='HALP!',
                    text="Either press the button attached to this message and select the chat you would like to post in or simply enter \"@BeamModeBot \" into your text box.",
                    description="Send the usage guideliness to this chat.",
                    thumb = thumb,
                    buttons=buttons
                )
            ]

            if len(users) > 0:
                seed_hash = pseudorand.hash("spin", unix_epoch, 60)
                speen_wheel_pick = users[seed_hash % len(users)]
                articles.append(builder.article(
                    title='Spin the Wheel',
                    text=f'**Beam Wheel Result**: the winner is `{speen_wheel_pick}`',
                    description='Let\'s see who\'s lucky',
                    thumb=thumb
                ))
                rng = random.Random(seed_hash)
                top5 = rng.sample(users, 5)
                scores_top = [rng.randint(85, 100) for _ in top5]
                users_not_top = [u for u in users if u not in top5]
                bottom5 = rng.sample(users_not_top, 5)
                scores_bottom = [rng.randint(-50, 15) for _ in top5]
                scores_bottom.sort(reverse=True)
                scores_top.sort(reverse=True)
                articles.append(builder.article(
                    title='Top 5',
                    description='Top 5 Beamers Right Now',
                    thumb=thumb,
                    text="**Top 5 Beamers Right Now:**\n\n" + "\n".join([f'{place}. `{name}`: **{score}%**' for place, (name, score) in enumerate(zip(top5, scores_top), 1)])
                ))
                articles.append(builder.article(
                    title='Bottom 5',
                    description='Bottom 5 Beamers Right Now',
                    thumb=thumb,
                    text="**Bottom 5 Beamers Right Now:**\n\n" + "\n".join([f'{place}. `{name}`: **{score}%**' for place, (name, score) in enumerate(zip(bottom5, scores_bottom), len(users) - 4)])
                ))



            await event.answer(articles)

        await bot.run_until_disconnected()


def main():
    """Synchronous entry point for the bot (used by Poetry's entry point)."""
    asyncio.run(_main_async())


if __name__ == "__main__":
    main()

