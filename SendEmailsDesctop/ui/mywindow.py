# -*- coding: utf-8 -*-
import json
import os
import re
import time
# import time
import traceback
from datetime import datetime, timedelta
import sys
import shutil
# from functools import partial
# import random

import win32com.client as win32
# import win32com.client

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Slot, QPropertyAnimation, QSortFilterProxyModel, Qt, QAbstractTableModel, QTimer, QEventLoop, QEvent, QObject, QDate, \
	QDateTime
from PySide2.QtGui import Qt, QColor, QIcon, QMovie
from PySide2.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QCompleter, QComboBox, QTableWidgetItem, \
	QDataWidgetMapper, QSizeGrip, QFileDialog, QGraphicsBlurEffect, QProgressBar, QStyledItemDelegate, QSpacerItem, \
	QLabel, QLineEdit, QGroupBox, QRadioButton, QDateEdit, QPushButton, QListWidgetItem, QDesktopWidget, QAbstractButton

from models.database import sync_engine, sync_engine_gasi, session_factory, session_factory_gasi, currect_connect_in_db
from models.models import LIST_USERS_ADMIN  # PATH_DATA,
from models.worker import SyncORM
from models.worker_gasi import SyncGasiORM
from tools.CustomQCompleter import MyCustomQCompleter  # , CompleterItemDelegate
from tools.Responses import Responses
from tools.Verifications import Verifications
# from tools.toast import Toast
from ui.gt_base_ui.ui_mywindow import Ui_MainWindow
from ui.addemail_widget import AddEmailOperatorWidget

# from models.newworker import Worker
from ui.gt_base_ui.ui_windowAddEmail import Ui_WindowAddEmailOperator
from ui.widgests.listIncidents_widget import BaseItemIncidentsWidget
from ui.widgests.listsAdmins_widget import ListAdminsWidget
from ui.widgests.widgetChangeNameRegion import ChangeNameRegionWidget
# from ui.widgests.widgetChangeNameRegion import ChangeNameRegionWidget
from ui.windows.functions_main_window import MainFunctions, STYLE_HOVER

from utils import check, convertJsonToList, get_extension, hidden_visible_obj

from convert_csv import (
	uploadDataSpInPandas,
	savePandasMgmn,
	downloadEmailsAllRegionsInDb,
	csvListOperatorsORM,
	downloadEmailsAllOperatorsJson
)


# os.system('pyside2-rcc resource.qrc -o resource_rc.py')

import ctypes
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
time.sleep(1)

countListFieldEmailOperator = 0

USER = MainFunctions.get_display_loggin()
USERCURRENT = MainFunctions.get_display_name()

STATUS_COLOR = {
	'INFO': QColor(61, 174, 233),
	'ADD': QColor(143, 188, 143),
	'DELETE': QColor(118, 121, 124),
	'ERROR': QColor(255, 0, 0),
	'OPEN': QColor(89, 131, 167),
	'CLOSED': QColor(62, 90, 116),
	'INCIDENT': QColor(46, 208, 60)
}

class MySortFilterProxyModel(QSortFilterProxyModel):
	def __init__(self, role=None, parent=None):
		super(MySortFilterProxyModel, self).__init__(parent)

		self.role = role
		self.minDate = QDate()
		self.maxDate = QDate()

	def setFilterMinimumDate(self, date):
		self.minDate = date
		self.invalidateFilter()

	def filterMinimumDate(self):
		return self.minDate

	def setFilterMaximumDate(self, date):
		self.maxDate = date
		self.invalidateFilter()

	def filterMaximumDate(self):
		return self.maxDate

	def lessThan (self, left, right):
		leftData = self.sourceModel().data(left, self.role)
		rightData = self.sourceModel().data(right, self.role)
		if leftData is None:
			return True
		elif rightData is None:
			return False
		elif type(leftData) != type(rightData):
		# don't want to sort at all in these cases, False is just a copout ...
		# should warn user
			return False
		return leftData < rightData


# class DataframeQSortFilterProxyModel(QtCore.QSortFilterProxyModel):
# 	def __init__ (self):
# 		super(DataframeQSortFilterProxyModel, self).__init__()
# 		self.role = QtCore.Qt.DisplayRole
# 	# def lessThan (self, left, right):
# 	# 	col = left.column()
# 	#
# 	# 	dataleft = left.data()
# 	# 	dataright = right.data()
# 	#
# 	# 	# if col == 2:
# 	# 	# 	dataleft = float(dataleft)
# 	# 	# 	dataright = float(dataright)
# 	# 	if col == 4:
# 	# 		dataleft = QtCore.QDate.fromString(dataleft, "d/M/yy").addYears(100)
# 	# 		dataright = QtCore.QDate.fromString(dataright, "d/M/yy").addYears(100)
# 	#
# 	# 	return dataleft < dataright
#
# 	def lessThan (self, left, right):
# 		# role = self.role
# 		leftData = self.sourceModel().data(left, self.role)
# 		rightData = self.sourceModel().data(right, self.role)
# 		if leftData is None:
# 			return True
# 		elif rightData is None:
# 			return False
# 		elif type(leftData) != type(rightData):
# 			# don't want to sort at all in these cases, False is just a copout ...
# 			# should warn user
# 			return False
# 		return leftData < rightData


# class QToaster(QtWidgets.QFrame):
# 	closed = QtCore.Signal()
#
# 	def __init__ (self, *args, **kwargs):
# 		super(QToaster, self).__init__(*args, **kwargs)
# 		QtWidgets.QHBoxLayout(self)
#
# 		self.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
#
# 		self.setStyleSheet('''
#             QToaster {
#                 border: 1px solid black;
#                 border-radius: 4px;
#                 background-color: rgb(33, 47, 61);
#             }
#         ''')
#
# 		self.timer = QtCore.QTimer(singleShot = True, timeout = self.hide)
#
# 		if self.parent():
# 			self.opacityEffect = QtWidgets.QGraphicsOpacityEffect(opacity = 0)
# 			self.setGraphicsEffect(self.opacityEffect)
# 			self.opacityAni = QPropertyAnimation(self.opacityEffect, b'opacity')
# 			# we have a parent, install an eventFilter so that when it's resized
# 			# the notification will be correctly moved to the right corner
# 			self.parent().installEventFilter(self)
# 		else:
# 			# there's no parent, use the window opacity property, assuming that
# 			# the window manager supports it; if it doesn't, this won'd do
# 			# anything (besides making the hiding a bit longer by half a second)
# 			self.opacityAni = QPropertyAnimation(self, b'windowOpacity')
# 		self.opacityAni.setStartValue(0)
# 		self.opacityAni.setEndValue(1)
# 		self.opacityAni.setDuration(100)
# 		self.opacityAni.finished.connect(self.checkClosed)
#
# 		self.corner = QtCore.Qt.TopLeftCorner
# 		self.margin = 10
#
# 	def checkClosed (self):
# 		# if we have been fading out, we're closing the notification
# 		if self.opacityAni.direction() == self.opacityAni.Backward:
# 			self.close()
#
# 	def restore (self):
# 		# this is a "helper function", that can be called from mouseEnterEvent
# 		# and when the parent widget is resized. We will not close the
# 		# notification if the mouse is in or the parent is resized
# 		self.timer.stop()
# 		# also, stop the animation if it's fading out...
# 		self.opacityAni.stop()
# 		# ...and restore the opacity
# 		if self.parent():
# 			self.opacityEffect.setOpacity(1)
# 		else:
# 			self.setWindowOpacity(1)
#
# 	def hide (self):
# 		# start hiding
# 		self.opacityAni.setDirection(self.opacityAni.Backward)
# 		self.opacityAni.setDuration(500)
# 		self.opacityAni.start()
#
# 	def eventFilter (self, source, event):
# 		if source == self.parent() and event.type() == QtCore.QEvent.Resize:
# 			self.opacityAni.stop()
# 			parentRect = self.parent().rect()
# 			geo = self.geometry()
# 			if self.corner == QtCore.Qt.TopLeftCorner:
# 				geo.moveTopLeft(
# 					parentRect.topLeft() + QtCore.QPoint(self.margin, self.margin))
# 			elif self.corner == QtCore.Qt.TopRightCorner:
# 				geo.moveTopRight(
# 					parentRect.topRight() + QtCore.QPoint(-self.margin, self.margin))
# 			elif self.corner == QtCore.Qt.BottomRightCorner:
# 				geo.moveBottomRight(
# 					parentRect.bottomRight() + QtCore.QPoint(-self.margin, -self.margin))
# 			else:
# 				geo.moveBottomLeft(
# 					parentRect.bottomLeft() + QtCore.QPoint(self.margin, -self.margin))
# 			self.setGeometry(geo)
# 			self.restore()
# 			self.timer.start()
# 		return super(QToaster, self).eventFilter(source, event)
#
# 	def enterEvent (self, event):
# 		self.restore()
#
# 	def leaveEvent (self, event):
# 		self.timer.start()
#
# 	def closeEvent (self, event):
# 		# we don't need the notification anymore, delete it!
# 		self.deleteLater()
#
# 	def resizeEvent (self, event):
# 		super(QToaster, self).resizeEvent(event)
# 		# if you don't set a stylesheet, you don't need any of the following!
# 		if not self.parent():
# 			# there's no parent, so we need to update the mask
# 			path = QtGui.QPainterPath()
# 			path.addRoundedRect(QtCore.QRectF(self.rect()).translated(-.5, -.5), 4, 4)
# 			self.setMask(QtGui.QRegion(path.toFillPolygon(QtGui.QTransform()).toPolygon()))
# 		else:
# 			self.clearMask()
#
# 	@staticmethod
# 	def showMessage (parent, message, icon = QtWidgets.QStyle.SP_MessageBoxCritical,
# 					 corner = None, margin = 10, closable = True,
# 					 timeout = 5000, desktop = False, parentWindow = True):
#
# 		if parent and parentWindow:
# 			parent = parent.window()
#
# 		if not parent or desktop:
# 			self = QToaster(None)
# 			self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint | QtCore.Qt.BypassWindowManagerHint)
# 			# This is a dirty hack!
# 			# parentless objects are garbage collected, so the widget will be
# 			# deleted as soon as the function that calls it returns, but if an
# 			# object is referenced to *any* other object it will not, at least
# 			# for PyQt (I didn't test it to a deeper level)
# 			self.__self = self
#
# 			currentScreen = QtWidgets.QApplication.primaryScreen()
# 			if parent and parent.window().geometry().size().isValid():
# 				# the notification is to be shown on the desktop, but there is a
# 				# parent that is (theoretically) visible and mapped, we'll try to
# 				# use its geometry as a reference to guess which desktop shows
# 				# most of its area; if the parent is not a top level window, use
# 				# that as a reference
# 				reference = parent.window().geometry()
# 			else:
# 				# the parent has not been mapped yet, let's use the cursor as a
# 				# reference for the screen
# 				reference = QtCore.QRect(
# 					QtGui.QCursor.pos() - QtCore.QPoint(1, 1),
# 					QtCore.QSize(3, 3))
# 			maxArea = 0
# 			for screen in QtWidgets.QApplication.screens():
# 				intersected = screen.geometry().intersected(reference)
# 				area = intersected.width() * intersected.height()
# 				if area > maxArea:
# 					maxArea = area
# 					currentScreen = screen
# 			parentRect = currentScreen.availableGeometry()
# 		else:
# 			self = QToaster(parent)
# 			parentRect = parent.rect()
#
# 		self.timer.setInterval(timeout)
#
# 		# use Qt standard icon pixmaps; see:
# 		# https://doc.qt.io/qt-5/qstyle.html#StandardPixmap-enum
# 		if isinstance(icon, QtWidgets.QStyle.StandardPixmap):
# 			labelIcon = QtWidgets.QLabel()
# 			self.layout().addWidget(labelIcon)
# 			icon = self.style().standardIcon(icon)
# 			size = self.style().pixelMetric(QtWidgets.QStyle.PM_SmallIconSize)
# 			labelIcon.setPixmap(icon.pixmap(size))
# 			labelIcon.setStyleSheet('background-color: transparent;')
#
# 		self.label = QtWidgets.QLabel(message)
# 		self.layout().addWidget(self.label)
# 		self.label.setStyleSheet('background-color: transparent;')
#
# 		if closable:
# 			self.closeButton = QtWidgets.QToolButton()
# 			self.layout().addWidget(self.closeButton)
# 			# closeIcon = self.style().standardIcon(QtWidgets.QStyle.SP_TitleBarCloseButton)
# 			# self.closeButton.setIcon(closeIcon)
# 			self.closeButton.setIcon(QIcon(u":/icons/icons/x_.svg"))
# 			# self.closeButton.setStyleSheet('background-color: transparent; color: red;')
# 			self.closeButton.setStyleSheet('''
#                         QToolButton {
#                             background-color: transparent;
#                             padding: 5px;
#                             border-radius: 3px;
#                         }
#                         QToolButton:hover {
#                             background-color: red;
#                         }
#                     ''')
# 			self.closeButton.setCursor(Qt.PointingHandCursor)
# 			self.closeButton.setAutoRaise(True)
# 			self.closeButton.clicked.connect(self.close)
#
# 		self.timer.start()
#
# 		# raise the widget and adjust its size to the minimum
# 		self.raise_()
# 		self.adjustSize()
#
# 		self.corner = corner
# 		self.margin = margin
#
# 		_margin = parent.width() / 2 - self.width() / 2
# 		# _margin = self.parent().width() / 2 - self.width() / 2
#
# 		geo = self.geometry()
# 		# now the widget should have the correct size hints, let's move it to the
# 		# right place
# 		if corner == 'TopCenterCorner':
# 			geo.moveCenter(parentRect.center())
#
# 		elif corner == QtCore.Qt.TopLeftCorner:
# 			geo.moveTopLeft(
# 				parentRect.topLeft() + QtCore.QPoint(_margin, margin))
# 		elif corner == QtCore.Qt.TopRightCorner:
# 			geo.moveTopRight(
# 				parentRect.topRight() + QtCore.QPoint(-margin, margin))
# 		elif corner == QtCore.Qt.BottomRightCorner:
# 			geo.moveBottomRight(
# 				parentRect.bottomRight() + QtCore.QPoint(-margin, -margin))
# 		else:
# 			geo.moveBottomLeft(
# 				parentRect.bottomLeft() + QtCore.QPoint(margin, -margin))
#
# 		self.setGeometry(geo)
# 		self.show()
# 		self.opacityAni.start()


