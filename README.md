<!DOCTYPE html>
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
</html>
