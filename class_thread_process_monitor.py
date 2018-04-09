#coding:utf8

from PyQt5 import QtWidgets
from class_pcb_simulator import pcb_simulator
import threading
import time

import global_pcb

class thread_process_monitor(threading.Thread):
	def __init__(self , QWidget):
		super(thread_process_monitor,self).__init__()
		self.mainwindow = QWidget
		self.running = True
		
	def run(self):
		while self.running:
			head = global_pcb.pcb.head_ready
			p = head.next
			if p != None:
				if p.pid == 1:
					self.mainwindow.running1_signal.emit(1)
				elif p.pid == 2:
					self.mainwindow.running2_signal.emit(2)
				elif p.pid == 3:
					self.mainwindow.running3_signal.emit(3)
				elif p.pid == 4:
					self.mainwindow.running4_signal.emit(4)
				elif p.pid == 5:
					self.mainwindow.running5_signal.emit(5)
			else:
				if global_pcb.pcb.head_running.next == None:
					time.sleep(1)
					continue
				else:
					p = global_pcb.pcb.head_running.next
				
			global_pcb.pcb.running()
			time.sleep(1)
			p.run_progress+=10
			
			p.run_time+=1
			
			progress_list = []
			progress_list.append(str(p.pid))
			progress_list.append(str(p.run_progress))
			progress_list.append(str(p.total_progress))
			progress_list.append(p.run_time - p.start_time)
			
			self.mainwindow.progress_signal.emit(progress_list)
			if p.run_progress == p.total_progress:
				pass
			time.sleep(2)
				
	def terminate(self):
		self.running = False