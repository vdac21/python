import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QDateEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PYTHON")
        self.resize(400, 300)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.ADD_USER(), "ADD_USER")
        tabs.addTab(self.LIST_USER(), "LIST_USER")
        layout.addWidget(tabs)

    def ADD_USER(self):
        """Create the General page UI."""
        tab1_user_details = QWidget()
        layout_gender = QHBoxLayout()
        layout1=QFormLayout()
        #user components for tab1
        self.obj_le_fname = QLineEdit()
        self.obj_le_lname = QLineEdit()
        self.obj_le_email = QLineEdit()
        self.obj_le_dob = QLineEdit()
        self.obj_bt_submit = QPushButton("SUBMIT")
        self.obj_rbt_male = QRadioButton("Male")
        self.obj_rbt_female = QRadioButton("Female")

        #adding radio buttons to Hbox layout
        layout_gender.addWidget(self.obj_rbt_male)
        layout_gender.addWidget(self.obj_rbt_female)

        #adding all components to the form layout
        layout1.addRow("FIRST NAME",self.obj_le_fname)
        layout1.addRow("LAST NAME",self.obj_le_lname)
        layout1.addRow("EMAIL",self.obj_le_email)
        layout1.addRow("DOB",self.obj_le_dob)       
        layout1.addRow(QLabel("Gender"),layout1)        
        layout1.addRow(self.obj_bt_submit)
   
        #adding form layout to tab1_widget
        tab1_user_details.setLayout(layout1)
        self.obj_bt_submit.clicked.connect(self.submit_action)
        return tab1_user_details
    def submit_action(self):
        fname = self.obj_le_fname.text()
        print(fname)
        lname = self.obj_le_lname.text()
        print(lname)
        email = self.obj_le_email.text()
        print(email)
        dob = self.obj_le_dob.text()
        print(dob)
      
        male = self.obj_rbt_male.text()
        print(male)
        #female = self.obj_rbt_female.text()
        #print(female)

    def LIST_USER(self):
        """Create the Network page UI."""
        listuserTab = QWidget()
        
        
        return listuserTab

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
