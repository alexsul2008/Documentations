# from PyQt5.Qt import QTranslator, QLocale, QLibraryInfo
#
#
# app = str('C:\\Users\\avsulyay\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\PyQt5\\Qt5\\translations\\')
# translator = QTranslator(app)
# # if translator.load("qt_" + QLocale.system().name(), QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
# #     app.installTranslator(translator)
# if translator.load('qt_ru'):
#     app.installTranslator(translator)


from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton("Australia")
        radiobutton.setChecked(True)
        radiobutton.country = "Australia"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("China")
        radiobutton.country = "China"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton("Japan")
        radiobutton.country = "Japan"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 2)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Country is %s" % (radioButton.country))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())


