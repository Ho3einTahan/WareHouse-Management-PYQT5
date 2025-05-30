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
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt
from helper.database import Database
from model.product import Product


class AddProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🛒 افزودن کالای جدید")
        self.setGeometry(500, 200, 500, 550)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #f5f7fa;
                font-family: Vazir;
                font-size: 14px;
            }
            QLabel {
                color: #333;
                padding: 3px;
            }
            QLineEdit, QComboBox, QTextEdit, QSpinBox {
                background-color: white;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                padding: 8px;
                min-width: 200px;
                selection-background-color: #3b82f6;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top left;
                width: 20px;
                border-left-width: 1px;
                border-left-color: #d1d5db;
                border-left-style: solid;
                border-top-right-radius: 6px;
                border-bottom-right-radius: 6px;
            }
            QTextEdit {
                min-height: 80px;
            }
            QPushButton {
                background-color: #3b82f6;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                min-width: 100px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
            QPushButton:pressed {
                background-color: #1d4ed8;
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
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
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

        save_btn.clicked.connect(
            lambda: self.saveProduct(
                productName=self.name_input.text(),
                buyPrice=float(self.buy_price_input.text()),
                sellPrice=float(self.sell_price_input.text()),
                inventory=int(self.stock_input.text()),
                description=self.desc_input.toPlainText(),
            )
        )

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

    def saveProduct(
        self,productName, buyPrice, sellPrice, inventory, description, categoryId
    ):
        db = Database()
        try:
            product = Product(
                productName, buyPrice, sellPrice, inventory, description, categoryId
            )
            db.addNewProduct(product)
            print("محصول با موفقیت ذخیره شد.")
            self.close()
        except Exception as e:
            print("خطا هنگام ذخیره محصول:", e)
        finally:
            db.close()