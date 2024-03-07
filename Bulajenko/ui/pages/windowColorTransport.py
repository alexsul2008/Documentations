# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Core.Models.Worker import Usuarios

from ui.widjets.colorTransport_widget import ColorTransportWidget

from ui.windows.ui_ColorTransportWindow import Ui_ColorTransportWindow




class ColorTransportWindow(QMainWindow):

    def __init__(self, parent=None, widget=None):
        super(ColorTransportWindow, self).__init__(parent)
        self.ui = Ui_ColorTransportWindow()
        self.ui.setupUi(self)

        self.parent = parent
        #
        self.setMinimumWidth(widget.rect().width())
        self.setMaximumWidth(widget.rect().width())

        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.users_db = Usuarios()

        self.id_count_color: int = 0

        self.listColorTransport()

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
    def listColorTransport(self):
        for item in self.users_db.color_transport():
            self.id_count_color += 1
            add_colorwidget = ColorTransportWidget(id_widget_color = self.id_count_color, id_color = item.id, name = item.name, color = item.color,
                                                    parent = self)
            # print(f'Высота цвета: {add_colorwidget.height()} номер цвета: {self.id_count_color}')
            self.ui.list_color_layout.addWidget(add_colorwidget)
            add_colorwidget.clickedColor.connect(self.selected_color)

        self.setFixedHeight(34 * self.id_count_color)

    @pyqtSlot()
    def selected_color(self):
        widget = self.sender()
        self.parent.ui.btn_select_color.setText(widget.ui.btn_name.text())
        self.parent.ui.btn_select_color.setStyleSheet(f"border: none; background-color: %s;" % (widget.ui.lbl_color.text()))
        self.parent.ui.lbl_id_color.setText(widget.ui.lbl_id.text())
        self.close()
