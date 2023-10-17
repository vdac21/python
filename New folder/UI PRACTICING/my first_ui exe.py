
# importing the required modules  
import sys  
from PyQt5.QtWidgets import QApplication  
from PyQt5.QtWidgets import QDialog  
from PyQt5.QtWidgets import QDialogButtonBox  
from PyQt5.QtWidgets import QFormLayout  
from PyQt5.QtWidgets import QLineEdit  
from PyQt5.QtWidgets import QVBoxLayout  
  
# defining the class that inherits QDialog  
class myDialog(QDialog):  
    
    def __init__(self, parent = None):  
        nitializer 
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
        myButtons = QDialogButtonBox()  
        myButtons.setStandardButtons(  
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok  
            )  
        dialog_layout.addWidget(myButtons)  
        self.setLayout(dialog_layout)  
  
# executing the application  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    my_dialog = myDialog()  
    my_dialog.show()  
    sys.exit(app.exec_())  
    tab_1.setLayout(tab_1.layout)
    tab_2.setLayout(tab_2.layout)
    layout.addWidget(tab_holder)
    self.setLayout(layout)
@pyqtSlot()
def on_click(self):
    button = self.sender().text()
    if button == self.lang["btn_start"]:
        print("Dank")
    elif button == self.lang["btn_stop"]:
        print("Not dank")
def AddToTab(self, tab, obj):
    tab.layout.addWidget(obj)

if _name_ == '_main_':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TabWidget(QDialog):
    def _init_(self):
        super()._init_()
        self.setWindowTitle('Tab Widget Application')

        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), 'First Tab')
        tabwidget.addTab(SecondTab(),'Second Tab')

        vbox=QVBoxLayout()
        vbox.addWidget(tabwidget)

        self.setLayout(vbox)
class FirstTab(QWidget):
    def _init_(self):
        super().__init__()
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)
        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
        self.btn=QPushButton('switch',self)
        self.btn.move(80, 50)
        self.btn.clicked.connect(lambda: SecondTab.display(SecondTab(),self.nameLabel.text()))
class SecondTab(QWidget):
    def _init_(self):
        super()._init_()
        self.layout = QVBoxLayout()
        self.editor=QTextEdit()
        self.layout.addWidget(self.editor)
        self.setLayout(self.layout)


    def display(self,text):
        self.editor.setText(text)

if _name_ == '_main_':
    app=QApplication(sys.argv)
    tabwidget = TabWidget()
    tabwidget.resize(500,500)
    tabwidget.show()
    app.exec()
python
"""
