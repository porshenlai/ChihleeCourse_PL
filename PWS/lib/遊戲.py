import random

class 猜範圍 :
    def __init__ (self, Min=0, Max=100) :
        self.目標 = random.randint(Min, Max)
        self.範圍 = (Min, Max);
    def guess (self, val) :
        if val < self.範圍[0] or  val > self.範圍[1] :
            return None
        if val == self.目標 :
            return (val,self.目標)
        self.範圍 = (self.範圍[0],val) if self.目標 < val else (val,self.範圍[1])
        return self.範圍

class 猜數字 :
	"""
	猜幾個字 = 2
	可猜的字 = "0123456789abcdef"
	遊戲 = 猜數字(猜幾個字,可猜的字)
	遊戲.挑戰()
	"""
	def __init__ (self,猜幾個字=4,可猜的字="0123456789") :
		可猜的字=list(可猜的字)
		random.shuffle(可猜的字)
		self.字數 = 猜幾個字
		self.答案 = "".join(可猜的字[0:猜幾個字])
		# print(self.答案)

	def 比對 (self, 猜測) :
		AB=[0,0]
		for 位置 in range(0,len(猜測)) :
			if 猜測[位置] not in self.答案 :
				continue
			if 猜測[位置] == self.答案[位置] :
				AB[0]+=1
			else :
				AB[1]+=1
		return AB

	def 挑戰 (self, 可挑戰次數=10000) :
		重試=0
		while 重試 < 可挑戰次數 :
			try :
				猜測=input(f"請輸入 {self.字數} 個猜測的字:")
				if len(猜測)!=self.字數 :
					continue
				比對結果=self.比對(猜測)
				if 比對結果[0] >= self.字數 :
					print("您猜中了，答案是:",self.答案)
					break
				else :
					print(猜測," => {0:d} A {1:d} B".format(*比對結果))
				重試+=1
			except Exception as x:
				print(x)

