listuserTab = QWidget()
      layout = QVBoxLayout()
      layout1 = QFormLayout()

      self.combo_box= QComboBox()
      self.line=QLineEdit()
      self.button_search=QPushButton("SEARCH")

      self.combo_box.addItems(["FIRST NAME","LAST NAME","EMAIL"])
      layout1.addRow("select",self.combo_box)
      layout1.addRow(self.line)
      layout1.addRow(self.button_search)
      listuserTab.setLayout(layout1)
      self.button_search.clicked.connect(self.get_last_details)
      self.submit_action()
      return listuserTab

   def get_last_details(self):
      f=open('UI_excel.csv','r')
      text=f.read()
      f.close()
      print(text)
      
      
def main():"""
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

    def ADDUSERTAB (self):
        """Create the ADDUSERTAB ."""
        addusertab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("ID"))
        layout.addWidget(QCheckBox("FIRSTNAME"))
        layout.addWidget(QCheckBox("LASTNAME"))
        layout.addWidget(QCheckBox("EMAIL"))
        layout.addWidget(QCheckBox("DOB"))
        addusertab.setLayout(layout)
        return addusertab

    def LISTUSERTAB (self):
        """ Create the LISTUSERTAB ."""
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