# class QToaster(QtWidgets.QFrame):
#     closed = QtCore.Signal()
#
#     def __init__(self, *args, **kwargs):
#         super(QToaster, self).__init__(*args, **kwargs)
#         QtWidgets.QHBoxLayout(self)
#
#         self.setSizePolicy(QtWidgets.QSizePolicy.Maximum,
#                            QtWidgets.QSizePolicy.Maximum)
#
#         self.setStyleSheet('''
#             QToaster {
#                 border: 1px solid black;
#                 border-radius: 4px;
#                 background: palette(window);
#             }
#         ''')
#         # alternatively:
#         # self.setAutoFillBackground(True)
#         # self.setFrameShape(self.Box)
#
#         self.timer = QtCore.QTimer(singleShot=True, timeout=self.hide)
#
#         if self.parent():
#             self.opacityEffect = QtWidgets.QGraphicsOpacityEffect(opacity=0)
#             self.setGraphicsEffect(self.opacityEffect)
#             self.opacityAni = QtCore.QPropertyAnimation(self.opacityEffect, b'opacity')
#             # we have a parent, install an eventFilter so that when it's resized
#             # the notification will be correctly moved to the right corner
#             self.parent().installEventFilter(self)
#         else:
#             # there's no parent, use the window opacity property, assuming that
#             # the window manager supports it; if it doesn't, this won'd do
#             # anything (besides making the hiding a bit longer by half a second)
#             self.opacityAni = QtCore.QPropertyAnimation(self, b'windowOpacity')
#         self.opacityAni.setStartValue(0.)
#         self.opacityAni.setEndValue(1.)
#         self.opacityAni.setDuration(100)
#         self.opacityAni.finished.connect(self.checkClosed)
#
#         self.corner = QtCore.Qt.TopLeftCorner
#         self.margin = 10
#
#     def checkClosed(self):
#         # if we have been fading out, we're closing the notification
#         if self.opacityAni.direction() == self.opacityAni.Backward:
#             self.close()
#
#     def restore(self):
#         # this is a "helper function", that can be called from mouseEnterEvent
#         # and when the parent widget is resized. We will not close the
#         # notification if the mouse is in or the parent is resized
#         self.timer.stop()
#         # also, stop the animation if it's fading out...
#         self.opacityAni.stop()
#         # ...and restore the opacity
#         if self.parent():
#             self.opacityEffect.setOpacity(1)
#         else:
#             self.setWindowOpacity(1)
#
#     def hide(self):
#         # start hiding
#         self.opacityAni.setDirection(self.opacityAni.Backward)
#         self.opacityAni.setDuration(500)
#         self.opacityAni.start()
#
#     def eventFilter(self, source, event):
#         if source == self.parent() and event.type() == QtCore.QEvent.Resize:
#             self.opacityAni.stop()
#             parentRect = self.parent().rect()
#             geo = self.geometry()
#             if self.corner == QtCore.Qt.TopLeftCorner:
#                 geo.moveTopLeft(
#                     parentRect.topLeft() + QtCore.QPoint(self.margin, self.margin))
#             elif self.corner == QtCore.Qt.TopRightCorner:
#                 geo.moveTopRight(
#                     parentRect.topRight() + QtCore.QPoint(-self.margin, self.margin))
#             elif self.corner == QtCore.Qt.BottomRightCorner:
#                 geo.moveBottomRight(
#                     parentRect.bottomRight() + QtCore.QPoint(-self.margin, -self.margin))
#             else:
#                 geo.moveBottomLeft(
#                     parentRect.bottomLeft() + QtCore.QPoint(self.margin, -self.margin))
#             self.setGeometry(geo)
#             self.restore()
#             self.timer.start()
#         return super(QToaster, self).eventFilter(source, event)
#
#     def enterEvent(self, event):
#         self.restore()
#
#     def leaveEvent(self, event):
#         self.timer.start()
#
#     def closeEvent(self, event):
#         # we don't need the notification anymore, delete it!
#         self.deleteLater()
#
#     def resizeEvent(self, event):
#         super(QToaster, self).resizeEvent(event)
#         # if you don't set a stylesheet, you don't need any of the following!
#         if not self.parent():
#             # there's no parent, so we need to update the mask
#             path = QtGui.QPainterPath()
#             path.addRoundedRect(QtCore.QRectF(self.rect()).translated(-.5, -.5), 4, 4)
#             self.setMask(QtGui.QRegion(path.toFillPolygon(QtGui.QTransform()).toPolygon()))
#         else:
#             self.clearMask()
#
#     @staticmethod
#     def showMessage(parent, message,
#                     icon=QtWidgets.QStyle.SP_MessageBoxInformation,
#                     corner=QtCore.Qt.TopLeftCorner, margin=10, closable=True,
#                     timeout=5000, desktop=False, parentWindow=True):
#
#         if parent and parentWindow:
#             parent = parent.window()
#
#         if not parent or desktop:
#             self = QToaster(None)
#             self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint |
#                 QtCore.Qt.BypassWindowManagerHint)
#             # This is a dirty hack!
#             # parentless objects are garbage collected, so the widget will be
#             # deleted as soon as the function that calls it returns, but if an
#             # object is referenced to *any* other object it will not, at least
#             # for PyQt (I didn't test it to a deeper level)
#             self.__self = self
#
#             currentScreen = QtWidgets.QApplication.primaryScreen()
#             if parent and parent.window().geometry().size().isValid():
#                 # the notification is to be shown on the desktop, but there is a
#                 # parent that is (theoretically) visible and mapped, we'll try to
#                 # use its geometry as a reference to guess which desktop shows
#                 # most of its area; if the parent is not a top level window, use
#                 # that as a reference
#                 reference = parent.window().geometry()
#             else:
#                 # the parent has not been mapped yet, let's use the cursor as a
#                 # reference for the screen
#                 reference = QtCore.QRect(
#                     QtGui.QCursor.pos() - QtCore.QPoint(1, 1),
#                     QtCore.QSize(3, 3))
#             maxArea = 0
#             for screen in QtWidgets.QApplication.screens():
#                 intersected = screen.geometry().intersected(reference)
#                 area = intersected.width() * intersected.height()
#                 if area > maxArea:
#                     maxArea = area
#                     currentScreen = screen
#             parentRect = currentScreen.availableGeometry()
#         else:
#             self = QToaster(parent)
#             parentRect = parent.rect()
#
#         self.timer.setInterval(timeout)
#
#         # use Qt standard icon pixmaps; see:
#         # https://doc.qt.io/qt-5/qstyle.html#StandardPixmap-enum
#         if isinstance(icon, QtWidgets.QStyle.StandardPixmap):
#             labelIcon = QtWidgets.QLabel()
#             self.layout().addWidget(labelIcon)
#             icon = self.style().standardIcon(icon)
#             size = self.style().pixelMetric(QtWidgets.QStyle.PM_SmallIconSize)
#             labelIcon.setPixmap(icon.pixmap(size))
#
#         self.label = QtWidgets.QLabel(message)
#         self.layout().addWidget(self.label)
#
#         if closable:
#             self.closeButton = QtWidgets.QToolButton()
#             self.layout().addWidget(self.closeButton)
#             closeIcon = self.style().standardIcon(
#                 QtWidgets.QStyle.SP_TitleBarCloseButton)
#             self.closeButton.setIcon(closeIcon)
#             self.closeButton.setAutoRaise(True)
#             self.closeButton.clicked.connect(self.close)
#
#         self.timer.start()
#
#         # raise the widget and adjust its size to the minimum
#         self.raise_()
#         self.adjustSize()
#
#         self.corner = corner
#         self.margin = margin
#
#         geo = self.geometry()
#         # now the widget should have the correct size hints, let's move it to the
#         # right place
#         if corner == QtCore.Qt.TopLeftCorner:
#             geo.moveTopLeft(
#                 parentRect.topLeft() + QtCore.QPoint(margin, margin))
#         elif corner == QtCore.Qt.TopRightCorner:
#             geo.moveTopRight(
#                 parentRect.topRight() + QtCore.QPoint(-margin, margin))
#         elif corner == QtCore.Qt.BottomRightCorner:
#             geo.moveBottomRight(
#                 parentRect.bottomRight() + QtCore.QPoint(-margin, -margin))
#         else:
#             geo.moveBottomLeft(
#                 parentRect.bottomLeft() + QtCore.QPoint(margin, -margin))
#
#         self.setGeometry(geo)
#         self.show()
#         self.opacityAni.start()

class MouseObserver(QObject):
	clicked_widget = QtCore.Signal(object)

	def __init__(self, widget):
		super().__init__(widget)
		self._widget = widget
		self.widget.installEventFilter(self)

	@property
	def widget(self):
		return self._widget

	def eventFilter(self, obj, event):
		if obj is self.widget and event.type() == QEvent.MouseButtonPress:
			# print(obj, event)
			self.clicked_widget.emit(obj.objectName())
		return super().eventFilter(obj, event)


class UploadDataRossvyaz(QtCore.QObject):
	mysignal = QtCore.Signal(object)
	progressHiden = QtCore.Signal(bool)
	cleared = QtCore.Signal(bool)

	def __init__ (self, path, parent = None):
		QtCore.QObject.__init__(self, parent)
		self._stopped = True
		self._progress = True
		self._path = path

	def run (self):
		self._stopped = False
		self._progress = False
		self.change_reestr()

	def change_reestr (self):
		while (not self._stopped and not self._progress):
			self.progressHiden.emit(self._progress)
			records = ''
			records = 'Получение данных из загруженного файла...'
			self.mysignal.emit(records)

			ls_operators = csvListOperatorsORM(self._path)

			records = 'Загрузка операторов в БД...'

			# Передача данных из потока через сигнал
			self.mysignal.emit(records)

			SyncORM.insert_operators_ORM(ls_operators, flags = False)

			records = 'Загрузка сигнальных точек и мест расположения операторов в БД...'

			self.mysignal.emit(records)

			locations, locations_DPC = uploadDataSpInPandas(self._path)
			if SyncORM.notEmptyDPC():
				SyncORM.uploadLocatSpInDb(locations)
			SyncORM.uploadSpInDb(locations_DPC)

			records = 'Загрузка данных из Россреестра завершена'

			self.mysignal.emit(records)

			self._stopped = True
			self._progress = True
			self.progressHiden.emit(self._progress)
			self.cleared.emit(self._progress)

	def stop (self):
		self._stopped = True
		self._progress = True


class UploadMgmnFromOutlook(QtCore.QObject):
	signalMgmn = QtCore.Signal(object)
	progressHiden = QtCore.Signal(bool)
	cleared = QtCore.Signal(bool)

	def __init__ (self, path, parent = None):
		QtCore.QObject.__init__(self, parent)
		self._stopped = True
		self._progress = True
		self._path = path

	def run (self):
		self._stopped = False
		self._progress = False
		self.change_mgmn()

	def change_mgmn (self):
		while not self._stopped:
			self.progressHiden.emit(self._progress)
			records = ''
			records = 'Получение данных из загруженного файла...'
			self.signalMgmn.emit(records)

			data = savePandasMgmn(self._path)
			# self.updateProgress.emit(5)

			# NewFileNameAttachment = 'MGMN_TRUNKS_REGISTRY_GNOC.xlsx'
			# self.path_file = os.path.realpath(os.path.join(PATH_DATA, NewFileNameAttachment))
			# file_exists = os.path.exists(self.path_file)
			#
			# if file_exists:
			# 	os.remove(self.path_file)
			#
			# print(1)
			# try:
			# 	print(2)
			# 	self.ol = win32.gencache.EnsureDispatch('Outlook.Application').GetNamespace("MAPI")
			# 	print(3)
			# except AttributeError:
			# 	# Remove cache and try again.
			# 	MODULE_LIST = [m.__name__ for m in sys.modules.values()]
			# 	for module in MODULE_LIST:
			# 		if re.match(r'win32com\.gen_py', module):
			# 			del sys.modules[module]
			# 	shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp', 'gen_py'))
			# 	self.ol = win32.gencache.EnsureDispatch('Outlook.Application').GetNamespace("MAPI")
			#
			# print(4)
			# account = self.ol.Folders['gnoc_sss_smena@mts.ru']
			# inbox = account.Folders['Входящие'].Folders['Отчеты']
			# reestr = inbox.Folders['Реестр транковых групп']
			#
			# last_mail = reestr.Items.GetLast()
			# self.attach_exel = last_mail.Attachments
			# self.attach_exel.Item(1).SaveAsFile(self.path_file)

			# print(f'Файл из Outlock: {self._path}')

			records = 'Загрузка операторов в БД...'
			# Передача данных из потока через сигнал
			self.signalMgmn.emit(records)

			SyncORM.insert_operators_ORM(data['list_operators'], flags = True)

			records = 'Загрузка операторов в БД завершена'
			self.signalMgmn.emit(records)

			records = 'Загрузка Email операторов в БД...'
			self.signalMgmn.emit(records)

			SyncORM.insertEmailsOperatorsORM(data['listOperatorsToEmails'])

			records = 'Загрузка данных по операторам в БД...'
			# Передача данных из потока через сигнал
			self.signalMgmn.emit(records)
			# self.updateProgress.emit(50)
			SyncORM.uploadDataMgmnInDbORM(data['data_in_mgmn'])

			records = 'Загрузка данных по операторам в БД завершена'
			# Передача данных из потока через сигнал
			self.signalMgmn.emit(records)
			# self.updateProgress.emit(100)

			self._stopped = True
			self._progress = True
			self.progressHiden.emit(self._progress)
			self.cleared.emit(self._progress)

	def stop (self):
		self._stopped = True
		self._progress = True


class UploadEmailsRegion(QtCore.QObject):
	signal_region = QtCore.Signal(object)
	signal_region_error = QtCore.Signal(object)
	signal_list_region = QtCore.Signal(list)

	def __init__ (self, path, parent = None):
		QtCore.QObject.__init__(self, parent)
		self._stopped = True
		self._path = path

	def run (self):
		self._stopped = False
		self.uploadEmailRegions()

	def uploadEmailRegions (self):
		while not self._stopped:
			records = 'Получение данных из загруженного файла...'
			self.signal_region.emit(records)
			data = downloadEmailsAllRegionsInDb(self._path)

			records = 'Загрузка регионов в БД...'
			self.signal_region.emit(records)
			result = SyncORM.uploadEmailsRegionORM(data)

			if result:
				records = 'Загрузка регионов в БД завершена'
				self.signal_region.emit(records)
			else:
				records = 'Что-то пошло не так. Попробуйте позже ещё раз.'
				self.signal_region_error.emit(records)

			records = 'Загрузка данных по регионам в БД...'
			self.signal_region.emit(records)
			lists_regions = SyncORM.listAllRegionsORM()

			self.signal_list_region.emit(lists_regions)
			records = 'Загрузка данных завершена.'
			self.signal_region.emit(records)

			self._stopped = True

	def stop (self):
		self._stopped = True


