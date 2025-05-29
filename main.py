import sys
from PyQt5.QtWidgets import QApplication , QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WareHouse Management")
        self.setGeometry(450,150,500,500)
        
        label=QLabel("helo lable",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0,0,200,100)
        label.setStyleSheet("color:blue;"
                            "background-color:red;"
                            "font-weight:bold;"
                            "text-decoration:underline")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()