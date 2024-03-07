# -*- coding: utf-8 -*-
import os

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QMainWindow, QComboBox, QLineEdit, QMessageBox, QGraphicsBlurEffect, QSpacerItem, \
    QLabel, QApplication, QCompleter

from Core.Models.Worker import Usuarios
from Core.Utils.utils import enabled_elements
from Login_System.Verifications_and_Responses.Responses import Responses
from Login_System.Verifications_and_Responses.Verifications import Verifications
from ui.pages.windowTransportCard import TransportCardWindow
from ui.widjets.itemListTransport_widget import ItemListTransportWidget

from ui.windows.ui_ListTransportWindow import Ui_ListTransportWindow





class ListTransportsWindow(QMainWindow):

    def __init__(self, parent=None, widget=None, role=None):
        super(ListTransportsWindow, self).__init__(parent)
        self.ui = Ui_ListTransportWindow()
        self.ui.setupUi(self)
        self.statusBar().setStyleSheet('color: #ffffff;')
        self.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.setWindowTitle(f'Список транспортных средств')

        # Выравнивание окна по центру монитора
        desktop = QApplication.desktop()
        x = (desktop.width() - self.frameSize().width()) // 2
        y = (desktop.height() - self.frameSize().height()) // 2
        self.move(x, y)

        self.parent = parent
        self.role = role

        self.count_item: int = 0
        self.init_filters: bool = False

        self.effect = QGraphicsBlurEffect()
        self.effect.setBlurRadius(4)
        self.setGraphicsEffect(self.effect)
        self.effect.setEnabled(False)


        self.responses = Responses()
        self.verify = Verifications()

        self.users_db = Usuarios()

        self.list_transports = self.users_db.list_transport()
        self.loadingListTransports(self.list_transports)

        self.ui.market_price__min.setText(str(self.list_transports['min_price']))
        self.ui.market_price__max.setText(str(self.list_transports['max_price']))

        self.ui.cb_sorting.addItem('')
        self.ui.cb_sorting.addItem(f'Ближайшее ТО', 'date_next_to')
        self.ui.cb_sorting.addItem(f'Цена аренды по возрастанию', 'payment_categoryed___min_pc')
        self.ui.cb_sorting.addItem(f'Цена аренды по убыванию', 'payment_categoryed___max_pc')
        self.ui.cb_sorting.addItem(f'Пробег по возрастанию', 'prev_mileage___min_pm')
        self.ui.cb_sorting.addItem(f'Пробег по убыванию', 'prev_mileage___max_pm')

        self.ui.type_transport_id.addItem('')
        for type_ts in self.list_transports['types_ts']:
            self.ui.type_transport_id.addItem(type_ts.name, type_ts.id)

        self.ui.status_transport_id.addItem('')
        for status_ts in self.list_transports['status_ts']:
            self.ui.status_transport_id.addItem(status_ts.name, status_ts.id)

        self.ui.color_id.addItem('')
        for color_ts in self.list_transports['color']:
            # print(color_ts.name)
            self.ui.color_id.addItem(color_ts.name, color_ts.id)

        enabled_elements(role = self.role, element = self.ui.btn_add_ts, hideted = 'yes')


        # self.ui.bodywork.setEditable(True)
        self.ui.bodywork.setInsertPolicy(QComboBox.NoInsert)
        # cb_completer = MyCustomQCompleter(self.ui.bodywork)
        cb_completer = QCompleter(self.ui.bodywork)
        cb_completer.setCompletionMode(QCompleter.PopupCompletion)
        cb_completer.setModel(self.ui.bodywork.model())
        self.ui.bodywork.setCompleter(cb_completer)
        cb_completer.popup().setStyleSheet('font-size: 14px; \
                                font-family: Arial, Helvetica, sans-serif; \
                                background-color: rgb(69, 100, 129); \
                                color: #ffffff;')


        self.ui.btn_add_ts.clicked.connect(self.add_transport)


        # brand_all = []
        # for brand in self.list_transports['brands']:
        #     brand_all.append(brand[0])
        # self.ui.cb_brand.addItems(brand_all)
        #
        # models_all = []
        # for model in self.list_transports['models']:
        #     models_all.append(model[0])
        # self.ui.cb_model.addItems(models_all)
        #
        # bodyworks_all = []
        # for bodywork in self.list_transports['bodywork']:
        #     bodyworks_all.append(bodywork[0])
        # self.ui.cb_bodywork.addItems(bodyworks_all)
        #
        # colors_all = []
        # for color in self.list_transports['color']:
        #     colors_all.append(color[0])
        # self.ui.cb_color.addItems(colors_all)

        self.ui.btn_clear_filters.clicked.connect(self.clear_all_filters)

        self.ui.type_transport_id.textActivated.connect(self.filters_in_db)
        self.ui.status_transport_id.textActivated.connect(self.filters_in_db)
        self.ui.brand.textActivated.connect(self.filters_in_db)
        self.ui.model.textActivated.connect(self.filters_in_db)
        self.ui.bodywork.textActivated.connect(self.filters_in_db)
        self.ui.color_id.textActivated.connect(self.filters_in_db)
        self.ui.cb_sorting.textActivated.connect(self.filters_in_db)

        self.ui.market_price__min.editingFinished.connect(self.filters_in_db)
        self.ui.market_price__max.editingFinished.connect(self.filters_in_db)


    def add_transport(self):
        self.effect.setEnabled(True)
        self.card_transport = TransportCardWindow(parent=self, role=self.role)
        self.card_transport.show()

    def filters_in_db(self):

        filter_layout = {}
        def search_filter(layout):
            for i in reversed(range(layout.count())):
                layoutItem = layout.itemAt(i)
                if type(layoutItem) is QSpacerItem:
                    continue

                if layoutItem.widget() is not None:
                    widgetToFilter = layoutItem.widget()
                    if isinstance(widgetToFilter, QLabel):
                        continue

                    if isinstance(widgetToFilter, QComboBox):
                        list_name_cut = widgetToFilter.objectName()

                        if widgetToFilter.currentData():
                            data_filter = widgetToFilter.currentData()
                        else:
                            data_filter = widgetToFilter.currentText()

                    if isinstance(widgetToFilter, QLineEdit):
                        list_name_cut = widgetToFilter.objectName()
                        data_filter = widgetToFilter.text()

                    filter_layout.update({list_name_cut: data_filter})

                else:
                    layoutToFilter = layout.itemAt(i)
                    search_filter(layoutToFilter)

        search_filter(self.ui.layoutFiltersTransports)
        # self.list_new_transports = self.users_db.list_transport(filters=filter_cb)
        # print(filter_layout)
        self.list_new_transports = self.users_db.list_transport(filters=filter_layout)
        self.loadingListTransports(self.list_new_transports)


    @pyqtSlot()
    def loadingListTransports(self, list_all_transports):
        # print('Update после update')

        while self.ui.listTransportLayout.count() > 0:
            item = self.ui.listTransportLayout.takeAt(0)
            item.widget().deleteLater()

        for item in list_all_transports['result_all']:
            self.count_item += 1
            item_transport = ItemListTransportWidget(
                id_widget_item = self.count_item,
                id_ts = item.id,
                brand = item.brand,
                model = item.model,
                bodywork = item.bodywork,
                color_name = item.colored.name,
                color_hex = item.colored.color,
                prev_mileage = item.prev_mileage,
                next_mileage = item.next_mileage,
                market_price = item.market_price,
                date_next_to = item.date_next_to,
                image = item.image,
                name_status = item.statused.name,
                color_status = item.statused.color,
                contract_number = item.contract_number,
                payment_categoryed = item.payment_categoryed.size,
                parent=self,
                role=self.role
            )
            self.ui.listTransportLayout.addWidget(item_transport)

            item_transport.delete_ts.connect(self.delete_item_ts_widget)
            item_transport.mouse_button_dbl_click.connect(self.item_mouse_button_dbl_click_widget)


        self.statusBar().showMessage(f"Выбрано: {list_all_transports['result_all'].count()}")

        # self.ui.cb_type_transport_id.currentText()
        # self.ui.cb_status_transport_id.currentText()
        # self.ui.cb_brand.currentText()
        # self.ui.cb_model.currentText()
        # self.ui.cb_bodywork.currentText()
        # self.ui.cb_color.currentText()

        #
        #
        # self.ui.cb_type_transport_id.clear()
        # self.ui.cb_type_transport_id.addItem('')
        # for type_ts in list_all_transports['types_ts']:
        #     self.ui.cb_type_transport_id.addItem(type_ts.name, type_ts.id)
        #
        # self.ui.cb_status_transport_id.clear()
        # self.ui.cb_status_transport_id.addItem('')
        # for status_ts in list_all_transports['status_ts']:
        #     self.ui.cb_status_transport_id.addItem(status_ts.name, status_ts.id)
        #
        #


        cb_brand_text = self.ui.brand.currentText()
        self.ui.brand.clear()
        self.ui.brand.addItem('')
        brand_all = []
        for brand in list_all_transports['brands']:
            brand_all.append(brand[0])
        self.ui.brand.addItems(brand_all)
        self.ui.brand.setCurrentText(cb_brand_text)


        cb_model_text = self.ui.model.currentText()
        # print('cb_model_text: ', cb_model_text)
        self.ui.model.clear()
        self.ui.model.addItem('')
        models_all = []
        for model in list_all_transports['models']:
            models_all.append(model[0])
        self.ui.model.addItems(models_all)
        self.ui.model.setCurrentText(cb_model_text)


        cb_bodywork_text = self.ui.bodywork.currentText()
        self.ui.bodywork.clear()
        self.ui.bodywork.addItem('')
        bodyworks_all = []
        for bodywork in list_all_transports['bodywork']:
            bodyworks_all.append(bodywork[0])
        self.ui.bodywork.addItems(bodyworks_all)
        self.ui.bodywork.setCurrentText(cb_bodywork_text)


    def clear_all_filters(self):
        for comboboxes in self.ui.groupBox.findChildren(QComboBox):
            comboboxes.setCurrentIndex(-1)

        self.ui.market_price__min.setText(str(self.list_new_transports['min_price']))
        self.ui.market_price__max.setText(str(self.list_new_transports['max_price']))

        self.filters_in_db()


    @pyqtSlot()
    def item_mouse_button_dbl_click_widget(self):
        widget = self.sender()
        self.effect.setEnabled(True)
        self.card_transport = TransportCardWindow(ts_id=int(widget.ui.lbl_id_ts.text()), parent=self, role=self.role)
        self.card_transport.show()


    @pyqtSlot()
    def delete_item_ts_widget(self):
        widget = self.sender()
        self.effect.setEnabled(True)
        self.msg = QMessageBox(self)
        self.msg.setWindowIcon(QIcon(":/Images/logo-mini.png"))
        self.msg.setWindowTitle("Удаление транспортного средства")
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setText(f"Вы уверены, что хотите удалить транспортное средство:  {widget.ui.lbl_brand.text()} {widget.ui.lbl_model.text()} ?")

        self.buttonAceptar = self.msg.addButton("Да, хочу", QMessageBox.YesRole)
        self.buttonCancelar = self.msg.addButton("Отменить", QMessageBox.RejectRole)
        self.msg.setDefaultButton(self.buttonAceptar)

        for button in self.msg.buttons():
            button.setCursor(QCursor(Qt.PointingHandCursor))

        self.msg.exec_()

        if self.msg.clickedButton() == self.buttonAceptar:

            self.users_db.delete_ts(ids = widget.ui.lbl_id_ts.text())

            self.ui.listTransportLayout.removeWidget(widget)
            widget.deleteLater()
            self.effect.setEnabled(False)
            self.filters_in_db()
            # self.remove_photo.connect(self.remove_photo_ts_item(photo=photo_ts))
            # print('image: ', widget.image)
            os.remove(widget.image)

        elif self.msg.clickedButton() == self.buttonCancelar:
            self.effect.setEnabled(False)

    # @pyqtSlot()
    # def update (self) -> None:
    #     print('UPDATERRRRRRRRRRRRRRRRRRRR ListTransports')
    #     self.filters_in_db()







