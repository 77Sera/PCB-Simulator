#coding:utf8

#模拟pcb类,所有链表都是有空头的

from class_process_node import process_node

class pcb_simulator():
	def __init__(self):
		self.head_running = process_node(pid=-1) #初始化running队列的head
		self.head_ready = process_node(pid=-1) #初始化ready队列的head
		self.head_block = process_node(pid=-1) #初始化block队列的head
		self.head_spare = process_node(pid=-1) #初始化spare队列的head
		
	# 新建一个节点，将它放入空闲(spare)队列中
	# 且status自动设为'spare'
	def create(self,pid,PRL=1):
		new_node = process_node(pid,PRL)
		new_node.status = 'spare'
		if self.head_spare.next == None:
			self.head_spare.next = new_node
		else:
			p = self.head_spare
			while p.next != None:
				p = p.next
			p.next = new_node
		return new_node
		
	#根据节点的status找到此节点的所在队列的head
	def find_head(self,status):
		if status == 'ready':
			return self.head_ready
		elif status == 'running':
			return self.head_running
		elif status == 'block':
			return self.head_block
		elif status == 'spare':
			return self.head_spare
		
	#将某节点放入block队列中,传入参数需为process_node()的实例
	#先要判断此节点在哪个队列中，根据其状态判断
	def block(self,block_node):
		head = self.find_head(block_node.status)
		block_node = self.drop_node(block_node)
		block_node.status = 'block'
		p = self.head_block
		while p.next != None:
			p = p.next
		p.next = block_node
		
	# 在ready队列中找优先级最高的节点，置running队列中
	# 因为是单处理器，所以running队列只能有一个节点
	# 因此先要将running队列中的节点取出，放到ready队列最尾端
	def running(self):
		if self.head_running.next != None:
			if self.head_ready.next == None:
				return
			else:
				running_node = self.head_running.next
				running_node = self.drop_node(running_node)
				running_node.status = 'ready'
			
				ready_node = self.head_ready.next
				ready_node = self.drop_node(ready_node)
				ready_node.status = 'running'
				
				self.head_running.next = ready_node
			
				p = self.head_ready
				while p.next != None:
					p = p.next
				p.next = running_node
		# running队列为空
		else:
			if self.head_ready.next == None:
				return
			#running队列为空，ready队列不为空
			else:
				ready_node = self.head_ready.next
				ready_node = self.drop_node(ready_node)
				ready_node.status = 'running'
				self.head_running.next = ready_node
		
	#使进程ready的函数
	def enter(self,ready_node):
		ready_node = self.drop_node(ready_node)
		head = self.head_ready
		p = head
		while p.next != None:
			p = p.next
		p.next = ready_node
		ready_node.status = 'ready'
		
	#使进程从阻塞(block)队列中被唤醒，进入ready队列
	def wakeup(self,wakeup_node):
		wakeup_node = self.drop_node(wakeup_node)
		
		head_ready = self.head_ready
		p = head_ready
		while p.next != None:
			p = p.next
		p.next = wakeup_node
		wakeup_node.status = 'ready'
		
	def terminate(self,terminate_node):
		terminate_node = self.drop_node(terminate_node)
		
	#实现各种中间调度过程，根据用户指令来相应执行进程
	def schedule(self,target_node):
		#if target_node.status == ''
		cmd = input('input command=>')
		if cmd == 'enter':
			target_node = self.drop_node(target_node)
			head = self.head_ready
			p = head
			while p.next != None:
				p = p.next
			p.next = target_node
			target_node.status = 'ready'
	
	#删除某节点，传入参数为要删除的节点
	def drop_node(self,drop_node):
		head = self.find_head(drop_node.status)
		p = head
		while p.next != drop_node:
			p = p.next
		p.next = drop_node.next
		drop_node.next = None
		return drop_node
		
	#传入参数为某队列的head节点，求出队列的长度
	def length(self,head):
		p , n = head , 0
		while p.next != None:
			n+=1
			p = p.next
		return n
		
if __name__ == '__main__':
	pcb = pcb_simulator()
	pid1 = pcb.create(1)
	pid2 = pcb.create(2)
	pid3 = pcb.create(3)
	pid4 = pcb.create(4)
	pid5 = pcb.create(5)
	
	pcb.block(pid4)
	pcb.wakeup(pid4)
	pcb.running()
	#打印空闲队列所有元素
	p = pcb.head_running.next
	while p != None:
		p.print_status()
		p = p.next