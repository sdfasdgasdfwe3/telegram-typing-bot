import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.channels import CreateChannelRequest

# Получаем конфигурацию из файла .env
from dotenv import load_dotenv
load_dotenv()

API_ID = 'ваш_api_id'
API_HASH = 'ваш_api_hash'
PHONE_NUMBER = 'ваш_номер_телефона'

client = TelegramClient('sessions', API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r'/p (.+)', func=lambda e: True))
async def animated_typing(event):
    text = event.pattern_match.group(1)
    await event.edit('▮')
    typed_text = ''
    for char in text:
        typed_text += char
        await event.edit(typed_text + '▮')
        await asyncio.sleep(0.1)
    await event.edit(typed_text)

async def main():
    await client.start(phone=PHONE_NUMBER)
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
