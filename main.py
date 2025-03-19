from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from PyQt5.QtCore import QDate
from gtts import gTTS
import os
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets

class PersonUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 435)
        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(100, 380, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setAutoRepeatDelay(298)
        self.ok_button.setObjectName("ok_button")
        self.cancl_button = QtWidgets.QPushButton(Form)
        self.cancl_button.setGeometry(QtCore.QRect(190, 380, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancl_button.setFont(font)
        self.cancl_button.setAutoRepeatDelay(298)
        self.cancl_button.setObjectName("cancl_button")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(96, 181, 255);\n"
"border-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.play_button = QtWidgets.QPushButton(Form)
        self.play_button.setGeometry(QtCore.QRect(280, 380, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.play_button.setFont(font)
        self.play_button.setAutoRepeatDelay(298)
        self.play_button.setObjectName("play_button")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 100, 491, 271))
        self.groupBox.setObjectName("groupBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(50, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.reasonvisit_combobox = QtWidgets.QComboBox(self.groupBox)
        self.reasonvisit_combobox.setGeometry(QtCore.QRect(140, 180, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reasonvisit_combobox.setFont(font)
        self.reasonvisit_combobox.setObjectName("reasonvisit_combobox")
        self.male_radiobutton = QtWidgets.QRadioButton(self.groupBox)
        self.male_radiobutton.setGeometry(QtCore.QRect(140, 100, 77, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.male_radiobutton.setFont(font)
        self.male_radiobutton.setChecked(True)
        self.male_radiobutton.setAutoRepeatDelay(298)
        self.male_radiobutton.setObjectName("male_radiobutton")
        self.symptoms_textedit = QtWidgets.QTextEdit(self.groupBox)
        self.symptoms_textedit.setGeometry(QtCore.QRect(140, 220, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.symptoms_textedit.setFont(font)
        self.symptoms_textedit.setObjectName("symptoms_textedit")
        self.female_radiobutton = QtWidgets.QRadioButton(self.groupBox)
        self.female_radiobutton.setGeometry(QtCore.QRect(260, 100, 77, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.female_radiobutton.setFont(font)
        self.female_radiobutton.setAutoRepeatDelay(298)
        self.female_radiobutton.setObjectName("female_radiobutton")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(250, 140, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.birthdate_dateedit = QtWidgets.QDateEdit(self.groupBox)
        self.birthdate_dateedit.setGeometry(QtCore.QRect(140, 60, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.birthdate_dateedit.setFont(font)
        self.birthdate_dateedit.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.birthdate_dateedit.setObjectName("birthdate_dateedit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.height_textedit = QtWidgets.QTextEdit(self.groupBox)
        self.height_textedit.setGeometry(QtCore.QRect(310, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.height_textedit.setFont(font)
        self.height_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.height_textedit.setObjectName("height_textedit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.weight_textedit = QtWidgets.QTextEdit(self.groupBox)
        self.weight_textedit.setGeometry(QtCore.QRect(140, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weight_textedit.setFont(font)
        self.weight_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.weight_textedit.setObjectName("weight_textedit")
        self.other_radiobutton = QtWidgets.QRadioButton(self.groupBox)
        self.other_radiobutton.setGeometry(QtCore.QRect(380, 100, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.other_radiobutton.setFont(font)
        self.other_radiobutton.setAutoRepeatDelay(298)
        self.other_radiobutton.setObjectName("other_radiobutton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name_textedit = QtWidgets.QTextEdit(self.groupBox)
        self.name_textedit.setGeometry(QtCore.QRect(140, 20, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_textedit.setFont(font)
        self.name_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name_textedit.setObjectName("name_textedit")
        self.groupBox.raise_()
        self.ok_button.raise_()
        self.cancl_button.raise_()
        self.label_8.raise_()
        self.play_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ok_button.setText(_translate("Form", "Ok"))
        self.cancl_button.setText(_translate("Form", "Cancel"))
        self.label_8.setText(_translate("Form", "Patient Information"))
        self.play_button.setText(_translate("Form", "Read Infomation"))
        self.groupBox.setTitle(_translate("Form", "Information"))
        self.label_7.setText(_translate("Form", "Symptom:"))
        self.label_6.setText(_translate("Form", "Reason of visit:"))
        self.male_radiobutton.setText(_translate("Form", "Male"))
        self.female_radiobutton.setText(_translate("Form", "Female"))
        self.label_5.setText(_translate("Form", "Height:"))
        self.birthdate_dateedit.setDisplayFormat(_translate("Form", "dd-MM-yyyy"))
        self.label_4.setText(_translate("Form", "Weight:"))
        self.label_3.setText(_translate("Form", "Gender:"))
        self.label_2.setText(_translate("Form", "Date of Birth:"))
        self.other_radiobutton.setText(_translate("Form", "Others"))
        self.label.setText(_translate("Form", "Name:"))


class MainUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(518, 381)
        self.add_button = QtWidgets.QPushButton(Form)
        self.add_button.setGeometry(QtCore.QRect(60, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QPushButton(Form)
        self.remove_button.setGeometry(QtCore.QRect(200, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.show_button = QtWidgets.QPushButton(Form)
        self.show_button.setGeometry(QtCore.QRect(340, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_button.setFont(font)
        self.show_button.setObjectName("show_button")
        self.patient_list = QtWidgets.QListWidget(Form)
        self.patient_list.setGeometry(QtCore.QRect(50, 100, 401, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.patient_list.setFont(font)
        self.patient_list.setObjectName("patient_list")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(-10, 0, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(96, 181, 255);\n"
"border-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_button.setText(_translate("Form", "Add Patient"))
        self.remove_button.setText(_translate("Form", "Remove Patient"))
        self.show_button.setText(_translate("Form", "Show "))
        self.label_9.setText(_translate("Form", "Patient List"))


def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def get_text(name, birthdate, height, weight, gender, reason_visit, symptoms):
    if gender == 'Male':
        genderx = 'he'
    elif gender == 'Female':
        genderx = 'she'
    else:
        genderx = 'they'
    
    text = f"The patient's name is {name}, {genderx} is born on {birthdate}, is {height} centimeter tall ,and weigh "
    text += f"{weight} kilograms, {genderx},came here for a {reason_visit} and have {symptoms} symptoms."
    print(text)
    return text

class Person:
    def __init__(self, name):
       self.name = name
       self.birthdate = 0
       self.gender = "Female"
       self.height = 165
       self.weight = 50
       self.reason_visit = ""
       self.symptoms = ""
       
class PersonFrame(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui_form = PersonUI()
        self.ui_form.setupUi(self)
        self.parent = parent
        
        self.reasonvisit_list = ["follow-up", "check-up", "injury", "specific symptom"]
        for i in range(len(self.reasonvisit_list)):
            self.ui_form.reasonvisit_combobox.addItem(self.reasonvisit_list[i])
            
        self.ui_form.ok_button.clicked.connect(self.ok_clicked)
        self.ui_form.cancl_button.clicked.connect(self.cancel_clicked)
        self.ui_form.play_button.clicked.connect(self.play_clicked)
        
    def play_clicked(self):
        info = self.get_information()
        text = get_text(info['name'], info['birthdate'],info['height'], info['weight'], 
                        info['gender'], info['reasonvisit'], info['symptoms'])
        voice = gTTS(text)
        voice.save("output.mp3")
        play_sound("output.mp3")
        
    def get_information(self):
        info = {}
        info['name'] = self.ui_form.name_textedit.toPlainText()
        info['birthdate'] = self.ui_form.birthdate_dateedit.text()
        
        if self.ui_form.male_radiobutton.isChecked():
            info['gender']="Male"
        elif self.ui_form.female_radiobutton.isChecked():
            info['gender']="Female"
        else:
            info['gender']="Unknown"
            
        info['height'] = self.ui_form.height_textedit.toPlainText()
        info['weight'] = self.ui_form.weight_textedit.toPlainText()
        info['symptoms'] = self.ui_form.symptoms_textedit.toPlainText()
        info['reasonvisit'] = self.ui_form.reasonvisit_combobox.currentText()
        
        return info
    
    def ok_clicked(self):
        
        info = self.get_information()
        
        print("name", info['name'])
        print("birthdate", info['birthdate'])
        print("gender", info['gender'])
        print("height", info['height'])
        print("weight", info['weight'])
        print("reasonvisit", info['reasonvisit'])
        print("symptoms", info['symptoms'])
        
        person = Person(info['name'])
        person.birthdate = info['birthdate']
        person.gender = info['gender']
        person.height = info['height']
        person.weight = info['weight']
        person.symptoms = info['symptoms']
        person.reason_visit = info['reasonvisit']
        
        self.parent.patient_list.append(person)
        self.parent.refresh_patient_list()
        self.close()
    
    def cancel_clicked(self):
        self.close()

class MainFrame(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui_form = MainUI()
        self.ui_form.setupUi(self)
        
        self.patient_list = []
        
        self.ui_form.add_button.clicked.connect(self.add_clicked)
        self.ui_form.remove_button.clicked.connect(self.remove_clicked)
        self.ui_form.show_button.clicked.connect(self.show_clicked)
        
    def refresh_patient_list(self):
        self.ui_form.patient_list.clear()
        for i in range(len(self.patient_list)):
            self.ui_form.patient_list.addItem(self.patient_list[i].name)
            
    def remove_patient(self, name):
        for i in range(len(self.patient_list)):
            if self.patient_list[i].name == name:
                del self.patient_list[i]
                break
        self.refresh_patient_list()
    
    def add_clicked(self):
        self.person_frame = PersonFrame(parent=self)
        self.person_frame.show()
        
    def remove_clicked(self):
        index = self.ui_form.patient_list.currentRow()
        if index >= 0:
            name = self.patient_list[index].name
            self.remove_patient(name)

    def show_clicked(self):
        index = self.ui_form.patient_list.currentRow()
        if index >= 0:
            self.person_frame = PersonFrame(parent=self)
            self.person_frame.show()
            
            self.person_frame.ui_form.name_textedit.setText(
                self.patient_list[index].name
            )
            self.person_frame.ui_form.height_textedit.setText(
                self.patient_list[index].height
            )
            self.person_frame.ui_form.weight_textedit.setText(
                self.patient_list[index].weight
            )
            self.person_frame.ui_form.symptoms_textedit.setText(
                self.patient_list[index].symptoms
            )
            index_rv = self.person_frame.reasonvisit_list.index(
                self.patient_list[index].reason_visit
            )
            self.person_frame.ui_form.reasonvisit_combobox.setCurrentIndex(index_rv)
            
            if self.patient_list[index].gender == 'Male':
                self.person_frame.ui_form.male_radiobutton.setChecked(True)
            elif self.patient_list[index].gender == 'Female':
                self.person_frame.ui_form.female_radiobutton.setChecked(True)
            else:
                self.person_frame.ui_form.other_radiobutton.setChecked(True)
            text_date = self.patient_list[index].birthdate 
            day = int(text_date.split("-")[0])
            month = int(text_date.split("-")[1])
            year = int(text_date.split("-")[2])
            self.person_frame.ui_form.birthdate_dateedit.setDate(
                QDate(year, month, day)
            )
            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    myapp = MainFrame()
    myapp.show()
    sys.exit(app.exec_())