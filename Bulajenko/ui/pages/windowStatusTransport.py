# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Core.Models.Worker import Usuarios

from ui.widjets.statusTransport_widget import StatusTransportWidget

from ui.windows.ui_StatusTransportWindow import Ui_StatusTransportWindow



class StatusTransportWindow(QMainWindow):

    def __init__(self, parent=None, widget=None):
        super(StatusTransportWindow, self).__init__(parent)
        self.ui = Ui_StatusTransportWindow()
        self.ui.setupUi(self)

        self.parent = parent

        self.setMinimumWidth(widget.rect().width())


        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.users_db = Usuarios()

        self.id_count_status: int = 0

        self.listStatusTransport()

        # calculate the botoom right point from the parents rectangle
        point = widget.rect().bottomRight()

        # map that point as a global position
        global_point = widget.mapToGlobal(point)

        # print(global_point)
        # print('size menu: ', self.rect().width(), self.rect().height())
        # print('size button: ', widget.rect().width(), widget.rect().height())

        # by default, a widget will be placed from its top-left corner, so
        # we need to move it to the left based on the widgets width
        self.move(global_point - QPoint(self.width(), self.rect().height() // 2 + widget.rect().height() // 2))

    # @pyqtSlot()
    def listStatusTransport(self):
        for item in self.users_db.status_transport():
            self.id_count_status += 1
            add_statuswidget = StatusTransportWidget(id_widget_status = self.id_count_status, id_status = item.id, name = item.name, color = item.color, parent = self)
            self.ui.list_status_layout.addWidget(add_statuswidget)
            add_statuswidget.clickedStatus.connect(self.selected_status)

    @pyqtSlot()
    def selected_status(self):
        widget = self.sender()
        # print(widget.ui.btn_status.text(), widget.ui.lbl_id.text(), widget.ui.lbl_color.text())
        self.parent.ui.btn_select_status.setText(widget.ui.btn_status.text())
        self.parent.ui.btn_select_status.setStyleSheet(f"border: none; background-color: %s;" % (widget.ui.lbl_color.text()))
        self.parent.ui.lbl_id_status.setText(widget.ui.lbl_id.text())
        self.close()
