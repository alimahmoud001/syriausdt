<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>نظام تحويل USDT في سورية</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #0047AB;
            --primary-dark: #003380;
            --secondary: #1a73e8;
            --accent: #0d8bf2;
            --light: #f5f9ff;
            --dark: #1a1a2e;
            --success: #28a745;
            --warning: #ffc107;
            --danger: #dc3545;
            --gray: #6c757d;
            --light-gray: #e9ecef;
            --border-radius: 8px;
            --box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
            --transition: all 0.2s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #e6f0ff 0%, #f0f7ff 100%);
            color: var(--dark);
            min-height: 100vh;
            padding: 10px;
            line-height: 1.5;
            font-size: 16px;
        }

        .container {
            max-width: 100%;
            margin: 0 auto;
            padding: 0 5px;
        }

        header {
            text-align: center;
            padding: 15px 0;
            margin-bottom: 15px;
        }

        .logo {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            margin-bottom: 10px;
        }

        .logo i {
            font-size: 1.8rem;
            color: var(--primary);
        }

        .logo h1 {
            font-size: 1.5rem;
            color: var(--primary);
            font-weight: 700;
            line-height: 1.3;
        }

        .subtitle {
            color: var(--secondary);
            font-size: 0.95rem;
            font-weight: 500;
            max-width: 100%;
            margin: 0 auto;
        }

        .card {
            background: white;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px 15px;
            margin-bottom: 15px;
            transition: var(--transition);
        }

        .card-title {
            color: var(--primary);
            font-size: 1.3rem;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--light-gray);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .card-title i {
            font-size: 1.1rem;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            font-weight: 600;
            color: var(--dark);
            font-size: 0.95rem;
        }

        .required::after {
            content: " *";
            color: var(--danger);
        }

        input, select, textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid var(--light-gray);
            border-radius: var(--border-radius);
            font-size: 0.95rem;
            transition: var(--transition);
        }

        input:focus, select:focus, textarea:focus {
            border-color: var(--accent);
            outline: none;
            box-shadow: 0 0 0 3px rgba(13, 139, 242, 0.2);
        }

        .btn {
            display: block;
            padding: 13px 20px;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: var(--border-radius);
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            text-align: center;
            width: 100%;
            margin-top: 10px;
        }

        .btn:hover {
            background: var(--primary-dark);
        }

        .btn-secondary {
            background: var(--gray);
        }

        .btn-success {
            background: var(--success);
        }

        .payment-methods {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin: 15px 0;
        }

        .method-card {
            background: var(--light);
            border: 2px solid var(--light-gray);
            border-radius: var(--border-radius);
            padding: 12px;
            text-align: center;
            cursor: pointer;
            transition: var(--transition);
            font-size: 0.9rem;
        }

        .method-card:hover, .method-card.selected {
            border-color: var(--accent);
            background: rgba(13, 139, 242, 0.05);
        }

        .method-card i {
            font-size: 1.5rem;
            color: var(--primary);
            margin-bottom: 8px;
        }

        .copy-field {
            display: flex;
            background: var(--light);
            border-radius: var(--border-radius);
            overflow: hidden;
            margin: 8px 0;
        }

        .copy-field input {
            border: none;
            background: transparent;
            flex: 1;
            padding: 10px 12px;
            font-size: 0.9rem;
        }

        .copy-btn {
            background: var(--light-gray);
            border: none;
            padding: 0 12px;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            justify-content: center;
            min-width: 50px;
        }

        .copy-btn:hover {
            background: var(--accent);
            color: white;
        }

        .summary-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px dashed var(--light-gray);
            font-size: 0.95rem;
        }

        .summary-total {
            font-weight: 700;
            font-size: 1.1rem;
            color: var(--primary);
            padding-top: 12px;
            margin-top: 8px;
            border-top: 2px solid var(--light-gray);
        }

        .note-box {
            background: #fff8e1;
            border-left: 4px solid var(--warning);
            padding: 12px;
            border-radius: 0 var(--border-radius) var(--border-radius) 0;
            margin: 15px 0;
            font-size: 0.9rem;
        }

        .hidden {
            display: none;
        }

        .step-indicator {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }

        .step {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: var(--light-gray);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 5px;
            font-weight: 700;
            position: relative;
            font-size: 0.9rem;
        }

        .step.active {
            background: var(--primary);
            color: white;
        }

        .step:not(:last-child)::after {
            content: '';
            position: absolute;
            top: 50%;
            left: calc(100% + 3px);
            width: 20px;
            height: 2px;
            background: var(--light-gray);
            transform: translateY(-50%);
        }

        .flex-buttons {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .flex-buttons .btn {
            width: auto;
            flex: 1;
            padding: 12px 10px;
            font-size: 0.95rem;
        }

        .summary-section {
            margin-bottom: 20px;
        }

        .summary-section h3 {
            margin-bottom: 12px;
            color: var(--primary);
            font-size: 1.1rem;
        }

        /* Toast notification */
        .toast {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--success);
            color: white;
            padding: 12px 20px;
            border-radius: var(--border-radius);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1000;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .toast.show {
            opacity: 1;
        }

        @media (min-width: 480px) {
            .container {
                max-width: 95%;
            }
            
            .payment-methods {
                grid-template-columns: repeat(4, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">
                <i class="fas fa-coins"></i>
                <h1>نظام تحويل USDT في سورية</h1>
            </div>
            <p class="subtitle">خدمة تحويل آمنة وسريعة مع دعم جميع وسائل الدفع السورية</p>
        </header>

        <div class="step-indicator">
            <div class="step active">1</div>
            <div class="step">2</div>
            <div class="step">3</div>
        </div>

        <div class="card" id="step1">
            <h2 class="card-title"><i class="fas fa-user"></i> المعلومات الشخصية</h2>
            
            <div class="form-group">
                <label for="fullname" class="required">الاسم الثلاثي</label>
                <input type="text" id="fullname" placeholder="الاسم الكامل">
            </div>
            
            <div class="form-group">
                <label for="phone" class="required">رقم الهاتف</label>
                <input type="tel" id="phone" placeholder="09XXXXXXXX">
            </div>
            
            <div class="form-group">
                <label for="city" class="required">المدينة</label>
                <input type="text" id="city" placeholder="المدينة التي تقيم فيها">
            </div>
            
            <button class="btn" onclick="nextStep(2)">التالي <i class="fas fa-arrow-left"></i></button>
        </div>

        <div class="card hidden" id="step2">
            <h2 class="card-title"><i class="fas fa-exchange-alt"></i> تفاصيل العملية</h2>
            
            <div class="form-group">
                <label for="operationType" class="required">نوع العملية</label>
                <select id="operationType" onchange="toggleOperationDetails()">
                    <option value="">-- اختر نوع العملية --</option>
                    <option value="buy">شراء USDT</option>
                    <option value="sell">بيع USDT</option>
                </select>
            </div>
            
            <!-- شراء USDT -->
            <div id="buySection" class="hidden">
                <div class="form-group">
                    <label for="buyAmount" class="required">الكمية المطلوبة (USDT)</label>
                    <input type="number" id="buyAmount" placeholder="أدخل الكمية">
                </div>
                
                <div class="form-group">
                    <label for="buyNetwork" class="required">اختر شبكة التحويل</label>
                    <select id="buyNetwork">
                        <option value="bep20">BEP20</option>
                        <option value="trc20">TRC20</option>
                        <option value="erc20">ERC20</option>
                        <option value="binance">Binance Pay</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="buyAddress" class="required">عنوان المحفظة</label>
                    <input type="text" id="buyAddress" placeholder="أدخل عنوان محفظتك">
                </div>
                
                <div class="form-group">
                    <label for="buyNotes">ملاحظات (اختياري)</label>
                    <textarea id="buyNotes" rows="2" placeholder="أي ملاحظات أو معلومات إضافية"></textarea>
                </div>
                
                <div class="form-group">
                    <label class="required">طريقة الدفع</label>
                    <div class="payment-methods">
                        <div class="method-card" onclick="selectPaymentMethod(this, 'sham')">
                            <i class="fas fa-money-bill-wave"></i>
                            <div>شام كاش</div>
                        </div>
                        <div class="method-card" onclick="selectPaymentMethod(this, 'bemo')">
                            <i class="fas fa-university"></i>
                            <div>بنك بيمو</div>
                        </div>
                        <div class="method-card" onclick="selectPaymentMethod(this, 'syriatel')">
                            <i class="fas fa-mobile-alt"></i>
                            <div>سيريتل كاش</div>
                        </div>
                        <div class="method-card" onclick="selectPaymentMethod(this, 'harem')">
                            <i class="fas fa-money-check"></i>
                            <div>حوالة الهرم</div>
                        </div>
                    </div>
                    <input type="hidden" id="paymentMethod">
                </div>
            </div>
            
            <!-- بيع USDT -->
            <div id="sellSection" class="hidden">
                <div class="form-group">
                    <label for="sellAmount" class="required">الكمية المعروضة (USDT)</label>
                    <input type="number" id="sellAmount" placeholder="أدخل الكمية">
                </div>
                
                <div class="form-group">
                    <label class="required">طريقة الاستلام</label>
                    <div class="payment-methods">
                        <div class="method-card" onclick="selectReceiveMethod(this, 'sham')">
                            <i class="fas fa-money-bill-wave"></i>
                            <div>شام كاش</div>
                        </div>
                        <div class="method-card" onclick="selectReceiveMethod(this, 'bemo')">
                            <i class="fas fa-university"></i>
                            <div>بنك بيمو</div>
                        </div>
                        <div class="method-card" onclick="selectReceiveMethod(this, 'syriatel')">
                            <i class="fas fa-mobile-alt"></i>
                            <div>سيريتل كاش</div>
                        </div>
                        <div class="method-card" onclick="selectReceiveMethod(this, 'harem')">
                            <i class="fas fa-money-check"></i>
                            <div>حوالة الهرم</div>
                        </div>
                    </div>
                    <input type="hidden" id="receiveMethod">
                </div>
                
                <div id="receiveDetails" class="hidden">
                    <div class="form-group">
                        <label for="accountInfo" class="required">تفاصيل الحساب</label>
                        <input type="text" id="accountInfo" placeholder="رقم الحساب أو رقم الهاتف">
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="sellNetwork" class="required">اختر شبكة التحويل</label>
                    <select id="sellNetwork">
                        <option value="bep20">BEP20</option>
                        <option value="trc20">TRC20</option>
                        <option value="erc20">ERC20</option>
                        <option value="binance">Binance Pay</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="sellNotes">ملاحظات (اختياري)</label>
                    <textarea id="sellNotes" rows="2" placeholder="أي ملاحظات أو معلومات إضافية"></textarea>
                </div>
            </div>
            
            <div class="flex-buttons">
                <button class="btn btn-secondary" onclick="prevStep(1)"><i class="fas fa-arrow-right"></i> السابق</button>
                <button class="btn" onclick="nextStep(3)">التالي <i class="fas fa-arrow-left"></i></button>
            </div>
        </div>

        <div class="card hidden" id="step3">
            <h2 class="card-title"><i class="fas fa-file-invoice"></i> تفاصيل الطلب</h2>
            
            <div id="reviewContent"></div>
            
            <div class="note-box">
                <p><strong>ملاحظة هامة:</strong> عمولة التسديد على طرق التحويل المختلفة بالليرة السورية تقع على المستخدم كما تحددها هذه الجهات</p>
            </div>
            
            <div class="flex-buttons">
                <button class="btn btn-secondary" onclick="prevStep(2)"><i class="fas fa-arrow-right"></i> السابق</button>
                <button class="btn btn-success" onclick="submitOrder()"><i class="fas fa-check-circle"></i> تأكيد وإرسال</button>
            </div>
        </div>
    </div>
    
    <div id="toast" class="toast">تم النسخ إلى الحافظة!</div>

    <script>
        // متغيرات النظام
        const EXCHANGE_RATE = 10000; // سعر الصرف: 1 دولار = 10000 ليرة سورية
        const BASE_FEE = 1; // عمولة ثابتة 1 دولار
        const PERCENTAGE_FEE = 0.005; // 0.5%
        const TRC20_FEE = 2; // عمولة إضافية لشبكة TRC20
        
        // عناصر واجهة المستخدم
        const stepElements = document.querySelectorAll('.step');
        const stepCards = [
            document.getElementById('step1'),
            document.getElementById('step2'),
            document.getElementById('step3')
        ];
        
        const operationType = document.getElementById('operationType');
        const buySection = document.getElementById('buySection');
        const sellSection = document.getElementById('sellSection');
        const receiveDetails = document.getElementById('receiveDetails');
        const reviewContent = document.getElementById('reviewContent');
        const toast = document.getElementById('toast');
        
        // متغيرات البيانات
        let orderData = {
            step1: {},
            step2: {}
        };
        
        // وظائف التنقل بين الخطوات
        function nextStep(step) {
            if (step === 2 && !validateStep1()) return;
            if (step === 3 && !validateStep2()) return;
            
            // تحديث مؤشر الخطوات
            stepElements.forEach((el, index) => {
                if (index < step) el.classList.add('active');
                else el.classList.remove('active');
            });
            
            // إخفاء جميع الخطوات وإظهار الخطوة الحالية
            stepCards.forEach(card => card.classList.add('hidden'));
            stepCards[step - 1].classList.remove('hidden');
            
            // إذا كانت الخطوة 3، قم بملء محتوى المراجعة
            if (step === 3) {
                fillReviewContent();
            }
            
            // التمرير إلى أعلى الصفحة
            window.scrollTo(0, 0);
        }
        
        function prevStep(step) {
            nextStep(step);
        }
        
        // التحقق من صحة البيانات في الخطوة 1
        function validateStep1() {
            const fullname = document.getElementById('fullname').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const city = document.getElementById('city').value.trim();
            
            if (!fullname || !phone || !city) {
                alert('الرجاء ملء جميع الحقول المطلوبة');
                return false;
            }
            
            // حفظ البيانات للمراجعة
            orderData.step1 = { fullname, phone, city };
            return true;
        }
        
        // التحقق من صحة البيانات في الخطوة 2
        function validateStep2() {
            const opType = operation
