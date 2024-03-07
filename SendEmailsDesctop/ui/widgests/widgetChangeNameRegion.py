
from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QIcon, QColor
from PySide2.QtWidgets import QGraphicsDropShadowEffect, QMainWindow, QTableWidgetItem

from models.worker import SyncORM
# from models.newworker import Worker
from ui.gt_base_ui.ui_windowChangeNameRegion import Ui_WindowChangeNameRegion



class ChangeNameRegionWidget(QMainWindow):
    currentTextRegion = Signal(str)

    def __init__(self, id_region: int = 0, cur_index: int = 0, name_region=None, parent=None):
        super(ChangeNameRegionWidget, self).__init__()
        self.ui = Ui_WindowChangeNameRegion()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icon.ico'))

        self.setWindowModality(Qt.ApplicationModal)

        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))

        # self.ui.le_name_region.installEventFilter(self)

        self.id_region = id_region
        self.name_region = name_region
        self.cur_index = cur_index
        self.parent = parent

        # print(f'Parent: {self.parent}')

        self.ui.lbl_id_region.setText(str(self.id_region))
        self.ui.le_name_region.setText(self.name_region)

        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_save_region.clicked.connect(self.saveNameRegion)

        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.frame_top.mouseMoveEvent = moveWindow

    def mousePressEvent (self, event):
        self.clickPosition = event.globalPos()

    def closeEvent(self, event):
        self.parent.effect.setEnabled(False)
        super(ChangeNameRegionWidget, self).closeEvent(event)

    def saveNameRegion(self):
        save_name = SyncORM.updateRegionORM(id_region = self.id_region, value = self.ui.le_name_region.text().strip())
        # save_name = True
        if save_name:
            self.parent.ui.cb_list_regions.setCurrentText(self.ui.le_name_region.text().strip())
            self.parent.ui.lbl_selected_region.setText(self.ui.le_name_region.text().strip())
            item = QTableWidgetItem("{}".format(self.ui.le_name_region.text().strip()))
            self.parent.ui.emails_region.setItem(self.cur_index - 1, 0, item)
            self.parent.effect.setEnabled(False)
            self.close()
        else:
            self.responses.error_message_status_bar(
                self.statusBar(),
                'Что-то пошло не так! Попробуйте позже ещё раз!',
                3000
            )

