import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import csv
class TabDemo(QTabWidget):
   def __init__(self, parent = None):
      super(TabDemo, self).__init__(parent)
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      self.resize(500,500)
      
		
      self.addTab(self.tab1,"Tab 1")
      self.addTab(self.tab2,"Tab 2")
      
      self.tab1UI()
      self.tab2UI()
      
      self.setWindowTitle("VDAC TEAM.COM")
		
   def tab1UI(self):
      """ create general page UI"""
      layout = QFormLayout()
      Gender = QHBoxLayout()
      layout1_gender=QHBoxLayout()
      #user compoents for tab1
      self.le_fid=QLineEdit()
      self.le_fname=QLineEdit()
      self.le_lname=QLineEdit()
      self.le_email=QLineEdit()
      self.dt_dob=QDateEdit()
      self.bt_submit=QPushButton("SUBMIT")
      self.rbt1_male=QRadioButton("Male")
      self.rbt2_female=QRadioButton("Female")
      layout.addRow("ID",self.le_fid)
      layout.addRow("FIRST NAME",self.le_fname)
      layout.addRow("LAST NAME",self.le_lname)
      layout.addRow("EMAIL",self.le_email)
      layout.addRow("DOB",self.dt_dob)
      #Gender = QHBoxLayout()
      
      layout1_gender.addWidget(self.rbt1_male)
      layout1_gender.addWidget(self.rbt2_female)
      layout.addRow(QLabel("Gender"),layout1_gender)
      layout.addRow(self.bt_submit)
      
      self.setTabText(0,"TAB1:ADD USER")
      self.tab1.setLayout(layout)
      self.bt_submit.clicked.connect(self.get_user_details)
   with open('Deployemnt_file.csv', mode='a') as Deployemnt_file:
      Deployment_writer = csv.writer(Deployemnt_file,quotechar='"',quoting=csv.QUOTE_MINIMAL)

      Deployment_writer.writerow(['101', 'bhagyalakshmi', 'peddineni', 'bhagya2589@gmail.com', '25-10-1998'])

      




   def get_user_details(self):
      print("hii")
      #QLineEdit.text()
      fid=self.le_fid.text()
      fname=self.le_fname.text()
      lname=self.le_lname.text()
      email=self.le_email.text()
      dob=self.dt_dob.text()
      #male=self.rbt1_male.text()
      #female=self.rbt2_male.text()
      #gender=layout1_gender.text()
      print([fname,lname,email,dob])
   
   def tab2UI(self):
       layout = QFormLayout()

       
       self.setTabText(1,"TAB2:LIST USER")	
def main():
   app = QApplication(sys.argv)
   ex = TabDemo()
   ex.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()
