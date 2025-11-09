from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
from bot.handlers import (
    start_command,
    handle_menu_selection,
    handle_pdf,
    handle_image,
    done_command,
    handle_format_choice,
    handle_restart,
    handle_page_selection,
    handle_page_input
)
from config import BOT_TOKEN
import logging

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot"""
    
    logger.info("🤖 Bot starting...")
    print("🤖 Bot starting...")
    
    # Build application with increased timeouts
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .read_timeout(30)
        .write_timeout(30)
        .connect_timeout(10)
        .pool_timeout(10)
        .build()
    )
    
    # Command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('done', done_command))
    
    # Restart button handler
    app.add_handler(MessageHandler(
        filters.Regex("^🔄 Start New Conversion$"),
        handle_restart
    ))
    
    # Menu selection handler
    app.add_handler(MessageHandler(
        filters.Regex("^(📄 PDF to Images|🖼️ Images to PDF|🎨 Change Image Format)$"),
        handle_menu_selection
    ))
    
    # Page selection handlers
    app.add_handler(MessageHandler(
        filters.Regex("^(📄 All Pages|🎯 Page Range \\(e\\.g\\., 3-15\\)|🔢 Specific Pages \\(e\\.g\\., 3,7,8,15\\))$"),
        handle_page_selection
    ))
    
    # Page input handler
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_page_input
    ))
    
    # PDF handler
    app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))
    
    # Image handler
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    
    # Format choice handler
    app.add_handler(MessageHandler(
        filters.Regex("^(PNG|JPG|WebP|BMP|GIF|TIFF)$"),
        handle_format_choice
    ))
    
    # Start polling
    logger.info("🟢 Bot is running!")
    print("🟢 Bot is running!", flush=True)
    
    # PythonAnywhere-friendly polling
    app.run_polling(
        poll_interval=3,
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True
    )

if __name__ == '__main__':
    main()
