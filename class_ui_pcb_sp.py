#coding:utf8

# pcb模拟控制器的界面类

from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QInputDialog
from ui_pcb_simulator_panel import Ui_pcb_sp
from class_pcb_simulator import pcb_simulator
from class_thread_process_monitor import thread_process_monitor
import global_pcb
import time

class ui_pcb_sp(QtWidgets.QWidget,Ui_pcb_sp):
	create1_signal = QtCore.pyqtSignal(int) #create按钮信号
	create2_signal = QtCore.pyqtSignal(int) #create按钮信号
	create3_signal = QtCore.pyqtSignal(int) #create按钮信号
	create4_signal = QtCore.pyqtSignal(int) #create按钮信号
	create5_signal = QtCore.pyqtSignal(int) #create按钮信号
	block1_signal = QtCore.pyqtSignal(int) #block按钮信号
	block2_signal = QtCore.pyqtSignal(int) #block按钮信号
	block3_signal = QtCore.pyqtSignal(int) #block按钮信号
	block4_signal = QtCore.pyqtSignal(int) #block按钮信号
	block5_signal = QtCore.pyqtSignal(int) #block按钮信号
	wakeup1_signal = QtCore.pyqtSignal(int) #wakeup按钮信号
	wakeup2_signal = QtCore.pyqtSignal(int) #wakeup按钮信号
	wakeup3_signal = QtCore.pyqtSignal(int) #wakeup按钮信号
	wakeup4_signal = QtCore.pyqtSignal(int) #wakeup按钮信号
	wakeup5_signal = QtCore.pyqtSignal(int) #wakeup按钮信号
	schedule1_signal = QtCore.pyqtSignal(int) #schedule按钮信号
	schedule2_signal = QtCore.pyqtSignal(int) #schedule按钮信号
	schedule3_signal = QtCore.pyqtSignal(int) #schedule按钮信号
	schedule4_signal = QtCore.pyqtSignal(int) #schedule按钮信号
	schedule5_signal = QtCore.pyqtSignal(int) #schedule按钮信号
	running1_signal = QtCore.pyqtSignal(int) #修改running状态信号
	running2_signal = QtCore.pyqtSignal(int) #修改running状态信号
	running3_signal = QtCore.pyqtSignal(int) #修改running状态信号
	running4_signal = QtCore.pyqtSignal(int) #修改running状态信号
	running5_signal = QtCore.pyqtSignal(int) #修改running状态信号
	progress_signal = QtCore.pyqtSignal(list) #传递进程运行状态信号
	def __init__(self):
		super(ui_pcb_sp,self).__init__()
		self.setupUi(self)
		
		#应用ui样式
		self.stylesheet = self.load_qss('./qss/pcb_qss.txt')
		self.setStyleSheet(self.stylesheet)
		
		for i in range(1,6):
			self.init_button(i)
		
		#启动进程监视器,监视ready队列
		self.process_monitor = thread_process_monitor(self)
		self.process_monitor.start()
		
		self.status_bar.appendPlainText(self.get_time()+'\t[main]\tPCB Simulator Panel ready')
		
		#给所有create按钮通过信号槽绑定创建进程事件
		self.btn_create1.clicked.connect(self.create1_emit)
		self.btn_create2.clicked.connect(self.create2_emit)
		self.btn_create3.clicked.connect(self.create3_emit)
		self.btn_create4.clicked.connect(self.create4_emit)
		self.btn_create5.clicked.connect(self.create5_emit)
		self.create1_signal.connect(self.create_process)
		self.create2_signal.connect(self.create_process)
		self.create3_signal.connect(self.create_process)
		self.create4_signal.connect(self.create_process)
		self.create5_signal.connect(self.create_process)
		
		#给所有block按钮通过信号槽绑定阻塞进程事件
		self.btn_block1.clicked.connect(self.block1_emit)
		self.btn_block2.clicked.connect(self.block2_emit)
		self.btn_block3.clicked.connect(self.block3_emit)
		self.btn_block4.clicked.connect(self.block4_emit)
		self.btn_block5.clicked.connect(self.block5_emit)
		self.block1_signal.connect(self.block_process)
		self.block2_signal.connect(self.block_process)
		self.block3_signal.connect(self.block_process)
		self.block4_signal.connect(self.block_process)
		self.block5_signal.connect(self.block_process)
		
		#给所有wakeup按钮通过信号槽绑定唤醒进程事件
		self.btn_wakeup1.clicked.connect(self.wakeup1_emit)
		self.btn_wakeup2.clicked.connect(self.wakeup2_emit)
		self.btn_wakeup3.clicked.connect(self.wakeup3_emit)
		self.btn_wakeup4.clicked.connect(self.wakeup4_emit)
		self.btn_wakeup5.clicked.connect(self.wakeup5_emit)
		self.wakeup1_signal.connect(self.wakeup_process)
		self.wakeup2_signal.connect(self.wakeup_process)
		self.wakeup3_signal.connect(self.wakeup_process)
		self.wakeup4_signal.connect(self.wakeup_process)
		self.wakeup5_signal.connect(self.wakeup_process)
		
		#给所有schedule按钮通过信号槽绑定调度进程事件
		self.btn_schedule1.clicked.connect(self.schedule1_emit)
		self.btn_schedule2.clicked.connect(self.schedule2_emit)
		self.btn_schedule3.clicked.connect(self.schedule3_emit)
		self.btn_schedule4.clicked.connect(self.schedule4_emit)
		self.btn_schedule5.clicked.connect(self.schedule5_emit)
		self.schedule1_signal.connect(self.schedule_process)
		self.schedule2_signal.connect(self.schedule_process)
		self.schedule3_signal.connect(self.schedule_process)
		self.schedule4_signal.connect(self.schedule_process)
		self.schedule5_signal.connect(self.schedule_process)
		
		#给所有running状态信号绑定running_process函数
		self.running1_signal.connect(self.running_process)
		self.running2_signal.connect(self.running_process)
		self.running3_signal.connect(self.running_process)
		self.running4_signal.connect(self.running_process)
		self.running5_signal.connect(self.running_process)	
		
		#给progress处理信号绑定process_progress函数
		self.progress_signal.connect(self.process_progress)
		
	def create1_emit(self):
		self.create1_signal.emit(1)
	def create2_emit(self):
		self.create2_signal.emit(2)
	def create3_emit(self):
		self.create3_signal.emit(3)
	def create4_emit(self):
		self.create4_signal.emit(4)
	def create5_emit(self):
		self.create5_signal.emit(5)
		
	def block1_emit(self):
		self.block1_signal.emit(1)
	def block2_emit(self):
		self.block2_signal.emit(2)
	def block3_emit(self):
		self.block3_signal.emit(3)
	def block4_emit(self):
		self.block4_signal.emit(4)
	def block5_emit(self):
		self.block5_signal.emit(5)
		
	def wakeup1_emit(self):
		self.wakeup1_signal.emit(1)
	def wakeup2_emit(self):
		self.wakeup2_signal.emit(2)
	def wakeup3_emit(self):
		self.wakeup3_signal.emit(3)
	def wakeup4_emit(self):
		self.wakeup4_signal.emit(4)
	def wakeup5_emit(self):
		self.wakeup5_signal.emit(5)
		
	def schedule1_emit(self):
		self.schedule1_signal.emit(1)
	def schedule2_emit(self):
		self.schedule2_signal.emit(2)
	def schedule3_emit(self):
		self.schedule3_signal.emit(3)
	def schedule4_emit(self):
		self.schedule4_signal.emit(4)
	def schedule5_emit(self):
		self.schedule5_signal.emit(5)
		
	def process_progress(self,progress_list):
		self.status_bar.appendPlainText(self.get_time()+'\t[PID'+progress_list[0]+']\tPID'+progress_list[0]+'已执行: '+progress_list[1]+'/'+progress_list[2])
		self.status_bar.appendPlainText(self.get_time()+'\t[PID'+progress_list[0]+']\tPID'+progress_list[0]+'已运行时间: '+self.get_time(progress_list[3]))
		
	def running_process(self,number):
		if number == 1:
			self.clear_status_running()
			self.status1.setText('running')
			self.status_bar.appendPlainText(self.get_time()+'\t[PID1]\tPID1 is running')
			
			#将status状态颜色变为绿色
			self.stylesheet = self.stylesheet+'#status1{background-color:#99CC33;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 2:
			self.clear_status_running()
			self.status2.setText('running')
			self.status_bar.appendPlainText(self.get_time()+'\t[PID2]\tPID2 is running')
			
			#将status状态颜色变为绿色
			self.stylesheet = self.stylesheet+'#status2{background-color:#99CC33;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 3:
			self.clear_status_running()
			self.status3.setText('running')
			self.status_bar.appendPlainText(self.get_time()+'\t[PID3]\tPID3 is running')
			
			#将status状态颜色变为绿色
			self.stylesheet = self.stylesheet+'#status3{background-color:#99CC33;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 4:
			self.clear_status_running()
			self.status4.setText('running')
			self.status_bar.appendPlainText(self.get_time()+'\t[PID4]\tPID4 is running')
			
			#将status状态颜色变为绿色
			self.stylesheet = self.stylesheet+'#status4{background-color:#99CC33;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 5:
			self.clear_status_running()
			self.status5.setText('running')
			self.status_bar.appendPlainText(self.get_time()+'\t[PID5]\tPID5 is running')
			
			#将status状态颜色变为绿色
			self.stylesheet = self.stylesheet+'#status5{background-color:#99CC33;}'
			self.setStyleSheet(self.stylesheet)
		
	# 将status为running的状态栏进程的状态栏变为ready
	def clear_status_running(self):
		if self.status1.text() == 'running':
			self.status1.setText('ready')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status1{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		elif self.status2.text() == 'running':
			self.status2.setText('ready')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status2{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		elif self.status3.text() == 'running':
			self.status3.setText('ready')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status3{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		elif self.status4.text() == 'running':
			self.status4.setText('ready')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status4{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		elif self.status5.text() == 'running':
			self.status5.setText('ready')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status5{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		
	# 创建进程，根据按钮的点击来创建对应进程
	# 或者为终止进程
	def create_process(self,number):
		if number == 1:
			if self.btn_create1.text() == 'Terminate':
				global_pcb.pcb.terminate(global_pcb.pid1)
				self.label_1.setText('not created')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID1]\tPID1 is terminated')
				
				#恢复原来的样式，即status为无色
				self.stylesheet = self.stylesheet+'#status1{background-color:transparent;}'
				self.setStyleSheet(self.stylesheet)
			else:
				global_pcb.pid1 = global_pcb.pcb.create(pid=1)
				self.label_1.setText('PID1')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID1]\tPID1 is created')
				
				#将status状态颜色变为淡黄
				self.stylesheet = self.stylesheet+'#status1{background-color:#FFFF66;}'
				self.setStyleSheet(self.stylesheet)
		elif number == 2:
			if self.btn_create2.text() == 'Terminate':
				global_pcb.pcb.terminate(global_pcb.pid2)
				self.label_2.setText('not created')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID2]\tPID2 is terminated')
				
				#恢复原来的样式，即status为无色
				self.stylesheet = self.stylesheet+'#status2{background-color:transparent;}'
				self.setStyleSheet(self.stylesheet)
			else:
				global_pcb.pid2 = global_pcb.pcb.create(pid=2)
				self.label_2.setText('PID2')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID2]\tPID2 is created')
				
				#将status状态颜色变为淡黄
				self.stylesheet = self.stylesheet+'#status2{background-color:#FFFF66;}'
				self.setStyleSheet(self.stylesheet)
		elif number == 3:
			if self.btn_create3.text() == 'Terminate':
				global_pcb.pcb.terminate(global_pcb.pid3)
				self.label_3.setText('not created')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID3]\tPID3 is terminated')
				
				#恢复原来的样式，即status为无色
				self.stylesheet = self.stylesheet+'#status3{background-color:transparent;}'
				self.setStyleSheet(self.stylesheet)
			else:
				global_pcb.pid3 = global_pcb.pcb.create(pid=3)
				self.label_3.setText('PID3')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID3]\tPID3 is created')
				
				#将status状态颜色变为淡黄
				self.stylesheet = self.stylesheet+'#status3{background-color:#FFFF66;}'
				self.setStyleSheet(self.stylesheet)
		elif number == 4:
			if self.btn_create4.text() == 'Terminate':
				global_pcb.pcb.terminate(global_pcb.pid4)
				self.label_4.setText('not created')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID4]\tPID4 is terminated')
				
				#恢复原来的样式，即status为无色
				self.stylesheet = self.stylesheet+'#status4{background-color:transparent;}'
				self.setStyleSheet(self.stylesheet)
			else:
				global_pcb.pid4 = global_pcb.pcb.create(pid=4)
				self.label_4.setText('PID4')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID4]\tPID4 is created')
				
				#将status状态颜色变为淡黄
				self.stylesheet = self.stylesheet+'#status4{background-color:#FFFF66;}'
				self.setStyleSheet(self.stylesheet)
		elif number == 5:
			if self.btn_create5.text() == 'Terminate':
				global_pcb.pcb.terminate(global_pcb.pid5)
				self.label_5.setText('not created')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID5]\tPID5 is terminated')
				
				#恢复原来的样式，即status为无色
				self.stylesheet = self.stylesheet+'#status5{background-color:transparent;}'
				self.setStyleSheet(self.stylesheet)
			else:
				global_pcb.pid5 = global_pcb.pcb.create(pid=5)
				self.label_5.setText('PID5')
				self.init_button(number)
				self.status_bar.appendPlainText(self.get_time()+'\t[PID5]\tPID5 is created')
				
				#将status状态颜色变为淡黄
				self.stylesheet = self.stylesheet+'#status5{background-color:#FFFF66;}'
				self.setStyleSheet(self.stylesheet)

	#阻塞进程按钮绑定函数
	def block_process(self,number):
		if number == 1:
			global_pcb.pcb.block(global_pcb.pid1)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID1]\tPID1 is blocked')
			
			#将status状态颜色变为红色
			self.stylesheet = self.stylesheet+'#status1{background-color:#CC3333;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 2:
			global_pcb.pcb.block(global_pcb.pid2)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID2]\tPID2 is blocked')
			
			#将status状态颜色变为红色
			self.stylesheet = self.stylesheet+'#status2{background-color:#CC3333;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 3:
			global_pcb.pcb.block(global_pcb.pid3)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID3]\tPID3 is blocked')
			
			#将status状态颜色变为红色
			self.stylesheet = self.stylesheet+'#status3{background-color:#CC3333;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 4:
			global_pcb.pcb.block(global_pcb.pid4)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID4]\tPID4 is blocked')
			
			#将status状态颜色变为红色
			self.stylesheet = self.stylesheet+'#status4{background-color:#CC3333;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 5:
			global_pcb.pcb.block(global_pcb.pid5)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID5]\tPID5 is blocked')
			
			#将status状态颜色变为红色
			self.stylesheet = self.stylesheet+'#status5{background-color:#CC3333;}'
			self.setStyleSheet(self.stylesheet)
		self.change_status(number,'block')
	
	#唤醒进程按钮绑定函数
	def wakeup_process(self,number):
		if number == 1:
			global_pcb.pcb.wakeup(global_pcb.pid1)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID1]\tPID1 is awaked(ready)')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status1{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 2:
			global_pcb.pcb.wakeup(global_pcb.pid2)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID2]\tPID2 is awaked(ready)')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status2{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 3:
			global_pcb.pcb.wakeup(global_pcb.pid3)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID3]\tPID3 is awaked(ready)')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status3{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 4:
			global_pcb.pcb.wakeup(global_pcb.pid4)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID4]\tPID4 is awaked(ready)')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status4{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		elif number == 5:
			global_pcb.pcb.wakeup(global_pcb.pid5)
			self.status_bar.appendPlainText(self.get_time()+'\t[PID5]\tPID5 is awaked(ready)')
			
			#将status状态颜色变为淡蓝
			self.stylesheet = self.stylesheet+'#status5{background-color:#99CCFF;}'
			self.setStyleSheet(self.stylesheet)
		self.change_status(number,'ready')

	# 与schedule按钮绑定的函数
	def schedule_process(self,number):
		#对话框有两个按钮(ok/cancel)一个输入框，ok是按钮值(True/False),text是输入框值
		text , ok = QInputDialog.getText(self,"Schedule Input", "\n\n\t输入'enter' : 使进程ready\t\n\n\t 输入'esc' : 使进程block\t\n\n\t   输入其它字符 : 无效\t\n\n\t        cmd here:\t\n\n\n")
		if ok:
			if number == 1:
				if text == 'enter':
					global_pcb.pcb.enter(global_pcb.pid1)
					self.change_status(number,'ready')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID1]\tPID1 is ready')
					
					#将status状态颜色变为淡蓝
					self.stylesheet = self.stylesheet+'#status1{background-color:#99CCFF;}'
					self.setStyleSheet(self.stylesheet)
				elif text == 'esc':
					global_pcb.pcb.block(global_pcb.pid1)
					self.change_status(number,'block')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID1]\tPID1 is blocked')
					
					#将status状态颜色变为红色
					self.stylesheet = self.stylesheet+'#status1{background-color:#CC3333;}'
					self.setStyleSheet(self.stylesheet)
			elif number == 2:
				if text == 'enter':
					global_pcb.pcb.enter(global_pcb.pid2)
					self.change_status(number,'ready')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID2]\tPID2 is ready')
					
					#将status状态颜色变为淡蓝
					self.stylesheet = self.stylesheet+'#status2{background-color:#99CCFF;}'
					self.setStyleSheet(self.stylesheet)
				elif text == 'esc':
					global_pcb.pcb.block(global_pcb.pid2)
					self.change_status(number,'block')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID2]\tPID2 is blocked')
					
					#将status状态颜色变为红色
					self.stylesheet = self.stylesheet+'#status2{background-color:#CC3333;}'
					self.setStyleSheet(self.stylesheet)
			elif number == 3:
				if text == 'enter':
					global_pcb.pcb.enter(global_pcb.pid3)
					self.change_status(number,'ready')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID3]\tPID3 is ready')
					
					#将status状态颜色变为淡蓝
					self.stylesheet = self.stylesheet+'#status3{background-color:#99CCFF;}'
					self.setStyleSheet(self.stylesheet)
				elif text == 'esc':
					global_pcb.pcb.block(global_pcb.pid3)
					self.change_status(number,'block')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID3]\tPID3 is blocked')
					
					#将status状态颜色变为红色
					self.stylesheet = self.stylesheet+'#status3{background-color:#CC3333;}'
					self.setStyleSheet(self.stylesheet)
			elif number == 4:
				if text == 'enter':
					global_pcb.pcb.enter(global_pcb.pid4)
					self.change_status(number,'ready')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID4]\tPID4 is ready')
					
					#将status状态颜色变为淡蓝
					self.stylesheet = self.stylesheet+'#status4{background-color:#99CCFF;}'
					self.setStyleSheet(self.stylesheet)
				elif text == 'esc':
					global_pcb.pcb.block(global_pcb.pid4)
					self.change_status(number,'block')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID4]\tPID4 is blocked')
					
					#将status状态颜色变为红色
					self.stylesheet = self.stylesheet+'#status4{background-color:#CC3333;}'
					self.setStyleSheet(self.stylesheet)
			elif number == 5:
				if text == 'enter':
					global_pcb.pcb.enter(global_pcb.pid5)
					self.change_status(number,'ready')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID5]\tPID5 is ready')
					
					#将status状态颜色变为淡蓝
					self.stylesheet = self.stylesheet+'#status5{background-color:#99CCFF;}'
					self.setStyleSheet(self.stylesheet)
				elif text == 'esc':
					global_pcb.pcb.block(global_pcb.pid5)
					self.change_status(number,'block')
					self.status_bar.appendPlainText(self.get_time()+'\t[PID5]\tPID5 is blocked')
					
					#将status状态颜色变为红色
					self.stylesheet = self.stylesheet+'#status5{background-color:#CC3333;}'
					self.setStyleSheet(self.stylesheet)
				
	#如节点为None，则只能先创建节点
	def init_button(self,number):
		if number == 1:
			if self.btn_create1.text() == 'Terminate':
				global_pcb.pid1 = None
				self.status1.setText('')
				self.btn_create1.setText('create')
				self.btn_schedule1.setEnabled(False)
				self.btn_block1.setEnabled(False)
				self.btn_wakeup1.setEnabled(False)
				
				#恢复原来的样式，即status为无色
				self.setStyleSheet(self.stylesheet)
			else:
				self.status1.setText('spare')
				self.btn_create1.setText('Terminate')
				self.btn_schedule1.setEnabled(True)
				self.btn_block1.setEnabled(True)
				self.btn_wakeup1.setEnabled(True)
		elif number == 2:
			if self.btn_create2.text() == 'Terminate':
				global_pcb.pid2 = None
				self.status2.setText('')
				self.btn_create2.setText('create')
				self.btn_schedule2.setEnabled(False)
				self.btn_block2.setEnabled(False)
				self.btn_wakeup2.setEnabled(False)
				
				#恢复原来的样式，即status为无色
				self.setStyleSheet(self.stylesheet)
			else:
				self.status2.setText('spare')
				self.btn_create2.setText('Terminate')
				self.btn_schedule2.setEnabled(True)
				self.btn_block2.setEnabled(True)
				self.btn_wakeup2.setEnabled(True)
		elif number == 3:
			if self.btn_create3.text() == 'Terminate':
				global_pcb.pid3 = None
				self.status3.setText('')
				self.btn_create3.setText('create')
				self.btn_schedule3.setEnabled(False)
				self.btn_block3.setEnabled(False)
				self.btn_wakeup3.setEnabled(False)
				
				#恢复原来的样式，即status为无色
				self.setStyleSheet(self.stylesheet)
			else:
				self.status3.setText('spare')
				self.btn_create3.setText('Terminate')
				self.btn_schedule3.setEnabled(True)
				self.btn_block3.setEnabled(True)
				self.btn_wakeup3.setEnabled(True)
		elif number == 4:
			if self.btn_create4.text() == 'Terminate':
				global_pcb.pid4 = None
				self.status4.setText('')
				self.btn_create4.setText('create')
				self.btn_schedule4.setEnabled(False)
				self.btn_block4.setEnabled(False)
				self.btn_wakeup4.setEnabled(False)
				
				#恢复原来的样式，即status为无色
				self.setStyleSheet(self.stylesheet)
			else:
				self.status4.setText('spare')
				self.btn_create4.setText('Terminate')
				self.btn_schedule4.setEnabled(True)
				self.btn_block4.setEnabled(True)
				self.btn_wakeup4.setEnabled(True)
		elif number == 5:
			if self.btn_create5.text() == 'Terminate':
				global_pcb.pid5 = None
				self.status5.setText('')
				self.btn_create5.setText('create')
				self.btn_schedule5.setEnabled(False)
				self.btn_block5.setEnabled(False)
				self.btn_wakeup5.setEnabled(False)
				
				#恢复原来的样式，即status为无色
				self.setStyleSheet(self.stylesheet)
			else:
				self.status5.setText('spare')
				self.btn_create5.setText('Terminate')
				self.btn_schedule5.setEnabled(True)
				self.btn_block5.setEnabled(True)
				self.btn_wakeup5.setEnabled(True)
	
	#进程状态发生变化时执行的参数，传入参数为number是第几行，status是进程状态如: ready running status block
	def change_status(self,number,status=''):
		if number == 1:
			label_status =  self.status1
		elif number == 2:
			label_status =  self.status2
		elif number == 3:
			label_status =  self.status3
		elif number == 4:
			label_status =  self.status4
		elif number == 5:
			label_status =  self.status5
		label_status.setText(status)
	
	def get_time(self,run_time=0):
		if run_time == 0:
			timestamp = int(time.time())
			tArray = time.localtime(timestamp)
			return time.strftime('%H:%M:%S',tArray)
		else:
			timestamp = run_time
			run_hours = timestamp // 3600
			timestamp = timestamp % 3600
			run_minutes = timestamp // 60
			run_seconds = timestamp % 60
			return str(run_hours)+'时 '+str(run_minutes)+'分 '+str(run_seconds)+'秒'
	
	#加载txt后缀的qss样式，如qss.txt，输入参数为qss.txt的路径(str)，返回stylesheet(str)
	def load_qss(self,qss_path):
		stylesheet = ''
		try:
			file = open(qss_path,'r')
			stylesheet = ''
			for line in file:
				stylesheet+=line
		except:
			print('qss import error')
		return stylesheet