import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler
)

# إعدادات البوت
TOKEN = "7521799915:AAEQEM_Ajk5_hMWQUrlmvdNbDBJAUMMwgrg"
ADMIN_CHAT_ID = 910021564

# مراحل المحادثة
CHOOSING_TRANSACTION, BUY_DATA, SELL_DATA, PAYMENT_METHOD, RECEIVE_METHOD, NETWORK_CHOICE = range(6)

# خيارات الدفع
PAYMENT_METHODS = {
    "شام كاش": {
        "details": "العنوان: be456e0ea9392db4d68a7093ee317bc8\nالحساب: 5991161126028260"
    },
    "سيريتل كاش": {
        "details": "الرقم: 0934598967"
    },
    "حوالة الفؤاد": {
        "details": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية"
    },
    "حوالة الهرم": {
        "details": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية"
    },
    "بنك البركة": {
        "details": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية"
    },
    "البنك الاسلامي": {
        "details": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية"
    }
}

# عناوين الشبكات
NETWORK_ADDRESSES = {
    "bep20": "0x21802218d8d661d66F2C7959347a6382E1cc614F",
    "trc20": "TD2LoErPRkVPBxDk72ZErtiyi6agirZQjX",
    "erc20": "0x21802218d8d661d66F2C7959347a6382E1cc614F",
    "ton": "اختيار TON",
    "sol": "اختيار SOL",
    "avax": "اختيار AVAX"
}

