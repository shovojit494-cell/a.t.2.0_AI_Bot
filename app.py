import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import settings
from handlers.start import start
from handlers.callbacks import button_router
from handlers.messages import message_router

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("animation_tach_bot")

async def error_handler(update: object, context) -> None:
    logger.exception("Unhandled exception", exc_info=context.error)
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text("দুঃখিত, এই মুহূর্তে কাজটি সম্পন্ন করা যাচ্ছে না। আবার চেষ্টা করুন।")
        except Exception:
            pass

def build_app():
    app = Application.builder().token(settings.bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CallbackQueryHandler(button_router))
    app.add_handler(MessageHandler(filters.ALL, message_router))
    app.add_error_handler(error_handler)
    return app

def main():
    app = build_app()
    logger.info("Animation_Tach AI Bot starting in polling mode")
    app.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
        close_loop=False,
    )

if __name__ == "__main__":
    main()
