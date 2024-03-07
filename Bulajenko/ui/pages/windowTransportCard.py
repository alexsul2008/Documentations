# -*- coding: utf-8 -*-
import os.path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLineEdit, QSpacerItem, QLabel

from Core.Models.Models import UPLOAD_FOLDER
from Core.Models.Worker import Usuarios
from Core.Utils.utils import object_name, enabled_elements

from ui.pages.windowColorTransport import ColorTransportWindow
from ui.pages.windowStatusTransport import StatusTransportWindow

from ui.windows.ui_TransportCardWindow import Ui_TransportCardWindow

from Login_System.Verifications_and_Responses.Responses import Responses



class TransportCardWindow(QMainWindow):

    def __init__(self, ts_id: int = None, parent=None, role=None):
        super(TransportCardWindow, self).__init__(parent)
        self.ui = Ui_TransportCardWindow()
        self.ui.setupUi(self)
        self.statusBar().setStyleSheet('color: #ffffff;')
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'Карточка транспортного средства')
        self.filename = None

        self.ts_id = ts_id
        self.parent = parent
        self.role = role

        if self.role not in ['root', 'admin']:
            self.denable_all_fields(True)
            self.ui.frm_purchase_price.setStyleSheet('background: transparent; color: transparent;')

        self.ui.lbl_photo.setStyleSheet('border: 1px solid orange;')

        self.responses = Responses()
        # self.verify = Verifications()

        self.users_db = Usuarios()

        # Ценовая категория
        for pcat in self.users_db.payment_category_db():
            self.ui.payment_category.addItem(str(pcat.size), pcat.id)

        # Тип ТС
        for item in self.users_db.type_transport():
            self.ui.cb_type_transport_id.addItem(item.name, item.id)

        # Установка статуса по умолчанию из поля Default
        default_status = self.users_db.status_transport(default=True)
        if default_status:
            self.ui.btn_select_status.setText(default_status.name)
            self.ui.lbl_id_status.setText(str(default_status.id))
            self.ui.btn_select_status.setStyleSheet(f"border: none; background-color: %s;" % (default_status.color))

        # Установка цвета по умолчанию из поля Default
        default_color = self.users_db.color_transport(default = True)
        if default_color:
            self.ui.lbl_id_color.setText(str(default_color.id))
            self.ui.btn_select_color.setText(default_color.name)
            self.ui.btn_select_color.setStyleSheet(f"border: none; background-color: %s;" % (default_color.color))


        if self.ts_id is not None:
            self.ui.btn_cancel.setText('Закрыть')
            self.get_ts = self.users_db.get_transport_in_id(self.ts_id)
            print(self.get_ts.date_purchase)
            self.ui.lbl_ts_id.setText(str(self.get_ts.id))
            self.ui.le_brand.setText(self.get_ts.brand)
            self.ui.le_model.setText(self.get_ts.model)
            self.ui.le_bodywork.setText(self.get_ts.bodywork)
            self.ui.lbl_id_color.setText(str(self.get_ts.color_id))

            self.ui.btn_select_color.setStyleSheet(f"border: none; background-color: %s;" % (self.get_ts.colored.color))
            self.ui.btn_select_color.setText(self.get_ts.colored.name)
            self.ui.btn_select_color.setEnabled(False)
            enabled_elements(role = self.role, element = self.ui.btn_select_color, enableted = 'yes')

            self.ui.le_engine_volume.setText(str(self.get_ts.engine_volume))
            self.ui.de_date_purchase.setDate(self.get_ts.date_purchase)
            self.ui.le_place_purchase.setText(self.get_ts.place_purchase)
            self.ui.le_number_engine.setText(self.get_ts.number_engine)
            self.ui.market_price.setText(str(self.get_ts.market_price))
            self.ui.purchase_price.setText(str(self.get_ts.purchase_price))
            self.ui.number_simcard.setText(str(self.get_ts.number_simcard))
            self.ui.gps_id.setText(str(self.get_ts.gps_id))
            self.ui.type_gps.setText(str(self.get_ts.type_gps))
            self.ui.de_date_prev_to.setDate(self.get_ts.date_prev_to)
            self.ui.de_date_next_to.setDate(self.get_ts.date_next_to)
            self.ui.le_prev_mileage.setText(str(self.get_ts.prev_mileage))
            self.ui.le_next_mileage.setText(str(self.get_ts.next_mileage))
            self.ui.le_comment_prev_to.setText(self.get_ts.comment_prev_to)
            self.ui.le_comment_next_to.setText(self.get_ts.comment_next_to)
            self.ui.te_comment_general.setPlainText(self.get_ts.comment_general)
            self.ui.cb_type_transport_id.setCurrentText(self.get_ts.type_transported.name)

            self.ui.payment_category.setCurrentText(str(self.get_ts.payment_categoryed.size))

            contract_number = self.get_ts.contract_number if self.get_ts.contract_number != 0 else ''
            nomer = '№' if contract_number != '' else ''

            self.ui.btn_select_status.setText(f'{self.get_ts.statused.name} {nomer}{contract_number}')
            self.ui.btn_select_status.setStyleSheet(f"border: none; background-color: %s;" % (self.get_ts.statused.color))
            # self.ui.btn_select_status.setEnabled(False)

            enabled_elements(role = self.role, element = self.ui.btn_select_status, enableted = 'yes')

            self.ui.lbl_id_status.setText(str(self.get_ts.status_transport_id))

            self.ui.lbl_filename.setText(self.get_ts.image)
            pixmap = QPixmap(os.path.join(UPLOAD_FOLDER, self.get_ts.image))
            pixmap_resized = pixmap.scaled(self.ui.lbl_photo.width() - 2, self.ui.lbl_photo.height(), Qt.KeepAspectRatio,
                                           Qt.FastTransformation)
            self.ui.lbl_photo.setPixmap(pixmap_resized)


        self.ui.btn_image_upload.clicked.connect(self.upload_image)

        self.ui.btn_save.clicked.connect(self.create_or_update_transport)
        self.ui.btn_cancel.clicked.connect(lambda: self.cancel_transport())
        self.ui.btn_select_status.clicked.connect(self.select_status_transport)
        self.ui.btn_select_color.clicked.connect(self.select_color_transport)



    def upload_image(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Открыть картинку', './', "Image (*.png *.jpg *jpeg)")
        if file:

            filename = object_name(file.split('/')[-1]) + '.jpg'

            pixmap = QPixmap(file)
            pixmap_resized = pixmap.scaled(self.ui.lbl_photo.width() - 2, self.ui.lbl_photo.height(), Qt.KeepAspectRatio, Qt.FastTransformation)
            pixmap_resized.save(os.path.join(UPLOAD_FOLDER, filename))
            self.ui.lbl_photo.setPixmap(pixmap_resized)

            self.ui.lbl_filename.setText(filename)


    def create_or_update_transport(self):
        # print('Ok1')

        self.items_transport = self.create_items_transport()
        id_ts, responce = self.users_db.add_transport_db(fields = self.items_transport)

        # print(f'Responce: {responce}')

        if responce == 'save':
            self.ui.lbl_ts_id.setText(str(id_ts))
            self.responses.message_from_db(responce, self.statusBar(), f'ТС успешно добавлено')
            if self.ui.lbl_ts_id.text() != '':
                self.ui.btn_cancel.setText('Закрыть')
        elif responce == 'update':
            self.responses.message_from_db(responce, self.statusBar(), f'Данные ТС успешно обновлены')
        elif responce == 'error':
            self.responses.message_from_db(responce, self.statusBar(), f'Что-то пошло не так! Попробуй ещё раз.')


        # print(f'Parent {self.parent.objectName()}')

        if self.parent.objectName() == 'ListArendatorWindow':
            self.parent.update()
        elif self.parent.objectName() == 'MainWindow':
            pass
        else:
            self.parent.filters_in_db()


    def create_items_transport(self):
        list_items_transport = {
            'ts_id': self.ui.lbl_ts_id.text() if self.ui.lbl_ts_id.text() != '' else 0,
            'brand': self.ui.le_brand.text().strip(),
            'model': self.ui.le_model.text().strip(),
            'bodywork': self.ui.le_bodywork.text().strip(),
            'engine_volume': self.ui.le_engine_volume.text().strip(),
            'date_purchase': self.ui.de_date_purchase.date().toPyDate(),
            'place_purchase': self.ui.le_place_purchase.text().strip(),
            'number_engine': self.ui.le_number_engine.text().strip(),
            'market_price': self.ui.market_price.text().strip(),
            'purchase_price': self.ui.purchase_price.text().strip(),
            'number_simcard': self.ui.number_simcard.text().strip(),
            'gps_id': self.ui.gps_id.text().strip(),
            'type_gps': self.ui.type_gps.text().strip(),
            'date_prev_to': self.ui.de_date_prev_to.date().toPyDate(),
            'date_next_to': self.ui.de_date_next_to.date().toPyDate(),
            'prev_mileage': self.ui.le_prev_mileage.text().strip(),
            'next_mileage': self.ui.le_next_mileage.text().strip(),
            'comment_prev_to': self.ui.le_comment_prev_to.text().strip(),
            'comment_next_to': self.ui.le_comment_next_to.text().strip(),
            'comment_general': self.ui.te_comment_general.toPlainText(),
            'image': self.ui.lbl_filename.text(),
            'type_transport_id': self.ui.cb_type_transport_id.itemData(self.ui.cb_type_transport_id.currentIndex()),
            'status_transport_id': self.ui.lbl_id_status.text(),
            'color_id': self.ui.lbl_id_color.text(),
            'paymentcategory_id': self.ui.payment_category.itemData(self.ui.payment_category.currentIndex())
        }

        return list_items_transport


    def closeEvent(self, event) -> None:
        # print('closeEvent: ', event)
        self.parent.effect.setEnabled(False)
        if self.parent.objectName() == 'ListTransportWindow':
            for widget in self.findChildren(QLineEdit):
                widget.clear()
            self.parent.filters_in_db()


    def cancel_transport(self):
        self.parent.effect.setEnabled(False)
        self.close()


    def select_status_transport(self):
        self.status = StatusTransportWindow(self, self.ui.btn_select_status)
        self.status.show()


    def select_color_transport (self):
        self.color = ColorTransportWindow(self, self.ui.btn_select_color)
        self.color.show()


    def denable_all_fields (self, bool):
        if bool:
            def search_field (layout):
                for i in reversed(range(layout.count())):
                    layoutItem = layout.itemAt(i)
                    if type(layoutItem) is QSpacerItem:
                        continue

                    if layoutItem.widget() is not None:
                        widgetToFilter = layoutItem.widget()
                        if isinstance(widgetToFilter, QLabel):
                            continue

                        if widgetToFilter.objectName() not in ['lbl_photo', 'btn_save', 'btn_cancel', 'de_date_prev_to', 'le_prev_mileage', 'le_comment_prev_to', 'de_date_next_to', 'le_next_mileage', 'le_comment_next_to']:
                            widgetToFilter.setEnabled(False)
                        else:
                            continue
                    else:
                        layoutToFilter = layout.itemAt(i)
                        search_field(layoutToFilter)

            search_field(self.ui.all_fields_layout)




        # print('X: ', self.ui.btn_select_status.x())
        # print('Y: ', self.ui.btn_select_status.y())
        # print('Rect size: ', self.ui.btn_select_status.rect().size())
        # print('Size: ', self.ui.btn_select_status.size())
        # print('Geometry size: ', self.ui.btn_select_status.geometry().size())
        # print('Geometry: ', self.ui.btn_select_status.geometry())
        # print('Geometry width: ', self.ui.btn_select_status.geometry().width())
        # print('Geometry height: ', self.ui.btn_select_status.geometry().height())
        # print('frameGeometry: ', self.ui.btn_select_status.frameGeometry())
        # print('frameGeometry size: ', self.ui.btn_select_status.frameGeometry().size())
        # print('frameGeometry width: ', self.ui.btn_select_status.frameGeometry().width())
        # print('frameGeometry height: ', self.ui.btn_select_status.frameGeometry().height())
        # print('frameGeometry topLeft: ', self.ui.btn_select_status.frameGeometry().topLeft())
        # print('pos: ', self.ui.btn_select_status.pos())
        # print('pos x ', self.ui.btn_select_status.pos().x())
        # print('pos y: ', self.ui.btn_select_status.pos().y())







