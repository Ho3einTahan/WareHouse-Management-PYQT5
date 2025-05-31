from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import ( QFormLayout, QHBoxLayout,
                             QHeaderView, QLabel, QLineEdit, QPushButton,
                             QTableWidget, QTableWidgetItem, QVBoxLayout,
                             QWidget)

from di.injection import product_service
from Model.product import Product


class EditProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.productService=product_service
        self.setWindowTitle("🛒 مدیریت کالا")
        self.setGeometry(500, 200, 850, 600)
        self.setStyleSheet("background-color: #f9f9f9;")

        self.selected_row = None

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(20)

        # فونت پیش‌فرض
        app_font = QFont("B Nazanin", 13)
        self.setFont(app_font)

        # جدول کالاها
        products = self.productService.list_products()
        num_columns = len(vars(products[0])) if products else 0

        self.table = QTableWidget(len(products), num_columns)
        self.table.setHorizontalHeaderLabels(
            ["کد کالا", "نام کالا", "قیمت خرید", "قیمت فروش", "موجودی", "توضیحات"]
        )
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet(
            """
            QHeaderView::section {
                background-color: #3c8dbc;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
            QTableWidget {
                background-color: #ffffff;
                alternate-background-color: #f2f7fb;
                gridline-color: #cfd8dc;
                border: 1px solid #ddd;
                border-radius: 6px;
            }
            QTableWidget::item:selected {
                background-color: #cbe7ff;
            }
        """
        )
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for row, product in enumerate(products):
            product_dict = vars(product)
            for col, (key, value) in enumerate(product_dict.items()):
                item = QTableWidgetItem(str(value) if value else "")
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)

        main_layout.addWidget(self.table)

        # فرم ویرایش اطلاعات
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        self.setLayoutDirection(Qt.RightToLeft)

        def create_input():
            field = QLineEdit()
            field.setFixedHeight(40)
            field.setStyleSheet(
                """
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 8px 12px;
                background-color: #fafafa;
                font-size: 14px;
                font-family: 'B Nazanin';
                color: #333;
                direction: rtl;
                transition: all 0.3s ease;
            }

            QLineEdit:focus {
            border: 2px solid #3c8dbc;
            background-color: #ffffff;
            }
        """
            )

            return field

        self.code_edit = create_input()
        self.code_edit.setReadOnly(True)
        self.name_edit = create_input()
        self.buy_price_edit = create_input()
        self.sell_price_edit = create_input()
        self.inventory_edit = create_input()
        self.desc_edit = create_input()

        inputs = [
            ("کد کالا :", self.code_edit),
            ("نام کالا :", self.name_edit),
            ("قیمت خرید :", self.buy_price_edit),
            ("قیمت فروش :", self.sell_price_edit),
            ("موجودی :", self.inventory_edit),
            ("توضیحات :", self.desc_edit),
        ]

        for label, field in inputs:
            form_layout.addRow(QLabel(label), field)

        main_layout.addLayout(form_layout)

        # دکمه ذخیره
        button_layout = QHBoxLayout()
        save_button = QPushButton("💾 ذخیره تغییرات")
        save_button.setFixedHeight(45)
        save_button.setFixedWidth(220)
        #########################
        delete_button = QPushButton("❌ حذف کالا")
        delete_button.setFixedHeight(45)
        delete_button.setFixedWidth(220)

        save_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )

        delete_button.setStyleSheet(
            """
            QPushButton {
                background-color: red;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
        """
        )

        button_layout.addStretch()
        button_layout.addWidget(save_button)
        button_layout.addWidget(delete_button)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        # سیگنال‌ها
        self.table.cellClicked.connect(self.load_selected_row)
        save_button.clicked.connect(self.save_changes)
        delete_button.clicked.connect(lambda:self.deleteProduct(int(self.code_edit.text())))
        
    def load_selected_row(self, row):
        self.selected_row = row
        self.code_edit.setText(self.table.item(row, 0).text())
        self.name_edit.setText(self.table.item(row, 1).text())
        self.buy_price_edit.setText(self.table.item(row, 2).text())
        self.sell_price_edit.setText(self.table.item(row, 3).text())
        self.inventory_edit.setText(self.table.item(row, 4).text())
        self.desc_edit.setText(self.table.item(row, 5).text())

    def save_changes(self):
        row = self.selected_row
        if row is not None:
            prCode = self.code_edit.text()
            prName = self.name_edit.text()
            buyPrice = self.buy_price_edit.text()
            sellPrice = self.sell_price_edit.text()
            inventory = self.inventory_edit.text()
            desc = self.desc_edit.text()

            self.table.setItem(row, 1, QTableWidgetItem(prName))
            self.table.setItem(row, 2, QTableWidgetItem(buyPrice))
            self.table.setItem(row, 3, QTableWidgetItem(sellPrice))
            self.table.setItem(row, 4, QTableWidgetItem(inventory))
            self.table.setItem(row, 5, QTableWidgetItem(desc))

            self.productService.update_product(
                Product(prCode, prName, buyPrice, sellPrice, inventory, desc)
            )
            print(f"✅ ردیف {row} با موفقیت بروزرسانی شد.")
    
    def deleteProduct(self,prCode):
        self.table.removeRow(self.selected_row)
        self.productService.deleteProduct(prCode)