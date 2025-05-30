from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QApplication,
)

from PyQt5.QtCore import Qt
from model.product import Product
from helper.database import Database


class EditProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.database = Database()
        self.setWindowTitle("🛒 مدیریت کالا")
        self.setGeometry(500, 200, 470, 450)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        self.database.getAllProduct()
        
        products = [
            ["001", "Apple", "$1.20", "Fresh red apple"],
            ["002", "Banana", "$122", "Fresh red Banana"],
        ]

        self.table = QTableWidget(len(products), len(products[0]))
        self.table.setHorizontalHeaderLabels(["کدکالا", "نام کالا", "قیمت", "توضیحات"])

        for row, product in enumerate(products):
            for col, item_text in enumerate(product):
                item = QTableWidgetItem(item_text)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.table.setItem(row, col, item)

        main_layout.addWidget(self.table)

        # فرم ویرایش پایین جدول
        form_layout = QFormLayout()
        self.code_edit = QLineEdit()
        self.code_edit.setReadOnly(True)
        self.name_edit = QLineEdit()
        self.desc_edit = QLineEdit()
        self.price_edit = QLineEdit()

        # Set RTL direction
        self.setLayoutDirection(Qt.RightToLeft)
        for widget in [
            self.code_edit,
            self.name_edit,
            self.desc_edit,
            self.price_edit,
        ]:
            widget.setFixedHeight(35)
            widget.setFixedWidth(300)
            widget.setLayoutDirection(Qt.RightToLeft)

        form_layout.setLabelAlignment(Qt.AlignRight)

        form_layout.addRow(QLabel("کد کالا :"), self.code_edit)
        form_layout.addRow(QLabel("نام کالا :"), self.name_edit)
        form_layout.addRow(QLabel("قیمت کالا :"), self.price_edit)
        form_layout.addRow(QLabel("توضیحات :"), self.desc_edit)

        main_layout.addLayout(form_layout)

        # دکمه ذخیره
        button_layout = QHBoxLayout()
        save_button = QPushButton("ذخیره تغییرات")
        save_button.setFixedHeight(40)
        save_button.setFixedWidth(200)
        button_layout.addWidget(save_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # اتصال سیگنال‌ها
        self.table.cellClicked.connect(self.load_selected_row)
        save_button.clicked.connect(self.save_changes)

    def load_selected_row(self, row):

        self.selected_row = row
        self.code_edit.setText(self.table.item(row, 0).text())
        self.name_edit.setText(self.table.item(row, 1).text())
        self.price_edit.setText(self.table.item(row, 2).text())
        self.desc_edit.setText(self.table.item(row, 3).text())

    def save_changes(self):
        row = self.selected_row
        prCode = self.code_edit.text()
        prName = self.name_edit.text()
        buyPrice = self.price_edit.text()
        desc = self.desc_edit.text()
        if row is not None:
            self.table.setItem(row, 0, QTableWidgetItem(prCode))
            self.table.setItem(row, 1, QTableWidgetItem(prName))
            self.table.setItem(row, 2, QTableWidgetItem(buyPrice))
            self.table.setItem(row, 3, QTableWidgetItem(desc))
            self.database.updateProductById(
                Product(prCode, prName, buyPrice, 11, 1, desc)
            )
            self.database.close()
            print(f"Row {row} updated.")
