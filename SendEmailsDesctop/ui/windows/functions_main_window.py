
import ctypes

from PySide2.QtWidgets import QPushButton

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////

from ui.gt_base_ui.ui_windowAddEmail import Ui_WindowAddEmailOperator

# STYLE_ACTIVE = 'background-color:rgb(42, 61, 79);'
# STYLE_NOT_ACTIVE = 'background-color: transparent;'

# STYLE
# ///////////////////////////////////////////////////////////////
STYLE_ACTIVE = '''
    QPushButton {        
        background-color: rgb(42, 61, 79);
        border-top: 1px solid rgb(42, 61, 79);
        border-bottom: 1px solid rgb(42, 61, 79);
        border-left: none;
        border-right: none;
    }    
    QLabel{
        background-color: #3daee9;
    }   
'''
# QPushButton
STYLE_NOT_ACTIVE = '''    
    QPushButton {
        background-color: transparent;
    }   
    QPushButton:hover, QPushButton:hover QLabel{
        background-color: rgb(42, 61, 79);        
    } 
    QLabel{
        background-color: rgb(33, 47, 61);
    }
    
'''

STYLE_HOVER = '''
    QPushButton{
        text-align: center;
    }
    QPushButton:hover {
        background-color: rgb(39, 111, 147); 
        border-color: rgb(39, 111, 147);
    } 
'''
STYLE_HOVER_RED = '''
    QPushButton:hover {
        background-color: rgb(235, 0, 0); 
        border-color: rgb(171, 0, 0);
    } 
'''

STYLE_HOVER_GREEN = '''
    QPushButton:hover {
        background-color: #eb0000; 
        border-color:#ab0000;
    } 
'''


class MainFunctions():
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowAddEmailOperator()
        self.ui.setupUi(self)

    # def set_page (self, page, frm_btn, frm_menu):
    #     # for item in range(self.ui.left_menu_verticalLayout.count()):
    #     print(range(self.ui.frame_menu_verticalLayout.count()))
    #
    #     # for item in range(frm_menu.count()):
    #     for item in range(self.ui.frame_menu_verticalLayout.count()):
    #         frm_menu.itemAt(item).widget().setStyleSheet(STYLE_NOT_ACTIVE)
    #
    #     self.ui.stackedWidget.setCurrentWidget(page)
    #     frm_btn.setStyleSheet(STYLE_ACTIVE)




    # SET MAIN WINDOW PAGES
    # ///////////////////////////////////////////////////////////////
    # def set_page(self, page, frm_btn):
    #     for item in range(self.ui.left_menu_verticalLayout.count()):
    #         self.ui.left_menu_verticalLayout.itemAt(item).widget().setStyleSheet(STYLE_NOT_ACTIVE)
    #
    #     if frm_btn != self.ui.frame_btn_log:
    #         self.ui.frame_btn_log.setStyleSheet(STYLE_NOT_ACTIVE)
    #
    #     self.ui.stackedWidget.setCurrentWidget(page)
    #     frm_btn.setStyleSheet(STYLE_ACTIVE)
    #     self.ui.ledit_page.setText(str(self.ui.stackedWidget.currentIndex()))



    def set_page_stackedWidget(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)
        self.ui.ledit_page.setText(str(self.ui.stackedWidget.currentIndex()))


    @staticmethod
    def set_page_statistics_stackedWidget(self, page):
        self.ui.statistics_stackedWidget.setCurrentWidget(page)
        self.ui.ledit_statistics_page.setText(str(self.ui.statistics_stackedWidget.currentIndex()))





    # Получаем Имя Фамилию залогиненого пользователя
    def get_display_name ():
        GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
        NameDisplay = 3

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameEx(NameDisplay, None, size)

        nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameEx(NameDisplay, nameBuffer, size)
        return nameBuffer.value

    # def get_display_loggin (self):
    def get_display_loggin():
        GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
        NameDisplay = 8

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameEx(NameDisplay, None, size)

        nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameEx(NameDisplay, nameBuffer, size)
        return nameBuffer.value


