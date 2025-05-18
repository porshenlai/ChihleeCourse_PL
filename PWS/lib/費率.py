from math import ceil

class 計程車 :
	"""
	搭車地區="桃園" # @param ["桃園","高雄","台北"]
	搭車距離=5.5 # @param {"type":"number"}
	停等時間=0  # @param {"type":"number"}

	exec("計費器="+搭車地區+"計程車費率計算器()")
	print("在%s搭車，%d公里，停等%d秒，需花費 %d NTD" % (搭車地區,搭車距離,停等時間,計費器.費率試算(1000*搭車距離,停等時間)) )
	"""
	def __init__ (self) :
		self.起跳=(85,1250)
		self.續跳=(5,200)
		self.延滯=(5,100)
	def 里程費率試算 (self, 里程) :
		""" 以公尺為單位 """
		基本費率,基本里程 = self.起跳
		if 基本里程 > 里程 :
			return 基本費率
		累加費率,累加里程 = self.續跳
		return 累加費率*ceil((里程-基本里程)/累加里程) + 基本費率
	def 停等費率試算 (self, 時間) :
		""" 以秒為單位 """
		延滯費率,延滯時間 = self.延滯
		return 延滯費率*(時間//延滯時間)
	def 費率試算 (self, 里程, 時間=0) :
		""" 路程公尺, 停等秒數 """
		return self.里程費率試算(里程) + self.停等費率試算(時間)

class 高雄計程車(計程車) :
	def __init__ (self) :
		super().__init__()
		self.起跳=(85,1250)
		self.續跳=(5,200)
		self.延滯=(5,100)

class 桃園計程車(計程車) :
	def __init__ (self) :
		super().__init__()
		self.起跳=(95,1250)
		self.續跳=(5,250)
		self.延滯=(5,150)

class 台北計程車(計程車) :
	def __init__ (self) :
		super().__init__()
		self.起跳=(85,1250)
		self.續跳=(5,200)
		self.延滯=(5,60)

