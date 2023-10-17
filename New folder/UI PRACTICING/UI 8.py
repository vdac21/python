import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QGroupBox
class MoodExample(QGroupBox):

    def _init_(self):
        super(MoodExample, self)._init_()

        # Create an array of radio buttons
        moods = [QRadioButton("male"), QRadioButton("female")]

        # Set a radio button to be checked by default
        moods[0].setChecked(True)

        # Radio buttons usually are in a vertical layout
        button_layout = QVBoxLayout()

        # Create a button group for radio buttons
        self.mood_button_group = QButtonGroup()

        for i in xrange(len(moods)):
            # Add each radio button to the button layout
            button_layout.addWidget(moods[i])
            # Add each radio button to the button group & give it an ID of i
            self.mood_button_group.addButton(moods[i], i)
            # Connect each radio button to a method to run when it's clicked
            self.connect(moods[i], SIGNAL("clicked()"), self.radio_button_clicked)

        # Set the layout of the group box to the button layout
        self.setLayout(button_layout)

    #Print out the ID & text of the checked radio button
    def radio_button_clicked(self):
        print(self.mood_button_group.checkedId())
        print(self.mood_button_group.checkedButton().text())

app = QApplication(sys.argv)
mood_example = MoodExample()
mood_example.show()
sys.exit(app.exec_())

