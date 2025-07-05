# syriausdt

<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نظام تحويل USDT في سورية</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #0047AB;
            --secondary: #1a73e8;
            --accent: #0d8bf2;
            --light: #f5f9ff;
            --dark: #1a1a2e;
            --success: #28a745;
            --warning: #ffc107;
            --danger: #dc3545;
            --gray: #6c757d;
            --light-gray: #e9ecef;
            --border-radius: 12px;
            --box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #f5f9ff 0%, #e6f0ff 100%);
            color: var(--dark);
            min-height: 100vh;
            padding: 20px;
            line-height: 1.6;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            padding: 20px 0;
            margin-bottom: 30px;
        }

        .logo {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            margin-bottom: 15px;
        }

        .logo i {
            font-size: 2.5rem;
            color: var(--primary);
        }

        .logo h1 {
            font-size: 2.2rem;
            color: var(--primary);
            font-weight: 700;
        }

        .subtitle {
            color: var(--secondary);
            font-size: 1.2rem;
            font-weight: 500;
            max-width: 600px;
            margin: 0 auto;
        }

        .card {
            background: white;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 30px;
            margin-bottom: 25px;
            transition: var(--transition);
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        }

        .card-title {
            color: var(--primary);
            font-size: 1.5rem;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 2px solid var(--light-gray);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .card-title i {
            font-size: 1.3rem;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--dark);
        }

        .required::after {
            content: " *";
            color: var(--danger);
        }

        input, select, textarea {
            width: 100%;
            padding: 14px;
            border: 2px solid var(--light-gray);
            border-radius: var(--border-radius);
            font-size: 1rem;
            transition: var(--transition);
        }

        input:focus, select:focus, textarea:focus {
            border-color: var(--accent);
            outline: none;
            box-shadow: 0 0 0 3px rgba(13, 139, 242, 0.2);
        }

        .btn {
            display: inline-block;
            padding: 14px 28px;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: var(--border-radius);
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            text-align: center;
            width: 100%;
        }

        .btn:hover {
            background: var(--secondary);
            transform: translateY(-3px);
        }

        .btn-secondary {
            background: var(--gray);
        }

        .btn-success {
            background: var(--success);
        }

        .payment-methods {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }

        .method-card {
            background: var(--light);
            border: 2px solid var(--light-gray);
            border-radius: var(--border-radius);
            padding: 15px;
            text-align: center;
            cursor: pointer;
            transition: var(--transition);
        }

        .method-card:hover, .method-card.selected {
            border-color: var(--accent);
            background: rgba(13, 139, 242, 0.05);
        }

        .method-card i {
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 10px;
        }

        .copy-field {
            display: flex;
            background: var(--light);
            border-radius: var(--border-radius);
            overflow: hidden;
            margin: 10px 0;
        }

        .copy-field input {
            border: none;
            background: transparent;
            flex: 1;
        }

        .copy-btn {
            background: var(--light-gray);
            border: none;
            padding: 0 15px;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .copy-btn:hover {
            background: var(--accent);
            color: white;
        }

        .summary-item {
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px dashed var(--light-gray);
        }

        .summary-total {
            font-weight: 700;
            font-size: 1.2rem;
            color: var(--primary);
            padding-top: 15px;
            margin-top: 10px;
            border-top: 2px solid var(--light-gray);
        }

        .note-box {
            background: #fff8e1;
            border-left: 4px solid var(--warning);
            padding: 15px;
            border-radius: 0 var(--border-radius) var(--border-radius) 0;
            margin: 20px 0;
        }

        .hidden {
            display: none;
        }

        .step-indicator {
            display: flex;
            justify-content: center;
            margin-bottom: 30px;
        }

        .step {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            background: var(--light-gray);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 10px;
            font-weight: 700;
            position: relative;
        }

        .step.active {
            background: var(--primary);
            color: white;
        }

        .step:not(:last-child)::after {
            content: '';
            position: absolute;
            top: 50%;
            left: calc(100% + 5px);
            width: 40px;
            height: 2px;
            background: var(--light-gray);
            transform: translateY(-50%);
        }

        .flex-buttons {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }

        .flex-buttons .btn {
            width: auto;
            flex: 1;
        }

        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .card {
                padding: 20px;
            }
            
            .logo h1 {
                font-size: 1.8rem;
            }
            
            .payment-methods {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .flex-buttons {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">
                <i class="fas fa-exchange-alt"></i>
                <h1>نظام تحويل USDT في سورية</h1>
            </div>
            <p class="subtitle">خدمة آمنة وسريعة لتحويل العملات الرقمية مع دعم جميع وسائل الدفع السورية</p>
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
                <input type="text" id="fullname" placeholder="الاسم الكامل كما في الوثائق الرسمية">
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
            <h2 class="card-title"><i class="fas fa-shopping-cart"></i> تفاصيل العملية</h2>
            
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
                    <input type="number" id="buyAmount" placeholder="أدخل الكمية التي ترغب بشرائها">
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
                    <textarea id="buyNotes" rows="3" placeholder="أي ملاحظات أو معلومات إضافية"></textarea>
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
                    <input type="number" id="sellAmount" placeholder="أدخل الكمية التي ترغب ببيعها">
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
                    <textarea id="sellNotes" rows="3" placeholder="أي ملاحظات أو معلومات إضافية"></textarea>
                </div>
            </div>
            
            <div class="flex-buttons">
                <button class="btn btn-secondary" onclick="prevStep(1)"><i class="fas fa-arrow-right"></i> السابق</button>
                <button class="btn" onclick="nextStep(3)">التالي <i class="fas fa-arrow-left"></i></button>
            </div>
        </div>

        <div class="card hidden" id="step3">
            <h2 class="card-title"><i class="fas fa-file-invoice-dollar"></i> تفاصيل الطلب</h2>
            
            <div id="reviewContent"></div>
            
            <div class="note-box">
                <p><strong>ملاحظة هامة:</strong> عمولة التسديد على طرق التحويل المختلفة بالليرة السورية تقع على المستخدم كما تحددها هذه الجهات</p>
            </div>
            
            <div class="flex-buttons">
                <button class="btn btn-secondary" onclick="prevStep(2)"><i class="fas fa-arrow-right"></i> السابق</button>
                <button class="btn btn-success" onclick="submitOrder()"><i class="fas fa-paper-plane"></i> تأكيد وإرسال الطلب</button>
            </div>
        </div>
    </div>

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
            const opType = operationType.value;
            
            if (!opType) {
                alert('الرجاء اختيار نوع العملية (شراء أو بيع)');
                return false;
            }
            
            if (opType === 'buy') {
                const amount = document.getElementById('buyAmount').value;
                const network = document.getElementById('buyNetwork').value;
                const address = document.getElementById('buyAddress').value.trim();
                const method = document.getElementById('paymentMethod').value;
                
                if (!amount || !address || !method) {
                    alert('الرجاء ملء جميع الحقول المطلوبة في قسم الشراء');
                    return false;
                }
                
                orderData.step2 = {
                    type: 'buy',
                    amount: parseFloat(amount),
                    network,
                    address,
                    paymentMethod: method,
                    notes: document.getElementById('buyNotes').value.trim()
                };
            } else {
                const amount = document.getElementById('sellAmount').value;
                const method = document.getElementById('receiveMethod').value;
                const accountInfo = document.getElementById('accountInfo')?.value.trim() || '';
                const network = document.getElementById('sellNetwork').value;
                
                if (!amount || !method || (method && !accountInfo)) {
                    alert('الرجاء ملء جميع الحروف المطلوبة في قسم البيع');
                    return false;
                }
                
                orderData.step2 = {
                    type: 'sell',
                    amount: parseFloat(amount),
                    receiveMethod: method,
                    accountInfo,
                    network,
                    notes: document.getElementById('sellNotes').value.trim()
                };
            }
            
            return true;
        }
        
        // تبديل تفاصيل العملية بناءً على الاختيار
        function toggleOperationDetails() {
            const opType = operationType.value;
            
            buySection.classList.add('hidden');
            sellSection.classList.add('hidden');
            
            if (opType === 'buy') {
                buySection.classList.remove('hidden');
            } else if (opType === 'sell') {
                sellSection.classList.remove('hidden');
            }
        }
        
        // اختيار طريقة الدفع (للشراء)
        function selectPaymentMethod(element, method) {
            // إزالة التحديد من جميع العناصر
            document.querySelectorAll('#step2 .method-card').forEach(el => {
                el.classList.remove('selected');
            });
            
            // تحديد العنصر المختار
            element.classList.add('selected');
            document.getElementById('paymentMethod').value = method;
        }
        
        // اختيار طريقة الاستلام (للبيع)
        function selectReceiveMethod(element, method) {
            // إزالة التحديد من جميع العناصر
            document.querySelectorAll('#step2 .method-card').forEach(el => {
                el.classList.remove('selected');
            });
            
            // تحديد العنصر المختار
            element.classList.add('selected');
            document.getElementById('receiveMethod').value = method;
            
            // إظهار حقل تفاصيل الحساب
            receiveDetails.classList.remove('hidden');
        }
        
        // ملء محتوى مراجعة الطلب
        function fillReviewContent() {
            const {step1, step2} = orderData;
            let content = '';
            
            // معلومات العميل
            content += `<h3 style="margin-bottom: 15px; color: var(--primary);">معلومات العميل</h3>`;
            content += `<div class="summary-item"><span>الاسم:</span><span>${step1.fullname}</span></div>`;
            content += `<div class="summary-item"><span>الهاتف:</span><span>${step1.phone}</span></div>`;
            content += `<div class="summary-item"><span>المدينة:</span><span>${step1.city}</span></div>`;
            
            content += `<div style="height: 20px;"></div>`;
            
            // تفاصيل العملية
            if (step2.type === 'buy') {
                content += `<h3 style="margin-bottom: 15px; color: var(--primary);">تفاصيل الشراء</h3>`;
                content += `<div class="summary-item"><span>الكمية:</span><span>${step2.amount} USDT</span></div>`;
                content += `<div class="summary-item"><span>شبكة التحويل:</span><span>${getNetworkName(step2.network)}</span></div>`;
                content += `<div class="summary-item"><span>عنوان المحفظة:</span><span>${step2.address}</span></div>`;
                content += `<div class="summary-item"><span>طريقة الدفع:</span><span>${getPaymentMethodName(step2.paymentMethod)}</span></div>`;
                
                // معلومات الدفع
                content += `<div style="height: 20px;"></div>`;
                content += `<h3 style="margin-bottom: 15px; color: var(--primary);">معلومات الدفع</h3>`;
                content += getPaymentDetails(step2.paymentMethod);
                
                // العمولة والتكلفة
                const fees = calculateFees(step2.amount, step2.network);
                content += `<div style="height: 20px;"></div>`;
                content += `<h3 style="margin-bottom: 15px; color: var(--primary);">العمولة والتكلفة</h3>`;
                content += `<div class="summary-item"><span>سعر الصرف:</span><span>1 USD = ${EXCHANGE_RATE.toLocaleString()} SYP</span></div>`;
                content += `<div class="summary-item"><span>العمولة الثابتة:</span><span>${BASE_FEE} USD</span></div>`;
                content += `<div class="summary-item"><span>عمولة النسبة (0.5%):</span><span>${fees.percentageFee.toFixed(2)} USD</span></div>`;
                
                if (step2.network === 'trc20') {
                    content += `<div class="summary-item"><span>عمولة شبكة TRC20:</span><span>${TRC20_FEE} USD</span></div>`;
                }
                
                content += `<div class="summary-item summary-total"><span>المبلغ الإجمالي بالدولار:</span><span>${fees.totalUSD.toFixed(2)} USD</span></div>`;
                content += `<div class="summary-item summary-total"><span>المبلغ الإجمالي بالليرة السورية:</span><span>${fees.totalSYP.toLocaleString()} SYP</span></div>`;
                
            } else {
                content += `<h3 style="margin-bottom: 15px; color: var(--primary);">تفاصيل البيع</h3>`;
                content += `<div class="summary-item"><span>الكمية:</span><span>${step2.amount} USDT</span></div>`;
                content += `<div class="summary-item"><span>طريقة الاستلام:</span><span>${getPaymentMethodName(step2.receiveMethod)}</span></div>`;
                content += `<div class="summary-item"><span>تفاصيل الحساب:</span><span>${step2.accountInfo}</span></div>`;
                content += `<div class="summary-item"><span>شبكة التحويل:</span><span>${getNetworkName(step2.network)}</span></div>`;
                
                // معلومات المحفظة
                content += `<div style="height: 20px;"></div>`;
                content += `<h3 style="margin-bottom: 15px; color: var(--primary);">معلومات المحفظة</h3>`;
                content += getWalletDetails(step2.network);
                
                // العمولة والمبلغ المستحق
                const fees = calculateFees(step2.amount, step2.network);
                content += `<div style="height: 20px;"></div>`;
                content += `<h3 style="margin-bottom: 15px; color: var(--primary);">العمولة والمبلغ المستحق</h3>`;
                content += `<div class="summary-item"><span>سعر الصرف:</span><span>1 USD = ${EXCHANGE_RATE.toLocaleString()} SYP</span></div>`;
                content += `<div class="summary-item"><span>العمولة الثابتة:</span><span>${BASE_FEE} USD</span></div>`;
                content += `<div class="summary-item"><span>عمولة النسبة (0.5%):</span><span>${fees.percentageFee.toFixed(2)} USD</span></div>`;
                
                if (step2.network === 'trc20') {
                    content += `<div class="summary-item"><span>عمولة شبكة TRC20:</span><span>${TRC20_FEE} USD</span></div>`;
                }
                
                content += `<div class="summary-item summary-total"><span>المبلغ المستحق بالدولار:</span><span>${fees.receivedUSD.toFixed(2)} USD</span></div>`;
                content += `<div class="summary-item summary-total"><span>المبلغ المستحق بالليرة السورية:</span><span>${fees.receivedSYP.toLocaleString()} SYP</span></div>`;
            }
            
            // الملاحظات
            if (step2.notes) {
                content += `<div style="height: 20px;"></div>`;
                content += `<h3 style="margin-bottom: 15px; color: var(--primary);">ملاحظات العميل</h3>`;
                content += `<div class="summary-item"><span>${step2.notes}</span></div>`;
            }
            
            reviewContent.innerHTML = content;
            
            // إضافة وظيفة النسخ للعناوين
            addCopyFunctionality();
        }
        
        // حساب العمولات والمبالغ
        function calculateFees(amount, network) {
            const percentageFee = amount * PERCENTAGE_FEE;
            let networkFee = 0;
            
            if (network === 'trc20') {
                networkFee = TRC20_FEE;
            }
            
            const totalFees = BASE_FEE + percentageFee + networkFee;
            
            return {
                percentageFee,
                networkFee,
                totalFees,
                totalUSD: amount + totalFees,
                totalSYP: (amount + totalFees) * EXCHANGE_RATE,
                receivedUSD: amount - totalFees,
                receivedSYP: (amount - totalFees) * EXCHANGE_RATE
            };
        }
        
        // الحصول على اسم الشبكة
        function getNetworkName(network) {
            const names = {
                'bep20': 'BEP20',
                'trc20': 'TRC20',
                'erc20': 'ERC20',
                'binance': 'Binance Pay'
            };
            return names[network] || network;
        }
        
        // الحصول على اسم طريقة الدفع
        function getPaymentMethodName(method) {
            const names = {
                'sham': 'شام كاش',
                'bemo': 'بنك بيمو',
                'syriatel': 'سيريتل كاش',
                'harem': 'حوالة الهرم'
            };
            return names[method] || method;
        }
        
        // الحصول على تفاصيل الدفع بناءً على الطريقة
        function getPaymentDetails(method) {
            let details = '';
            
            switch(method) {
                case 'sham':
                    details += `<div class="summary-item"><span>الاسم:</span><span>علي ابراهيم محمود</span></div>`;
                    details += `<div class="summary-item"><span>عنوان المحفظة:</span><span>be456e0ea9392db4d68a7093ee317bc8</span></div>`;
                    details += `<div class="summary-item"><span>رقم الحساب:</span><span>5991161126028260</span></div>`;
                    break;
                case 'syriatel':
                    details += `<div class="summary-item"><span>الاسم:</span><span>علي ابراهيم محمود</span></div>`;
                    details += `<div class="summary-item"><span>رقم الهاتف:</span><span>0934598967</span></div>`;
                    break;
                case 'harem':
                    details += `<div class="summary-item"><span>الاسم:</span><span>علي ابراهيم محمود</span></div>`;
                    details += `<div class="summary-item"><span>رقم الهاتف:</span><span>0934598967</span></div>`;
                    details += `<div class="summary-item"><span>المدينة:</span><span>اللاذقية</span></div>`;
                    break;
                case 'bemo':
                    details += `<div class="summary-item"><span>الاسم:</span><span>علي ابراهيم محمود</span></div>`;
                    details += `<div class="summary-item"><span>رقم الحساب:</span><span>060104947910013000000</span></div>`;
                    break;
            }
            
            return details;
        }
        
        // الحصول على تفاصيل المحفظة بناءً على الشبكة
        function getWalletDetails(network) {
            let details = '';
            
            switch(network) {
                case 'bep20':
                    details += `<div class="summary-item"><span>العنوان:</span><span>0x21802218d8d661d66F2C7959347a6382E1cc614F</span></div>`;
                    break;
                case 'trc20':
                    details += `<div class="summary-item"><span>العنوان:</span><span>TD2LoErPRkVPBxDk72ZErtiyi6agirZQjX</span></div>`;
                    break;
                case 'erc20':
                    details += `<div class="summary-item"><span>العنوان:</span><span>0x21802218d8d661d66F2C7959347a6382E1cc614F</span></div>`;
                    break;
                case 'binance':
                    details += `<div class="summary-item"><span>رقم Binance Pay:</span><span>969755964</span></div>`;
                    break;
            }
            
            return details;
        }
        
        // إضافة وظيفة النسخ للعناوين
        function addCopyFunctionality() {
            document.querySelectorAll('.summary-item span:last-child').forEach(span => {
                span.style.cursor = 'pointer';
                span.style.position = 'relative';
                
                span.onclick = function() {
                    const text = this.textContent;
                    navigator.clipboard.writeText(text);
                    
                    // إظهار إشعار النسخ
                    const notification = document.createElement('div');
                    notification.textContent = 'تم النسخ!';
                    notification.style.position = 'absolute';
                    notification.style.background = 'var(--success)';
                    notification.style.color = 'white';
                    notification.style.padding = '5px 10px';
                    notification.style.borderRadius = '4px';
                    notification.style.top = '-35px';
                    notification.style.left = '50%';
                    notification.style.transform = 'translateX(-50%)';
                    notification.style.zIndex = '100';
                    
                    this.appendChild(notification);
                    
                    setTimeout(() => {
                        notification.remove();
                    }, 2000);
                };
            });
        }
        
        // إرسال الطلب
        function submitOrder() {
            const {step1, step2} = orderData;
            
            // إنشاء محتوى البريد الإلكتروني
            let subject = `طلب جديد: ${step2.type === 'buy' ? 'شراء' : 'بيع'} USDT`;
            let body = `تفاصيل الطلب الجديد:\n\n`;
            
            body += `معلومات العميل:\n`;
            body += `الاسم: ${step1.fullname}\n`;
            body += `الهاتف: ${step1.phone}\n`;
            body += `المدينة: ${step1.city}\n\n`;
            
            if (step2.type === 'buy') {
                body += `نوع العملية: شراء USDT\n`;
                body += `الكمية: ${step2.amount} USDT\n`;
                body += `شبكة التحويل: ${getNetworkName(step2.network)}\n`;
                body += `عنوان المحفظة: ${step2.address}\n`;
                body += `طريقة الدفع: ${getPaymentMethodName(step2.paymentMethod)}\n`;
            } else {
                body += `نوع العملية: بيع USDT\n`;
                body += `الكمية: ${step2.amount} USDT\n`;
                body += `طريقة الاستلام: ${getPaymentMethodName(step2.receiveMethod)}\n`;
                body += `تفاصيل الحساب: ${step2.accountInfo}\n`;
                body += `شبكة التحويل: ${getNetworkName(step2.network)}\n`;
            }
            
            // حساب العمولة
            const fees = calculateFees(step2.amount, step2.network);
            
            body += `\nالعمولة:\n`;
            body += `العمولة الثابتة: ${BASE_FEE} USD\n`;
            body += `عمولة النسبة (0.5%): ${fees.percentageFee.toFixed(2)} USD\n`;
            
            if (step2.network === 'trc20') {
                body += `عمولة شبكة TRC20: ${TRC20_FEE} USD\n`;
            }
            
            if (step2.type === 'buy') {
                body += `المبلغ الإجمالي بالدولار: ${fees.totalUSD.toFixed(2)} USD\n`;
                body += `المبلغ الإجمالي بالليرة السورية: ${fees.totalSYP.toLocaleString()} SYP\n`;
            } else {
                body += `المبلغ المستحق بالدولار: ${fees.receivedUSD.toFixed(2)} USD\n`;
                body += `المبلغ المستحق بالليرة السورية: ${fees.receivedSYP.toLocaleString()} SYP\n`;
            }
            
            if (step2.notes) {
                body += `\nملاحظات العميل: ${step2.notes}\n`;
            }
            
            // إنشاء رابط البريد الإلكتروني
            const mailtoLink = `mailto:alimahmoud001a@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            
            // فتح عميل البريد الإلكتروني
            window.location.href = mailtoLink;
            
            // عرض رسالة نجاح
            alert('تم إرسال طلبك بنجاح! سيتم التواصل معك قريباً لتأكيد العملية.');
            
            // إعادة تعيين النموذج
            setTimeout(() => {
                window.location.reload();
            }, 3000);
        }
    </script>
</body>
</html>
