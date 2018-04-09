#coding:utf8

if __name__ == '__main__':
	import sys
	from PyQt5 import QtWidgets
	from class_ui_pcb_sp import ui_pcb_sp
	
	app = QtWidgets.QApplication(sys.argv)
	window = ui_pcb_sp()
	window.show()
	sys.exit(app.exec_())