import os
import logging
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton
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

# تهيئة التسجيل
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# تعريف حالات المحادثة
(
    CHOOSE_ACTION,
    BUY_NAME, BUY_PHONE, BUY_CITY, BUY_AMOUNT, BUY_PAYMENT, BUY_WALLET, BUY_NETWORK,
    SELL_NAME, SELL_PHONE, SELL_CITY, SELL_AMOUNT, SELL_PAYMENT, SELL_NETWORK
) = range(13)

# تفاصيل الدفع
PAYMENT_DETAILS = {
    "شام كاش": "العنوان: be456e0ea9392db4d68a7093ee317bc8\nالحساب: 5991161126028260",
    "سيريتل كاش": "الرقم: 0934598967",
    "حوالة الفؤاد": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية",
    "حوالة الهرم": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية",
    "بنك البركة": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية",
    "البنك الاسلامي": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية"
}

# عناوين الشبكات
NETWORK_ADDRESSES = {
    "bep20": "0x21802218d8d661d66F2C7959347a6382E1cc614F",
    "trc20": "TD2LoErPRkVPBxDk72ZErtiyi6agirZQjX",
    "erc20": "0x21802218d8d661d66F2C7959347a6382E1cc614F",
    "ton": "يرجى استخدام العنوان المخصص لتون",
    "sol": "يرجى استخدام العنوان المخصص لسولانا",
    "avax": "يرجى استخدام العنوان المخصص لأفالانش"
}

# توكن البوت ورقم الدردشة
TOKEN = os.getenv("TOKEN", "7521799915:AAEQEM_Ajk5_hMWQUrlmvdNbDBJAUMMwgrg")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "910021564")

