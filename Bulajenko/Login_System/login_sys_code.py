
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QGraphicsBlurEffect, QMessageBox, QApplication

from Core.Models.Worker import Usuarios
from ui.pages.windowBaseMain import MainBaseWindow
from ui.windows.ui_Login_form import Ui_LoginWindow

from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications


class LoginSystem(QMainWindow):
    def __init__(self, parent=None):
        super(LoginSystem, self).__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))

        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.responses = Responses()
        self.verify = Verifications()

        self.users_db = Usuarios()

        self.ui.le_username.setStyleSheet('background-image: url(:/Images/user_32x32.png);')
        self.ui.le_password.setStyleSheet('background-image: url(:/Images/lock_32x32.png);')

        # self.ui.le_password.returnPressed.connect(self.ui.btnSignIn.click)
        self.ui.le_password.returnPressed.connect(self.ui.btnSignIn.click)

        self.ui.btnClose.clicked.connect(self.close)
        self.ui.btnSignIn.clicked.connect(self.log_in_system)

        def moveWindow (e):
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.frame_top.mouseMoveEvent = moveWindow

    def mousePressEvent (self, event):
        self.clickPosition = event.globalPos()

    def keyPressEvent (self, e):
        # print(e.key())
        # if (self.ui.le_username.text().strip() or self.ui.le_password.text().strip()) == '':
        if self.verify.empty_fields(self.get_user_login_input()):
            self.responses.raise_alert(self.ui.Login_response, 'Все поля должны быть заполнены.')
            return

        if e.key() == Qt.Key_Enter:
            self.log_in_system()

    def get_user_login_input(self) -> list:
        return [
            self.ui.le_username.displayText().strip(),
            self.ui.le_password.text().strip()
        ]

    def log_in_system (self):
        user_login_inputs = self.get_user_login_input()

        # print(f'user_login_inputs: {user_login_inputs}')

        if self.verify.empty_fields(user_login_inputs):
            self.responses.raise_alert(self.ui.Login_response, 'Все поля должны быть заполнены.')
            return

        try:
            confirm_inputs = self.users_db.confirm_login(
                user_login_inputs[0],
                user_login_inputs[1]
            )

            # print('confirm_inputs : ', confirm_inputs)
        except Exception:
            self.responses.raise_error(self.ui.Login_response,
                                       'An Error has occurred '
                                       'while trying to login')

        if confirm_inputs[0] == 'Confirm':
            self.responses.success_message(self.ui.Login_response, 'Доступ предоставлен!')

            self.base_window = MainBaseWindow(user_fields = confirm_inputs[1])
            self.base_window.show()
            self.close()

        elif confirm_inputs[0] == 'Не верный пароль':
            self.responses.raise_error(self.ui.Login_response, confirm_inputs[0])

        elif confirm_inputs[0] == 'Not user':
            self.responses.raise_alert(self.ui.Login_response, 'Пользователь не зарегистрирован в системе')

        else:
            self.responses.raise_alert(self.ui.Login_response, 'Проверьте введенные данные')

    # def clear_inputs(self):
    #     self.ui.le_username.clear()
    #     self.ui.le_password.clear()
    #     self.ui.Login_response.setText('')
























#
# class ColorQLineEdit(QLineEdit):
#     def __init__(self, parent=None):
#         super(QLineEdit, self).__init__(parent)
#
#     def focusInEvent(self, event):
#         print("in")
#         self.setStyleSheet("background-color: yellow; color: red;")
#         super().focusInEvent(event)
#
#     def focusOutEvent(self, event):
#         print("out")
#         self.setStyleSheet("background-color: white; color: black;")
#         super().focusOutEvent(event)





