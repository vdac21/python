class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()

    def generate_pstest_tab_elements(self,str1):
        groupBox = QGroupBox(str1)
        label1 = QLabel(self)
        label1.setText('Serial No:')
        line1 = QLineEdit(self)
        line1.setText("XXXX")
        label2 = QLabel(self)
        label2.setText('Chip ID:')
        line2 = QLineEdit(self)
        line2.setText("XXXX")
        rd_group = QButtonGroup()
        rdbtn_FCB15 = QRadioButton("FCB-15")
        rdbtn_DCB15 = QRadioButton("DCB-15")
        rd_group.addButton(rdbtn_FCB15)
        rd_group.addButton(rdbtn_FCB15)

        layout1 = QFormLayout()
        layout1.addRow(label1,line1)
        layout1.addRow(label2,line2)
        layout1.addRow(rdbtn_FCB15,rdbtn_DCB15)

        grid1 = QGridLayout()

        grid1.addWidget(label1,0,0)
        grid1.addWidget(line1,0,1)

        grid1.addWidget(rdbtn_FCB15,0,2)
        grid1.addWidget(rdbtn_DCB15,0,3)

        grid1.addWidget(label2,1,0)
        grid1.addWidget(line2,1,1)

        groupBox.setLayout(grid1)

        return groupBox

    def generate_pscalib_tab_elements(self,str1):
        groupBox = QGroupBox(str1)
        label1 = QLabel(self)
        label1.setText('Serial No:')
        line1 = QLineEdit(self)
        line1.setText("XXXX")
        label2 = QLabel(self)
        label2.setText('Chip ID:')
        line2 = QLineEdit(self)
        line2.setText("XXXX")
        label3 = QLabel(self)
        label3.setText('QR Code:')
        line3 = QLineEdit(self)
        line3.setText("XXXX")
        label4 = QLabel(self)
        label4.setText('Current Range:')
        line4 = QLineEdit(self)
        line4.setText("1.0")
        label5 = QLabel(self)
        label5.setText("PS Offset")
        line5 = QLineEdit(self)
        line5.setText("0.0")
        line5.setReadOnly(True)
        label6 = QLabel()
        label6.setText("PSGain")
        line6 = QLineEdit(self)
        line6.setText("1.0")
        line6.setReadOnly(True)

        grid2 = QGridLayout()

        grid2.addWidget(label1,0,0)
        grid2.addWidget(line1,0,1)

        grid2.addWidget(label2,1,0)
        grid2.addWidget(line2,1,1)

        grid2.addWidget(label3,2,0)
        grid2.addWidget(line3,2,1)

        grid2.addWidget(label4,3,0)
        grid2.addWidget(line4,3,1)

        grid2.addWidget(label5,4,0)
        grid2.addWidget(line5,4,1)

        grid2.addWidget(label6,5,0)
        grid2.addWidget(line6,5,1)
        groupBox.setLayout(grid2)        
        return groupBox

    def setupUi(self):

            self.title = 'BiPolar Power Supply Testing'
            self.setWindowTitle(self.title)             
            print (self.title)
            self.left = 50
            self.top = 50
            self.width = 1000
            self.height = 800

            self.PSTestTabGrid = QGridLayout()
            self.PSCalibTabGrid = QGridLayout()
            #self.setGeometry(self.left, self.top, self.width, self.height)

            #Create one main box that will hold all the tabs
            self.mainbox = QFormLayout()

            ##################### Items for PS Functional Test Tab #################

            self.PSTestTabGrid.addWidget(self.generate_pstest_tab_elements("PS1"), 0,0)
            self.PSTestTabGrid.addWidget(self.generate_pstest_tab_elements("PS2"), 1,0)
            self.PSTestTabGrid.addWidget(self.generate_pstest_tab_elements("PS3"), 2,0)
            self.PSTestTabGrid.addWidget(self.generate_pstest_tab_elements("PS4"), 3,0)
            self.PSTestTabGrid.addWidget(self.generate_pstest_tab_elements("PS5"), 4,0)
            self.PSTestTabGrid.addWidget(self.generate_pstest_tab_elements("PS6"), 5,0)
            self.PSTestTabGrid.addWidget(self.generate_pstest_tab_elements("PS7"), 6,0)
            self.PSTestTabGrid.addWidget(self.generate_pstest_tab_elements("PS8"), 7,0)

            self.PSFStart_btn = QPushButton("Start",self)
            self.PSFStop_btn = QPushButton("Stop",self)

            self.PSTestTabGrid.addWidget(self.PSFStart_btn,8,0)
            self.PSTestTabGrid.addWidget(self.PSFStop_btn,9,0)


            ##################### Items for PS Calib Tab #################

            self.PSCalibTabGrid.addWidget(self.generate_pscalib_tab_elements("PS"), 0,0)

            self.PSCalibStart_btn = QPushButton("Calib Start",self)
            self.PSCalibStop_btn = QPushButton("Calib Stop",self)

            self.PSCalibTabGrid.addWidget(self.PSCalibStart_btn,1,0)
            self.PSCalibTabGrid.addWidget(self.PSCalibStop_btn,2,0)

            ######################################################################
            #Init Tab Screen
            self.tabs = QTabWidget()
            self.tab1 = QWidget()
            self.tab2 = QWidget()

            #Add Tab
            self.tabs.addTab(self.tab1, "PS Tests")
            self.tabs.addTab(self.tab2, "PS Calib")

            #Set Layout for tab1, tab2
            self.tab1.setLayout(self.PSTestTabGrid)
            self.tab2.setLayout(self.PSCalibTabGrid)

            #Add the Tabs widget to MainBox
            self.mainbox.addWidget(self.tabs)

            #self.mainbox.addRow(self.tab2HBox)
            self.wid = QWidget(self)
            self.setCentralWidget(self.wid)
            #layout = QtGui.QVBoxLayout()
            self.wid.setLayout(self.mainbox)