# بدء المحادثة
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"بدأ المستخدم {user.id} المحادثة")
    
    keyboard = [["شراء USDT", "بيع USDT"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        "مرحباً! ماذا يمكن لهذا البوت فعله؟\n"
        "شراء وبيع USDT عن طريق وسائل الدفع المتاحة في سوريا\n"
        "عمولة التحويل: 0.05% من المبلغ الكامل",
        reply_markup=reply_markup
    )
    
    return CHOOSE_ACTION

# اختيار العملية
async def choose_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    context.user_data['action'] = text
    
    await update.message.reply_text(
        "الرجاء إدخال الاسم الثلاثي:",
        reply_markup=ReplyKeyboardRemove()
    )
    
    return BUY_NAME if "شراء" in text else SELL_NAME

# معالجة عملية الشراء
async def buy_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['name'] = update.message.text
    await update.message.reply_text("الرجاء إدخال رقم الهاتف:")
    return BUY_PHONE

async def buy_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("الرجاء إدخال المدينة:")
    return BUY_CITY

async def buy_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['city'] = update.message.text
    await update.message.reply_text("الرجاء إدخال الكمية المطلوبة (USDT):")
    return BUY_AMOUNT

async def buy_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['amount'] = update.message.text
    
    keyboard = [[method] for method in PAYMENT_DETAILS.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        "اختر طريقة الدفع:",
        reply_markup=reply_markup
    )
    return BUY_PAYMENT

async def buy_payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    payment = update.message.text
    context.user_data['payment'] = payment
    
    await update.message.reply_text(
        f"تفاصيل الدفع لـ {payment}:\n{PAYMENT_DETAILS[payment]}"
    )
    await update.message.reply_text("الرجاء إدخال عنوان محفظة USDT:")
    return BUY_WALLET

async def buy_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['wallet'] = update.message.text
    
    keyboard = [["bep20", "trc20", "erc20"], ["ton", "sol", "avax"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        "اختر شبكة التحويل:",
        reply_markup=reply_markup
    )
    return BUY_NETWORK

async def buy_network(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    network = update.message.text
    context.user_data['network'] = network
    
    # حساب العمولة
    try:
        amount = float(context.user_data['amount'])
        fee = amount * 0.0005
        total = amount + fee
        fee_msg = f"العمولة: {fee:.2f} USDT\nالمجموع: {total:.2f} USDT"
    except:
        fee_msg = "حساب العمولة فشل"
    
    # إعداد تفاصيل الطلب
    order_details = (
        "✅ طلب شراء جديد\n"
        f"الاسم: {context.user_data['name']}\n"
        f"الهاتف: {context.user_data['phone']}\n"
        f"المدينة: {context.user_data['city']}\n"
        f"الكمية: {context.user_data['amount']} USDT\n"
        f"طريقة الدفع: {context.user_data['payment']}\n"
        f"عنوان المحفظة: {context.user_data['wallet']}\n"
        f"الشبكة: {network}\n"
        f"{fee_msg}"
    )
    
    # إرسال التأكيد للمستخدم
    await update.message.reply_text(
        f"تم استلام طلبك بنجاح!\n\n{order_details}",
        reply_markup=ReplyKeyboardRemove()
    )
    
    # إرسال الطلب للمسؤول
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=order_details)
    
    return ConversationHandler.END

# معالجة عملية البيع
async def sell_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['name'] = update.message.text
    await update.message.reply_text("الرجاء إدخال رقم الهاتف:")
    return SELL_PHONE

async def sell_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("الرجاء إدخال المدينة:")
    return SELL_CITY

async def sell_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['city'] = update.message.text
    await update.message.reply_text("الرجاء إدخال الكمية المراد بيعها (USDT):")
    return SELL_AMOUNT

async def sell_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['amount'] = update.message.text
    
    keyboard = [[method] for method in list(PAYMENT_DETAILS.keys())[:4]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        "اختر طريقة الاستلام:",
        reply_markup=reply_markup
    )
    return SELL_PAYMENT

async def sell_payment(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    payment = update.message.text
    context.user_data['payment'] = payment
    
    # طلب تأكيد حسب طريقة الدفع
    if payment == "شام كاش":
        await update.message.reply_text("الرجاء إدخال عنوان شام كاش أو رقم الحساب:")
    else:
        await update.message.reply_text("الرجاء تأكيد رقم هاتفك:")
    return SELL_NETWORK

async def sell_network(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['payment_details'] = update.message.text
    
    keyboard = [["bep20", "trc20", "erc20"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    await update.message.reply_text(
        "اختر شبكة التحويل:",
        reply_markup=reply_markup
    )
    return ConversationHandler.END

async def sell_network_final(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    network = update.message.text
    context.user_data['network'] = network
    address = NETWORK_ADDRESSES.get(network, "العنوان غير متوفر")
    
    # إعداد تفاصيل الطلب
    order_details = (
        "✅ طلب بيع جديد\n"
        f"الاسم: {context.user_data['name']}\n"
        f"الهاتف: {context.user_data['phone']}\n"
        f"المدينة: {context.user_data['city']}\n"
        f"الكمية: {context.user_data['amount']} USDT\n"
        f"طريقة الاستلام: {context.user_data['payment']}\n"
        f"تفاصيل الدفع: {context.user_data.get('payment_details', '')}\n"
        f"الشبكة: {network}"
    )
    
    # إرسال التأكيد للمستخدم
    await update.message.reply_text(
        f"تم استلام طلبك بنجاح!\n\n"
        f"يرجى إرسال {context.user_data['amount']} USDT إلى العنوان التالي:\n"
        f"{address}\n"
        f"على شبكة {network}",
        reply_markup=ReplyKeyboardRemove()
    )
    
    # إرسال الطلب للمسؤول
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=order_details)
    
    return ConversationHandler.END

# إلغاء المحادثة
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "تم إلغاء العملية",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def main() -> None:
    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()
    
    # تعريف معالج المحادثة
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSE_ACTION: [
                MessageHandler(
                    filters.Regex(r"^(شراء USDT|بيع USDT)$"), choose_action
                )
            ],
            BUY_NAME: [MessageHandler(filters.TEXT, buy_name)],
            BUY_PHONE: [MessageHandler(filters.TEXT, buy_phone)],
            BUY_CITY: [MessageHandler(filters.TEXT, buy_city)],
            BUY_AMOUNT: [MessageHandler(filters.TEXT, buy_amount)],
            BUY_PAYMENT: [
                MessageHandler(
                    filters.Regex(r"^({})$".format("|".join(PAYMENT_DETAILS.keys()))),
                    buy_payment
                )
            ],
            BUY_WALLET: [MessageHandler(filters.TEXT, buy_wallet)],
            BUY_NETWORK: [
                MessageHandler(
                    filters.Regex(r"^(bep20|trc20|erc20|ton|sol|avax)$"),
                    buy_network
                )
            ],
            SELL_NAME: [MessageHandler(filters.TEXT, sell_name)],
            SELL_PHONE: [MessageHandler(filters.TEXT, sell_phone)],
            SELL_CITY: [MessageHandler(filters.TEXT, sell_city)],
            SELL_AMOUNT: [MessageHandler(filters.TEXT, sell_amount)],
            SELL_PAYMENT: [
                MessageHandler(
                    filters.Regex(r"^(شام كاش|سيريتل كاش|حوالة الفؤاد|حوالة الهرم)$"),
                    sell_payment
                )
            ],
            SELL_NETWORK: [MessageHandler(filters.TEXT, sell_network_final)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
