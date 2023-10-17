import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtWidgets import *
import csv





class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DEPLOYEMENTTEAM")
        self.resize(1200, 400)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.ADDUSER(), "ADDUSER")
        tabs.addTab(self.LISTUSER(), "LISTUSER")
        layout.addWidget(tabs)

    def ADDUSER(self):
        #Create the General page UI.
        generalTab = QWidget()
        layout = QVBoxLayout()
        layout1=QFormLayout()
        Gender = QHBoxLayout()
        self.le_fname=QLineEdit()
        self.le_lname=QLineEdit()
        self.le_email=QLineEdit()
        self.dt_dob=QDateEdit()
        self.bt_submit=QPushButton("SUBMIT")
        self.rbt1_male=QRadioButton("Male")
        self.rbt2_female=QRadioButton("Female")
        self.gender_button=QLabel("Gender")


        
        layout1.addRow("FIRST NAME",self.le_fname)
        layout1.addRow("LAST NAME",self.le_lname)
        layout1.addRow("EMAIL",self.le_email)
        layout1.addRow("DOB",self.dt_dob)
        
        
        Gender.addWidget(self.rbt1_male)
        Gender.addWidget(self.rbt2_female)
        layout1.addRow(self.gender_button,Gender)
        layout1.addRow(self.bt_submit)
        self.bt_submit.clicked.connect(self.get_user_details)
      

        generalTab.setLayout(layout1)
        
        return generalTab
    def get_user_details(self):
        fname=self.le_fname.text()
        lname=self.le_lname.text()
        email=self.le_email.text()
        dob=self.dt_dob.text()
        print([fname,lname,email,dob])
        
        
        f=open('UI.csv','a',newline='')
        w = csv.writer(f)
        w.writerow(["ID","FIRST NAME","LAST NAME","EMAIL","DOB"])
        w.writerow([101,fname,lname,email,dob])
        #f.close()
    

    def LISTUSER(self):
        """Create the Network page UI."""
        listuserTab = QWidget()
        
        layout = QVBoxLayout()
        layout1=QFormLayout()

        self.combo_box= QComboBox()
        self.line=QLineEdit()
        self.button_search=QPushButton("SEARCH")
        
        self.combo_box.addItems(["FIRST NAME","LAST NAME","EMAIL"])
        
        layout1.addRow("select",self.combo_box)
        layout1.addRow(self.line)
        layout1.addRow(self.button_search)
        listuserTab.setLayout(layout1)
        self.button_search.clicked.connect(self.get_last_details)
       
        table = QTableWidget(listuserTab)
        table.setRowCount(20)
        table.setColumnCount(4)
        table.setGeometry(50, 150,800,800)
        headerH = ["FIRST NAME","LAST NAME","EMAIL","DOB"]
        table.setHorizontalHeaderLabels(headerH)
       
        
        return listuserTab


    
    def get_last_details(self):
        f=open('UI.csv','r')
        text=f.read()
        #f.close()
        print(text)

    def loadCsv(self):
        fileName = 'C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\UI.csv'
        with open(UI.csv, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
