# -*- coding: utf-8 -*-
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QCompleter, QStyledItemDelegate
from PyQt5.QtCore import Qt, QSortFilterProxyModel

class CompleterItemDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(CompleterItemDelegate, self).initStyleOption(option, index)
        option.backgroundBrush = QColor("red")
        option.palette.setBrush(QPalette.Text, QColor("blue"))
        option.displayAlignment = Qt.AlignCenter

class CustomQCompleter(QCompleter):
	def __init__ (self, parent = None):
		super(CustomQCompleter, self).__init__(parent)
		self.local_completion_prefix = ""
		self.source_model = None

	def setModel (self, model):
		self.source_model = model
		super(CustomQCompleter, self).setModel(self.source_model)

	def updateModel (self):
		local_completion_prefix = self.local_completion_prefix

		class InnerProxyModel(QSortFilterProxyModel):
			def filterAcceptsRow (self, sourceRow, sourceParent):
				index0 = self.sourceModel().index(sourceRow, 0, sourceParent)
				searchStr = local_completion_prefix.lower()
				searchStr_list = searchStr.split()
				modelStr = self.sourceModel().data(index0, Qt.DisplayRole).lower()
				for string in searchStr_list:
					if not string in modelStr:
						return False
				return True

		proxy_model = InnerProxyModel()
		proxy_model.setSourceModel(self.source_model)
		super(CustomQCompleter, self).setModel(proxy_model)

	def splitPath (self, path):
		self.local_completion_prefix = str(path)
		self.updateModel()
		return ""


class MyCustomQCompleter(QCompleter):
	def __init__(self, parent=None):
		super(MyCustomQCompleter, self).__init__(parent)
		self.local_completion_prefix = ""
		self.source_model = None

	def setModel(self, model):
		self.source_model = model
		super(MyCustomQCompleter, self).setModel(self.source_model)

	def updateModel(self):
		local_completion_prefix = self.local_completion_prefix
		class InnerProxyModel(QSortFilterProxyModel):
			def filterAcceptsRow(self, sourceRow, sourceParent):
				index0 = self.sourceModel().index(sourceRow, 0, sourceParent)
				return local_completion_prefix.lower() in self.sourceModel().data(index0).lower()
		proxy_model = InnerProxyModel()
		proxy_model.setSourceModel(self.source_model)
		super(MyCustomQCompleter, self).setModel(proxy_model)

	def splitPath(self, path):
		self.local_completion_prefix = path
		self.updateModel()
		return ""
