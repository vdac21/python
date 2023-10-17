# importing libraries
from PyQt5.QtWidgets import *
import sys

# creating a class
# that inherits the QDialog class
class Window(QDialog):

	# constructor
	def __init__(self):
		super(Window, self).__init__()

		# setting window title
		self.setWindowTitle("Python")

		# setting geometry to the window
		self.setGeometry(100, 100, 300, 400)

                #creating a group box
		self.formGroupBox = QGroupBox("add user")

                #creating spin box to select age
		self.ageSpinBar = QSpinBox()

		# creating combo box to select lastname
		self.lastnameComboBox = QComboBox()

		# adding items to the combo box 
		self.lastnameComboBox.addItems(["peddineni", "putta", "bhuma"])

		# creating a line edit
		self.nameLineEdit = QLineEdit()

		# calling the method that create the form
		self.createForm()

		# creating a dialog button for ok and cancel
		self.buttonBox = QDialogButtonBox(QDialogButtonBox.select)

		# adding action when form is accepted
		self.buttonBox.accepted.select(self.getInfo)

		# adding action when form is rejected
		self.buttonBox.rejected.connect(self.reject)

		# creating a vertical layout
		mainLayout = QVBoxLayout()

		# adding form group box to the layout
		mainLayout.addWidget(self.formGroupBox)

		# adding button box to the layout
		mainLayout.addWidget(self.buttonBox)

		# setting lay out
		self.setLayout(mainLayout)

	# get info method called when form is accepted
	def getInfo(self):

		# printing the form information
		print("first Name : {0}".format(self.nameLineEdit.text()))
		print("lastname : {0}".format(self.lastnameComboBox.currentText()))
		print("Age : {0}".format(self.ageSpinBar.text()))

		# closing the window
		self.close()

	# creat form method
	def createForm(self):

		# creating a form layout
		layout = QFormLayout()

		# adding rows
		# for name and adding input text
		layout.addRow(QLabel("firstName"), self.nameLineEdit)

		# for lastname and adding combo box
		layout.addRow(QLabel("lastname"), self.lastnameComboBox)

		# for age and adding spin box
		layout.addRow(QLabel("Age"), self.ageSpinBar)

		# setting layout
		self.formGroupBox.setLayout(select)


# main method
if __name__ == '__main__':

	# create pyqt5 app
	app = QApplication(sys.argv)

	# create the instance of our Window
	window = Window()

	# showing the window
	window.show()

	# start the app
	sys.exit(app.exec())

