import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QAction
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Forms.add_product_form import AddProductForm
from Forms.edit_product_form import EditProductForm
from pdf.pdf_generator import generatePdf

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warehouse Management")
        self.setGeometry(450, 150, 600, 500)

        self._createMenuBar()
        self._createLabel()

    def _createMenuBar(self):
        menuBar = self.menuBar()

        # اطلاعات پایه
        baseInfoMenu = menuBar.addMenu("اطلاعات پایه")

        addItemAction = QAction("افزودن کالا", self)
        addItemAction.triggered.connect(self._openAddProductForm)
        baseInfoMenu.addAction(addItemAction)

        # ویرایش
        editMenu = menuBar.addMenu("ویرایش")
        editItemAction = QAction("ویرایش کالا", self)
        editItemAction.triggered.connect(self._openEditProductForm)
        editMenu.addAction(editItemAction)

        # گزارش‌ها
        reportMenu = menuBar.addMenu("گزارش‌ها")
        stockReportAction = QAction("(pdf) گزارش", self)
        stockReportAction.triggered.connect(generatePdf)
        reportMenu.addAction(stockReportAction)

        # خروج
        exitMenu = menuBar.addMenu("خروج")
        exitAction = QAction("خروج از برنامه", self)
        exitAction.triggered.connect(self.close)
        exitMenu.addAction(exitAction)

    def _createLabel(self):
        label = QLabel("به نرم‌افزار مدیریت انبار خوش آمدید", self)
        label.setFont(QFont("Arial", 14))
        label.setGeometry(50, 200, 500, 50)
        label.setStyleSheet(
            "color: darkblue;"
            "background-color: lightyellow;"
            "border: 1px solid gray;"
            "font-weight: bold;"
        )
        label.setAlignment(Qt.AlignCenter)

    def _openAddProductForm(self):
        self.addProductForm = AddProductForm()
        self.addProductForm.show()

    def _openEditProductForm(self):
        self.editProductForm = EditProductForm()
        self.editProductForm.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()