import asyncio
from bot_conf import dp,bot
from handlers.complaint_dialog import complaint_router
from handlers.start import start_router
from bot_conf import database

async def startup(bot):
    database.create_table()

async def main():
    dp.include_routers(start_router,complaint_router)
    dp.startup.register(startup)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())