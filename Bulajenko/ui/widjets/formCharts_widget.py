# -*- coding: utf-8 -*-
import datetime
from PyQt5.QtCore import Qt, QDateTime, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QPaintDevice
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QDateTimeAxis, QValueAxis, QLineSeries
from PyQt5.QtWidgets import QWidget

from Core.Models.Worker import Usuarios
from ui.windows.ui_FormCharts import Ui_FormCharts



class BaseFormCharts(QWidget):
    dataChanged = pyqtSignal()

    # def __init__ (self, charts_item=None, parent = None):
    def __init__ (self, parent = None):
        super(BaseFormCharts, self).__init__(parent)
        self.ui = Ui_FormCharts()
        self.ui.setupUi(self)
        self.parent = parent



        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle(f"Статусы договоров")
        self.chart.setTitleFont(QFont('Arial', 14))

        # chart.legend().setVisible(True)
        # chart.legend().setAlignment(Qt.AlignBottom)


        # chart.series()[0].clicked.connect(lambda: self.series_clicked(series))

        self.chart.setTheme(QChart.ChartThemeDark)
        self.chart.setBackgroundVisible(False)

        # chart.addSeries(series)

        # chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setAnimationOptions(QChart.AllAnimations)

        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)

        self.ui.chartLayoutFormContract.addWidget(self.chartview)


        self.updater()

        # self.chart_new(self.charts_item['count_arendators'])

    def create_data_charts (self):
        result = self.parent.users_db.charts_data()
        return result


    def updater(self):
        self.dater = self.create_data_charts()
        self.status_contract(self.dater['status_contract'].all())



    def status_contract(self, data):
        # self.dataChanged.emit()
        self.series = QPieSeries()
        self.series.setHoleSize(0.45)

        # self.series.clear()

        for item in data:
            self.series.append(f'Открытые договора ({item.count_opened})', item.count_opened)
            self.series.append(f'Закрытые договора ({item.count_closed})', item.count_closed)


        self.chart.addSeries(self.series)
        self.chart.series()[0].setLabelsVisible(True)
        self.chart.series()[0].setLabelsPosition(QPieSlice.LabelOutside)      # LabelInsideTangential, LabelInsideHorizontal, LabelInsideNormal
        self.chartview.chart().update()

        # chart = QChart()
        #
        # chart.legend().hide()
        # chart.addSeries(series)
        # chart.createDefaultAxes()
        # chart.setAnimationOptions(QChart.SeriesAnimations)
        # chart.setTitle(f"Статусы договоров")
        # chart.setTitleFont(QFont('Arial', 14))
        #
        # # chart.legend().setVisible(True)
        # # chart.legend().setAlignment(Qt.AlignBottom)
        #
        # chart.series()[0].setLabelsVisible(True)
        # chart.series()[0].setLabelsPosition(QPieSlice.LabelOutside) # LabelInsideTangential, LabelInsideHorizontal, LabelInsideNormal
        #
        # chart.series()[0].clicked.connect(lambda: self.series_clicked(series))
        #
        # chart.setTheme(QChart.ChartThemeDark)
        # chart.setBackgroundVisible(False)
        #
        # # chart.addSeries(series)
        #
        # # chart.setAnimationOptions(QChart.SeriesAnimations)
        # chart.setAnimationOptions(QChart.AllAnimations)
        #
        #
        # chartview = QChartView(chart)
        # chartview.setRenderHint(QPainter.Antialiasing)
        #
        # self.ui.chartLayoutFormContract.addWidget(chartview)


    def series_clicked(self, series):
        slice = QPieSlice()
        slice.setExploded(True)
        slice = series.slices()[0]
        slice.setLabelVisible(True)
        print(series)

        # slice = series.append(f'Открытые договора ', data[0].count_opened)
        # slice = series.slices()[0]
        # slice.setLabelVisible(True)








    def chart_new(self, data_arendator):

        self.model = data_arendator

        # print(len(self.model))

        # Creating QChart
        self.chart2 = QChart()
        self.chart2.setAnimationOptions(QChart.AllAnimations)
        self.chart2.setTheme(QChart.ChartThemeDark)
        self.chart2.setBackgroundVisible(False)

        self.add_series("Magnitude (Column 1)", [0, 1])

        # Creating QChartView
        self.chart_view = QChartView(self.chart2)
        self.chart_view.setRenderHint(QPainter.Antialiasing)


        self.ui.chartLayoutFormArendators.addWidget(self.chart_view)



    def add_series(self, name, columns):
        # Create QLineSeries
        self.series = QLineSeries()

        self.series.setName(name)

        # Filling QLineSeries
        for i in range(len(self.model)):
            # Getting the data
            t = str(self.model[i][0])
            # t = self.model[i][0]

            date_fmt = "yyyy-MM-dd HH:mm:ss.zzz"

            # print(f'T: {t}')

            x = QDateTime().fromString(t, date_fmt).toSecsSinceEpoch()
            # x = QDateTime().toString()
            # x = QDateTime(t).date()
            # print(f'X: {x}')
            # y = float(self.model[i][1])
            y = self.model[i][1]
            # print(f'Y: {y}')
        #
            if x > 0 and y > 0:
                self.series.append(x, y)


        self.chart2.addSeries(self.series)

        # Setting X-axis
        # self.axis_x = QDateTimeAxis()
        self.axis_x = QValueAxis()
        # self.axis_x.setTickCount(10)
        # self.axis_x.setFormat("dd.MM")
        self.axis_x.setTitleText("Date")
        self.chart2.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)
        # Setting Y-axis
        self.axis_y = QValueAxis()
        # self.axis_y.setTickCount(10)
        # self.axis_y.setLabelFormat("%.0f")
        self.axis_y.setTitleText("Кол-во")
        self.chart2.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        # # Getting the color from the QChart to use it on the QTableView
        # color_name = self.series.pen().color().name()
        # print(f'Color: {color_name}')
        # self.model[0].color = f"{color_name}"

