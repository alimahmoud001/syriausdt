            color: var(--dark-color);
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>شام كاش - بيع وشراء USDT</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --success-color: #27ae60;
            --warning-color: #f39c12;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f5f7fa;
            color: var(--dark-color);
            line-height: 1.6;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            font-size: 28px;
            margin-bottom: 10px;
        }
        
        .description {
            font-size: 16px;
            margin-bottom: 15px;
        }
        
        .requirement {
            background-color: var(--warning-color);
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
            font-weight: bold;
        }
        
        .requirement a {
            color: white;
            text-decoration: underline;
        }
        
        .tabs {
            display: flex;
            margin-bottom: 20px;
            background-color: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .tab {
            flex: 1;
            padding: 15px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
        }
        
        .tab.active {
            background-color: var(--secondary-color);
            color: white;
        }
        
        .tab-content {
            display: none;
            background-color: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        
        input, select {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
        }
        
        button {
            background-color: var(--secondary-color);
            color: white;
            border: none;
            padding: 15px;
            border-radius: 6px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        
        button:hover {
            background-color: var(--primary-color);
        }
        
        .result {
            margin-top: 25px;
            padding: 20px;
            border-radius: 8px;
            background-color: var(--light-color);
            display: none;
        }
        
        .commission-notice {
            background-color: var(--light-color);
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
            font-size: 14px;
        }
        
        .info-box {
            background-color: #e8f4fc;
            border-right: 4px solid var(--secondary-color);
            padding: 15px;
            margin: 15px 0;
            border-radius: 6px;
        }
        
        .warning-box {
            background-color: #fde9e7;
            border-right: 4px solid var(--accent-color);
            padding: 15px;
            margin: 15px 0;
            border-radius: 6px;
            font-size: 14px;
        }
        
        .instructions {
            margin-top: 30px;
            padding: 20px;
            background-color: var(--light-color);
            border-radius: 10px;
        }
        
        .instructions h3 {
            margin-bottom: 15px;
            color: var(--primary-color);
        }
        
        .instructions ol {
            padding-right: 20px;
            margin-bottom: 15px;
        }
        
        .instructions li {
            margin-bottom: 10px;
        }
        
        footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: var(--dark-color);
            font-size: 14px;
        }
        
        @media (max-width: 600px) {
            .tabs {
                flex-direction: column;
            }
            
            .container {
                padding: 15px;
            }
            
            header {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>شام كاش - بيع وشراء USDT</h1>
            <p class="description">خدمة آمنة وسريعة لبيع وشراء العملات الرقمية</p>
        </header>
        
        <div class="requirement">
            ⚠️ يجب الانضمام إلى <a href="https://t.me/shamcashusdt1" target="_blank">قناة التلجرام</a> أولاً لاستخدام الخدمة
        </div>
        
        <div class="tabs">
            <div class="tab active" data-tab="buy">شراء USDT</div>
            <div class="tab" data-tab="sell">بيع USDT</div>
        </div>
        
        <div class="tab-content active" id="buy-content">
            <h2>شراء USDT</h2>
            <div class="info-box">
                <p>لشراء USDT، يرجى تعبئة المعلومات التالية:</p>
            </div>
            
            <form id="buy-form">
                <div class="form-group">
                    <label for="buy-amount">المبلغ الذي تريد شراءه (USDT)</label>
                    <input type="number" id="buy-amount" placeholder="أدخل المبلغ بالUSDT" required>
                </div>
                
                <div class="form-group">
                    <label for="network">عنوان الشبكة (BEP20 فقط)</label>
                    <input type="text" id="network" placeholder="أدعنوان محفظتك BEP20" required>
                </div>
                
                <div class="form-group">
                    <label for="currency">طريقة الدفع</label>
                    <select id="currency" required>
                        <option value="">اختر طريقة الدفع</option>
                        <option value="syp">الليرة السورية</option>
                        <option value="usd">الدولار الأمريكي</option>
                    </select>
                </div>
                
                <div class="commission-notice">
                    العمولة: 1$ + 0.5% من المبلغ الإجمالي
                </div>
                
                <button type="submit">متابعة الطلب</button>
            </form>
            
            <div class="result" id="buy-result">
                <h3>تفاصيل طلبك:</h3>
                <p>المبلغ: <span id="result-amount"></span> USDT</p>
                <p>طريقة الدفع: <span id="result-currency"></span></p>
                <p>العمولة: <span id="result-commission"></span></p>
                <p>المبلغ الإجمالي: <span id="result-total"></span></p>
                
                <div class="warning-box">
                    <p>⏳ سوف يتم اعتماد سعر صرف الدولار كما هو سعر الصرف في البنك المركزي</p>
                    <p>💵 عنوان شام كاش: be456e0ea9392db4d68a7093ee317bc8</p>
                    <p>📸 يرجى إرسال صورة screenshot للتحويل إلى الدعم على Telegram: <a href="https://t.me/ali0619000" target="_blank">@ali0619000</a></p>
                    <p>📢 سيتم إرسال جميع معلومات الطلب إلى <a href="https://t.me/shamcashusdt1" target="_blank">مجموعة التلجرام</a></p>
                </div>
            </div>
        </div>
        
        <div class="tab-content" id="sell-content">
            <h2>بيع USDT</h2>
            <div class="info-box">
                <p>لبيع USDT، يرجى تعبئة المعلومات التالية:</p>
            </div>
            
            <form id="sell-form">
                <div class="form-group">
                    <label for="sell-amount">المبلغ الذي تريد بيعه (USDT)</label>
                    <input type="number" id="sell-amount" placeholder="أدخل المبلغ بالUSDT" required>
                </div>
                
                <div class="form-group">
                    <label for="shamcash-address">عنوان شام كاش الخاص بك</label>
                    <input type="text" id="shamcash-address" placeholder="أدخل عنوان شام كاش الخاص بك" required>
                </div>
                
                <div class="form-group">
                    <label for="receive-currency">طريقة الاستلام</label>
                    <select id="receive-currency" required>
                        <option value="">اختر طريقة الاستلام</option>
                        <option value="syp">الليرة السورية</option>
                        <option value="usd">الدولار الأمريكي</option>
                    </select>
                </div>
                
                <div class="commission-notice">
                    العمولة: 1$ + 0.5% من المبلغ الإجمالي
                </div>
                
                <button type="submit">متابعة الطلب</button>
            </form>
            
            <div class="result" id="sell-result">
                <h3>تفاصيل طلبك:</h3>
                <p>المبلغ: <span id="sell-result-amount"></span> USDT</p>
                <p>طريقة الاستلام: <span id="sell-result-currency"></span></p>
                <p>العمولة: <span id="sell-result-commission"></span></p>
                <p>المبلغ الإجمالي: <span id="sell-result-total"></span></p>
                
                <div class="warning-box">
                    <p>⏳ سوف يتم اعتماد سعر صرف الدولار كما هو سعر الصرف في البنك المركزي</p>
                    <p>💵 عنوان USDT BEP20: 0x2F1A184B6abBb49De547D539eDC3b5eAdc3E01F9</p>
                    <p>📸 يرجى إرسال صورة screenshot للتحويل إلى الدعم على Telegram: <a href="https://t.me/ali0619000" target="_blank">@ali0619000</a></p>
                    <p>📢 سيتم إرسال جميع معلومات الطلب إلى <a href="https://t.me/shamcashusdt1" target="_blank">مجموعة التلجرام</a></p>
                    <p>⏰ سوف يتم إرسال المبلغ خلال دقائق بعد التأكيد</p>
                </div>
            </div>
        </div>
        
        <div class="instructions">
            <h3>تعليمات مهمة:</h3>
            <ol>
                <li>يجب الانضمام إلى <a href="https://t.me/shamcashusdt1" target="_blank">قناة التلجرام</a> قبل استخدام الخدمة</li>
                <li>العمولة: 1$ + 0.5% من المبلغ الإجمالي</li>
                <li>يجب إرسال صورة screenshot للتحويل إلى الدعم على <a href="https://t.me/ali0619000" target="_blank">@ali0619000</a></li>
                <li>يتم اعتماد سعر صرف الدولار حسب سعر البنك المركزي</li>
                <li>جميع الطلبات يتم إرسالها إلى <a href="https://t.me/shamcashusdt1" target="_blank">مجموعة التلجرام</a></li>
            </ol>
            <p>للاستفسارات والدعم: <a href="https://t.me/ali0619000" target="_blank">@ali0619000</a></p>
        </div>
        
        <footer>
            <p>© 2023 شام كاش - جميع الحقوق محفوظة</p>
            <p>هذه الخدمة مقدمة من شام كاش</p>
        </footer>
    </div>

    <script>
        // تبديل التبويبات
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                
                tab.classList.add('active');
                document.getElementById(`${tab.dataset.tab}-content`).classList.add('active');
            });
        });
        
        // معالجة نموذج الشراء
        document.getElementById('buy-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const amount = parseFloat(document.getElementById('buy-amount').value);
            const currency = document.getElementById('currency').value;
            const network = document.getElementById('network').value;
            
            if (!amount || !currency || !network) {
                alert('يرجى ملء جميع الحقول');
                return;
            }
            
            // حساب العمولة
            const commission = 1 + (amount * 0.005);
            const total = amount - commission;
            
            // عرض النتيجة
            document.getElementById('result-amount').textContent = amount;
            document.getElementById('result-currency').textContent = currency === 'syp' ? 'الليرة السورية' : 'الدولار الأمريكي';
            document.getElementById('result-commission').textContent = commission.toFixed(2) + ' USDT';
            document.getElementById('result-total').textContent = total.toFixed(2) + ' USDT';
            
            document.getElementById('buy-result').style.display = 'block';
            
            // هنا يمكن إضافة كود لإرسال البيانات إلى الخادم
        });
        
        // معالجة نموذج البيع
        document.getElementById('sell-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const amount = parseFloat(document.getElementById('sell-amount').value);
            const shamcashAddress = document.getElementById('shamcash-address').value;
            const receiveCurrency = document.getElementById('receive-currency').value;
            
            if (!amount || !shamcashAddress || !receiveCurrency) {
                alert('يرجى ملء جميع الحقول');
                return;
            }
            
            // حساب العمولة
            const commission = 1 + (amount * 0.005);
            const total = amount - commission;
            
            // عرض النتيجة
            document.getElementById('sell-result-amount').textContent = amount;
            document.getElementById('sell-result-currency').textContent = receiveCurrency === 'syp' ? 'الليرة السورية' : 'الدولار الأمريكي';
            document.getElementById('sell-result-commission').textContent = commission.toFixed(2) + ' USDT';
            document.getElementById('sell-result-total').textContent = total.toFixed(2) + ' USDT';
            
            document.getElementById('sell-result').style.display = 'block';
            
            // هنا يمكن إضافة كود لإرسال البيانات إلى الخادم
        });
    </script>