class MyTableModel(QAbstractTableModel):
	global STATUS_COLOR

	def __init__ (self, datatable = None, headers = None, parent = None):
		super(MyTableModel, self).__init__(parent = None)
		self.datatable = datatable
		self.headers = headers

	def rowCount (self, parent = QtCore.QModelIndex()):
		return len(self.datatable)

	def columnCount (self, parent = QtCore.QModelIndex()):
		if len(self.datatable) > 0:
			return len(self.datatable[0])
		else:
			return len(self.headers)

	# def data (self, index, role): # = (QtCore.Qt.DisplayRole or QtCore.Qt.BackgroundRole)):
	#     if not index.isValid():
	#         return None
	#     row = index.row()
	#     column = index.column()
	#
	#     if 0 <= row < self.rowCount() and 0 <= column < self.columnCount():
	#         item = self.datatable[row][column]
	#
	#     if role == QtCore.Qt.BackgroundRole:
	#         # if self.datatable[row][1] in STATUS_COLOR.keys():
	#         if item in STATUS_COLOR.keys():
	#             color = STATUS_COLOR.get(item)
	#             return QtGui.QColor(color)
	#
	#     if role == Qt.ItemDataRole.TextAlignmentRole:
	#         if isinstance(item, datetime):
	#             # return Qt.AlignmentFlag.AlignCenter
	#             return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
	#
	#     if role == QtCore.Qt.DisplayRole:
	#         if isinstance(item, datetime):
	#             return datetime.strftime(item, "%Y-%m-%d %H:%M:%S")
	#         else:
	#             return item
	#     elif role == QtCore.Qt.EditRole:
	#         return item

	def data (self, index, role):
		if not index.isValid():
			return None
		row = index.row()
		column = index.column()

		if role == Qt.DisplayRole:
			value = self.datatable[row][column]
			if isinstance(value, datetime):
				return datetime.strftime(value, "%d-%m-%Y %H:%M:%S")
			else:
				return value
		elif role == Qt.EditRole:
			return self.datatable[row][column]
		elif role == Qt.BackgroundRole and column == 1:
			value = self.datatable[row][column]
			if value == "INFO":
				return STATUS_COLOR.get('INFO')
			elif value == "ADD":
				return STATUS_COLOR.get('ADD')
			elif value == "DELETE":
				return STATUS_COLOR.get('DELETE')
			elif value == "ERROR":
				return STATUS_COLOR.get('ERROR')
			elif value == "OPEN":
				return STATUS_COLOR.get('OPEN')
			elif value == "CLOSED":
				return STATUS_COLOR.get('CLOSED')
			elif value == "INCIDENT":
				return STATUS_COLOR.get('INCIDENT')

		elif role == Qt.TextAlignmentRole:
			value = self.datatable[row][column]
			if isinstance(value, datetime):
				# Align right, vertical middle.
				return int(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

		elif role == Qt.ForegroundRole:
			value = self.datatable[row][column]
			if ((isinstance(value, int) or isinstance(value, float)) and value < 0):
				return QtGui.QColor('red')
		# else:
		#     return QtCore.QVariant()

	def headerData (self, section, orientation, role = QtCore.Qt.DisplayRole):
		if orientation == QtCore.Qt.Orientation.Horizontal:
			if role == QtCore.Qt.DisplayRole and section < len(self.headers):
				return self.headers[section]
		return super(MyTableModel, self).headerData(section, orientation, role)

	def flags (self, index):
		if index.column() == 0 or index.column() == 1 or index.column() == 2 or index.column() == 3 or index.column() == 4:
			return Qt.ItemIsSelectable | Qt.ItemIsEnabled
		else:
			return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

	def sort (self, column, order = QtCore.Qt.AscendingOrder):
		self.layoutAboutToBeChanged.emit()
		self.datatable.sort(key = lambda x: x[column], reverse = order == QtCore.Qt.DescendingOrder)
		self.layoutChanged.emit()

	# def update (self, dataIn, headers):
	#     print('Updating Model')
	#     self.datatable = dataIn
	#     self.header = headers
	#     print('Datatable : {0}'.format(self.datatable))

	# def setData (self, index, value, role = QtCore.Qt.EditRole):
	#     if index.isValid() and 0 <= index.row():
	#         if role == QtCore.Qt.EditRole:
	#             self.datatable[index.column()][index.row()] = value
	#             print("edit", value)
	#             self.dataChanged.emit(index, index)  # NOT WORKING
	#             return True
	#         else:
	#             return False
	#     else:
	#         return False

	@staticmethod
	def continuous_slices (numbers):
		if not numbers:
			return
		numbers.sort(reverse = True)
		start_idx = 0
		for idx in range(1, len(numbers)):
			if numbers[idx - 1] > (numbers[idx] + 1):
				yield numbers[idx - 1], numbers[start_idx]
				start_idx = idx
		yield numbers[-1], numbers[start_idx]

	def removeRows (self, row_indices, parent = QtCore.QModelIndex()):
		self.layoutAboutToBeChanged.emit()
		for first, last in self.continuous_slices(row_indices):
			# self.beginRemoveRows(parent, first, last)
			self.beginRemoveRows(parent, last, first)
			# del(self.datatable[first: last + 1])
			del (self.datatable[last + 1: first])
			self.endRemoveRows()
		self.layoutChanged.emit()
		return True

	# def removeRows(self, position, rows, QModelIndex):
	#     self.beginRemoveRows(QModelIndex, position, position+rows-1)
	#     for i in range(rows):
	#         del(self.datatable[position])
	#     self.endRemoveRows()
	#     self.layoutChanged.emit()
	#     return True

	# def removeRow (self, row, count, parent = QtCore.QModelIndex()):
	#     self.beginRemoveRows(parent, row, row + count - 1)
	#     for r in range(count):
	#         del self.datatable[row]
	#     self.endRemoveRows()
	#     return True


class MainWindow(QMainWindow):
	global USER, USERCURRENT

	emit_stop = QtCore.Signal(int)

	def __init__ (self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ctrl = {'break': False}

		self.setWindowIcon(QIcon(u':/logo/icon.png'))

		self._animation = QPropertyAnimation(self, b'windowOpacity')
		self._animation.setDuration(600)

		# print(f'{USERCURRENT} ({USER})')
		self.responses = Responses()
		self.verify = Verifications()

		self.threadpool = QtCore.QThreadPool()

		# print(f'Active_0: {self.threadpool.activeThreadCount()}')

		# self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground, True)

		grip = QSizeGrip(self)
		self.ui.horizontalLayout_15.addWidget(grip, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 92, 157, 150))

		self.ui.centralwidget.setGraphicsEffect(self.shadow)

		self.ui.rbtn_sp.setCursor(Qt.PointingHandCursor)
		self.ui.rbtn_cic.setCursor(Qt.PointingHandCursor)

		self.ui.search_btn.setStyleSheet(STYLE_HOVER)

		self.ui.le_opc.setPlaceholderText("Сигнальная точка десятичного формата")
		self.ui.le_dpc.setPlaceholderText("Сигнальная точка десятичного формата")
		self.ui.le_inc.setPlaceholderText("Номер зарегистрированного инцидента")
		self.ui.le_CIC.setPlaceholderText("Укажите заблокированные CIC")

		self.ui.minimizated_btn.clicked.connect(lambda: self.showMinimized())
		# self.ui.minimizated_btn.clicked.connect(self.showMinimized)
		# self.ui.close_btn.clicked.connect(self.quit_app)
		self.ui.close_btn.clicked.connect(self.close)

		self.ui.rbtn_sp.toggled.connect(self.rbtn_sp_checked)
		self.ui.rbtn_cic.toggled.connect(self.rbtn_cic_checked)
		self.ui.rbtn_rossvyaz.toggled.connect(self.rbtn_rossvyaz_checked)
		self.ui.rbtn_mgmn.toggled.connect(self.rbtn_rbtn_mgmn_checked)
		self.ui.menu_btn.clicked.connect(self.show_form_add_email_oper)

		self.ui.search_btn.setEnabled(False)

		if len(self.ui.le_dpc.text().strip()) > 0:
			self.ui.search_btn.setEnabled(True)

		self.ui.search_btn.clicked.connect(self.loadingFormSendEmailOperator)

		# if len(self.ui.le_dpc.text().strip()) > 0:
		# self.ui.le_dpc.returnPressed.connect(self.ui.search_btn.click)


		# self.ui.cb_mgmn_msx.currentIndexChanged.connect(self.current_text_cb_mgmn_msx)
		self.ui.le_cur_cb.setText(str(self.ui.cb_mgmn_msx.currentText()))

		# corner = getattr(QtCore.Qt, TopRightCorner)
		self.ui.le_dpc.textChanged.connect(self.currentStatusDPC)
		self.ui.le_dpc.textChanged.connect(self.borderLineEdit)
		self.ui.cb_mgmn_msx.currentTextChanged.connect(self.borderComboBox)

		# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		# SyncORM.logInfoORM('OPEN', f'{USERCURRENT} ({USER})', 'Запуск программы')

		def moveWindow (e):
			if self.isMaximized() == False:
				if e.buttons() == Qt.LeftButton:
					self.move(self.pos() + e.globalPos() - self.clickPosition)
					self.clickPosition = e.globalPos()
					e.accept()

		self.ui.main_header_frame.mouseMoveEvent = moveWindow

		self.timer_dpc = QTimer()
		self.timer_dpc.setSingleShot(True)
		self.timer_dpc.setInterval(3000)
		self.timer_dpc.timeout.connect(self.timer_finished_dpc)

		self.timer_cmb = QTimer()
		self.timer_cmb.setSingleShot(True)
		self.timer_cmb.setInterval(3000)
		self.timer_cmb.timeout.connect(self.timer_finished_cmb)

		self._loader = QMovie(":/gif/icons/gif/loading4.gif")
		self.ui.lbl_loading.setScaledContents(True)
		self.ui.lbl_loading.setMovie(self._loader)
		self.ui.lbl_loading.setHidden(True)

		self.installEventFilter(self)

		base_bd = currect_connect_in_db(sync_engine)
		base_gasi = currect_connect_in_db(sync_engine_gasi)

		if not base_bd:
			self.ui.menu_btn.setEnabled(False)
			self.ui.search_btn.setEnabled(False)
			self.responses.raise_error_bd(
				self.ui.lbl_error,
				"Отсутствует подключение к основной БД."
			)
		elif not base_gasi:
			self.responses.raise_error_bd(
				self.ui.lbl_error,
				"Отсутствует подключение к основной БД SJ."
			)
		else:
			pass


	# def eventFilter (self, obj, event):
	#     if obj is self.ui and event.type() == QtGui.QCloseEvent:
	#         self.quit_app()
	#         # self.do_close()
	#
	#         event.ignore()
	#         return True
	#     return super(MainWindow, self).eventFilter(obj, event)


	def loadingGif (self, status):
		if status:
			self.ui.lbl_loading.setVisible(True)
			self._loader.start()
		else:
			self.ui.lbl_loading.setVisible(False)
			self._loader.stop()

	def borderLineEdit(self):
		# self.ui.search_btn.setEnabled(True)
		self.ui.le_dpc.setStyleSheet('*{border: 2px solid rgb(61, 174, 233);} ')
		self.ui.lbl_error.setText('')

	def borderComboBox(self):
		# self.ui.search_btn.setEnabled(True)
		self.ui.cb_mgmn_msx.setStyleSheet('*{border: 2px solid rgb(61, 174, 233);}')
		self.timer_finished_cmb()

	def keyPressEvent (self, e):
		if self.verify.empty_fields(self.get_dpc_input()):
			self.ui.le_dpc.setStyleSheet('*{border: 2px solid red;} ')
			self.apply_click_line_edit()
			return

		if e.key() == QtCore.Qt.Key_Enter:
			self.loadingFormSendEmailOperator()

	def get_dpc_input (self):
		return [self.ui.le_dpc.text().strip(),]

	def apply_click_line_edit (self):
		if not self.timer_dpc.isActive():
			self.ui.lbl_error.setStyleSheet('*{color: red;}')
			self.ui.lbl_error.setText('Поле обязательно для заполнения.')
			self.timer_dpc.start()

	def timer_finished_dpc(self):
		self.ui.lbl_error.setText('')

	def apply_empty_combobox (self):
		if not self.timer_cmb.isActive():
			self.ui.cb_mgmn_msx.setStyleSheet('*{border: 2px solid red;}')
			self.ui.lbl_error.setStyleSheet('*{color: red;}')
			self.ui.lbl_error.setText('Выберите региональный ТМгУС')
			self.timer_cmb.start()

	def timer_finished_cmb(self):
		self.ui.lbl_error.setText('')


	@Slot()
	def quit_app (self):

		# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		# SyncORM.logInfoORM('CLOSED', f'{USERCURRENT} ({USER})', 'Программа закрыта')

		self.removeEventFilter(self)
		# self.fade_out()
		self.close()

	def fade_in (self):
		try:
			self._animation.finished.disconnect(self.close)
		except:
			pass
		self._animation.stop()
		self._animation.setStartValue(0)
		self._animation.setEndValue(1)
		self._animation.start()

	def fade_out (self):
		loop = QEventLoop()
		self._animation.finished.connect(loop.quit)
		self._animation.setDirection(QPropertyAnimation.Backward)
		self._animation.start()
		loop.exec_()

	def showEvent (self, event):
		super().showEvent(event)
		self.fade_in()

	def closeEvent (self, event):
		event.ignore()
		self.fade_out()
		self.quit_app()
		super().closeEvent(event)

	# def hideEvent (self, event):
	# 	self.fade_out()
	# 	super().hideEvent(event)

	def showToaster (self, msg):
		pass
		# Toast(text=msg)
		# parent = self
		# desktop = False
		# corner = QtCore.Qt.TopLeftCorner
		# QToaster.showMessage(parent, message = msg, corner = corner, desktop = desktop)

	@Slot()
	def currentStatusDPC (self):
		self.ui.search_btn.setEnabled(True)
		if len(self.ui.le_dpc.text()) > 7:
			self.ui.rbtn_mgmn.toggle()
			self.rbtn_rbtn_mgmn_checked()
		else:
			self.ui.rbtn_rossvyaz.toggle()
			self.rbtn_rossvyaz_checked()

	def rbtn_sp_checked (self):
		if self.ui.rbtn_sp.isChecked():
			self.ui.frame_CIC.setMinimumHeight(0)
			self.ui.frame_CIC.setMaximumHeight(0)
			self.ui.le_CIC.clear()

	def rbtn_cic_checked (self):
		if self.ui.rbtn_cic.isChecked():
			self.ui.frame_CIC.setMinimumHeight(45)
			self.ui.frame_CIC.setMaximumHeight(45)

	@Slot()
	def rbtn_rossvyaz_checked (self):
		if self.ui.rbtn_rossvyaz.isChecked():
			self.ui.cb_mgmn_msx.setEnabled(False)
			self.ui.lbl_dpc.setText('DPC:')
			self.ui.le_dpc.setPlaceholderText("Сигнальная точка десятичного формата")
			self.ui.frame_opc.setEnabled(True)

	@Slot()
	def rbtn_rbtn_mgmn_checked (self):
		if self.ui.rbtn_mgmn.isChecked():
			self.ui.cb_mgmn_msx.setEnabled(True)
			self.ui.cb_mgmn_msx.setCursor(Qt.PointingHandCursor)
			self.ui.lbl_dpc.setText('Trunk Group Name:')
			self.ui.le_dpc.setPlaceholderText("Trunk Group Name берём из аварии из NGSA")
			self.ui.frame_opc.setEnabled(False)


	def mousePressEvent (self, event):
		self.clickPosition = event.globalPos()

	def loadingFormSendEmailOperator(self):
		if len(self.ui.le_dpc.text().strip()) > 0:
			self.worker = Worker(self.show_form_send_email_operator)
			self.worker.signals.loading_start.connect(self.loadingGif)
			self.worker.signals.loading_stop.connect(self.loadingGif)
			self.threadpool.start(self.worker)
		else:
			if self.verify.empty_fields(self.get_dpc_input()):
				self.ui.le_dpc.setStyleSheet('*{border: 2px solid red;} ')
				self.apply_click_line_edit()
				return

	def show_form_send_email_operator (self):
		self.ui.search_btn.setEnabled(False)

		flag_blocking = True
		search_region = None
		self.dpc = []

		opc_le = self.ui.le_opc.text().strip()
		dpc_le = self.ui.le_dpc.text().strip()
		inc = self.ui.le_inc.text().strip()[:15]
		cic = None


		if self.ui.rbtn_cic.isChecked():
			flag_blocking = False
			cic = self.ui.le_CIC.text()

		self.flag = False
		self.email_region = ''
		current_text_cb = ''

		# print(dpc_le)
		if self.ui.rbtn_rossvyaz.isChecked():
			if (dpc_le.startswith('2-') or dpc_le.startswith('0-')) and self.flag == False:
				dpc_le = dpc_le.split('-')[1]
			if (opc_le.startswith('2-') or opc_le.startswith('0-')) and self.flag == False:
				opc_le = opc_le.split('-')[1]
		else:
			self.flag = True
			current_text_cb = self.ui.cb_mgmn_msx.currentText()

		if opc_le:
			# print(f'{opc_le=}')
			data_opc = {
				'flag': self.flag,
				'opc': opc_le,
				'current_msx': ''
			}
			self.email_region = SyncORM.serchRegionsInOpcORM(data_opc)

		if dpc_le:
			if dpc_le.isdigit():
				data_dpc = {
					'flag': self.flag,
					'dpc': dpc_le,
					'current_msx': ''
				}
			else:
				data_dpc = {
					'flag': self.flag,
					'dpc': dpc_le,
					'current_msx': current_text_cb
				}
			self.dpc = SyncORM.serchOperatorInDpcORM(data_dpc)


			if self.dpc == []:
				if self.flag:
					# self.showToaster('Указанная TG отсутствует в выгрузке MGMN')
					self.responses.raise_alert(
						self.ui.lbl_error,
						"Указанная TG отсутствует в выгрузке MGMN."
					)
					self.ui.search_btn.setEnabled(True)
				else:
					# self.showToaster('Указанный DPC отсутствует в Россреестре')
					# self.__toast = Toast(text = 'Указанный DPC отсутствует в Россреестре', parent = self)
					# self.__toast.show()
					self.responses.raise_alert(
						self.ui.lbl_error,
						"Указанный DPC отсутствует в Россреестре."
					)
					self.ui.search_btn.setEnabled(True)
				return

			if len(self.dpc) > 1:
				# print(f'{len(self.dpc)=}')
				self.ui.search_btn.setEnabled(True)
				# self.apply_empty_combobox()
				self.worker.signals.finished.connect(self.apply_empty_combobox)
				self.threadpool.cancel(self.worker)
				return

			if self.flag and self.dpc:
				data_opc = {
					'flag': self.flag,
					'opc': self.dpc[0]['opc'][2:],
					'current_msx': current_text_cb
				}
				self.email_region = SyncORM.serchRegionsInOpcORM(data_opc)
				# print(f'{self.email_region=}')

			# if dpc[0]['locations']['name']:
			#     # print('1')
			#     search_region = dpc[0]['locations']['name'].split('|')[-1]
			# elif dpc.get('region_shluza'):
			#     # print('2')
			#     search_region = dpc['region_shluza']

		# elif dpc_le == '':
		#     self.showToaster('Не указан DPC')
		#     return
		# else:
		#     self.showToaster('Не корректный DPC')
		#     return
		else:
			if current_text_cb == '':
				self.ui.search_btn.setEnabled(True)
				self.responses.raise_error(
					self.ui.lbl_error,
					'Выберите региональный ТМгУС.',
					self.ui.cb_mgmn_msx
				)
			else:
				self.ui.search_btn.setEnabled(True)
				self.responses.raise_error(
					self.ui.lbl_error,
					'Поле обязательно для заполнения.',
					self.ui.le_dpc
				)

		if inc != '':
			data = {
				'name': inc,
				'operator_id': self.dpc[0]['operators']['id'],
				'dpc_id': self.dpc[0]['id'],
				'operator_name': self.dpc[0]['operators']['name'],
				'dpc_name': self.dpc[0]['name'],
				'opc_name': opc_le,
				'flag': self.dpc[0]['operators']['flag'],
			}
			SyncORM.saveIncidentORM(data)
			SyncORM.logInfoORM('INCIDENT', f'{USERCURRENT} ({USER})', f'Отправлен инцидент: {data["name"]}')

		if self.dpc != []:
			if self.dpc[0]['operators']['flag']:
				if self.dpc[0]['region_kommutatora'] == self.dpc[0]['region_shluza']:
					operator_location = self.dpc[0]['region_kommutatora']
				else:
					operator_location = self.dpc[0]['region_kommutatora'] + '|' + self.dpc[0]['region_shluza']

			# emails_region = None
			# print('Email Region: ', emails_region)

			if self.email_region is None:
				self.email_region = ''

			if flag_blocking:
				if self.dpc[0]['operators']['flag']:
					text_theme = f"Недоступность сигнального направления в направлении " + str(
						self.dpc[0]['operators']['name']) + " " + str(operator_location) + " // " + str(inc)
					text_message_html = f'<body style="margin:0;padding:0;font-weight:lighter;"><font face="Arial" size="2"> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">Здравствуйте!</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">Коллеги, фиксируем недоступность сигнального направления и блокировку голосовых каналов в направлении ' \
										+ str(self.dpc[0]['operators']['name']) + ' ' + str(operator_location) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">OPC: ' + str(self.dpc[0]['opc']) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">DPC: ' + str(self.dpc[0]['name']) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">ТТ с нашей стороны ' + str(
						inc) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">Просьба проверить свою ЗО.</p>'


				else:
					text_theme = f"Недоступность сигнального направления в направлении " + str(
						self.dpc[0]['operators']['name']) + " " + str(self.dpc[0]['locations']['name']) + " // " + str(inc)

					text_message_html = f'<body style="margin:0;padding:0;font-weight:lighter;"><font face="Arial" size="2"> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">Здравствуйте!</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">Коллеги, фиксируем недоступность сигнального направления и блокировку голосовых каналов в направлении ' \
										+ str(self.dpc[0]['operators']['name']) + ' ' + str(self.dpc[0]['locations']['name']) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">OPC: 2 - ' + str(opc_le) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">DPC: 2 - ' + str(self.dpc[0]['name']) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">ТТ с нашей стороны ' + str(inc) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">Просьба проверить свою ЗО.</p>'  # \


			else:
				if self.dpc[0]['operators']['flag']:
					text_theme = f"Блокировка голосовых каналов в направлении " + str(self.dpc[0]['operators']['name']) + " " + str(
						operator_location) + " // " + str(inc)
					text_message_html = f'<body style="margin:0;padding:0;font-weight:lighter;"><font face="Arial" size="2"> \
                                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                                        <p style="margin:0;padding:0;font-weight:lighter;">Здравствуйте!</p> \
                                                        <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                                        <p style="margin:0;padding:0;font-weight:lighter;">Коллеги, фиксируем блокировку голосовых каналов в направлении ' \
										+ str(self.dpc[0]['operators']['name']) + ' ' + str(operator_location) + '</p> \
                                                           <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                                           <p style="margin:0;padding:0;font-weight:lighter;">OPC: ' + str(self.dpc[0]['opc']) + '</p> \
                                                           <p style="margin:0;padding:0;font-weight:lighter;">DPC: ' + str(self.dpc[0]['name']) + '</p> \
                                                           <p style="margin:0;padding:0;font-weight:lighter;">CIC: ' + str(cic) + '</p> \
                                                           <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                                            <p style="margin:0;padding:0;font-weight:lighter;">ТТ с нашей стороны ' + str(inc) + '</p> \
                                                            <p style="margin:0;padding:0;font-weight:lighter;">Просьба проверить свою ЗО.</p>'
				else:
					text_theme = f"Блокировка голосовых каналов в направлении " + str(self.dpc[0]['operators']['name']) + " " + str(
						self.dpc[0]['locations']['name']) + " // " + str(inc)
					text_message_html = f'<body style="margin:0;padding:0;font-weight:lighter;"><font face="Arial" size="2"> \
                                    <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                    <p style="margin:0;padding:0;font-weight:lighter;">Здравствуйте!</p> \
                                    <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                    <p style="margin:0;padding:0;font-weight:lighter;">Коллеги, фиксируем блокировку голосовых каналов в направлении ' \
										+ str(self.dpc[0]['operators']['name']) + ' ' + str(self.dpc[0]['locations']['name']) + '</p> \
                                       <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                       <p style="margin:0;padding:0;font-weight:lighter;">OPC: 2 - ' + str(opc_le) + '</p> \
                                       <p style="margin:0;padding:0;font-weight:lighter;">DPC: 2 - ' + str(self.dpc[0]['name']) + '</p> \
                                       <p style="margin:0;padding:0;font-weight:lighter;">CIC: ' + str(cic) + '</p> \
                                       <p style="margin:0;padding:0;font-weight:lighter;">&nbsp;</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">ТТ с нашей стороны ' + str(inc) + '</p> \
                                        <p style="margin:0;padding:0;font-weight:lighter;">Просьба проверить свою ЗО.</p>'  # \

			if self.dpc[0]['operators']['emails'] != None:
				text_emails = str(self.dpc[0]['operators']['emails']['email'])
			else:
				text_emails = ''

			signature_path = os.path.join((os.environ['USERPROFILE']), 'AppData\\Roaming\\Microsoft\\Signatures\\')
			files = os.listdir(signature_path)
			# print(f'{files=}')

			# if len(files) > 1:

			pattern = re.compile(r'.*\.htm')
			# pattern_files = re.compile(r'.*\.files')
			# print(f'{pattern=}')
			htm_list = []
			# files_list = []
			for it in files:
				if pattern.match(it):
					htm_list.append(it)
			# if pattern_files.match(it):
			# 	files_list.append(it)

			fullDir = signature_path + htm_list[0]

			# print(f'{fullDir=}')

			newDir = fullDir.rsplit("\\", 1)[0]
			subDir = fullDir.rsplit("\\", 1)[1]
			subDir = subDir.replace(" ", "%20")
			subDir = subDir.strip(".htm")
			subDir += ".files"
			newDir += "/" + subDir
			newDir = newDir.replace("\\", "/")
			newDir = newDir.replace("%20", " ")

			newsigfile = ""
			with open(fullDir, 'r') as file:
				for line in file:
					if "src=" in line:
						check = ""
						newline = ""
						check = r'src="' + subDir
						newDir = newDir.replace('/', r'\\')
						newline = re.sub(subDir, newDir, line)
						newsigfile += newline

					else:
						newsigfile += line

			win32.pythoncom.CoInitializeEx(0)
			# outlook = win32.gencache.EnsureDispatch('Outlook.Application')

			try:
				outlook = win32.gencache.EnsureDispatch('Outlook.Application')
			except AttributeError:
				# Remove cache and try again.
				MODULE_LIST = [m.__name__ for m in sys.modules.values()]
				for module in MODULE_LIST:
					if re.match(r'win32com\.gen_py\..+', module):
						del sys.modules[module]
				shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp', 'gen_py'))
				outlook = win32.gencache.EnsureDispatch('Outlook.Application')

			account_outlook = outlook.Session.Accounts.Item('gnoc_sss_smena@mts.ru')

			# outlook_obj = outlook.GetNamespace("MAPI")

			# print(account_outlook)

			mail = outlook.CreateItem(0)
			mail.BodyFormat = 2
			# mail.SentOnBehalfOfName = 'gnoc_sss_smena@mts.ru'
			# mail.Sender = 'gnoc_sss_smena@mts.ru'
			mail.To = text_emails
			mail.CC = f'gnoc_sss_smena@mts.ru; {self.email_region}'
			mail.Subject = text_theme
			mail.HTMLBody = text_message_html + newsigfile
			mail._oleobj_.Invoke(*(64209, 0, 8, 0, account_outlook))
			# mail.GetInspector

			# !!!!!!!!!!!!!!!!!!!!!!!
			# mail.Save()
			# !!!!!!!!!!!!!!!!!!!!!!!
			# mail.Send()
			mail.Display()
			self.ui.search_btn.setEnabled(True)
			self.ui.cb_mgmn_msx.setCurrentIndex(0)


	def show_form_add_email_oper (self):
		self.form = WindowAddEmailOperator()
		self.form.show()



class WindowAddEmailOperator(QMainWindow):
	global USER
	work_requested = QtCore.Signal(int)

	def __init__ (self):
		super(WindowAddEmailOperator, self).__init__()

		self.ui = Ui_WindowAddEmailOperator()
		self.ui.setupUi(self)

		self.setWindowIcon(QIcon(u':/logo/icon.png'))

		# Выравнивание окна по центру монитора
		self.center()

		self.ui.top_statistics_Layout.installEventFilter(self)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground, True)

		self._animation = QPropertyAnimation(self, b'windowOpacity')
		self._animation.setDuration(400)

		self.threadpool = QtCore.QThreadPool()
		# self.threadpool.setMaxThreadCount(2)

		self.data_sp_ros = []
		self.data_sp_ros_list = []
		self.data_sp_mgmn = []
		self.data_sp_mgmn_list = []

		self.loadGeneralStatistics()
		self.responses = Responses()

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 92, 157, 150))

		self.effect = QGraphicsBlurEffect()
		self.effect.setBlurRadius(4)
		self.ui.frame_central.setGraphicsEffect(self.effect)
		self.effect.setEnabled(False)

		self.timer_ok = QTimer(self)
		self.timer_ok.setInterval(1000)

		self._loader = QMovie(":/gif/icons/gif/loading4.gif")
		self.ui.loading_lbl.setScaledContents(True)
		self.ui.loading_lbl.setMovie(self._loader)
		self.ui.loading_lbl.setHidden(True)

		self.ui.users_total_lbl.setText(str(0))
		self.ui.operators_total_lbl.setText(str(0))
		self.ui.operators_total_emails_lbl.setText(str(0))
		self.ui.operators_total_out_emails_lbl.setText(str(0))
		self.ui.total_inc_lbl.setText(str(0))


		self.ui.labelRegionID.setText(str(0))

		self.ui.btn_close.clicked.connect(lambda: self.close())
		self.ui.btn_maximazed.clicked.connect(lambda: self.restore_or_maximize_window())
		self.ui.btn_minimazed.clicked.connect(lambda: self.showMinimized())

		if self.ui.cb_list_regions.currentText() == '':
			self.ui.btn_change_name_region.setDisabled(True)

		self.ui.btn_change_name_region.clicked.connect(lambda: self.showChangeNameRegion())

		self.ui.centralwidget.setGraphicsEffect(self.shadow)

		self.ui.cb_list_operators.addItem('', 0)
		self.ui.cb_list_operators.setMaxVisibleItems(30)
		self.ui.cb_list_operators.setItemDelegate(QStyledItemDelegate(self.ui.cb_list_operators))

		self.ui.cb_list_regions.addItem('', 0)
		self.ui.cb_list_regions.setMaxVisibleItems(30)
		self.ui.cb_list_regions.setItemDelegate(QStyledItemDelegate(self.ui.cb_list_regions))

		self.ui.status.addItem('', 0)
		self.ui.status.setMaxVisibleItems(10)
		self.ui.status.setItemDelegate(QStyledItemDelegate(self.ui.status))

		self.ui.creator.addItem('', 0)
		self.ui.creator.setMaxVisibleItems(10)
		self.ui.creator.setItemDelegate(QStyledItemDelegate(self.ui.creator))

		hidden_visible_obj(self.ui.menu_frame, QPushButton, 'admin__')

		# self.ui.tbl_log.setItemDelegate(QStyledItemDelegate(self.ui.tbl_log))

		self.counter_id: int = 0
		self.counter_regions: int = 0
		self.counter_admins: int = 0

		# self.ui.btn_ok.setFlat(True)
		# self.ui.btn_ok.setAutoFillBackground(True)
		#
		# self.ui.btn_ok_2.setFlat(True)
		# self.ui.btn_ok_2.setAutoFillBackground(True)

		# self.ui.btn_upload_mgmn_outlook.setStyleSheet(STYLE_HOVER)
		# self.ui.btn_pandas_upload.setStyleSheet(STYLE_HOVER)
		# self.ui.btn_add_admin.setStyleSheet(STYLE_HOVER)
		# self.ui.btn_add_field_email_operator.setStyleSheet(STYLE_HOVER)
		# self.ui.btn_change_name_region.setStyleSheet(STYLE_HOVER)
		# self.ui.btn_export_regions.setStyleSheet(STYLE_HOVER)
		# self.ui.btn_clear_log.setStyleSheet(STYLE_HOVER)
		# self.ui.btn_add_field_email_region.setStyleSheet(STYLE_HOVER)
		# self.ui.btn_delete_row_log.setStyleSheet(STYLE_HOVER_RED)

		self.ui.frame_only_icons.hide()
		self.ui.btn_page_add_email_operator.setChecked(True)
		self.ui.stackedWidget.setCurrentIndex(0)

		self.list_admins = SyncORM.listUsersAdminORM()
		self.listAdmins()

		if len(self.list_admins) > 0:
			admins = [item.name for item in self.list_admins]
		else:
			admins = LIST_USERS_ADMIN

		self.admin = [True if USER in admins else False][0]
		if self.admin:
			self.ui.frame_rossreestr.setEnabled(True)
			self.ui.btn_pandas_upload.setEnabled(True)
			self.ui.btn_upload_mgmn_outlook.setEnabled(True)

			hidden_visible_obj(self.ui.menu_frame, QPushButton, 'admin__', True)

			self.progressBar = QProgressBar()
			self.statusBar().addPermanentWidget(self.progressBar, stretch = 1)
			self.progressBar.setHidden(True)
			self.progressBar.setValue(0)

			self.data_log = ''


			self.all_inc_frm = MouseObserver(self.ui.all_inc_frm)
			self.all_operators_frm = MouseObserver(self.ui.all_operators_frm)
			self.operators_with_emails = MouseObserver(self.ui.operators_with_emails)
			self.operators_without_emails = MouseObserver(self.ui.operators_without_emails)
			self.users_frm = MouseObserver(self.ui.users_frm)

			self.all_inc_frm.clicked_widget.connect(self.selectCurrentPageStatistics)
			self.all_operators_frm.clicked_widget.connect(self.selectCurrentPageStatistics)
			self.operators_with_emails.clicked_widget.connect(self.selectCurrentPageStatistics)
			self.operators_without_emails.clicked_widget.connect(self.selectCurrentPageStatistics)
			self.users_frm.clicked_widget.connect(self.selectCurrentPageStatistics)

			self.ui.ledit_statistics_page.textChanged.connect(self.changePageStatistics)


		def moveWindow (e):
			if self.isMaximized() == True:
				self.showNormal()
				self.ui.btn_maximazed.setIcon(QIcon(u":/icons/icons/maximize-2_.svg"))

			if self.isMaximized() == False:
				if e.buttons() == Qt.LeftButton:
					self.move(self.pos() + e.globalPos() - self.clickPosition)
					self.clickPosition = e.globalPos()
					e.accept()

		self.ui.main_header_frame.mouseMoveEvent = moveWindow

		self.ui.admin__btn_upload_all_emails.clicked.connect(self.uploadEmailsFromDb)
		self.ui.admin__btn_upload_all_emails_2.clicked.connect(self.uploadEmailsFromDb)
		self.ui.admin__btn_download_all_emails.clicked.connect(self.downloadEmailsJson)
		self.ui.admin__btn_download_all_emails_2.clicked.connect(self.downloadEmailsJson)
		self.ui.btn_export_regions.clicked.connect(self.downloadEmailsRegionFromCsv)

		self.ui.btn_page_add_email_operator.clicked.connect(
			lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_add_email_operator))
		self.ui.btn_page_add_email_operator_2.clicked.connect(
			lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_add_email_operator))

		# Load Page 2
		self.ui.btn_page_add_emails_region.clicked.connect(
			lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_add_emails_region))
		self.ui.btn_page_add_emails_region_2.clicked.connect(
			lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_add_emails_region))

		# Load Page 3
		self.ui.btn_page_pandas_html_load.clicked.connect(
			lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_pandas_html_load))
		self.ui.btn_page_pandas_html_load_2.clicked.connect(
			lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_pandas_html_load))

		# Load Page 4
		self.ui.admin__btn_log.clicked.connect(lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_log))
		self.ui.admin__btn_log_2.clicked.connect(lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_log))

		# Load Page 5
		self.ui.admin__btn_statistics.clicked.connect(lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_statistics))
		self.ui.admin__btn_statistics_2.clicked.connect(lambda: MainFunctions.set_page_stackedWidget(self, self.ui.page_statistics))

		self.lists_operators = ''

		self.changePage()
		self.ui.ledit_page.textChanged.connect(self.changePage)

		########################################################################################
		# FOR PAGE 1
		########################################################################################
		self.ui.cb_list_operators.setEditable(True)
		self.ui.cb_list_operators.setInsertPolicy(QComboBox.NoInsert)
		cb_completer = MyCustomQCompleter(self.ui.cb_list_operators)
		cb_completer.setCompletionMode(QCompleter.PopupCompletion)
		cb_completer.setModel(self.ui.cb_list_operators.model())
		self.ui.cb_list_operators.setCompleter(cb_completer)
		self.ui.cb_list_operators.setPlaceholderText(u'Введите оператора...')
		self.ui.cb_list_operators.setStyleSheet("QLineEdit {background-color: red;}")

		cb_completer.popup().setStyleSheet('font-size: 14px; \
                                font-family: Arial, Helvetica, sans-serif; \
                                background-color: rgb(69, 100, 129); \
                                color: #ffffff;')

		# Отслеживаем изменение в ComboBox
		self.ui.cb_list_operators.activated.connect(self.getValueIdOperator)

		email = {'id': None, 'email': None}
		self.ui.btn_add_field_email_operator.clicked.connect(lambda: self.add_emailoperator(self.counter_id, email))
		self.ui.btn_save_emails_operator.clicked.connect(self.listTextLineEdit)

		########################################################################################
		# FOR PAGE 2
		########################################################################################
		self.list_regions = ''

		self.ui.count_regions.setText(str(5))

		self.setItemsTable(self.list_regions, self.ui.cb_list_regions, self.ui.emails_region, self.ui.count_regions)

		self.ui.emails_region.horizontalHeader().setStretchLastSection(True)

		self.ui.cb_list_regions.setEditable(True)
		self.ui.cb_list_regions.setInsertPolicy(QComboBox.NoInsert)
		cb_completer_region = MyCustomQCompleter(self.ui.cb_list_regions)
		cb_completer_region.setCompletionMode(QCompleter.PopupCompletion)
		cb_completer_region.setModel(self.ui.cb_list_regions.model())

		self.ui.cb_list_regions.setCompleter(cb_completer_region)
		self.ui.cb_list_regions.setPlaceholderText(u'Введите регион...')
		self.ui.cb_list_regions.setStyleSheet("QLineEdit {background-color: red;}")

		cb_completer_region.popup().setStyleSheet('font-size: 14px; \
                                        font-family: Arial, Helvetica, sans-serif; \
                                        background-color: rgb(69, 100, 129); \
                                        color: #ffffff;')

		# Отслеживаем изменение в ComboBox
		self.ui.cb_list_regions.activated.connect(self.getValueIdRegion)

		email_region = {'id': None, 'email': None}
		self.ui.btn_add_field_email_region.clicked.connect(lambda: self.add_emailregion(self.counter_regions, email_region))
		self.ui.btn_save_emails_region.clicked.connect(self.listTextLineEditRegion)

		########################################################################################
		# FOR PAGE 3
		########################################################################################
		self.counter = 0
		self.headers_ros = ["ID DPC", "Декадный", "AВС/DEF", "Структурный", "Зона обслуживания", "Оператор", "Место установки"]
		self.headers_mgmmn = ["DPC/IP", "OPC", "Коммутатор", "Название транка", "Регион коммутатора",
							  "Регион шлюза", "Уровень присоед.", "ID DPC", "Назначение транка"]
		self.header_log = ["ID", "Статус", "Пользователь", "Событие", "Дата и время записи"]

		# self.timer = QTimer()
		# self.timer.setInterval(1000)
		# # self.timer.timeout.connect(self.recurring_timer)
		# self.timer.timeout.connect(self.progress_fn)
		# self.timer.setInterval(1000)
		# self.timer.start()
		self.ui.tabWidget.setCurrentIndex(0)
		self.ui.tabWidget.currentChanged.connect(self.selectedOutlookTab)
		self.ui.btn_pandas_upload.clicked.connect(self.uploadDataFromRossreestr)
		self.ui.btn_upload_mgmn_outlook.clicked.connect(self.uploadDataFromMgmn)

		########################################################################################
		# FOR PAGE 4
		########################################################################################
		self.ui.btn_add_admin.clicked.connect(lambda: self.addNewAdmin(self.counter_admins))

		self.thread = QtCore.QThread(self)

		self.ui.btn_delete_row_log.clicked.connect(self.deleteRowLogUser)
		self.ui.btn_clear_log.clicked.connect(self.clearLogsInfo)

		########################################################################################
		# FOR PAGE 5
		########################################################################################
		self.list_incidents = ''
		self.checkedIncFromDelete = []
		self.listIncFromDelete = []
		self.count_item_base_list_incidents: int = 0
		self.side_menu = self.ui.statistics_menu_listWidget
		self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)

		self.side_menu.currentTextChanged.connect(self.set_title_incident)

		self.operators_statistics_menu = self.ui.operators_listWidget
		self.operators_statistics_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)


		self.main_content_statistics = self.ui.statistics_stackedWidget
		self.menu_statistics_list = [
			{
				"title": "Операторы",
				"name": "operators_page",
				"icon": ":/icons/icons/globe.svg"
			},
			{
				"title": "Пользователи",
				"name": "users_page",
				"icon": ":/icons/icons/users.svg"
			},
			{
				"title": "Инциденты",
				"name": "all_inc_page",
				"icon": ":/icons/icons/trello.svg"
			},
		]

	# def eventFilter (self, obj, event):
	# 	if obj is self.ui.top_statistics_widget and event.type() == QEvent.Type.MouseButtonPress:
	# 		print(f'{obj.objectName()=}')
	# 		print(f'{event=}')
	# 		print(f'{event.type()=}')
	# 	#
	# 	# 	event.ignore()
	# 	# 	return True
	# 	return super(WindowAddEmailOperator, self).eventFilter(obj, event)

	def center (self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def fade_in (self):
		try:
			self._animation.finished.disconnect(self.close)
		except:
			pass
		self._animation.stop()
		self._animation.setStartValue(0)
		self._animation.setEndValue(1)
		self._animation.start()

	def fade_out (self):
		# loop = QEventLoop()
		# print(f'{loop=}')
		# self._animation.finished.connect(loop.quit)
		self._animation.finished.connect(self.close)
		self._animation.setDirection(QPropertyAnimation.Backward)
		self._animation.start()
		# loop.exec_()

	def showEvent (self, event):
		super().showEvent(event)
		self.fade_in()

	def closeEvent (self, event):
		self.fade_out()
		super().closeEvent(event)

	# def hideEvent (self, event):
	# 	self.fade_out()
	# 	super().hideEvent(event)

	def progress_fn (self, n):
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(0)

	def print_output_ros (self, result_upload_table_ross):
		self.data_sp_ros = result_upload_table_ross
		self.data_sp_ros_list = convertJsonToList(self.data_sp_ros)

	def print_output_mgmn (self, result_upload_table_mgmn):
		self.data_sp_mgmn = result_upload_table_mgmn
		self.data_sp_mgmn_list = convertJsonToList(self.data_sp_mgmn)

	def completeUploadTableRossreestr (self):
		# print(f'{self.data_sp_ros_list=}')
		self.model_2 = MyTableModel(self.data_sp_ros_list, self.headers_ros)
		self.proxy_model_2 = QSortFilterProxyModel()
		self.proxy_model_2.setSourceModel(self.model_2)
		self.proxy_model_2.setFilterKeyColumn(-1)  # all columns

		self.proxy_model_2.sort(1, Qt.AscendingOrder)

		self.ui.tbl_data_pandas.setModel(self.proxy_model_2)
		self.ui.tbl_data_pandas.verticalHeader().setVisible(False)
		self.ui.tbl_data_pandas.setSortingEnabled(True)
		# self.ui.tbl_data_pandas.resizeColumnsToContents()
		self.ui.tbl_data_pandas.setColumnWidth(1, 130)
		self.ui.tbl_data_pandas.setColumnWidth(2, 200)
		self.ui.tbl_data_pandas.setColumnWidth(3, 130)
		# self.ui.tbl_data_pandas.setColumnWidth(4, 380)
		self.ui.tbl_data_pandas.setColumnWidth(5, 500)
		self.ui.tbl_data_pandas.setColumnWidth(6, 300)
		# self.ui.tbl_data_pandas.horizontalHeader().resizeSection(7, 350)

		# self.ui.tbl_data_pandas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.tbl_data_pandas.sortByColumn(0, QtCore.Qt.DescendingOrder)
		self.ui.tbl_data_pandas.horizontalHeader().setSortIndicatorShown(True)
		self.ui.tbl_data_pandas.setColumnHidden(0, True)
		self.ui.tbl_data_pandas.setColumnHidden(4, True)
		# self.ui.tbl_data_pandas.setColumnHidden(7, True)
		# self.ui.tbl_data_pandas.setColumnHidden(8, True)
		self.ui.tbl_data_pandas.setSelectionBehavior(self.ui.tbl_data_pandas.SelectRows)

		# def filter_function (text):
		#     self.proxy_model_2.setFilterFixedString(str(self.ui.le_search_rossreestr.text()))

		self.ui.le_search_rossreestr.setPlaceholderText("Искать...")
		self.ui.le_search_rossreestr.textChanged.connect(self.proxy_model_2.setFilterFixedString)
		# self.ui.le_search_rossreestr.textChanged.connect(filter_function)

		self.mapper_2 = QDataWidgetMapper()
		self.mapper_2.setModel(self.proxy_model_2)
		#
		# self.mapper.addMapping(self.dpc_id, 0)
		self.mapper_2.addMapping(self.ui.le_decadnii, 1)
		self.mapper_2.addMapping(self.ui.le_abc_def, 2)
		self.mapper_2.addMapping(self.ui.le_structurnii, 3)
		self.mapper_2.addMapping(self.ui.le_zone_obslujivaniya, 4)
		self.mapper_2.addMapping(self.ui.le_operator, 5)
		self.mapper_2.addMapping(self.ui.le_mesto_ustanovki, 6)

		self.ui.tbl_data_pandas.selectionModel().currentRowChanged.connect(self.mapper_2.setCurrentModelIndex)

		self.mapper_2.toFirst()  # .toLast() #.toFirst()

		if len(self.data_sp_ros) > 0:
			self.responses.success_message_status_bar(
				self.statusBar(),
				"Данные Россреестра успешно загружены",
				3000
			)

	def completeUploadTableMgmn (self):
		self.model = MyTableModel(self.data_sp_mgmn_list, self.headers_mgmmn)

		self.proxy_model = QSortFilterProxyModel()
		self.proxy_model.setSourceModel(self.model)
		# self.proxy_model.sort(1, QtCore.Qt.AscendingOrder) #.DescendingOrder) #.AscendingOrder)
		self.proxy_model.setFilterKeyColumn(-1)  # all columns
		self.ui.tbl_data_pandas_mgmn.setModel(self.proxy_model)
		self.ui.tbl_data_pandas_mgmn.verticalHeader().setVisible(False)
		self.ui.tbl_data_pandas_mgmn.setSortingEnabled(True)
		# self.ui.tbl_data_pandas.resizeColumnsToContents()
		self.ui.tbl_data_pandas_mgmn.setColumnWidth(0, 100)
		self.ui.tbl_data_pandas_mgmn.setColumnWidth(1, 100)
		self.ui.tbl_data_pandas_mgmn.setColumnWidth(2, 150)
		self.ui.tbl_data_pandas_mgmn.setColumnWidth(3, 250)
		self.ui.tbl_data_pandas_mgmn.setColumnWidth(4, 180)
		self.ui.tbl_data_pandas_mgmn.setColumnWidth(5, 180)
		self.ui.tbl_data_pandas_mgmn.setColumnWidth(6, 150)
		self.ui.tbl_data_pandas_mgmn.setColumnWidth(8, 450)

		# self.ui.tbl_data_pandas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.tbl_data_pandas_mgmn.sortByColumn(0, QtCore.Qt.AscendingOrder)
		self.ui.tbl_data_pandas_mgmn.horizontalHeader().setSortIndicatorShown(True)
		self.ui.tbl_data_pandas_mgmn.setColumnHidden(7, True)

		self.ui.le_search.setPlaceholderText("Искать...")
		self.ui.le_search.textChanged.connect(self.proxy_model.setFilterFixedString)

		self.mapper = QDataWidgetMapper()
		self.mapper.setModel(self.proxy_model)

		self.mapper.addMapping(self.ui.le_kommutator, 2)
		self.mapper.addMapping(self.ui.le_name_trank, 3)
		self.mapper.addMapping(self.ui.le_dpc_name, 0)
		self.mapper.addMapping(self.ui.le_opc, 1)
		self.mapper.addMapping(self.ui.le_operator_name, 8)
		self.mapper.addMapping(self.ui.le_region_kommutatora, 4)
		self.mapper.addMapping(self.ui.le_region_shluza, 5)
		self.mapper.addMapping(self.ui.le_uroven_prisoedineniya, 6)

		self.ui.tbl_data_pandas_mgmn.selectionModel().currentRowChanged.connect(self.mapper.setCurrentModelIndex)
		self.mapper.toFirst()  # .toLast() #.toFirst()

		if len(self.data_sp_mgmn) > 0:
			self.responses.success_message_status_bar(
				self.statusBar(),
				"Данные МгМн транкгрупп успешно загружены.",
				3000
			)

	def completeUploadLogs (self):

		self.model_log = []
		self.ui.tbl_log.viewport().update()
		self.model_log = MyTableModel(self.data_log_list, self.header_log)

		self.proxy_model_log = MySortFilterProxyModel(self)
		self.proxy_model_log.setSourceModel(self.model_log)
		self.proxy_model_log.setFilterKeyColumn(-1)  # all columns
		#
		self.ui.tbl_log.setSortingEnabled(True)
		self.ui.tbl_log.setModel(self.proxy_model_log)
		self.ui.tbl_log.verticalHeader().setVisible(False)

		# self.ui.tbl_log.resizeColumnToContents(4)
		self.ui.tbl_log.setColumnWidth(0, 50)
		self.ui.tbl_log.setColumnWidth(1, 100)
		self.ui.tbl_log.setColumnWidth(2, 200)
		self.ui.tbl_log.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
		# self.ui.tbl_log.setColumnWidth(3, 420)
		self.ui.tbl_log.setColumnWidth(4, 180)

		# self.ui.tbl_log.horizontalHeader().setSectionResizeMode()
		self.ui.tbl_log.sortByColumn(4, QtCore.Qt.AscendingOrder) #.DescendingOrder)
		self.ui.tbl_log.horizontalHeader().setSortIndicatorShown(True)
		# self.ui.tbl_log.setColumnHidden(0, True)

		self.responses.success_message_status_bar(
			self.statusBar(),
			"Логированные данные успешно загружены.",
			3000
		)

	def filters_in_db_logs (self):
		filter_layout = {}
		date_created = []

		def search_filter (layout):
			for i in reversed(range(layout.count())):
				layoutItem = layout.itemAt(i)

				if type(layoutItem) is QSpacerItem:
					continue

				if layoutItem.widget() is not None:
					widgetToFilter = layoutItem.widget()

					if isinstance(widgetToFilter, QDateEdit):
						list_name_cut = widgetToFilter.objectName()
						if list_name_cut.endswith('__start'):
							data = widgetToFilter.date()
							data_py = data.toPython()
							date_created.append({list_name_cut: data_py})
						if list_name_cut.endswith('__end'):
							data = widgetToFilter.date()
							data_py = data.toPython() + timedelta(days = +1)
							date_created.append({list_name_cut: data_py})

						list_name_cut = list_name_cut[:11]
						data_filter = date_created

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

					if isinstance(widgetToFilter, QGroupBox):
						for item in widgetToFilter.findChildren(QRadioButton):
							if item.isChecked():
								list_name_cut = item.objectName()
								data_filter = item.isChecked()

					filter_layout.update({list_name_cut: data_filter})

				else:
					layoutToFilter = layout.itemAt(i)
					search_filter(layoutToFilter)

		search_filter(self.ui.layoutFiltrsLogs)
		self.filter_log = filter_layout

		self.loadLogsInfo()

	def changePage (self):
		page = int(self.ui.ledit_page.text())
		if page == 0:
			if self.lists_operators == '':
				self.lists_operators = SyncORM.listAllOperatorsORM()
				# data_list_operators = SyncORM.listAllOperatorsORM()
				# self.lists_operators = data_list_operators
				self.loadListOperators(self.lists_operators)
				# self.loadListOperators(data_list_operators)
		elif page == 1:
			self.clear_area_region()
			if self.list_regions == '':
				self.list_regions = SyncORM.listAllRegionsORM()
			self.setItemsTable(self.list_regions, self.ui.cb_list_regions, self.ui.emails_region, self.ui.count_regions)

		elif page == 2:
			if len(self.data_sp_ros) == 0:
				self.loadRossreestr()

		elif page == 3:
			self.filters_in_db_logs()
			self.ui.status.textActivated.connect(self.filters_in_db_logs)
			self.ui.creator.textActivated.connect(self.filters_in_db_logs)
			self.ui.date_create__start.dateChanged.connect(self.filters_in_db_logs)
			self.ui.date_create__end.dateChanged.connect(self.filters_in_db_logs)

			self.getDataToListFromFilters()

		elif page == 4:
			self.init_single_slot()
			self.init_list_widget()

			self.side_menu.currentRowChanged['int'].connect(self.set_ledit_statistics_page)

			self.changePageStatistics()

	#######################################################################################
	#Page Statistics
	######################################################################################

	def init_single_slot (self):
		self.side_menu.currentRowChanged['int'].connect(self.main_content_statistics.setCurrentIndex)

	def init_list_widget (self):
		self.side_menu.clear()

		for menu in self.menu_statistics_list:
			item_new = QListWidgetItem()
			item_new.setIcon(QIcon(menu.get("icon")))
			item_new.setText(menu.get("title"))
			self.side_menu.addItem(item_new)
			self.side_menu.setCurrentRow(0)

	def init_list_widget_operators(self):
		self.operators_statistics_menu.clear()
		# print(self.lists_operators)
		for oper in self.lists_operators:
			# print(oper.name, oper.id, oper.flag)
			item_new = QListWidgetItem()
			item_new.setText(oper.name)
			self.operators_statistics_menu.addItem(item_new)
			self.operators_statistics_menu.setCurrentRow(0)


	def set_ledit_statistics_page(self, index):
		self.ui.ledit_statistics_page.setText(str(index))

	def set_title_incident(self, title):
		self.ui.title_inc_lbl.setText(title)


	def selectCurrentPageStatistics(self, obj):
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_statistics)
		self.ui.ledit_page.setText(str(self.ui.stackedWidget.currentIndex()))
		self.ui.admin__btn_statistics.setChecked(True)
		self.ui.admin__btn_statistics_2.setChecked(True)
		self.init_single_slot()
		self.init_list_widget()
		if obj == 'all_inc_frm':
			MainFunctions.set_page_statistics_stackedWidget(self, self.ui.all_inc_page)
		elif obj in ['all_operators_frm', 'operators_with_emails', 'operators_without_emails']:
			MainFunctions.set_page_statistics_stackedWidget(self, self.ui.operators_page)
		elif obj == 'users_frm':
			MainFunctions.set_page_statistics_stackedWidget(self, self.ui.users_page)
		self.side_menu.setCurrentRow(self.ui.statistics_stackedWidget.currentIndex())


	def changePageStatistics (self):
		# self.init_single_slot()
		page_stat = int(self.ui.ledit_statistics_page.text())
		# page_stat = int(self.ui.statistics_stackedWidget.currentIndex())
		if page_stat == 0:
			print(f'Выбрана страница: {page_stat}')
			# print(f'1_{self.lists_operators=}')
			self.init_list_widget_operators()
		elif page_stat == 1:
			print(f'Выбрана страница: {page_stat}')
			pass
		elif page_stat == 2:
			print(f'Выбрана страница: {page_stat}')

			icon_down = ':/icons/icons/chevrons-down.svg'
			icon_up = ':/icons/icons/chevrons-up.svg'
			self.ui.cmb_sorting_inc.clear()
			self.ui.cmb_sorting_inc.addItem('Сортировать по ...')
			self.ui.cmb_sorting_inc.addItem(QIcon(icon_down), '№ Инцидента', ('name__down'))
			self.ui.cmb_sorting_inc.addItem(QIcon(icon_up), '№ Инцидента', ('name__up'))
			self.ui.cmb_sorting_inc.addItem(QIcon(icon_down), 'Дате', ('date__down'))
			self.ui.cmb_sorting_inc.addItem(QIcon(icon_up), 'Дате', ('date__up'))

			self.ui.cmb_sorting_inc.currentIndexChanged.connect(self.sortingIncidents)

			self.ui.lbl_link_inc.setOpenExternalLinks(True)
			self.ui.inc_stat_toolBox.setCurrentIndex(0)
			self.ui.inc_stat_toolBox.currentChanged.connect(self.__onToolTabChanged__)
			# self.ui.inc_stat_toolBox.setStyleSheet("QToolBox{ icon-size: 40px; }")
			self.list_obj = self.ui.inc_stat_toolBox.findChildren(QAbstractButton, "qt_toolbox_toolboxbutton")
			self.list_obj[0].setIcon(QIcon(u':/icons/icons/chevron-up_.svg'))
			self.list_obj[1].setIcon(QIcon(u':/icons/icons/chevron-down_.svg'))
			for item in range(0, len(self.list_obj)):
				# print(f'{list_obj[item]=}')
				self.list_obj[item].setCursor(Qt.PointingHandCursor)

			if self.list_incidents == '':
				self.list_all_incidents()

			self.ui.btn_delete_inc.clicked.connect(self.deleteSelectedIncidents)


	def __onToolTabChanged__ (self, i):
		for h in range(len(self.list_obj)):
			if h == i:
				self.list_obj[h].setIcon(QIcon(u':/icons/icons/chevron-up_.svg'))
			else:
				self.list_obj[h].setIcon(QIcon(u':/icons/icons/chevron-down_.svg'))

	def sortingIncidents(self, index):
		self.list_all_incidents(self.ui.cmb_sorting_inc.currentData())

	def deleteSelectedIncidents(self):
		if len(self.checkedIncFromDelete) > 0:
			deleted_inc = SyncORM.deleteSelectedIncident(self.checkedIncFromDelete)
			if deleted_inc:
				new_list_incidents = []
				for item in self.list_incidents:
					if item.get("id") not in self.checkedIncFromDelete:
						new_list_incidents.append(item)
					else:
						continue
				self.list_incidents = new_list_incidents

				self.loadGeneralStatistics()
				self.loadingBaseListIncidents(self.list_incidents)

				self.responses.success_message_status_bar(
					self.statusBar(),
					f"Все выделенные инциденты: {self.listIncFromDelete} успешно удалены.",
					3000
				)
				self.checkedIncFromDelete.clear()
				self.listIncFromDelete.clear()
				# new_list_incidents.clear()

			else:
				self.responses.error_message_status_bar(
					self.statusBar(),
					"Что-то пошло не так. Попробуйте ещё раз.",
					3000
				)


	def list_all_incidents (self, sorting=None):
		self.list_incidents = SyncORM.listAllIncidentsORM(sorting)
		self.loadingBaseListIncidents(self.list_incidents)

		# worker_inc = Worker(SyncORM.listAllIncidentsORM, sorting)
		# worker_inc.signals.result.connect(self.loadingBaseListIncidents)
		# worker_inc.signals.error.connect(self.errorsLoadingIncidents)
		# worker_inc.signals.loading_start.connect(self.loadingGif)
		# worker_inc.signals.loading_stop.connect(self.loadingGif)
		# self.threadpool.start(worker_inc)

	# def errorsLoadingIncidents(self, errors):
	# 	print(f'{errors=}')
		# print(f'{value=}')
		# print(f'{traceback=}')


	def loadingBaseListIncidents(self, data_incidents):
		# print(f'Из loadingBaseListIncidents: {data_incidents=}')
		self.list_incidents = data_incidents
		while self.ui.list_incidents_layout.count() > 0:
			item = self.ui.list_incidents_layout.takeAt(0)
			item.widget().deleteLater()

		for item in data_incidents:
			self.count_item_base_list_incidents += 1
			item_incident = BaseItemIncidentsWidget(
				id_widget_base_item_incident = self.count_item_base_list_incidents,
				parent = self,
				**item
			)
			self.ui.list_incidents_layout.addWidget(item_incident)
			item_incident.checked_incident.connect(self.checkedIncident)
			item_incident.clicked_incident.connect(self.clickedIncident)

	def clickedIncident(self,id_wid, data, clicked_lbl=False):
		# print(f'ID widgeta: {id_wid=}  ID inc: {clicked_lbl=}')

		# widget = self.sender()
		# print(f'Из clickedIncident: {data=}')

		if data['dpc']['locations']:
			locations = ', '.join(data['dpc']['locations']['name'].split('|'))
		else:
			locations = ''
		# if clicked_lbl:
		# 	widget.setStyleSheet("""QLabel{color: red;}""")
		# else:
		# 	widget.setStyleSheet("""QLabel{color: green;}""")

		self.ui.le_inc_stat.setText(data['name'])
		self.ui.lbl_operator_stat_inc.setText(data['operator_name'])
		self.ui.le_opc_stat.setText(data['opc_name'])
		self.ui.le_dpc_stat.setText(data['dpc_name'])
		self.ui.lbl_location_operator_stat.setText(locations)
		if not data['flag']:
			self.ui.cb_type_operator.setCurrentIndex(1)
		else:
			self.ui.cb_type_operator.setCurrentIndex(2)

		self.ui.email_operator_listWidget.clear()
		if data['dpc']['operators']['emails'] != None:
			emails = data['dpc']['operators']['emails']['email'].split(';')
			for email in emails:
				self.ui.email_operator_listWidget.addItem(email.strip())

		self.selectedIncStatistics(data['name'])

	def selectedIncStatistics(self, inc_name):
		data = SyncGasiORM.selectedIncident(inc_name)
		if data:
			self.ui.lbl_status_inc_stat.setText(str(data[0]['status']))
			self.ui.lbl_cause_inc_stat.setText(str(data[0]['cause']))
			link = data[0]['link']
			if link:
				link_a = f"<a href='{link}' style='color:#5983a7; text-decoration: none;'>{link}</a>"
				self.ui.lbl_link_inc.setText(str(link_a))

			self.ui.lbl_source_inc_stat.setText(str(data[0]['source']))
			self.ui.le_parent_inc.setText(str(data[0]['parent_inc']))

	def checkedIncident(self, status, inc_name, id_inc):
		# print(f'Status: {status} ID widgeta: {id_wid=}  ID inc: {id_inc=}')
		if status:
			self.checkedIncFromDelete.append(id_inc)
			self.listIncFromDelete.append(inc_name)
		else:
			self.checkedIncFromDelete.remove(id_inc)
			self.listIncFromDelete.remove(inc_name)
		if len(self.checkedIncFromDelete):
			self.ui.btn_delete_inc.setIcon(QIcon(u":/icons/icons/trash-2.svg"))
		else:
			self.ui.btn_delete_inc.setIcon(QIcon(u":/icons/icons/trash.svg"))

	# def init_stackwidget (self):
	#     # Initialize the stack widget with content pages
	#     widget_list = self.main_content_statistics.findChildren(QWidget)
	#     for widget in widget_list:
	#         self.main_content_statistics.removeWidget(widget)
	#
	#     for menu in self.menu_statistics_list:
	#         page = menu.get("name")
	#         self.main_content_statistics
	# layout = QGridLayout()
	# label = QLabel(text)
	# label.setAlignment(Qt.AlignmentFlag.AlignCenter)
	# font = QFont()
	# font.setPixelSize(20)
	# label.setFont(font)
	# layout.addWidget(label)
	# new_page = QWidget()
	# new_page.setLayout(layout)
	# self.main_content_statistics.addWidget(new_page)
	def loadingGif (self, status):
		if status:
			self.ui.loading_lbl.setHidden(False)
			self._loader.start()
		else:
			self.ui.loading_lbl.setHidden(True)
			self._loader.stop()

	def print_output_top_stat_info (self, result_data):
		total_operators = result_data["operators_info"]["count_operators"]
		total_operators_with_emails = result_data["operators_info"]["count_operators_emails"]
		total_operators_without_emails = total_operators - total_operators_with_emails
		self.ui.users_total_lbl.setText(str(f'{result_data["count_users"]}'))
		self.ui.operators_total_lbl.setText(str(total_operators))
		self.ui.operators_total_emails_lbl.setText(str(total_operators_with_emails))
		self.ui.operators_total_out_emails_lbl.setText(str(total_operators_without_emails))
		self.ui.total_inc_lbl.setText(str(f'{result_data["total_inc"]}'))

	def loadGeneralStatistics (self):
		worker_general_stat = Worker(SyncORM.loadGeneralStatisticsORM)
		worker_general_stat.signals.result.connect(self.print_output_top_stat_info)
		worker_general_stat.signals.loading_start.connect(self.loadingGif)
		worker_general_stat.signals.loading_stop.connect(self.loadingGif)
		self.threadpool.start(worker_general_stat)

		# worker = Worker(SyncORM.loadGeneralStatisticsORM)
		# worker.signals.result.connect(self.print_output_ros)
		# worker.signals.finished.connect(self.completeUploadTableRossreestr)
		# worker.signals.progress.connect(self.progress_fn)
		# self.threadpool.start(worker)



	def loadRossreestr (self):
		worker = Worker(SyncORM.listAllSpORM, False)
		worker.signals.result.connect(self.print_output_ros)
		worker.signals.finished.connect(self.completeUploadTableRossreestr)
		worker.signals.progress.connect(self.progress_fn)
		worker.signals.loading_start.connect(self.loadingGif)
		worker.signals.loading_stop.connect(self.loadingGif)
		self.threadpool.start(worker)

	def loadLogsInfo (self):
		worker_log = Worker(SyncORM.listLogsORM, self.filter_log)
		worker_log.signals.result.connect(self.convert_data_log)
		worker_log.signals.finished.connect(self.completeUploadLogs)
		worker_log.signals.progress.connect(self.progress_fn)
		worker_log.signals.loading_start.connect(self.loadingGif)
		worker_log.signals.loading_stop.connect(self.loadingGif)
		self.threadpool.start(worker_log)

	def convert_data_log (self, data_log):
		self.data_log = data_log
		self.data_log_list = convertJsonToList(self.data_log)

	def getDataToListFromFilters (self):
		data_from_filters = SyncORM.getDataToListFromFiltersORM()
		# print(f'{type(data_from_filters)=}')
		data_status = set()
		data_creators = set()
		data_creates = []
		for item in data_from_filters:
			data_status.add(item['status'])
			data_creators.add(item['creator'])
			data_creates.append(item["date_create"])

		# print(f'Мин дата: {min(data_creates)}')
		# print(f'Макс дата: {max(data_creates)}')

		# max_data_creates = max(data_creates)

		# qtDate_min = datetime.strftime(min_data_creates, "%d-%m-%Y")

		# print(qtDate_min)

		# print(f'{type(min_data_creates)}')
		# print(f'{QtCore.QDateTime.fromString(qtDate_min, "dd-MM-yyyy hh:mm:ss")}')

		# qtDate_min = QtCore.QDate.fromString(min_data_creates, 'yyyy/M/d')

		# begin_text = QtCore.QDate.fromString(qtDate_min, "yyyy-MM-dd")
		#
		# print(f'{begin_text=}')

		# qtDate_end = QtCore.QDate.currentDate()
		# qtDate_min = QtCore.QDate.setDate(QtCore.QDateTime.fromString(qtDate_min, "dd-MM-yyyy hh:mm:ss"))

		min_data_creates = min(data_creates)
		self.ui.date_create__start.setDateTime(min_data_creates)
		self.ui.date_create__end.setDateTime(QtCore.QDateTime.currentDateTime())

		self.ui.status.clear()
		self.ui.status.addItem('')
		for status in data_status:
			self.ui.status.addItem(status)

		# self.ui.status.setCurrentIndex(-1)
		# self.ui.status.setPlaceholderText('Проба')

		self.ui.creator.clear()
		self.ui.creator.addItem('')
		for creator in data_creators:
			self.ui.creator.addItem(creator)
		self.ui.creator.setCurrentIndex(-1)

	def clearLogsInfo (self):
		self.ui.tbl_log.setModel(None)
		clears_all = SyncORM.clearLogsORM()
		if clears_all:
			self.responses.success_message_status_bar(
				self.statusBar(),
				"Все записи успешно удалены.",
				3000
			)
		else:
			self.responses.error_message_status_bar(
				self.statusBar(),
				"Что-то пошло не так. Попробуйте ещё раз.",
				3000
			)

	def selectedOutlookTab (self):
		if self.ui.tabWidget.currentIndex() == 1:
			if len(self.data_sp_mgmn) == 0:
				worker = Worker(SyncORM.listAllSpORM, True)
				worker.signals.result.connect(self.print_output_mgmn)
				worker.signals.finished.connect(self.completeUploadTableMgmn)
				worker.signals.progress.connect(self.progress_fn)
				worker.signals.loading_start.connect(self.loadingGif)
				worker.signals.loading_stop.connect(self.loadingGif)
				self.threadpool.start(worker)

		# self.data_sp_mgmn_list = convertJsonToList(self.data_sp_mgmn)

		# self.model = MyTableModel(self.data_sp_mgmn_list, self.headers_mgmmn)
		#
		# self.proxy_model = QSortFilterProxyModel()
		# self.proxy_model.setSourceModel(self.model)
		# # self.proxy_model.sort(1, QtCore.Qt.AscendingOrder) #.DescendingOrder) #.AscendingOrder)
		# self.proxy_model.setFilterKeyColumn(-1)  # all columns
		# self.ui.tbl_data_pandas_mgmn.setModel(self.proxy_model)
		# self.ui.tbl_data_pandas_mgmn.verticalHeader().setVisible(False)
		# self.ui.tbl_data_pandas_mgmn.setSortingEnabled(True)
		# # self.ui.tbl_data_pandas.resizeColumnsToContents()
		# self.ui.tbl_data_pandas_mgmn.setColumnWidth(0, 100)
		# self.ui.tbl_data_pandas_mgmn.setColumnWidth(1, 100)
		# self.ui.tbl_data_pandas_mgmn.setColumnWidth(2, 150)
		# self.ui.tbl_data_pandas_mgmn.setColumnWidth(3, 250)
		# self.ui.tbl_data_pandas_mgmn.setColumnWidth(4, 180)
		# self.ui.tbl_data_pandas_mgmn.setColumnWidth(5, 180)
		# self.ui.tbl_data_pandas_mgmn.setColumnWidth(6, 150)
		# self.ui.tbl_data_pandas_mgmn.setColumnWidth(8, 450)
		#
		# # self.ui.tbl_data_pandas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		# self.ui.tbl_data_pandas_mgmn.sortByColumn(0, QtCore.Qt.AscendingOrder)
		# self.ui.tbl_data_pandas_mgmn.horizontalHeader().setSortIndicatorShown(True)
		# self.ui.tbl_data_pandas_mgmn.setColumnHidden(7, True)
		#
		# self.ui.le_search.setPlaceholderText("Искать...")
		# self.ui.le_search.textChanged.connect(self.proxy_model.setFilterFixedString)
		#
		# self.mapper = QDataWidgetMapper()
		# self.mapper.setModel(self.proxy_model)
		#
		# self.mapper.addMapping(self.ui.le_kommutator, 2)
		# self.mapper.addMapping(self.ui.le_name_trank, 3)
		# self.mapper.addMapping(self.ui.le_dpc_name, 0)
		# self.mapper.addMapping(self.ui.le_opc, 1)
		# self.mapper.addMapping(self.ui.le_operator_name, 8)
		# self.mapper.addMapping(self.ui.le_region_kommutatora, 4)
		# self.mapper.addMapping(self.ui.le_region_shluza, 5)
		# self.mapper.addMapping(self.ui.le_uroven_prisoedineniya, 6)
		#
		# self.ui.tbl_data_pandas_mgmn.selectionModel().currentRowChanged.connect(self.mapper.setCurrentModelIndex)
		# self.mapper.toFirst()  # .toLast() #.toFirst()

	def deleteRowLogUser (self):
		button = self.sender()
		if button:
			row_index = set()
			rows_ids = set()

			selected_rows = self.ui.tbl_log.selectionModel().selectedRows(column = 0)
			model = self.ui.tbl_log.model()
			role = Qt.DisplayRole
			for index in selected_rows:
				row_index.add(index.row())
				rows_ids.add(int(model.data(index, role)))
				self.ui.tbl_log.hideRow(index.row())

			# print(f'{row_index=}')
			# print(f'{rows_ids=}')

			# index = self.ui.tbl_log.currentIndex()
			# print(f'{index}')
			# self.model_log.removeRows(index.row(), 1, index)

			deleted_rows = SyncORM.deleteManyRowsLogsORM(rows_ids)

			if deleted_rows:
				self.model_log.removeRows(list(row_index))

				self.filters_in_db_logs()

				self.responses.success_message_status_bar(
					self.statusBar(),
					f'Запись(и) успешно удалена(ы).',
					3000
				)
			else:
				self.responses.error_message_status_bar(
					self.statusBar(),
					'Что-то пошло не так! Попробуйте позже ещё раз!',
					3000
				)

	def setItemsTable (self, lists, cb_list, tbl, count):
		tbl.setRowCount(0)
		count.setText(str(len(lists)))
		cb_list.clear()
		cb_list.addItem('', 0)
		for item in lists:
			cb_list.addItem(item['region'], (item['id'], item['email']))
			inx = list(lists).index(item)
			tbl.insertRow(inx)
			tbl.setItem(inx, 0, QTableWidgetItem(item['region']))
			tbl.setItem(inx, 1, QTableWidgetItem(item['email']))

	def mousePressEvent (self, event):
		self.clickPosition = event.globalPos()

	def restore_or_maximize_window (self):
		# If window is maxmized
		if self.isMaximized():
			self.showNormal()
			# Change Icon
			self.ui.btn_maximazed.setIcon(QIcon(u":/icons/icons/maximize-2_.svg"))
		else:
			self.showMaximized()
			# Change Icon
			self.ui.btn_maximazed.setIcon(QIcon(u":/icons/icons/minimize-2_.svg"))

	@Slot()
	def addNewAdmin (self, counter_admins):
		self.counter_admins = counter_admins
		self.counter_admins += 1
		lists_adminswidget = ListAdminsWidget(
			id_widget = self.counter_admins,
			# parent = self
		)
		lists_adminswidget.save_admin.connect(self.save_admin_widget)
		lists_adminswidget.delete_admin.connect(self.delete_adminwidget)
		self.ui.layout_view_admins.addWidget(lists_adminswidget)

	def save_admin_widget (self):
		widget = self.sender()
		text_email = widget.ui.le_name_admin.text().strip().lower()
		temp = check(text_email)
		if temp:
			add_admin = SyncORM.addAdminORM(name = text_email)
			if add_admin:
				SyncORM.logInfoORM('ADD', f'{USERCURRENT} ({USER})', f'Добавлен админ: {text_email}')
				self.responses.success_message_status_bar(
					self.statusBar(),
					f'Администратор/Модератор: {widget.ui.le_name_admin.text().strip()} - добавлен',
					3000
				)
				self.clear_areas(self.ui.layout_view_admins, self.counter_admins)
				self.list_admins.append(add_admin[0])
				self.listAdmins(list_admins = self.list_admins)
			else:
				SyncORM.logInfoORM('ERROR', f'{USERCURRENT} ({USER})', f'Ошибка добавления админа: {text_email}')
				self.responses.error_message_status_bar(
					self.statusBar(),
					'Что-то пошло не так! Попробуйте позже ещё раз!',
					3000
				)
		else:
			SyncORM.logInfoORM('ERROR', f'{USERCURRENT} ({USER})', 'Не корректно указан E-mail администратора!')
			self.responses.error_message_status_bar(
				self.statusBar(),
				'Не корректно указан E-mail администратора!',
				3000
			)

	def delete_adminwidget (self):
		widget = self.sender()
		admin = widget.ui.le_name_admin.text().strip()
		if admin != '':
			delete_admin = SyncORM.deleteAdminORM(id = int(widget.ui.lbl_id_admin.text()))
			if delete_admin:
				self.ui.layout_view_admins.removeWidget(widget)
				widget.deleteLater()
				widget.destroy()
				SyncORM.logInfoORM('DELETE', f'{USERCURRENT} ({USER})', f'Админ: {admin} - успешно удалён.')
				self.responses.success_message_status_bar(
					self.statusBar(),
					f'Администратор/Модератор: {widget.ui.le_name_admin.text().strip()} - удалён',
					3000
				)
			else:
				SyncORM.logInfoORM('ERROR', f'{USERCURRENT} ({USER})', f'Ошибка при удалении админа: {admin}.')
				self.responses.error_message_status_bar(
					self.statusBar(),
					'Что-то пошло не так! Попробуйте позже ещё раз!',
					3000
				)
		else:
			self.ui.layout_view_admins.removeWidget(widget)
			widget.deleteLater()
			widget.destroy()
			self.responses.success_message_status_bar(
				self.statusBar(),
				"Пустая запись удалена",
				3000
			)

	@Slot()
	def add_emailoperator (self, counter_id, email):
		self.counter_id = counter_id
		self.counter_id += 1
		add_emailwidget = AddEmailOperatorWidget(self.counter_id)
		self.ui.add_widget_layout.addWidget(add_emailwidget)
		if email['email'] != None:
			add_emailwidget.ui.lineEditNewEmall.setText(str(email['email']))
		add_emailwidget.delete.connect(self.delete_emailwidget)

	@Slot()
	def add_emailregion (self, counter_regions, email):
		self.counter_regions = counter_regions
		self.counter_regions += 1
		add_emailwidget_region = AddEmailOperatorWidget(self.counter_regions)
		self.ui.add_widget_layout_region.addWidget(add_emailwidget_region)
		if email['email'] != None:
			add_emailwidget_region.ui.lineEditNewEmall.setText(str(email['email']))
		add_emailwidget_region.delete.connect(self.delete_emailwidget_region)

	@Slot()
	def clear_area (self):
		while self.ui.add_widget_layout.count() > 0:
			item = self.ui.add_widget_layout.takeAt(0)
			item.widget().deleteLater()

	@Slot()
	def clear_area_region (self):
		while self.ui.add_widget_layout_region.count() > 0:
			item = self.ui.add_widget_layout_region.takeAt(0)
			item.widget().deleteLater()

	@Slot()
	def delete_emailwidget (self, wid: int):
		widget = self.sender()
		self.ui.add_widget_layout.removeWidget(widget)
		if widget.ui.lineEditNewEmall.text().strip() != '':
			self.listTextLineEdit(flag = 'delete')
			SyncORM.logInfoORM('DELETE', f'{USERCURRENT} ({USER})',
							   f'У оператора: {self.ui.cb_list_operators.currentText()} E-mail: {widget.ui.lineEditNewEmall.text()} - успешно удалён.')
			self.responses.success_message_status_bar(
				self.statusBar(),
				f"E-mail: {widget.ui.lineEditNewEmall.text()} - успешно удалён.",
				3000
			)
		widget.deleteLater()

	@Slot()
	def delete_emailwidget_region (self, wid: int):
		widget = self.sender()
		self.ui.add_widget_layout.removeWidget(widget)
		if widget.ui.lineEditNewEmall.text().strip() != '':
			self.listTextLineEditRegion(flag = 'delete', email_remove = widget.ui.lineEditNewEmall.text().strip())
			self.responses.success_message_status_bar(
				self.statusBar(),
				f"E-mail: {widget.ui.lineEditNewEmall.text()} - успешно удалён.",
				3000
			)
		widget.deleteLater()

	def getValueIdOperator (self):
		if self.ui.cb_list_operators.currentIndex() != 0:
			#     Получаем id оператора из установленных в UserData
			id_us = self.ui.cb_list_operators.itemData(self.ui.cb_list_operators.currentIndex())
			oper_id = id_us[0]
			flag_oper = id_us[1]

			self.ui.labelOperatorID.setText(str(oper_id))

			list_sp_operator = json.loads(SyncORM.listSpOperatorORM(oper_id, flag_oper)[0])

			# print(f'{list_sp_operator=}')

			self.ui.count_sp.setText(str(list_sp_operator["count_sp"]))
			self.ui.lbl_operator.setText(self.ui.cb_list_operators.currentText())
			while self.ui.sp_operator.rowCount() > 0:
				self.ui.sp_operator.removeRow(0)
			if flag_oper:
				self.ui.sp_operator.setColumnCount(3)
				self.ui.sp_operator.setHorizontalHeaderLabels(['SP', 'Регион', 'Транк группа'])

			else:
				self.ui.sp_operator.setColumnCount(2)

			self.ui.sp_operator.setSortingEnabled(False)
			for index in range(0, len(list_sp_operator['dpcs'])):
				# print(index, list_sp_operator['dpcs'][index])
				self.ui.sp_operator.insertRow(index)
				if flag_oper:
					self.ui.sp_operator.setItem(index, 0, QTableWidgetItem(list_sp_operator["dpcs"][index]["name"]))
					if list_sp_operator["dpcs"][index]["region_kommutatora"] == list_sp_operator["dpcs"][index]["region_shluza"]:
						self.ui.sp_operator.setItem(index, 1, QTableWidgetItem(f'г. {list_sp_operator["dpcs"][index]["region_shluza"]}'))
					else:
						item_join = list_sp_operator["dpcs"][index]["region_shluza"] + ' | г. ' + list_sp_operator["dpcs"][index][
							"region_kommutatora"]
						self.ui.sp_operator.setItem(index, 1, QTableWidgetItem(str(item_join)))
					self.ui.sp_operator.setItem(index, 2, QTableWidgetItem(list_sp_operator["dpcs"][index]["name_trank"]))
				else:
					self.ui.sp_operator.setItem(index, 0, QTableWidgetItem(f'2 - {int(list_sp_operator["dpcs"][index]["name"])}'))
					self.ui.sp_operator.setItem(index, 1, QTableWidgetItem(str(list_sp_operator["dpcs"][index]["locations"]["name"])))

			self.ui.sp_operator.setSortingEnabled(True)
			self.ui.sp_operator.horizontalHeader().setStretchLastSection(True)

			self.clear_area()
			self.counter_id = 0

			if (list_sp_operator["emails"] is not None and len(list_sp_operator["emails"]) > 0):
				list_emails_operator = list_sp_operator["emails"]["email"].split("; ")

				for email in list_emails_operator:
					item = {
						'email': email.replace(';', '')
					}
					self.add_emailoperator(self.counter_id, item)
		else:
			self.clear_area()
			self.counter_id = 0
			# self.ui.count_sp.setText("")
			# self.ui.lbl_operator.setText("")
			self.clearedOperatorsList()
			while (self.ui.sp_operator.rowCount() > 0):
				self.ui.sp_operator.setRowCount(0)

	def getValueIdRegion (self):
		if self.ui.cb_list_regions.currentIndex() != 0:
			self.ui.btn_change_name_region.setDisabled(False)
			# Получаем id региона из установленных в UserData
			data_region = self.ui.cb_list_regions.itemData(self.ui.cb_list_regions.currentIndex())
			id_region = data_region[0]
			emails_region = data_region[1]

			# print(f'Выбор региона: {data_region=}')

			self.ui.lbl_selected_region.setText(self.ui.cb_list_regions.currentText())
			# Получаем index оператора из ComboBox
			self.ui.labelRegionID.setText(str(id_region))

			self.clear_area_region()
			self.counter_regions = 0

			# print(f'{emails_region=}')
			# print(f'{list(emails_region[:-1].split(";"))=}')

			if isinstance(emails_region, str):
				list_emails_region = list(emails_region[:-1].split(';'))
			elif isinstance(emails_region, tuple):
				list_emails_region = list(emails_region[1][:-1].split(';'))

			# print(f'{list_emails_region=}')

			if len(list_emails_region) > 0:
				for i in list_emails_region:
					item = {
						'email': i.strip()
					}
					self.add_emailregion(self.counter_regions, item)
		else:
			self.clear_area_region()

	def showChangeNameRegion (self):
		self.effect.setEnabled(True)
		self.show_change_name_region = ChangeNameRegionWidget(
			id_region = int(self.ui.labelRegionID.text()),
			name_region = self.ui.lbl_selected_region.text(),
			cur_index = int(self.ui.cb_list_regions.currentIndex()),
			parent = self
		)
		self.show_change_name_region.show()

	def listTextLineEdit (self, flag = None):
		list_new_email = []
		id_operator = int(self.ui.labelOperatorID.text())
		name_operator = self.ui.cb_list_operators.currentText()

		for i in range(self.ui.add_widget_layout.count()):
			lineEmailWidget = self.ui.add_widget_layout.itemAt(i).widget()
			text_email = (lineEmailWidget.ui.lineEditNewEmall.text()).strip().lower()

			if len(text_email) > 0:
				# Проверка на корректность введенного e-mail
				temp = check(text_email)
				# print(text_email.lower())
				if temp:
					if flag is False:
						lineEmailWidget.ui.labelError.setText('E-mail корректный')
						lineEmailWidget.ui.labelError.setStyleSheet('color: green;')
					list_new_email.append(text_email)
				else:
					lineEmailWidget.ui.labelError.setText('E-mail не корректный')
					lineEmailWidget.ui.labelError.setStyleSheet('color: red;')
					break
			else:
				continue

		if len(list_new_email) > 0:
			data = []
			dict_new_emails = {
				"emails": '; '.join(list_new_email) + ';',
				"operator_id": id_operator,
				"name": name_operator
			}
			data.append(dict_new_emails)
			add_emails_operator = SyncORM.insertEmailsOperatorsORM(data)
			if add_emails_operator:
				SyncORM.logInfoORM('ADD', f'{USERCURRENT} ({USER})',
								   f'Добавлены/обновлены Email: {dict_new_emails["emails"]} для оператора: {dict_new_emails["name"]}.')
			else:
				SyncORM.logInfoORM('ERROR', f'{USERCURRENT} ({USER})', f'Ошибка при добавлении Email для оператора: {dict_new_emails["name"]}.')

	def listTextLineEditRegion (self, flag = None, email_remove = None):
		list_new_email = []
		id_region = int(self.ui.labelRegionID.text())
		for i in range(self.ui.add_widget_layout_region.count()):
			lineEmailWidget = self.ui.add_widget_layout_region.itemAt(i).widget()
			text_email = (lineEmailWidget.ui.lineEditNewEmall.text()).strip().lower()

			if len(text_email) > 0:
				# Проверка на корректность введенного e-mail
				temp = check(text_email)
				if temp:
					if flag is False:
						lineEmailWidget.ui.labelError.setText('E-mail корректный')
						lineEmailWidget.ui.labelError.setStyleSheet('color: green;')
					list_new_email.append(text_email)
				else:
					lineEmailWidget.ui.labelError.setText('E-mail не корректный')
					lineEmailWidget.ui.labelError.setStyleSheet('color: red;')
					continue
			else:
				continue

		if flag == 'delete':
			list_new_email.remove(email_remove)

		dict_new_email = {
			"id": id_region,
			"email": '; '.join(list_new_email) + ';'
		}

		update_emails = SyncORM.updateEmailsRegionORM(dict_new_email, USER)
		if update_emails:
			item = QTableWidgetItem(str(dict_new_email["email"]))
			self.ui.emails_region.setItem(int(self.ui.cb_list_regions.currentIndex()) - 1, 1, item)
			self.ui.cb_list_regions.setItemData(
				self.ui.cb_list_regions.currentIndex(),
				(dict_new_email['id'], dict_new_email["email"])
				# (self.ui.lbl_selected_region.text(), (dict_new_email['id'], dict_new_email["email"]))
			)

		else:
			self.responses.error_message_status_bar(
				self.statusBar(),
				"Что-то пошло не так. Попробуйте ещё раз",
				3000
			)

		if update_emails:
			SyncORM.logInfoORM('ADD', f'{USERCURRENT} ({USER})',
							   f'Добавлены/обновлены Email: {dict_new_email["email"]} для региона: {self.ui.cb_list_regions.currentText()}.')
		else:
			SyncORM.logInfoORM('ERROR', f'{USERCURRENT} ({USER})',
							   f'Ошибка при добавлении Email для региона: {self.ui.cb_list_regions.currentText()}.')

	def listAdmins (self, list_admins = None):
		if list_admins != None:
			self.list_admins = list_admins

		for item in self.list_admins:
			self.counter_admins += 1
			lists_adminswidget = ListAdminsWidget(
				id_widget = self.counter_admins,
				user_id = item.id,
				user_name = item.name,
			)
			self.ui.layout_view_admins.addWidget(lists_adminswidget)
			#
			lists_adminswidget.delete_admin.connect(self.delete_adminwidget)
			lists_adminswidget.save_admin.connect(self.save_admin_widget)

	def clear_areas (self, layout, counter):
		print(f'Counter: {counter}')
		counter = 0
		while layout.count() > 0:
			item = layout.takeAt(0)
			item.widget().deleteLater()
			item.widget().destroy()

	# Выгружаем все e-mail по операторам
	def uploadEmailsFromDb (self):
		# list_emails = Worker.uploadEmailsFromDb(self)
		# list_emails = list()
		# upload_ok = uploadEmailsAllOperatorsInCsv(list_emails)
		# btn_ok = self.ui.frame_btn_ok
		# if upload_ok:
		#     self.timer_ok_start(btn_ok, 5000)
		#
		# self.timer_ok.timeout.connect(lambda: self.timer_ok_finfsh(btn_ok))

		data_emails = SyncORM.uploadEmailsFromDbORM()
		if data_emails:
			self.saveFileDialog(data_emails)

		# worker = Worker(SyncORM.uploadEmailsFromDbORM)
		# worker.signals.result.connect(self.uploads_all_emails_operators)
		# worker.signals.finished.connect(self.completeUploadTableMgmn)
		# worker.signals.progress.connect(self.progress_fn)
		# self.threadpool.start(worker)

	def downloadEmailsJson (self):
		# groups_emails_for_operator = downloadEmailsAllOperatorsInDb()
		# Worker.downloadEmailsFromCsv(groups_emails_for_operator)
		# btn_ok = self.ui.frame_btn_ok_2
		# # if upload_ok:
		# self.timer_ok_start(btn_ok, 5000)
		# self.timer_ok.timeout.connect(lambda: self.timer_ok_finfsh(btn_ok))
		self.openFileDialog()

	def downloadEmailsRegionFromCsv (self):
		path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Загрузить файл"), self.tr("~/Desktop/"), self.tr("Excel (*.xlsx)"))
		if path_to_file:
			# groups_emails_for_region = downloadEmailsAllRegionsInDb(path_to_file)
			self.ui.btn_export_regions.setIcon(QtGui.QIcon(''))
			#
			self.worker = UploadEmailsRegion(path = path_to_file)
			self.worker.moveToThread(self.thread)
			self.worker.signal_region.connect(self.recordsLoadRegion)
			self.worker.signal_region_error.connect(self.recordsLoadRegion)
			self.worker.signal_list_region.connect(self.loadListRegion)
			self.thread.started.connect(self.worker.run)

			if self.thread.isRunning():
				self.worker.stop()
			else:
				self.thread.start()

	def recordsLoadRegion (self, records):
		self.thread.quit()
		self.responses.success_message_status_bar(
			self.statusBar(),
			records,
			3000
		)

	def recordsErrorLoadRegion (self, records):
		self.thread.quit()
		self.responses.error_message_status_bar(
			self.statusBar(),
			records,
			3000
		)

	def loadListRegion (self, list_regions):
		self.list_regions = list_regions
		self.clear_area_region()
		self.setItemsTable(self.list_regions, self.ui.cb_list_regions, self.ui.emails_region, self.ui.count_regions)

	def loadListOperators (self, list_operators):
		# self.lists_operators = ''
		# self.lists_operators = list_operators
		# for item in self.lists_operators:
		for item in list_operators:
			self.ui.cb_list_operators.addItem(item.name, (item.id, item.flag))

	def listsOperatorsCleared (self, cleared):
		if cleared:
			self.clearedOperatorsList()
			self.lists_operators = ''
			self.ui.cb_list_operators.clear()

	def clearedOperatorsList(self):
		self.ui.count_sp.setText("")
		self.ui.lbl_operator.setText("")


	def timer_ok_start (self, btn_ok, set_interval):
		self.timer_ok.stop()
		self.timer_ok.setInterval(set_interval)
		btn_ok.setMinimumWidth(60)
		btn_ok.setMaximumWidth(60)
		self.timer_ok.start()

	def timer_ok_finfsh (self, btn_ok):
		btn_ok.setMinimumWidth(0)
		btn_ok.setMaximumWidth(0)
		self.timer_ok.stop()

	def uploadDataFromRossreestr (self):
		path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Загрузить файл"), self.tr("~/Desktop/"), self.tr("Excel (*.csv)"))
		if path_to_file:
			self.ui.listWidget_operations.clear()

			self.worker_ros = UploadDataRossvyaz(path = path_to_file)
			self.worker_ros.moveToThread(self.thread)
			self.worker_ros.mysignal.connect(self.pandasUploadsData)
			self.worker_ros.cleared.connect(self.listsOperatorsCleared)
			self.worker_ros.progressHiden.connect(self.fisibleProgress)
			self.thread.started.connect(self.worker_ros.run)

			if self.thread.isRunning():
				self.worker_ros.stop()
			else:
				self.thread.start()

	def uploadDataFromMgmn (self):
		path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Загрузить файл"), self.tr("~/Desktop/"), self.tr("Excel (*.xlsx)"))

		if path_to_file:
			self.ui.listWidget_operations.clear()
			self.worker_mgmn = UploadMgmnFromOutlook(path = path_to_file)
			self.worker_mgmn.moveToThread(self.thread)
			self.worker_mgmn.progressHiden.connect(self.fisibleProgress)
			self.worker_mgmn.signalMgmn.connect(self.pandasUploadsData)
			self.worker_mgmn.cleared.connect(self.listsOperatorsCleared)
			self.thread.started.connect(self.worker_mgmn.run)

			if self.thread.isRunning():
				self.worker_mgmn.stop()
			else:
				self.thread.start()

	def fisibleProgress (self, hiddenProgress):
		if not hiddenProgress:
			self.progressBar.setHidden(hiddenProgress)
			self.progressBar.setMinimum(0)
			self.progressBar.setMaximum(0)
		else:
			self.progressBar.setHidden(hiddenProgress)
			self.progressBar.reset()

	def pandasUploadsData (self, records):
		self.thread.quit()
		self.ui.listWidget_operations.addItem(records)

	def closeEvent (self, event):
		if self.thread.isRunning():
			self.worker.stop()
			self.worker.deleteLater()
			self.thread.quit()

	def saveFileDialog (self, data):
		dialog = QFileDialog()
		options = dialog.Options()
		# options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Json Files (*.json)", options = options)
		extension = get_extension(fileName)
		if extension is None:
			fileName = fileName + '.json'

		# if options

		if fileName:
			with open(fileName, 'w', encoding = "utf-8") as f:
				json.dump(data, f, ensure_ascii = False)  # , indent=2) #.encode('utf8')

			if os.path.isfile(fileName):
				# self.ui.frame_btn_ok.setMaximumWidth(60)
				# btn_ok = self.ui.frame_btn_ok
				# self.timer_ok_start(btn_ok, 3000)
				# self.ui.btn_ok.setIcon(QtGui.QIcon(':/icons/icons/check-circle_.svg'))

				self.responses.success_message_status_bar(
					self.statusBar(),
					'E-mail операторов успешно сохранены.',
					3000
				)
				# self.timer_ok.timeout.connect(lambda: self.timer_ok_finfsh(btn_ok))

	def openFileDialog (self):
		options = QFileDialog.Options()
		file_file, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Json Files (*.json)", options = options)
		if file_file:
			# btn_ok = self.ui.frame_btn_ok_2
			data = SyncORM.uploadEmailsFromDbORM()
			if data:
				from_db = json.dumps(data, ensure_ascii = False)
				data = ''

			if from_db and file_file:
				data_update = downloadEmailsAllOperatorsJson(from_db, file_file)
				from_db = ''
				if data_update:
					result = SyncORM.updateEmailsOperORM(data_update)

				if result:
					self.responses.success_message_status_bar(
						self.statusBar(),
						'E-mail операторов успешно загружены.',
						3000
					)