# تفاصيل المستخدم
user_data = {}

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# أوامر البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"User {user.first_name} started the conversation.")
    
    keyboard = [
        [InlineKeyboardButton("شراء USDT", callback_data='buy')],
        [InlineKeyboardButton("بيع USDT", callback_data='sell')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "مرحباً! ماذا يمكن لهذا البوت فعله؟\n"
        "شراء وبيع USDT عن طريق وسائل الدفع المتاحة في سوريا\n"
        "عمولة التحويل 0.05% من المبلغ الكامل\n"
        "الرجاء اختيار نوع المعاملة:",
        reply_markup=reply_markup
    )
    
    return CHOOSING_TRANSACTION

async def transaction_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    user_data[query.from_user.id] = {'transaction_type': query.data}
    
    if query.data == 'buy':
        await query.edit_message_text("لقد اخترت عملية شراء USDT\nالرجاء إرسال اسمك الثلاثي:")
        return BUY_DATA
    else:
        await query.edit_message_text("لقد اخترت عملية بيع USDT\nالرجاء إرسال اسمك الثلاثي:")
        return SELL_DATA

# معالجة بيانات الشراء
async def buy_full_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['full_name'] = update.message.text
    
    await update.message.reply_text("الرجاء إرسال رقم هاتفك:")
    return BUY_DATA

async def buy_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['phone'] = update.message.text
    
    await update.message.reply_text("الرجاء إرسال مدينتك:")
    return BUY_DATA

async def buy_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['city'] = update.message.text
    
    await update.message.reply_text("الرجاء إرسال كمية USDT المطلوبة:")
    return BUY_DATA

async def buy_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['amount'] = update.message.text
    
    keyboard = [[KeyboardButton(method)] for method in PAYMENT_METHODS.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text(
        "الرجاء اختيار طريقة الدفع المناسبة:",
        reply_markup=reply_markup
    )
    return PAYMENT_METHOD

async def buy_payment_method(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    method = update.message.text
    
    if method not in PAYMENT_METHODS:
        await update.message.reply_text("طريقة دفع غير صالحة، الرجاء الاختيار من القائمة.")
        return PAYMENT_METHOD
    
    user_data[user_id]['payment_method'] = method
    user_data[user_id]['payment_details'] = PAYMENT_METHODS[method]["details"]
    
    keyboard = [[KeyboardButton(network)] for network in NETWORK_ADDRESSES.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text(
        "الرجاء اختيار عنوان الشبكة:",
        reply_markup=reply_markup
    )
    return NETWORK_CHOICE

# معالجة بيانات البيع
async def sell_full_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['full_name'] = update.message.text
    
    await update.message.reply_text("الرجاء إرسال رقم هاتفك:")
    return SELL_DATA

async def sell_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['phone'] = update.message.text
    
    await update.message.reply_text("الرجاء إرسال مدينتك:")
    return SELL_DATA

async def sell_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['city'] = update.message.text
    
    await update.message.reply_text("الرجاء إرسال كمية USDT التي تريد بيعها:")
    return SELL_DATA

async def sell_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['amount'] = update.message.text
    
    keyboard = [[KeyboardButton(method)] for method in list(PAYMENT_METHODS.keys())[:4]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text(
        "الرجاء اختيار طريقة استلام المبلغ:",
        reply_markup=reply_markup
    )
    return RECEIVE_METHOD

async def sell_receive_method(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    method = update.message.text
    
    if method not in PAYMENT_METHODS:
        await update.message.reply_text("طريقة غير صالحة، الرجاء الاختيار من القائمة.")
        return RECEIVE_METHOD
    
    user_data[user_id]['receive_method'] = method
    
    if method == "شام كاش":
        await update.message.reply_text("الرجاء إرسال عنوان شام كاش أو رقم الحساب:")
        return SELL_DATA
    else:
        await update.message.reply_text("الرجاء تأكيد رقم هاتفك:")
        return SELL_DATA

async def sell_payment_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    method = user_data[user_id]['receive_method']
    
    if method == "شام كاش":
        user_data[user_id]['receive_details'] = update.message.text
    else:
        user_data[user_id]['receive_details'] = f"رقم الهاتف: {update.message.text}"
    
    keyboard = [[KeyboardButton(network)] for network in ["bep20", "trc20", "erc20"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text(
        "الرجاء اختيار شبكة الإرسال:",
        reply_markup=reply_markup
    )
    return NETWORK_CHOICE

# معالجة اختيار الشبكة
async def network_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.message.from_user.id
    network = update.message.text.lower()
    
    if network not in NETWORK_ADDRESSES:
        await update.message.reply_text("شبكة غير صالحة، الرجاء الاختيار من القائمة.")
        return NETWORK_CHOICE
    
    user_data[user_id]['network'] = network
    user_data[user_id]['wallet_address'] = NETWORK_ADDRESSES[network]
    
    # إرسال تأكيد للمستخدم
    transaction_type = user_data[user_id]['transaction_type']
    
    if transaction_type == 'buy':
        message_text = (
            "✅ تم استلام طلبك بنجاح!\n"
            f"الاسم: {user_data[user_id]['full_name']}\n"
            f"الهاتف: {user_data[user_id]['phone']}\n"
            f"المدينة: {user_data[user_id]['city']}\n"
            f"الكمية: {user_data[user_id]['amount']} USDT\n"
            f"طريقة الدفع: {user_data[user_id]['payment_method']}\n"
            f"تفاصيل الدفع:\n{user_data[user_id]['payment_details']}\n"
            f"العنوان: {user_data[user_id]['wallet_address']}\n"
            f"الشبكة: {network.upper()}"
        )
    else:
        message_text = (
            "✅ تم استلام طلبك بنجاح!\n"
            f"الاسم: {user_data[user_id]['full_name']}\n"
            f"الهاتف: {user_data[user_id]['phone']}\n"
            f"المدينة: {user_data[user_id]['city']}\n"
            f"الكمية: {user_data[user_id]['amount']} USDT\n"
            f"طريقة الاستلام: {user_data[user_id]['receive_method']}\n"
            f"تفاصيل الاستلام: {user_data[user_id].get('receive_details', '')}\n"
            f"عنوان الإرسال: {user_data[user_id]['wallet_address']}\n"
            f"الشبكة: {network.upper()}"
        )
    
    await update.message.reply_text(message_text)
    
    # إرسال التفاصيل إلى المسؤول
    admin_message = f"📬 طلب جديد!\n{message_text}\n\nUser ID: {user_id}"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message)
    
    return ConversationHandler.END

# إلغاء المحادثة
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('تم إلغاء العملية.')
    return ConversationHandler.END

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING_TRANSACTION: [CallbackQueryHandler(transaction_choice)],
            BUY_DATA: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, buy_full_name),
                MessageHandler(filters.TEXT & ~filters.COMMAND, buy_phone),
                MessageHandler(filters.TEXT & ~filters.COMMAND, buy_city),
                MessageHandler(filters.TEXT & ~filters.COMMAND, buy_amount),
            ],
            SELL_DATA: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, sell_full_name),
                MessageHandler(filters.TEXT & ~filters.COMMAND, sell_phone),
                MessageHandler(filters.TEXT & ~filters.COMMAND, sell_city),
                MessageHandler(filters.TEXT & ~filters.COMMAND, sell_amount),
            ],
            PAYMENT_METHOD: [MessageHandler(filters.TEXT & ~filters.COMMAND, buy_payment_method)],
            RECEIVE_METHOD: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, sell_receive_method),
                MessageHandler(filters.TEXT & ~filters.COMMAND, sell_payment_confirmation)
            ],
            NETWORK_CHOICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, network_choice)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()