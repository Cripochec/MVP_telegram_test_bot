import logging
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update

from config import BOT_TOKEN
from migrate import migrate
from handlers import start, admin, text, buttons, fsm, errors
from middlewares import role

WEBHOOK_PATH = "/webhook"
WEBHOOK_HOST = "https://cripochec.ru"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

async def on_startup(bot: Bot):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(bot: Bot):
    await bot.delete_webhook()

async def handle_webhook(request: web.Request):
    data = await request.json()
    update = Update.model_validate(data)
    await request.app["dp"].feed_update(request.app["bot"], update)
    return web.Response(text="ok")

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    migrate()

    dp.message.middleware(role.RoleMiddleware())
    dp.callback_query.middleware(role.RoleMiddleware())

    dp.include_router(start.router)
    dp.include_router(admin.router)
    dp.include_router(buttons.router)
    dp.include_router(fsm.router)
    dp.include_router(text.router)
    dp.errors.register(errors.global_error_handler)

    app = web.Application()
    app["bot"] = bot
    app["dp"] = dp
    app.router.add_post(WEBHOOK_PATH, handle_webhook)

    await on_startup(bot)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