class WorkerSignals(QtCore.QObject):
	finished = QtCore.Signal()
	error = QtCore.Signal(tuple)
	result = QtCore.Signal(object)
	progress = QtCore.Signal(int)
	loading_start = QtCore.Signal(bool)
	loading_stop = QtCore.Signal(bool)


class Worker(QtCore.QRunnable):
	def __init__ (self, fn, *args, **kwargs):
		super(Worker, self).__init__()
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signals = WorkerSignals()
		# print(f'{self.args=}')
		# print(f'{self.kwargs=}')
		# self.kwargs['progress_callback'] = self.signals.progress
		# self.ctrl['break'] = False

	@Slot()  # QtCore.Slot
	def run (self):
		try:
			self.signals.loading_start.emit(True)
			result = self.fn(*self.args, **self.kwargs,
							 # status=self.signals.status,
							 # progress=self.signals.progress
							 )
		except:
			traceback.print_exc()
			exctype, value = sys.exc_info()[:2]
			self.signals.error.emit((exctype, value, traceback.format_exc()))
		else:
			self.signals.result.emit(result)
		finally:
			self.signals.finished.emit()
			self.signals.loading_stop.emit(False)

#
# class ThreadSignals(QtCore.QObject):
#     finished = QtCore.Signal(int)
#     error = QtCore.Signal(tuple)
#     result = QtCore.Signal(object, float)
#     progress = QtCore.Signal(int)


