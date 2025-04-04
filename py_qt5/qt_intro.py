import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("After_Beer_Belly")
        self.setGeometry(0,0,500,800)
        self.setWindowIcon(QIcon("/home/danbar/Desktop/project_x/istockphoto-502739469-612x612.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

