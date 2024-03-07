import os
import sys

from PyQt5.QtWidgets import QApplication

from Core.Models.Models import create_db, PATH_DATA_DB
from Login_System.login_sys_code import LoginSystem

# pyrcc5 -o resurce_rc.py resurce.qrc


if __name__ == '__main__':

	db_is_created = os.path.exists(PATH_DATA_DB)
	if not db_is_created:
		create_db()

	StyleApp = """  
        QMainWindow, QMessageBox{	
           /* background-color: rgba(255, 255, 255, 255);*/
            border: 1px solid rgba(255, 165, 0, 230); 
            font-size: 10pt;
        }      
        QWidget, QFrame{	
            background-color: #191919;
        }        
        
        QFrame#frame{border-bottom: 1px solid orange;}
        
         QFrame[objectName^=frm_settings], QWidget[objectName^=scroll_settings]{
            border: none;
            background-color: #232323;
        }
        
        
        #central, #centralwidget, QMenu, QCalendarWidget{	
            border: 1px solid rgba(255, 165, 0, 100);    
            /*border: 1px solid orange;       */
        }
        QStatusBar{
            /*background: rgba(255, 165, 0, 100); */
            background-color: rgba(57, 57, 57, 100);      
        }        
        QStatusBar::item {
            border: 5px solid rgba(255, 165, 0, 250);
            border-radius: 3px;
        }
        QStatusBar QLabel {
            border: 3px solid white;
        }
        QSizeGrip{
            background-color: transparent;      
        }
        
        QMenu, QCheckBox, QDateEdit, QDateTimeEdit{
            color: rgb(231, 231, 231);
        }
        QRadioButton::indicator, QCheckBox::indicator { width: 18px; height: 18px;}
        QRadioButton::indicator:unchecked {
             image: url(:/Icons/icons/circle_.svg);
        }
        QRadioButton::indicator:checked {
             image: url(:/Icons/icons/check-circle_.svg);
        }
        QCheckBox::indicator:unchecked {
             image: url(:/Icons/icons/square_.svg);
        }
        QCheckBox::indicator:checked {
             image: url(:/Icons/icons/check-square_.svg);
        }
        
        QCheckBox:disabled { 
            color: rgba(173, 173, 173, 200);
            /*color: #adadad;*/
        }        
        
        QCheckBox#sms::indicator:unchecked:disabled {
            image: url(:/Icons/icons/square_disabled.svg);
        }       
        
        QMenu::separator{
            height: 1px;
            border: none;
            background: rgba(255, 165, 0, 100);
            margin-left: 5px;
            margin-right: 5px;
        }
        QMenu::item:selected {
            background-color: rgb(255, 165, 0);
            color: rgb(255, 255, 255);
        }
        QLineEdit, QComboBox, QDateEdit, QDateTimeEdit{
            font-family: "Liberation Sans",sans-serif;
            font-size: 11pt;
            border: none;
            border-bottom: 2px solid transparent;
            padding: 0 5px;
            color: rgb(231, 231, 231);            
            background-repeat: no-repeat;
            background-position: left center;
            background-color: #393939;
        }   
        QLineEdit:focus, #LoginWindow #le_username:focus, #LoginWindow #le_password:focus{
            border-bottom: 2px solid orange;
        }  
        
        QScrollArea{border: none;}
        
        QGroupBox{border: none;}
        QGroupBox::title {
            color: white;
            background-color: transparent;
            subcontrol-origin: margin;
            subcontrol-position: top left;
        }
        
        #grb_equipment{margin-top: 10px; font-size: 10pt;}        
        #grb_equipment::title {;
            subcontrol-origin: padding;
            padding: -25px 5px 0 12px; 
            /*min-height: 39px;*/
        }
        QPushButton#btn_add_client{
            text-align: left;
            padding: 10px;
        }
               
        
        QGroupBox::indicator {
            width: 13px;
            height: 13px;
        }
        
        QGroupBox::indicator:unchecked {
            image: url(:/Icons/icons/check-circle_.svg);
        }   
        
        QLabel, QRadioButton, QTextEdit, QStatusBar{
            color: white;
            font-size: 10pt;
            font: 'Arial';            
        }  
        
        QLabel, QRadioButton, QTextEdit{
            background-color: transparent;
        } 
        
        QLabel#lbl_error, QLabel#lbl_error_2{font-size: 8pt;}
        QLabel#lbl_fio_arendator{font-size: 11pt;}
        
        
        QLabel#lbl_fio_arendator:hover, 
        QLabel#lbl_transport_model:hover{
            color: orange;
        }        
        
        QLabel#lbl_phone, QLabel#lbl_msg{font-size: 7pt;}
        
        QLabel#lbl_vikup{
            font-size: 8pt;
            color: green;
        }
      
        #LoginWindow #le_username, #LoginWindow #le_password{
            font: 15pt "Verdana";
            border-bottom: 2px solid grey;            
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
            border-bottom-left-radius: 3px;
            border-bottom-right-radius: 3px;
            padding: 0 5px 0 40px;
        }
        #btnClose{
            color: black;
            background-color: orange;
            border-radius: 1px;
        }
        #btnClose:hover, #btnSignIn:hover, #add_phone:hover{
            background-color: rgb(222, 141, 0);
        }
        
        QPushButton{
            color: rgb(231, 231, 231);            
            border: 2px solid orange;
            padding: 5px;
            border-radius: 3px;
            opacity: 200;
        }
        QPushButton:hover{
            background-color: orange;
        }
        
        QPushButton:disabled{  
            border: 2px solid qrey;
            color: rgba(195, 195, 195, 200);
            /*change-cursor: cursor('Forbidden');*/
            cursor: not-allowed;
        }
        
        #btnSignIn{
            font: 17pt "Verdana";
        }
        
       
        
        QPushButton[objectName^=btn_save],
        QPushButton[objectName^=btn_delete],
        QPushButton[objectName^=add_phone],
        QPushButton[objectName^=delete_phone]{
            border: none;
            border-radius: 3px;
            padding: 0;
        }
        QPushButton[objectName^=btn_delete]{	
            background-color: #d60000;
        }
        
        QPushButton[objectName^=btn_save]{	
            background-color: #2c9934;
        }        
        QPushButton[objectName^=btn_save]:hover{	
            background-color: #37be40;
        }
        
        QPushButton[objectName^=btn_delete]:hover,
        QPushButton[objectName^=delete_phone]:hover{	
            background-color: rgb(235, 0, 0);
        }
        
         
        QComboBox, QDateEdit, QDateTimeEdit{
            padding: 5px;
            min-width: 100px;
            color: white;
            border: none;
        }    
        QComboBox QAbstractItemView{
            font: 12pt "Verdana";            
            background-color: #7e8b98;
            selection-background-color: #2a79a3;
            outline-color: 0em;
            border-radius: 3px;
            padding-bottom: 5px;
        }   
        
        QComboBox QAbstractItemView::item {
            padding-left: 5px;
            padding-bottom: 5px;
            line-height: 1.5em;
        }
        
        QComboBox QListView {
            background-color: #2e2e2e;                       
        /*  outline: 0;                    попробуйте так    */
            outline: 2px solid orange;     /*    или так        */            
            color: white;
            selection-background-color: #5e5e5e;
            padding: 5%;            
        }  
        QComboBox::down-arrow:pressed {
            position: relative;
            top: 1px; left: 1px;
        }
            
        QComboBox::drop-down, QDateEdit::drop-down, QDateTimeEdit::drop-down
            {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;            
                border-left-width: 1px;
                border-left-style: solid;
                border-top-right-radius: 2px;
                border-bottom-right-radius: 2px;
            } 
            QComboBox::down-arrow, QDateEdit::down-arrow, QDateTimeEdit::down-arrow
            {
                border-image: url(:/Icons/icons/chevrons-down_.svg);
                width: 20px;
                height: 20px;
                margin-right: 5px;
            }
            
            QComboBox::down-arrow:on, QDateEdit::down-arrow:on, QDateTimeEdit::down-arrow:on
            {
                border-image: url(:/Icons/icons/chevrons-up_.svg);
                width: 20px;
                height: 20px;
                margin-right: 5px;
            } 
        QToolBar{
            border: 1px solid rgba(255, 165, 0, 200);
        } 
        QToolButton{
            margin: 5px;
        }           
        QToolButton:hover{
            background-color: orange;
            border-radius: 3px;
            cursor: pointer;
        }
        
        
        QCalendarWidget{
            width: 460px;
            min-width: 460px;
            max-width: 460px;
        }
        QCalendarWidget QToolButton{
            color: rgb(231, 231, 231);            
            border: 1px solid orange;
            padding: 5px;
            border-radius: 2px;
            opacity: 200;
            color: white;
            font-size: 14px;
            icon-size: 20px, 20px;            
        }
        #qt_calendar_prevmonth{
            qproperty-icon: url(:/Icons/icons/chevrons-left_.svg);
        }
        #qt_calendar_nextmonth{
            qproperty-icon: url(:/Icons/icons/chevrons-right_.svg);
        }
        #qt_calendar_prevmonth, #qt_calendar_nextmonth{
            min-width: 40px;
            max-width: 40px;
            min-height: 24px;
            max-height: 24px;
        }
        /* #qt_calendar_yearbutton, #qt_calendar_monthbutton */
        #qt_calendar_monthbutton {
            width: 120px;
            min-width: 120px;
            max-width: 120px;
        }     
        #qt_calendar_yearbutton {
            width: 100px;
            min-width: 100px;
            max-width: 100px;
        }    

        QCalendarWidget QMenu {
            width: 130px;
            left: 10px;
            color: white;
            font-size: 14px;
            background-color: rgb(100, 100, 100);
        }
        QCalendarWidget QToolButton::menu-indicator {
            image: url(:/Icons/icons/chevron-down_.svg);      /*  Удалите маленькую стрелку под выбором месяца !!! */
            width: 20px;
            height: 20px;
            subcontrol-position: right center;                /* Право по центру */
        }
        QCalendarWidget QSpinBox { 
            width: 70px; 
            font-size:16px; 
            color: white; 
            selection-background-color: rgb(136, 136, 136);
            selection-color: rgb(255, 255, 255);
        }
        QCalendarWidget QSpinBox{
            color: rgb(231, 231, 231);            
            background-repeat: no-repeat;
            background-position: left center;
            background-color: #393939;
        }   
        QCalendarWidget QSpinBox::up-button { 
            subcontrol-origin: border;  
            subcontrol-position: top right; 
            border-image: url(:/Icons/icons/chevron-up_.svg);
            width: 30px;
            height: 20px;
        }
        QCalendarWidget QSpinBox::down-button {
            subcontrol-origin: border; 
            subcontrol-position: bottom right; 
            border-image: url(:/Icons/icons/chevron-down_.svg);
            width: 30px;
            height: 20px;
        }
		QSpinBox::up-button:hover, QSpinBox::down-button:hover, QSpinBox::up-button:pressed, QSpinBox::down-button:pressed{background-color:orange;}
        QCalendarWidget QSpinBox::up-arrow { width:30px;  height:24px; }
        QCalendarWidget QSpinBox::down-arrow { width:30px;  height:24px; }
        
        /* header row */
        QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }
        
        /* normal days */
        QCalendarWidget QAbstractItemView:enabled 
        {
            font-size:20px; 
            color: rgb(180, 180, 180);  
            background-color: black;  
            selection-background-color: rgb(64, 64, 64); 
            selection-color: rgb(0, 255, 0); 
        }
        QCalendarWidget QAbstractItemView:disabled 
        { 
            color: rgb(64, 64, 64); 
        }
        
        QCalendarWidget QTableView{
            alternate-background-color: #393939;  /* day name/week number background */
        }
        QCalendarWidget#qt_calendar_calendarview {
            outline: 0px;
            selection-background-color: rgb(0, 188, 212); 
        }
        
        QTabWidget::pane { /* The tab widget frame */
            border-top: 2px solid orange;
        }
        
        QTabWidget::tab-bar {
            left: 10px; /* move to the right by 5px */
        }
        QTabBar::tab {
            background: transparent;
            border: 2px solid orange;
            /* border-bottom-color: #C2C7CB; same as the pane color */
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            min-width: 80px;
            padding: 10px;
            color: white;
        }
        QTabBar::tab:selected, QTabBar::tab:hover {
            background: orange;
        }
        /* QTabBar::tab:selected {
            border-color: #9B9B9B;
            border-bottom-color: #C2C7CB; same as pane color 
        }*/
        
        QTabBar::tab:!selected {
            margin: 5px; /* make non-selected tabs look smaller */
        }        
      
       
    
    """

	app = QApplication(sys.argv)
	app.setStyleSheet(StyleApp)
	system = LoginSystem()
	# system = MainBaseWindow()
	# system = ColorTransportWindow()
	# system = ArendatorWindow(id_arendator = 2)
	# system = ListArendatorsWindow()
	# system = PaymentArendatorWindow(id_arendator_confirm=1, fio_arendator_confirm='пупкин иван	степанович')
	# system = TransportCardWindow()
	# system = ListTransportsWindow()
	# system = StatusTransportWindow()
	# system = AdminWindow()
	# system = RoleForm()
	# system = WindowReturnVehicle()
	system.show()
	sys.exit(app.exec_())