# class JobRunner(QtCore.QRunnable):
#     def __init__(self):
#         super(JobRunner, self).__init__()
#         self.signals = ThreadSignals()
#
#     @Slot()
#     def run(self):
#         for n in range(100):
#             self.signals.progress.emit(n + 1)
#             time.sleep(0.1)


# class Worker(QtCore.QRunnable):
#     def __init__ (self, fn, path, *args, **kwargs):
#         super(Worker, self).__init__()
#         self.fn = fn
#         self.args = args
#         self.kwargs = kwargs
#         self.path = path
#         self.signals = ThreadSignals()
#
#         self.count = 0
#
#         # self.kwargs['progress_callback'] = self.signals.progress
#
#     # def setValueProgBar(self, count):
#     #     count = count + 1
#     #     self.signals.progress.emit(count)
#     #     QApplication.processEvents()
#
#     @Slot()
#     def run (self):
#         try:
#             print(f'Run: {self.fn} - {self.args} - {self.kwargs} - {self.path}')
#             # result = self.fn(*self.args, **self.kwargs)
#
#             result = 'Получение данных из файла Россреестра...'
#             self.signals.result.emit(result, 0)
#             start_time = time.time()
#             ls_operators = csvListOperatorsORM(self.path)
#             finish_time = start_time - time.time()
#             print(f'{finish_time=} - Type: {type(finish_time)}')
#             self.signals.result.emit(result, finish_time)
#
#             print(f'Len operators: {len(ls_operators)}')
#
#             result = 'Загрузка операторов в БД...'
#             self.signals.result.emit(result)
#
#             SyncORM.insert_operators_ORM(ls_operators, flag = False)
#             result = 'Загрузка сигнальных точек и мест расположения операторов в БД...'
#             self.signals.result.emit(result)
#             locations, locations_DPC = uploadDataSpInPandas(self.path)
#             # locations, locations_DPC = uploadDataSpInPandas(self.kwargs["path"])
#             if SyncORM.notEmptyDPC():
#                 SyncORM.uploadLocatSpInDb(locations)
#             SyncORM.uploadSpInDb(locations_DPC)
#
#
#             result = 'Загрузка данных из Россреестра завершена'
#             self.signals.result.emit(result)
#
#
#         except:
#             traceback.print_exc()
#             exctype, value = sys.exc_info()[:2]
#             self.signals.error.emit((exctype, value, traceback.format_exc()))
#         else:
#             pass
#             # self.signals.result.emit(result)  # Return the result of the processing
#         finally:
#             self.signals.finished.emit(100)


