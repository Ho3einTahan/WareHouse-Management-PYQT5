from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QTextEdit,
    QSpinBox,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QHBoxLayout,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Model.product import Product
from di.injection import product_service

class AddProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.productService=product_service
        self.setWindowTitle("🛒 افزودن کالای جدید")
        self.setGeometry(500, 200, 500, 550)
        self.setStyleSheet(
            """
    QWidget {
        background-color: #f3f4f6;
        font-family: Vazir;
        font-size: 15px;
    }

    QLabel {
        color: #1f2937;
        padding: 4px;
        font-weight: bold;
    }

    QLineEdit, QComboBox, QTextEdit, QSpinBox {
        background-color: #ffffff;
        border: 1px solid #d1d5db;
        border-radius: 10px;
        padding: 10px;
        font-size: 14px;
        color: #111827;
        selection-background-color: #3b82f6;
    }

    QLineEdit:focus, QComboBox:focus, QTextEdit:focus, QSpinBox:focus {
        border: 2px solid #3b82f6;
        background-color: #ffffff;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top left;
        width: 25px;
        border-left: 1px solid #d1d5db;
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
        background-color: #e5e7eb;
    }

    QTextEdit {
        min-height: 90px;
    }

    QPushButton {
        background-color: #10b981;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        font-size: 15px;
        min-width: 120px;
        transition: all 0.3s ease;
    }

    QPushButton:hover {
        background-color: #059669;
    }

    QPushButton:pressed {
        background-color: #047857;
    }

    #cancel_btn {
        background-color: #ef4444;
    }

    #cancel_btn:hover {
        background-color: #dc2626;
    }

    #cancel_btn:pressed {
        background-color: #b91c1c;
    }

    #header {
        background-color: #3b82f6;
        color: white;
        padding: 18px;
        border-radius: 14px;
        margin-bottom: 25px;
        font-size: 18px;
    }
"""
        )

        # Layouts
        form_layout = QFormLayout()
        form_layout.setVerticalSpacing(15)
        form_layout.setHorizontalSpacing(20)
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Fonts
        title_font = QFont("Vazir", 18, QFont.Bold)
        input_font = QFont("Vazir", 11)

        # Header
        header = QLabel("فرم افزودن کالای جدید")
        header.setObjectName("header")
        header.setFont(title_font)
        header.setAlignment(Qt.AlignCenter)

        # Fields
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("نام کالا را وارد کنید")
        self.name_input.setFont(input_font)

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("کد کالا را وارد کنید")
        self.code_input.setFont(input_font)

        self.unit_input = QComboBox()
        self.unit_input.addItems(["عدد", "کیلوگرم", "لیتر", "متر", "بسته"])
        self.unit_input.setFont(input_font)

        self.buy_price_input = QLineEdit()
        self.buy_price_input.setPlaceholderText("قیمت خرید به ریال")
        self.buy_price_input.setFont(input_font)

        self.sell_price_input = QLineEdit()
        self.sell_price_input.setPlaceholderText("قیمت فروش به ریال")
        self.sell_price_input.setFont(input_font)

        self.stock_input = QSpinBox()
        self.stock_input.setMaximum(1000000)
        self.stock_input.setFont(input_font)

        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("توضیحات اضافی درباره کالا...")
        self.desc_input.setFont(input_font)

        # Set RTL direction
        self.setLayoutDirection(Qt.RightToLeft)
        for widget in [
            self.name_input,
            self.code_input,
            self.unit_input,
            self.buy_price_input,
            self.sell_price_input,
            self.stock_input,
            self.desc_input,
        ]:
            widget.setLayoutDirection(Qt.RightToLeft)

        # Add fields to form layout
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.addRow(QLabel("نام کالا:"), self.name_input)
        form_layout.addRow(QLabel("کد کالا:"), self.code_input)
        form_layout.addRow(QLabel("قیمت خرید:"), self.buy_price_input)
        form_layout.addRow(QLabel("قیمت فروش:"), self.sell_price_input)
        form_layout.addRow(QLabel("موجودی اولیه:"), self.stock_input)
        form_layout.addRow(QLabel("توضیحات:"), self.desc_input)

        # Buttons
        save_btn = QPushButton("💾 ذخیره کالا")

        save_btn.clicked.connect(self.handleSave)

        save_btn.setCursor(Qt.PointingHandCursor)

        cancel_btn = QPushButton("❌ انصراف")
        cancel_btn.setObjectName("cancel_btn")
        cancel_btn.setCursor(Qt.PointingHandCursor)

        button_layout.addStretch()
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)

        # Assemble layout
        main_layout.addWidget(header)
        main_layout.addLayout(form_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def handleSave(self):
        try:
            pr_code = self.code_input.text()
            name = self.name_input.text()
            buy_price_text = self.buy_price_input.text()
            sell_price_text = self.sell_price_input.text()
            inventory = self.stock_input.value()
            desc = self.desc_input.toPlainText()

            # اعتبارسنجی
            if not buy_price_text or not sell_price_text:
                print("لطفاً قیمت خرید و فروش را وارد کنید.")
                return

            buy_price = float(buy_price_text)
            sell_price = float(sell_price_text)

            self.saveProduct(
                prCode=pr_code,
                productName=name,
                buyPrice=buy_price,
                sellPrice=sell_price,
                inventory=inventory,
                description=desc,
            )

        except ValueError:
            print("مقدار قیمت‌ها باید عددی باشند.")
        except Exception as e:
            print("خطا در ذخیره کالا:", e)

    def saveProduct(
        self,
        prCode=None,
        productName=None,
        buyPrice=None,
        sellPrice=None,
        inventory=None,
        description=None,
    ):
        try:
            self.productService.create_product(prCode,productName,buyPrice,sellPrice,inventory,description)
            print("محصول با موفقیت ذخیره شد.")
            self.close()
        except Exception as e:
            print("خطا هنگام ذخیره محصول:", e)