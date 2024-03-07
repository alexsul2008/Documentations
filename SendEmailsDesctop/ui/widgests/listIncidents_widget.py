from PySide2.QtCore import QEvent, Signal, Slot
from PySide2.QtWidgets import QWidget

from ui.gt_base_ui.ui_widgetIncidents import Ui_IncidentWidget



class BaseItemIncidentsWidget(QWidget):

	checked_incident = Signal(bool, str, int)
	clicked_incident = Signal(int, dict, bool)


	def __init__ (self, id_widget_base_item_incident: int, parent = None, *args, **kwargs):
		super(BaseItemIncidentsWidget, self).__init__(parent)
		self.ui = Ui_IncidentWidget()
		self.ui.setupUi(self)

		self.ui.inc_frame.installEventFilter(self)

		self.kwargs = kwargs

		# print(self.kwargs)

		self.inc_id = kwargs['id']
		self.inc_name = kwargs['name']
		self.operator_name = kwargs['operator_name']
		self.operator_id = kwargs['operator_id']
		self.flag = kwargs['flag']
		self.dpc_name = kwargs['dpc_name']
		self.opc_name = kwargs['opc_name']

		# self.operator = kwargs['operator']



		self.id_widget = id_widget_base_item_incident
		self.ui.incident_lbl.setText(self.inc_name)
		self.ui.operator_name.setText(self.operator_name)
		self.ui.id_incident_lbl.setText(str(self.inc_id))

		# if self.id_widget_base_item_incident % 2 == 0:
		# 	self.setStyleSheet("background-color: #222222;")
		# else:
		# 	self.setStyleSheet("background-color: #333333;")

		self.ui.chb_inc.stateChanged.connect(self.press_checked_incident)

	@Slot()
	def press_checked_incident(self):
		self.checked_incident.emit(self.ui.chb_inc.isChecked(), self.inc_name, self.inc_id)

	def mousePressEvent(self, event):
		child = self.childAt(event.pos())
		if child.objectName() == 'incident_lbl':
			self.clicked_incident.emit(self.id_widget, self.kwargs, True)

	def eventFilter (self, source, event):
		# if event.type() == QEvent.HoverEnter:
		if event.type() == QEvent.Enter:
			source.setStyleSheet("""QLabel{color: #5983a7;}""")
		elif event.type() == QEvent.Leave:
			source.setStyleSheet("""QLabel{color: #c5c5c5;}""")
		return super(BaseItemIncidentsWidget, self).eventFilter(source, event)