# class ThreadClass(QtCore.QThread):
# 	any_signal = QtCore.Signal(int)
#
# 	def __init__ (self, parent = None, index = 0):
# 		super(ThreadClass, self).__init__(parent)
# 		self.index = index
# 		self.is_running = True
#
# 	def run (self):
# 		print('Starting thread...', self.index)
# 		cnt = 0
# 		while (True):
# 			cnt += 1
# 			if cnt == 99: cnt = 0
# 			time.sleep(0.01)
# 			self.any_signal.emit(cnt)
#
# 	def stop (self):
# 		self.is_running = False
# 		print('Stopping thread...', self.index)
# 		self.terminate()


# def loadDataRossvyazInTable (self, data_rossvyaz):
# 	headers = data_rossvyaz.columns.values.tolist()
# 	self.ui.tbl_data_pandas.setColumnCount(len(headers))
# 	self.ui.tbl_data_pandas.setHorizontalHeaderLabels(headers)
# 	self.ui.tbl_data_pandas.setSortingEnabled(False)
#
# 	for i, row in data_rossvyaz.iterrows():
# 		# Добавление строки
# 		self.ui.tbl_data_pandas.setRowCount(self.ui.tbl_data_pandas.rowCount() + 1)
#
# 		for j in range(self.ui.tbl_data_pandas.columnCount()):
# 			self.ui.tbl_data_pandas.setItem(i, j, QTableWidgetItem(str(row[j])))
#
# 	self.ui.tbl_data_pandas.setSortingEnabled(True)
# 	# self.ui.tbl_data_pandas.resizeColumnsToContents()
# 	self.ui.tbl_data_pandas.horizontalHeader().resizeSection(0, 200)
# 	self.ui.tbl_data_pandas.horizontalHeader().resizeSection(1, 100)
# 	self.ui.tbl_data_pandas.horizontalHeader().resizeSection(2, 100)
# 	self.ui.tbl_data_pandas.horizontalHeader().resizeSection(3, 200)
# 	self.ui.tbl_data_pandas.horizontalHeader().resizeSection(4, 250)
# 	self.ui.tbl_data_pandas.horizontalHeader().resizeSection(5, 400)

