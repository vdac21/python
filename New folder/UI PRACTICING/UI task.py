import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class tabdemo(QTabWidget):
   def __init__(self, parent = None):
      super(tabdemo, self).__init__(parent)
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      
		
      self.addTab(self.tab1,"Tab 1")
      self.addTab(self.tab2,"Tab 2")
      

      self.tab1UI()
      self.tab2UI()
      
      self.setWindowTitle("Deployment.Team")
      self.resize(400,300)	
   def tab1UI(self):
      layout = QFormLayout()
      Gender = QHBoxLayout()
      layout.addRow("ID",QLineEdit())
      layout.addRow("First Name",QLineEdit())
      layout.addRow("Last Name",QLineEdit())
      
      layout.addRow("Email",QLineEdit())
      layout.addRow("DOB",QDateEdit())
      
      
      Gender.addWidget(QRadioButton("Male"))
      Gender.addWidget(QRadioButton("Female"))
      layout.addRow(QLabel("Gender"),Gender)
      layout.addRow(QPushButton("SUBMIT"))
      
     
      self.show() 
      self.setTabText(0,"Add Users")
      self.tab1.setLayout(layout)
   
   
   def tab2UI(self):
      layout = QFormLayout()
      
      self.setTabText(1,"List Users")
      self.tab2.setLayout(layout)

      	
   
def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == "__main__":
   main()
   