</body>
</html>          line-height: 1.6;
        }
        
        .container {
            max-width: 100%;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background-color: var(--primary-color);
            color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .header h1 {
            font-size: 28px;
            margin-bottom: 10px;
        }
        
        .form-section {
            background-color: white;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        .form-section h2 {
            color: var(--primary-color);
            margin-bottom: 20px;
            font-size: 22px;
            border-bottom: 2px solid var(--light-color);
            padding-bottom: 10px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: var(--dark-color);
        }
        
        .form-control {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        .form-control:focus {
            border-color: var(--secondary-color);
            outline: none;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
        }
        
        select.form-control {
            appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
            background-repeat: no-repeat;
            background-position: right 10px center;
            background-size: 1em;
        }
        
        .btn {
            display: inline-block;
            padding: 12px 24px;
            background-color: var(--secondary-color);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            transition: background-color 0.3s;
            width: 100%;
        }
        
        .btn:hover {
            background-color: #2980b9;
        }
        
        .btn-primary {
            background-color: var(--secondary-color);
        }
        
        .btn-success {
            background-color: var(--success-color);
        }
        
        .btn-warning {
            background-color: var(--warning-color);
        }
        
        .hidden {
            display: none;
        }
        
        .payment-details {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 6px;
            margin-top: 15px;
            border-left: 4px solid var(--secondary-color);
        }
        
        .payment-details h3 {
            margin-bottom: 10px;
            color: var(--primary-color);
        }
        
        .copy-address {
            display: flex;
            align-items: center;
            background-color: white;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 8px;
            border: 1px solid #ddd;
        }
        
        .copy-address span {
            flex-grow: 1;
            word-break: break-all;
            font-family: monospace;
        }
        
        .copy-btn {
            background-color: var(--light-color);
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            margin-left: 10px;
            transition: background-color 0.3s;
        }
        
        .copy-btn:hover {
            background-color: #d5dbdb;
        }
        
        .summary {
            background-color: #e8f4fd;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
        }
        
        .summary h3 {
            color: var(--primary-color);
            margin-bottom: 15px;
        }
        
        .summary-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 1px solid #d6e9ff;
        }
        
        .summary-item:last-child {
            border-bottom: none;
            font-weight: bold;
            color: var(--primary-color);
        }
        
        .note {
            font-size: 14px;
            color: #7f8c8d;
            margin-top: 20px;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 4px;
            border-left: 3px solid var(--warning-color);
        }
        
        .success-message {
            text-align: center;
            padding: 30px;
            background-color: #e8f8f0;
            border-radius: 8px;
            margin-top: 20px;
            border: 1px solid #27ae60;
        }
        
        .success-message i {
            font-size: 50px;
            color: var(--success-color);
            margin-bottom: 20px;
        }
        
        .success-message h2 {
            color: var(--success-color);
            margin-bottom: 15px;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 24px;
            }
            
            .form-section {
                padding: 15px;
            }
        }
        
        /* RTL specific styles */
        [dir="rtl"] .copy-btn {
            margin-left: 0;
            margin-right: 10px;
        }
        
        [dir="rtl"] select.form-control {
            background-position: left 10px center;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-exchange-alt"></i> منصة تبادل USDT في سوريا</h1>
            <p>تحويل USDT بوسائل الدفع المتاحة في سوريا</p>
        </div>
        
        <form id="exchangeForm">
            <!-- Personal Information Section -->
            <div class="form-section">
                <h2><i class="fas fa-user"></i> المعلومات الشخصية</h2>
                <div class="form-group">
                    <label for="fullName">الاسم الثلاثي</label>
                    <input type="text" id="fullName" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="phoneNumber">رقم الهاتف</label>
                    <input type="tel" id="phoneNumber" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="city">المدينة</label>
                    <input type="text" id="city" class="form-control" required>
                </div>
            </div>
            
            <!-- Transaction Type Section -->
            <div class="form-section">
                <h2><i class="fas fa-exchange-alt"></i> نوع العملية</h2>
                <div class="form-group">
                    <label>ماذا تريد أن تفعل؟</label>
                    <div style="display: flex; gap: 10px;">
                        <button type="button" id="btnBuy" class="btn btn-primary">شراء USDT</button>
                        <button type="button" id="btnSell" class="btn btn-success">بيع USDT</button>
                    </div>
                </div>
            </div>
            
            <!-- Buy USDT Section -->
            <div id="buySection" class="form-section hidden">
                <h2><i class="fas fa-shopping-cart"></i> شراء USDT</h2>
                <div class="form-group">
                    <label for="buyAmount">الكمية المطلوبة (USDT)</label>
                    <input type="number" id="buyAmount" class="form-control" step="0.01" min="1">
                </div>
                <div class="form-group">
                    <label for="buyNetwork">اختر شبكة التحويل</label>
                    <select id="buyNetwork" class="form-control">
                        <option value="bep20">BEP20</option>
                        <option value="trc20">TRC20</option>
                        <option value="erc20">ERC20</option>
                        <option value="binance_pay">Binance Pay</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="buyWalletAddress">عنوان المحفظة (سيتم إرسال USDT إليه)</label>
                    <input type="text" id="buyWalletAddress" class="form-control">
                </div>
                <div class="form-group">
                    <label for="buyNotes">ملاحظات (اختياري)</label>
                    <textarea id="buyNotes" class="form-control" rows="3"></textarea>
                </div>
                <div class="form-group">
                    <label for="buyPaymentMethod">طريقة الدفع</label>
                    <select id="buyPaymentMethod" class="form-control">
                        <option value="">-- اختر طريقة الدفع --</option>
                        <option value="sham">شام كاش</option>
                        <option value="bemo">بنك بيمو</option>
                        <option value="syriatel">سيريتل كاش</option>
                        <option value="pyramid">حوالة هرم</option>
                    </select>
                </div>
                
                <!-- Payment Details (Shown based on selection) -->
                <div id="shamDetails" class="payment-details hidden">
                    <h3><i class="fas fa-info-circle"></i> تفاصيل الدفع عبر شام كاش</h3>
                    <div class="copy-address">
                        <span>عنواني هو: be456e0ea9392db4d68a7093ee317bc8</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('be456e0ea9392db4d68a7093ee317bc8')">نسخ</button>
                    </div>
                    <div class="copy-address">
                        <span>رقم الحساب: 5991161126028260</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('5991161126028260')">نسخ</button>
                    </div>
                </div>
                
                <div id="bemoDetails" class="payment-details hidden">
                    <h3><i class="fas fa-info-circle"></i> تفاصيل الدفع عبر بنك بيمو</h3>
                    <p>الاسم: علي ابراهيم محمود</p>
                    <div class="copy-address">
                        <span>رقم الحساب: 060104947910013000000</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('060104947910013000000')">نسخ</button>
                    </div>
                </div>
                
                <div id="syriatelDetails" class="payment-details hidden">
                    <h3><i class="fas fa-info-circle"></i> تفاصيل الدفع عبر سيريتل كاش</h3>
                    <div class="copy-address">
                        <span>رقم الهاتف: 0934598967</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('0934598967')">نسخ</button>
                    </div>
                </div>
                
                <div id="pyramidDetails" class="payment-details hidden">
                    <h3><i class="fas fa-info-circle"></i> تفاصيل الدفع عبر حوالة الهرم</h3>
                    <p>الاسم: علي ابراهيم محمود</p>
                    <div class="copy-address">
                        <span>رقم الهاتف: 0934598967</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('0934598967')">نسخ</button>
                    </div>
                    <p>المدينة: اللاذقية</p>
                </div>
            </div>
            
            <!-- Sell USDT Section -->
            <div id="sellSection" class="form-section hidden">
                <h2><i class="fas fa-money-bill-wave"></i> بيع USDT</h2>
                <div class="form-group">
                    <label for="sellAmount">الكمية المراد بيعها (USDT)</label>
                    <input type="number" id="sellAmount" class="form-control" step="0.01" min="1">
                </div>
                <div class="form-group">
                    <label for="sellNetwork">اختر شبكة التحويل</label>
                    <select id="sellNetwork" class="form-control">
                        <option value="bep20">BEP20</option>
                        <option value="trc20">TRC20</option>
                        <option value="erc20">ERC20</option>
                        <option value="binance_pay">Binance Pay</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="receiveMethod">طريقة استلام المبلغ</label>
                    <select id="receiveMethod" class="form-control">
                        <option value="">-- اختر طريقة الاستلام --</option>
                        <option value="syriatel">سيريتل كاش</option>
                        <option value="pyramid">حوالة هرم</option>
                        <option value="bemo">بنك بيمو</option>
                        <option value="sham">شام كاش</option>
                    </select>
                </div>
                
                <!-- Receive Method Details -->
                <div id="receiveSyriatel" class="form-group hidden">
                    <label for="syriatelNumber">رقم سيريتل كاش</label>
                    <input type="text" id="syriatelNumber" class="form-control">
                </div>
                
                <div id="receivePyramid" class="form-group hidden">
                    <label for="pyramidName">الاسم كما سيظهر في الحوالة</label>
                    <input type="text" id="pyramidName" class="form-control">
                    <label for="pyramidPhone" style="margin-top: 10px;">رقم الهاتف</label>
                    <input type="text" id="pyramidPhone" class="form-control">
                </div>
                
                <div id="receiveBemo" class="form-group hidden">
                    <label for="bemoAccount">رقم الحساب البنكي</label>
                    <input type="text" id="bemoAccount" class="form-control">
                </div>
                
                <div id="receiveSham" class="form-group hidden">
                    <label for="shamAccount">رقم الحساب أو العنوان</label>
                    <input type="text" id="shamAccount" class="form-control">
                </div>
                
                <div class="form-group">
                    <label for="sellNotes">ملاحظات (اختياري)</label>
                    <textarea id="sellNotes" class="form-control" rows="3"></textarea>
                </div>
                
                <!-- Wallet Addresses -->
                <div class="payment-details">
                    <h3><i class="fas fa-wallet"></i> عناوين المحفظة</h3>
                    <p>يرجى إرسال USDT إلى أحد العناوين التالية حسب الشبكة المختارة:</p>
                    
                    <div id="bep20Address" class="copy-address">
                        <span>BEP20: 0x21802218d8d661d66F2C7959347a6382E1cc614F</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('0x21802218d8d661d66F2C7959347a6382E1cc614F')">نسخ</button>
                    </div>
                    
                    <div id="trc20Address" class="copy-address">
                        <span>TRC20: TD2LoErPRkVPBxBk72ZErtiyi6agirZQjX</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('TD2LoErPRkVPBxBk72ZErtiyi6agirZQjX')">نسخ</button>
                    </div>
                    
                    <div id="erc20Address" class="copy-address">
                        <span>ERC20: 0x21802218d8d661d66F2C7959347a6382E1cc614F</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('0x21802218d8d661d66F2C7959347a6382E1cc614F')">نسخ</button>
                    </div>
                    
                    <div id="binancePayAddress" class="copy-address">
                        <span>Binance Pay: 969755964</span>
                        <button type="button" class="copy-btn" onclick="copyToClipboard('969755964')">نسخ</button>
                    </div>
                </div>
            </div>
            
            <!-- Transaction Summary -->
            <div id="summarySection" class="summary hidden">
                <h3><i class="fas fa-file-invoice-dollar"></i> ملخص العملية</h3>
                <div class="summary-item">
                    <span>المبلغ:</span>
                    <span id="summaryAmount">0 USDT</span>
                </div>
                <div class="summary-item">
                    <span>عمولة ثابتة:</span>
                    <span id="summaryFixedFee">1 USD</span>
                </div>
                <div class="summary-item">
                    <span>عمولة نسبية (0.5%):</span>
                    <span id="summaryPercentageFee">0 USD</span>
                </div>
                <div class="summary-item">
                    <span>المبلغ الإجمالي:</span>
                    <span id="summaryTotal">0 USD</span>
                </div>
                <div class="summary-item">
                    <span>المبلغ بالليرة السورية (سعر الصرف: 10,000):</span>
                    <span id="summaryTotalSYP">0 SYP</span>
                </div>
            </div>
            
            <div class="note">
                <p><i class="fas fa-exclamation-circle"></i> عمولة التسديد على طرق التحويل المختلفة بالليرة السورية تقع على المستخدم كما تحددها هذه الجهات</p>
            </div>
            
            <button type="submit" id="submitBtn" class="btn btn-success hidden">
                <i class="fas fa-paper-plane"></i> إرسال الطلب
            </button>
        </form>
        
        <!-- Success Message -->
        <div id="successMessage" class="success-message hidden">
            <i class="fas fa-check-circle"></i>
            <h2>تم إرسال طلبك بنجاح!</h2>
            <p>سيتم التواصل معك قريباً لتأكيد التفاصيل.</p>
            <p id="successDetails"></p>
        </div>
    </div>

    <script>
        // Current exchange rate (can be changed manually)
        const exchangeRate = 10000;
        
        // DOM Elements
        const btnBuy = document.getElementById('btnBuy');
        const btnSell = document.getElementById('btnSell');
        const buySection = document.getElementById('buySection');
        const sellSection = document.getElementById('sellSection');
        const submitBtn = document.getElementById('submitBtn');
        const summarySection = document.getElementById('summarySection');
        const successMessage = document.getElementById('successMessage');
        const form = document.getElementById('exchangeForm');
        
        // Buy section elements
        const buyAmount = document.getElementById('buyAmount');
        const buyNetwork = document.getElementById('buyNetwork');
        const buyPaymentMethod = document.getElementById('buyPaymentMethod');
        
        // Sell section elements
        const sellAmount = document.getElementById('sellAmount');
        const sellNetwork = document.getElementById('sellNetwork');
        const receiveMethod = document.getElementById('receiveMethod');
        
        // Payment details sections
        const shamDetails = document.getElementById('shamDetails');
        const bemoDetails = document.getElementById('bemoDetails');
        const syriatelDetails = document.getElementById('syriatelDetails');
        const pyramidDetails = document.getElementById('pyramidDetails');
        
        // Receive method details
        const receiveSyriatel = document.getElementById('receiveSyriatel');
        const receivePyramid = document.getElementById('receivePyramid');
        const receiveBemo = document.getElementById('receiveBemo');
        const receiveSham = document.getElementById('receiveSham');
        
        // Summary elements
        const summaryAmount = document.getElementById('summaryAmount');
        const summaryFixedFee = document.getElementById('summaryFixedFee');
        const networkFeeItem = document.getElementById('networkFeeItem');
        const summaryPercentageFee = document.getElementById('summaryPercentageFee');
        const summaryTotal = document.getElementById('summaryTotal');
        const summaryTotalSYP = document.getElementById('summaryTotalSYP');
        
        // Event Listeners
        btnBuy.addEventListener('click', () => {
            buySection.classList.remove('hidden');
            sellSection.classList.add('hidden');
            submitBtn.classList.remove('hidden');
            updateSummary();
        });
        
        btnSell.addEventListener('click', () => {
            sellSection.classList.remove('hidden');
            buySection.classList.add('hidden');
            submitBtn.classList.remove('hidden');
            updateSummary();
        });
        
        buyAmount.addEventListener('input', updateSummary);
        buyNetwork.addEventListener('change', updateSummary);
        sellAmount.addEventListener('input', updateSummary);
        sellNetwork.addEventListener('change', updateSummary);
        
        buyPaymentMethod.addEventListener('change', function() {
            shamDetails.classList.add('hidden');
            bemoDetails.classList.add('hidden');
            syriatelDetails.classList.add('hidden');
            pyramidDetails.classList.add('hidden');
            
            if (this.value === 'sham') shamDetails.classList.remove('hidden');
            if (this.value === 'bemo') bemoDetails.classList.remove('hidden');
            if (this.value === 'syriatel') syriatelDetails.classList.remove('hidden');
            if (this.value === 'pyramid') pyramidDetails.classList.remove('hidden');
        });
        
        receiveMethod.addEventListener('change', function() {
            receiveSyriatel.classList.add('hidden');
            receivePyramid.classList.add('hidden');
            receiveBemo.classList.add('hidden');
            receiveSham.classList.add('hidden');
            
            if (this.value === 'syriatel') receiveSyriatel.classList.remove('hidden');
            if (this.value === 'pyramid') receivePyramid.classList.remove('hidden');
            if (this.value === 'bemo') receiveBemo.classList.remove('hidden');
            if (this.value === 'sham') receiveSham.classList.remove('hidden');
        });
        
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            submitOrder();
        });
        
        // Functions
        function updateSummary() {
            let amount = 0;
            let isBuy = !buySection.classList.contains('hidden');
            let network = isBuy ? buyNetwork.value : sellNetwork.value;
            
            if (isBuy) {
                amount = parseFloat(buyAmount.value) || 0;
            } else {
                amount = parseFloat(sellAmount.value) || 0;
            }
            
            if (amount > 0) {
                summarySection.classList.remove('hidden');
                
                // Calculate fees
                const fixedFee = 1; // $1 fixed fee
                const networkFee = network === 'trc20' ? 2 : 0; // $2 network fee for TRC20
                const percentageFee = amount * 0.005; // 0.5% of amount
                
                let total = amount + fixedFee + percentageFee;
                if (isBuy && network === 'trc20') {
                    total += networkFee;
                }
                
                // If selling, the user receives amount minus fees
                if (!isBuy) {
                    total = amount - fixedFee - percentageFee;
                    if (network === 'trc20') {
                        total -= networkFee;
                    }
                    // Ensure total doesn't go negative
                    total = Math.max(0, total);
                }
                
                // Update summary
                summaryAmount.textContent = amount.toFixed(2) + ' USDT';
                summaryFixedFee.textContent = fixedFee.toFixed(2) + ' USD';
                summaryPercentageFee.textContent = percentageFee.toFixed(2) + ' USD';
                
                if (network === 'trc20') {
                    networkFeeItem.classList.remove('hidden');
                } else {
                    networkFeeItem.classList.add('hidden');
                }
                
                if (isBuy) {
                    summaryTotal.textContent = total.toFixed(2) + ' USD';
                } else {
                    summaryTotal.textContent = total.toFixed(2) + ' USDT';
                }
                
                summaryTotalSYP.textContent = (total * exchangeRate).toLocaleString() + ' SYP';
            } else {
                summarySection.classList.add('hidden');
            }
        }
        
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                alert('تم نسخ النص: ' + text);
            }).catch(err => {
                console.error('Failed to copy: ', err);
            });
        }
        
        function submitOrder() {
            // Gather all form data
            const formData = {
                name: document.getElementById('fullName').value,
                phone: document.getElementById('phoneNumber').value,
                city: document.getElementById('city').value,
                transactionType: buySection.classList.contains('hidden') ? 'بيع' : 'شراء',
                amount: buySection.classList.contains('hidden') ? 
                       document.getElementById('sellAmount').value : 
                       document.getElementById('buyAmount').value,
                network: buySection.classList.contains('hidden') ? 
                        document.getElementById('sellNetwork').value : 
                        document.getElementById('buyNetwork').value,
                notes: buySection.classList.contains('hidden') ? 
                      document.getElementById('sellNotes').value : 
                      document.getElementById('buyNotes').value,
                timestamp: new Date().toISOString()
            };
            
            // Add transaction-specific details
            if (formData.transactionType === 'شراء') {
                formData.paymentMethod = document.getElementById('buyPaymentMethod').value;
                formData.walletAddress = document.getElementById('buyWalletAddress').value;
            } else {
                formData.receiveMethod = document.getElementById('receiveMethod').value;
                
                // Add receive method details
                if (formData.receiveMethod === 'syriatel') {
                    formData.syriatelNumber = document.getElementById('syriatelNumber').value;
                } else if (formData.receiveMethod === 'pyramid') {
                    formData.pyramidName = document.getElementById('pyramidName').value;
                    formData.pyramidPhone = document.getElementById('pyramidPhone').value;
                } else if (formData.receiveMethod === 'bemo') {
                    formData.bemoAccount = document.getElementById('bemoAccount').value;
                } else if (formData.receiveMethod === 'sham') {
                    formData.shamAccount = document.getElementById('shamAccount').value;
                }
            }
            
            // Add summary information
            formData.fixedFee = 1;
            formData.percentageFee = parseFloat(formData.amount) * 0.005;
            formData.networkFee = formData.network === 'trc20' ? 2 : 0;
            formData.totalAmount = calculateTotal(formData);
            formData.totalSYP = formData.totalAmount * exchangeRate;
            
            // Hide form and show success message
            form.classList.add('hidden');
            successMessage.classList.remove('hidden');
            
            // Display order details in success message
            let successDetails = `
                <p><strong>الاسم:</strong> ${formData.name}</p>
                <p><strong>رقم الهاتف:</strong> ${formData.phone}</p>
                <p><strong>المدينة:</strong> ${formData.city}</p>
                <p><strong>نوع العملية:</strong> ${formData.transactionType}</p>
                <p><strong>المبلغ:</strong> ${formData.amount} USDT</p>
                <p><strong>الشبكة:</strong> ${formatNetwork(formData.network)}</p>
                <p><strong>العمولة الثابتة:</strong> 1 USD</p>
                ${formData.network === 'trc20' ? '<p><strong>عمولة الشبكة (TRC20):</strong> 2 USD</p>' : ''}
                <p><strong>العمولة النسبية (0.5%):</strong> ${formData.percentageFee.toFixed(2)} USD</p>
                <p><strong>المبلغ الإجمالي:</strong> ${formData.totalAmount.toFixed(2)} ${formData.transactionType === 'شراء' ? 'USD' : 'USDT'}</p>
                <p><strong>المبلغ بالليرة السورية:</strong> ${formData.totalSYP.toLocaleString()} SYP</p>
            `;
            
            document.getElementById('successDetails').innerHTML = successDetails;
            
            // Send email (using mailto as requested)
            const subject = `طلب جديد ${formData.transactionType} USDT - ${formData.name}`;
            const body = `
اسم العميل: ${formData.name}
رقم الهاتف: ${formData.phone}
المدينة: ${formData.city}

تفاصيل الطلب:
نوع العملية: ${formData.transactionType}
المبلغ: ${formData.amount} USDT
الشبكة: ${formatNetwork(formData.network)}
${formData.transactionType === 'شراء' ? 'طريقة الدفع: ' + formatPaymentMethod(formData.paymentMethod) : 'طريقة الاستلام: ' + formatReceiveMethod(formData.receiveMethod)}

التفاصيل الإضافية:
${formData.transactionType === 'شراء' ? 'عنوان المحفظة: ' + formData.walletAddress : getReceiveDetails(formData)}

الملاحظات: ${formData.notes}

تفاصيل العمولة:
العمولة الثابتة: 1 USD
${formData.network === 'trc20' ? 'عمولة الشبكة (TRC20): 2 USD\n' : ''}
العمولة النسبية (0.5%): ${formData.percentageFee.toFixed(2)} USD
المبلغ الإجمالي: ${formData.totalAmount.toFixed(2)} ${formData.transactionType === 'شراء' ? 'USD' : 'USDT'}
المبلغ بالليرة السورية: ${formData.totalSYP.toLocaleString()} SYP

تاريخ الطلب: ${new Date().toLocaleString()}
            `;
            
            const mailtoLink = `mailto:alimahmoud001a@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            window.location.href = mailtoLink;
        }
        
        function calculateTotal(formData) {
            let total = parseFloat(formData.amount);
            const fixedFee = 1;
            const percentageFee = total * 0.005;
            const networkFee = formData.network === 'trc20' ? 2 : 0;
            
            if (formData.transactionType === 'شراء') {
                total += fixedFee + percentageFee + networkFee;
            } else {
                total -= fixedFee + percentageFee + networkFee;
                total = Math.max(0, total);
            }
            
            return total;
        }
        
        function formatNetwork(network) {
            const networks = {
                'bep20': 'BEP20',
                'trc20': 'TRC20',
                'erc20': 'ERC20',
                'binance_pay': 'Binance Pay'
            };
            return networks[network] || network;
        }
        
        function formatPaymentMethod(method) {
            const methods = {
                'sham': 'شام كاش',
                'bemo': 'بنك بيمو',
                'syriatel': 'سيريتل كاش',
                'pyramid': 'حوالة هرم'
            };
            return methods[method] || method;
        }
        
        function formatReceiveMethod(method) {
            // Same as payment methods in this case
            return formatPaymentMethod(method);
        }
        
        function getReceiveDetails(formData) {
            if (formData.transactionType === 'بيع') {
                if (formData.receiveMethod === 'syriatel') {
                    return `سيريتل كاش: ${formData.syriatelNumber}`;
                } else if (formData.receiveMethod === 'pyramid') {
                    return `حوالة هرم: الاسم ${formData.pyramidName}, الهاتف ${formData.pyramidPhone}`;
                } else if (formData.receiveMethod === 'bemo') {
                    return `بنك بيمو: ${formData.bemoAccount}`;
                } else if (formData.receiveMethod === 'sham') {
                    return `شام كاش: ${formData.shamAccount}`;
                }
            }
            return '';
        }
    </script>
</body>
</html>