# self.ui.tbl_data_pandas.horizontalHeader().resizeSection()

# self.ui.tbl_data_pandas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
# self.ui.tbl_data_pandas.sortByColumn(0, QtCore.Qt.DescendingOrder)
# self.ui.tbl_data_pandas.horizontalHeader().setSortIndicatorShown(True)

# def loadDataMgmnInTable (self, data_mgmn):
# 	print(data_mgmn)
# 	headers = data_mgmn.columns.values.tolist()
# 	self.ui.tbl_data_pandas_mgmn.setColumnCount(len(headers))
# 	self.ui.tbl_data_pandas_mgmn.setHorizontalHeaderLabels(headers)
# 	self.ui.tbl_data_pandas_mgmn.setSortingEnabled(False)
#
# 	for i, row in data_mgmn.iterrows():
# 		# Добавление строки
# 		self.ui.tbl_data_pandas_mgmn.setRowCount(self.ui.tbl_data_pandas_mgmn.rowCount() + 1)
#
# 		for j in range(self.ui.tbl_data_pandas_mgmn.columnCount()):
# 			self.ui.tbl_data_pandas_mgmn.setItem(i, j, QTableWidgetItem(str(row[j])))
#
# 	self.ui.tbl_data_pandas_mgmn.setSortingEnabled(True)
# self.ui.tbl_data_pandas.resizeColumnsToContents()
# self.ui.tbl_data_pandas_mgmn.horizontalHeader().resizeSection(0, 200)
# self.ui.tbl_data_pandas_mgmn.horizontalHeader().resizeSection(1, 100)
# self.ui.tbl_data_pandas_mgmn.horizontalHeader().resizeSection(2, 100)
# self.ui.tbl_data_pandas_mgmn.horizontalHeader().resizeSection(3, 200)
# self.ui.tbl_data_pandas_mgmn.horizontalHeader().resizeSection(4, 250)
# self.ui.tbl_data_pandas_mgmn.horizontalHeader().resizeSection(5, 400)

# import types
# def imported_modules():
# 	for name, val in globals().items():
# 		if isinstance(val, types.ModuleType):
# 			print(val)
# 			yield val.__name__
#
# imported = imported_modules()
# print(list(imported))


# def calc_container(path):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#     return total_size
#
#
# from pip._internal.utils.misc import get_installed_distributions
#
# size_all = 0
# for dist in get_installed_distributions():
# 	try:
# 		path = os.path.join(dist.location, dist.project_name)
# 		size = calc_container(path)
# 		if size:
# 			print(path)
# 			print(size)
# 			size_all += size
# 			print('Всего: ', size_all)
# 	except OSError:
# 		'{} no longer exists'.format(dist.project_name)
# print('Всего размер: ', size_all/1024/1024, 'Mb')
