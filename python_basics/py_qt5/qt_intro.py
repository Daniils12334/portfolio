import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("After_Beer_Belly")
        self.setGeometry(0,0,500,800)
        self.setWindowIcon(QIcon("/home/danbar/Desktop/project_x/istockphoto-502739469-612x612.jpg"))
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0,0, 500, 100)
        label.setStyleSheet("color:000000; background-color:#6fdcf7; font-weight:bold; font-style;italic; text-decoration:underline;")
        label1 = QLabel(self)
        pixmap = QPixmap("/home/danbar/Desktop/project_x/istockphoto-502739469-612x612.jpg")
        label1.setPixmap(pixmap)
        label.setScaledContents(True)
        label1.setGeometry(self.width() - label1.width(),self.height()-label1.height(),label1.width(),label1.height())


        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Right, VCenter, HCenter, Bottom, Top
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background-color: 6a6a6a")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