# https://www.w3.org/TR/selectors-3/#attribute-selectors
#
#
# [att^=val]
# Представляет элемент с att атрибутом, значение которого начинается с префикса "val". Если «val» — пустая строка, то селектор ничего не представляет.
# [att$=val]
# Представляет элемент с att атрибутом, значение которого заканчивается суффиксом "val". Если «val» — пустая строка, то селектор ничего не представляет.
# [att*=val]
# Представляет элемент с att атрибутом, значение которого содержит хотя бы один экземпляр подстроки "val". Если «val» — пустая строка,
# то селектор ничего не представляет.
#
#
# Примеры:
#
# Следующий селектор представляет HTML object, ссылающийся на изображение:
# object[type^="image/"]
#
# Следующий селектор представляет привязку HTML aс hrefатрибутом, значение которого заканчивается на «.html».
# а[href$=".html"]
#
# Следующий селектор представляет абзац HTML с titleатрибутом, значение которого содержит подстроку «hello».
# p[title*="hello"]


# QFrame[frameShape="4"] /* QFrame::HLine == 0x0004 */
# {}
# QFrame[frameShape="5"] /* QFrame::VLine == 0x0005 */
# {}


# /* Reference (from doc.qt.io/qt-5/qframe.html#types):
#  * - frameShape[4] --> QFrame::HLine = 0x0004
#  * - frameShape[5] --> QFrame::VLine = 0x0005
#  * - frameShadow[16] --> QFrame::Plain = 0x0010 (default for most widgets)
#  * - frameShadow[48] --> QFrame::Sunken = 0x0030 (default for HLine/VLine)
#  */
# QFrame[frameShape="4"][frameShadow="16"],
# QFrame[frameShape="5"][frameShadow="16"]
# {
#     ...
# }
#
# QFrame[frameShape="4"][frameShadow="48"],
# QFrame[frameShape="5"][frameShadow="48"]
# {
#     ...
# }
