"""
# h_layout.py

Horizontal layout example.

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QHBoxLayout")

layout = QHBoxLayout()
layout.addWidget(QPushButton("ADDUSER"))
#layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("LISTUSER"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())

"""
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
    QDialog,  
    QDialogButtonBox,
    QFormLayout,  
   QLineEdit  
)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Example")
        self.resize(270, 110)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.ADDUSERTAB(), "ADDUSER")
        tabs.addTab(self.LISTUSERTAB(), "LISTUSER")
        layout.addWidget(tabs)
"""
    
    def __init__(self, parent = None):  
        Initializer  
        super().__init__(parent)  
        self.setWindowTitle('QDialog Application')  
        dialog_layout = QVBoxLayout()  
        form_layout = QFormLayout() 
        form_layout.addRow('ID:', QLineEdit())  
        form_layout.addRow('First Name:', QLineEdit())  
        form_layout.addRow('Last Name:', QLineEdit())  
        form_layout.addRow('dob:', QLineEdit())          
        form_layout.addRow('E-mail Address:', QLineEdit())  
        form_layout.addRow('Mobile Number:', QLineEdit())  
        dialog_layout.addLayout(form_layout)  
        myButton = QDialogButtonBox()  
        myButton.StandardButtons(  
            QDialogButtonBox.submit  
            )  
        dialog_layout.addWidget(myButtons)  
        self.setLayout(dialog_layout)  
  

        
    def LISTUSERTAB (self):
        Create the LISTUSERTAB .
        listusertab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("ID"))
        layout.addWidget(QCheckBox("FIRSTNAME"))
        layout.addWidget(QCheckBox("LASTNAME"))
        layout.addWidget(QCheckBox("EMAIL"))
        layout.addWidget(QCheckBox("DOB"))
        layout.addWidget(QCheckBox("GENDER"))
        listusertab.setLayout(layout)
      return listusertab
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

