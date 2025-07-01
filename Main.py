import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackContext
)

# توكن البوت الخاص بك
TOKEN = os.getenv('TELEGRAM_TOKEN', '7521799915:AAEQEM_Ajk5_hMWQUrlmvdNbDBJAUMMwgrg')
# معرف الدردشة الخاص بك
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID', '910021564')

# تعريف مراحل المحادثة
SELECTING_ACTION, BUYING_USDT, SELLING_USDT = range(3)
# تعريف خطوات الشراء
GET_FULL_NAME, GET_PHONE, GET_CITY, GET_AMOUNT, GET_PAYMENT_METHOD, GET_WALLET, GET_NETWORK = range(7)

# وسائل الدفع للشراء
BUY_PAYMENT_METHODS = [
    "شام كاش",
    "سيريتل كاش",
    "حوالة الفؤاد",
    "حوالة الهرم",
    "بنك البركة",
    "البنك الاسلامي"
]

# وسائل الدفع للبيع
SELL_PAYMENT_METHODS = [
    "حوالة هرم",
    "حوالة الفؤاد",
    "سيريتل كاش",
    "شام كاش"
]

# عناوين الشبكات
NETWORK_ADDRESSES = {
    "bep20": "0x21802218d8d661d66F2C7959347a6382E1cc614F",
    "trc20": "TD2LoErPRkVPBxBk72ZErtiyi6agirZQjX",
    "erc20": "0x21802218d8d661d66F2C7959347a6382E1cc614F",
    "ton": "شبكة TON (أرسل العنوان)",
    "sol": "شبكة Solana (أرسل العنوان)",
    "avax": "شبكة Avalanche (أرسل العنوان)"
}

# تفاصيل وسائل الدفع
PAYMENT_DETAILS = {
    "شام كاش": "العنوان: be456e0ea9392db4d68a7093ee317bc8\nالحساب: 5991161126028260",
    "سيريتل كاش": "الرقم: 0934598967",
    "حوالة الفؤاد": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية",
    "حوالة الهرم": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية",
    "بنك البركة": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية",
    "البنك الاسلامي": "الاسم: علي ابراهيم محمود\nالرقم: 0934598967\nالمدينة: اللاذقية"
}

# تفعيل اللوغ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [InlineKeyboardButton("🛒 شراء USDT", callback_data='buy')],
        [InlineKeyboardButton("💰 بيع USDT", callback_data='sell')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "مرحباً! ماذا يمكن لهذا البوت فعله؟\n\n"
        "• شراء وبيع USDT\n"
        "• وسائل دفع متاحة في سوريا\n"
        "• عمولة التحويل 0.05% من المبلغ الكامل",
        reply_markup=reply_markup
    )
    return SELECTING_ACTION

async def handle_action(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    
    if query.data == 'buy':
        context.user_data['action'] = 'buy'
        await query.edit_message_text("📝 الرجاء إرسال اسمك الثلاثي:")
        return GET_FULL_NAME
        
    elif query.data == 'sell':
        context.user_data['action'] = 'sell'
        await query.edit_message_text("📝 الرجاء إرسال اسمك الثلاثي:")
        return GET_FULL_NAME
        
    return ConversationHandler.END

async def get_full_name(update: Update, context: CallbackContext) -> int:
    context.user_data['full_name'] = update.message.text
    await update.message.reply_text("📱 الرجاء إرسال رقم هاتفك:")
    return GET_PHONE

async def get_phone(update: Update, context: CallbackContext) -> int:
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("🏙️ الرجاء إرسال مدينتك:")
    return GET_CITY

async def get_city(update: Update, context: CallbackContext) -> int:
    context.user_data['city'] = update.message.text
    
    if context.user_data['action'] == 'buy':
        await update.message.reply_text("💵 الرجاء إرسال كمية USDT المطلوبة:")
        return GET_AMOUNT
    else:
        await update.message.reply_text("💵 الرجاء إرسال كمية USDT التي تريد بيعها:")
        return GET_AMOUNT

async def get_amount(update: Update, context: CallbackContext) -> int:
    try:
        amount = float(update.message.text)
        context.user_data['amount'] = amount
        
        # احتساب العمولة
        commission = amount * 0.0005
        context.user_data['commission'] = commission
        context.user_data['net_amount'] = amount - commission
        
        action = context.user_data['action']
        
        if action == 'buy':
            keyboard = [[InlineKeyboardButton(method, callback_data=method)] for method in BUY_PAYMENT_METHODS]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                "💳 اختر طريقة الدفع المناسبة:",
                reply_markup=reply_markup
            )
            return GET_PAYMENT_METHOD
            
        else:  # sell
            keyboard = [[InlineKeyboardButton(method, callback_data=method)] for method in SELL_PAYMENT_METHODS]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                "🏧 اختر طريقة استلام المبلغ:",
                reply_markup=reply_markup
            )
            return GET_PAYMENT_METHOD
            
    except ValueError:
        await update.message.reply_text("❌ الرجاء إدخال رقم صحيح. أرسل الكمية مرة أخرى:")
        return GET_AMOUNT

