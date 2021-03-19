#INSTALL PyQt5 WITH:
# 1. ANACONDA:
# conda install -c anaconda pyqt
# 2. PIP:
# pip install PyQt5
#3. LINUX:
# sudo apt-get install python3-pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)

<<<<<<< HEAD
# Set main window and it's properties
=======
>>>>>>> 01ac434e8b5a195224717cc3f528d7b8ae36a0c6
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)
<<<<<<< HEAD

# Show our window

window.show()

sys.exit(app.exec)
=======
>>>>>>> 01ac434e8b5a195224717cc3f528d7b8ae36a0c6
