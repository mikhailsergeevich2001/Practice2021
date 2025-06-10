from telethon.sync import TelegramClient

api_id = 123456  # Ваш api_id из my.telegram.org
api_hash = 'your_api_hash_here'  # Ваш api_hash
phone = '+1234567890'  # Ваш номер телефона

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)
    if await client.is_user_authorized():
        me = await client.get_me()
        print(f"Авторизован как {me.first_name} ({me.phone})")

with client:
    client.loop.run_until_complete(main())