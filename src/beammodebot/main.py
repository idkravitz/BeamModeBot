import asyncio
import time
from dotenv import load_dotenv
from telethon.types import InputWebDocument, DocumentAttributeImageSize
from telethon.tl.custom.button import Button

from .random_func import random_func
from .config import get_tg_config
from telethon import TelegramClient, events


async def _main_async():
    load_dotenv()

    api_id, api_hash, BOT_TOKEN = get_tg_config()

    """Main entry point for the bot."""
    print("BeamModeBot starting...")

    async with TelegramClient('bot', api_id, api_hash) as bot:
        await bot.start(bot_token=BOT_TOKEN)

        @bot.on(events.InlineQuery)
        async def handler(event: events.InlineQuery.Event):
            builder = event.builder
            sender_id = event.sender_id
            unix_epoch = int(time.time())
            query_text = event.text.strip() if event.text else ""

            perc = random_func(sender_id, unix_epoch)
            thumb = InputWebDocument(
                        url='https://raw.githubusercontent.com/idkravitz/BeamModeBot-assets/master/thumb.png',
                        size=0,
                        mime_type='image/png',
                        attributes=[DocumentAttributeImageSize(w=320, h=320)]
                    )
            buttons = [[Button.switch_inline('Share your beam mode!', query='')]]
            await event.answer([
                builder.article(
                    title=('How Beam Mode I am?' if query_text == "" else f"How Beam Mode is {query_text}"), 
                    text=(f'I am at {perc}% beam mode' if query_text == "" else f'{query_text} is at {perc}% beam mode'),
                    description="Send your current Beam Mode to this chat.",
                    thumb=thumb,
                    buttons=buttons
                ),
                builder.article(
                    title='HALP!',
                    text="Press the 1st (top) button, you retard",
                    description="Send the usage guideliness to this chat.",
                    thumb = thumb,
                    buttons=buttons
                )
            ])

        await bot.run_until_disconnected()


def main():
    """Synchronous entry point for the bot (used by Poetry's entry point)."""
    asyncio.run(_main_async())


if __name__ == "__main__":
    main()

