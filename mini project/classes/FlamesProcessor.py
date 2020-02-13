class FlameProcessor():
	proceed = True
	result = []
	count = 0
	p1_list = []
	p2_list = []
	#to remove the common characters
	def remove_char(sefl,list1,list2):
		for i in range(len(list1)):
			for j in range(len(list2)):
				if list1[i]==list2[j]:
					c=list1[i]
					list1.remove(c)
					list2.remove(c)
					list3=list1+["*"]+list2
					return[list3,True]
		list3=list1+["*"]+list2
		return[list3,False]
	
	def callFlow_of_Methods(self,p1,p2):
		self.setPLists(p1,p2)
		self.init_Result_and_Count()
		self.set_Result()
		self.proceed = True
	
	def process(self,p1,p2,label,canvas):
		self.callFlow_of_Methods(p1,p2)
		label.config(text = self.result[0])
		canvas.create_window(250, 180, window=label)
	
	def set_Result(self):
			while len(self.result)>1:
				split_index=(self.count%len(self.result)-1)
				if split_index >=0:
					right=self.result[split_index+1:]
					left=self.result[:split_index]
					self.result=right+left
				else:
					self.result=self.result[:len(self.result)-1]
	
	def setPLists(self,p1,p2):
		self.p1_list = Utility.list_lowstring(p1)
		self.p2_list = Utility.list_lowstring(p2)
		
	def init_Result_and_Count(self):
			while self.proceed:
				ret_list=self.remove_char(self.p1_list,self.p2_list)
				con_list=ret_list[0]
				self.proceed=ret_list[1]
				star_index=con_list.index("*")
				self.p1_list=con_list[:star_index]
				self.p2_list=con_list[star_index+1:]
				self.count=len(self.p1_list)+len(self.p2_list)
			self.result=["Friends","Love","Affection","Marriage","Enemy","Siblings"]

class Utility():
		@staticmethod
		def list_lowstring(string):
			string=string.lower()
			string.replace(" ","")
			return list(string)