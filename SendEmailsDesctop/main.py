import sys
import time
from os import path

# from pathlib import Path
#

from models.database import sync_engine, sync_engine_gasi

from models.worker import SyncORM

from PySide2.QtWidgets import QApplication

from ui.mywindow import MainWindow





if __name__ == '__main__':
	BASE_DIR = path.dirname(path.abspath(__file__))
	# global BASE_DIR
	# print(path.join(BASE_DIR, "style.qss"))


	# if sync_engine: # and sync_engine_gasi:
	# 	print('ПОдключение к БД есть')
	# 	SyncORM.create_tables()
	# # 	# SyncORM.insert_admins()
	# # 	# SyncORM.insert_operators()
	# else:
	# 	print('ПОдключение к БД нет')
	# # # except:
	# # # 	SyncORM.create_tables()



	app = QApplication(sys.argv)
	with open(path.join(BASE_DIR, "style.qss"), "r") as style_file:
		style_str = style_file.read()
	app.setStyleSheet(style_str)

	# splash = QSplashScreen(QPixmap("loading.png"))
	# splash.showMessage("Загрузка данных... 0%", Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
	# splash.show()  # Отображаем заставку
	#
	# app.processEvents()

	#################################################################
	if getattr(sys, 'frozen', False):
		import pyi_splash
		pyi_splash.update_text('Запуск пограммы ...')
	################################################################

	window = MainWindow()
	# load_data(splash)
	# splash.finish(window)
	#################################################################
	if getattr(sys, 'frozen', False):
		# pyi_splash.update_text('Запуск пограммы ...')
		pyi_splash.close()
	################################################################
	window.show()
	# app.setWindowIcon(QIcon(path.join(BASE_DIR, 'logo.ico')))
	# window.setWindowIcon(QIcon(path.join(BASE_DIR, 'logo.ico')))
	sys.exit(app.exec_())