async def get_payment_method(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    
    context.user_data['payment_method'] = query.data
    await query.edit_message_text(f"✅ اخترت: {query.data}")
    
    if context.user_data['action'] == 'buy':
        await query.message.reply_text("🔗 الرجاء إرسال عنوان محفظة USDT:")
        return GET_WALLET
    else:
        # طلب تفاصيل إضافية للبيع
        if query.data == "شام كاش":
            await query.message.reply_text("📝 الرجاء إرسال عنوان شام كاش أو رقم الحساب:")
        else:
            await query.message.reply_text("📱 الرجاء تأكيد رقم هاتفك:")
        return GET_WALLET

async def get_wallet(update: Update, context: CallbackContext) -> int:
    context.user_data['wallet_or_confirm'] = update.message.text
    
    keyboard = [[InlineKeyboardButton(network, callback_data=network)] for network in NETWORK_ADDRESSES]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if context.user_data['action'] == 'buy':
        await update.message.reply_text(
            "🌐 اختر شبكة التحويل:",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "🌐 اختر شبكة التحويل التي سترسل منها USDT:",
            reply_markup=reply_markup
        )
        
    return GET_NETWORK

async def get_network(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()
    
    network = query.data
    context.user_data['network'] = network
    
    # إرسال تفاصيل الطلب للمستخدم
    action = context.user_data['action']
    user_data = context.user_data
    
    if action == 'buy':
        message_text = (
            "✅ تم استلام طلب الشراء بنجاح!\n\n"
            f"👤 الاسم: {user_data['full_name']}\n"
            f"📱 الهاتف: {user_data['phone']}\n"
            f"🏙️ المدينة: {user_data['city']}\n"
            f"💵 الكمية: {user_data['amount']} USDT\n"
            f"💳 طريقة الدفع: {user_data['payment_method']}\n"
            f"🔗 المحفظة: {user_data.get('wallet_or_confirm', '')}\n"
            f"🌐 الشبكة: {network}\n\n"
            "سيتم معالجة طلبك خلال 24 ساعة."
        )
    else:
        message_text = (
            "✅ تم استلام طلب البيع بنجاح!\n\n"
            f"👤 الاسم: {user_data['full_name']}\n"
            f"📱 الهاتف: {user_data['phone']}\n"
            f"🏙️ المدينة: {user_data['city']}\n"
            f"💵 الكمية: {user_data['amount']} USDT\n"
            f"🏧 طريقة الاستلام: {user_data['payment_method']}\n"
            f"📝 تفاصيل التأكيد: {user_data.get('wallet_or_confirm', '')}\n"
            f"🌐 الشبكة: {network}\n\n"
            "سيتم معالجة طلبك خلال 24 ساعة."
        )
    
    await query.edit_message_text(message_text)
    
    # إرسال نفس الطلب للمدير
    admin_message = (
        f"📬 طلب جديد ({'شراء' if action == 'buy' else 'بيع'}):\n\n"
        f"👤 الاسم: {user_data['full_name']}\n"
        f"📱 الهاتف: {user_data['phone']}\n"
        f"🏙️ المدينة: {user_data['city']}\n"
        f"💵 الكمية: {user_data['amount']} USDT\n"
        f"💸 العمولة: {user_data['commission']:.4f} USDT\n"
        f"💰 الصافي: {user_data['net_amount']:.4f} USDT\n"
    )
    
    if action == 'buy':
        admin_message += (
            f"💳 طريقة الدفع: {user_data['payment_method']}\n"
            f"🔗 المحفظة: {user_data.get('wallet_or_confirm', '')}\n"
        )
    else:
        admin_message += (
            f"🏧 طريقة الاستلام: {user_data['payment_method']}\n"
            f"📝 تفاصيل التأكيد: {user_data.get('wallet_or_confirm', '')}\n"
        )
    
    admin_message += (
        f"🌐 الشبكة: {network}\n"
        f"👤 معرف المستخدم: {update.effective_user.id}"
    )
    
    # إرسال تفاصيل الدفع للمدير
    payment_details = PAYMENT_DETAILS.get(user_data['payment_method'], "لا توجد تفاصيل إضافية")
    admin_message += f"\n\n🔐 تفاصيل الدفع:\n{payment_details}"
    
    # إرسال عنوان الشبكة
    network_address = NETWORK_ADDRESSES.get(network, "لا يوجد عنوان محدد")
    admin_message += f"\n\n🌐 عنوان الشبكة:\n{network_address}"
    
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message)
    
    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('تم إلغاء العملية.')
    return ConversationHandler.END

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECTING_ACTION: [CallbackQueryHandler(handle_action)],
            GET_FULL_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_full_name)],
            GET_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            GET_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)],
            GET_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_amount)],
            GET_PAYMENT_METHOD: [CallbackQueryHandler(get_payment_method)],
            GET_WALLET: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_wallet)],
            GET_NETWORK: [CallbackQueryHandler(get_network)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    application.add_handler(conv_handler)
    
    # تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
