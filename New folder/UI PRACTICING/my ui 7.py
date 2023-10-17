from PyQt5 import QtWidgets,uic


def print():
    T=call.LineEdit.text()
    T1=call.LineEdit_2.text()
    T2=call.LineEdit_3.text()
    T3=call.LineEdit_4.text()
    T4=call.QDateEdit.text()
    T5=call.radiobutton.text()
    print("your successfully submited !! :",T)
    print("your firstname is :",T1)
    print("your lastname is :",T2)
    print("your Gmail is :",T3)
    print("your DOB is :",T4)
    print("your Gender is :",T5)


app=QtWidgets.QApplication([])
call=uic.loadUi("regg.ui")

call.pushButton.clicked.connect(print)




call.show()
app.exce()
    
   
