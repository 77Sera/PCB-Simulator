#coding:utf8

#进程 结点

import time

#要新建进程节点，必须传入进程节点的pid(1,2,3,4,5),PRL为节点的优先级
class process_node():
	def __init__(self,pid,PRL=1,next_=None):
		self.pid = pid
		self.PRL = PRL
		self.status = ''
		self.start_time = int(time.time())
		
		self.run_time = self.start_time #实际运行时间
		
		#因为是模拟，因此我模拟每个节点的程序，每次running进度+3,running5次，则程序就算运行完毕
		self.run_progress = 0 #初始化程序运行进度
		self.total_progress = 1000 #程序运行总进度
		
		self.next = next_
		
	#打印节点信息
	def print_status(self):
		print('pid: ',self.pid)
		print('status: ',self.status)
		print('start_time：',self.start_time)
		print('run_progress:',self.run_progress)