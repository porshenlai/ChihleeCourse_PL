from piers.AIO.Web import WebHome
from json import loads
from time import time
from lib.遊戲 import 猜數字

class H (WebHome.PostHandler) :
	def __init__ (self, args) :
		super().__init__(args)
		self.MaxGameLife = 3000*100
		self.Sessions = {} # {int(time()*100):猜字遊戲(),174753058022:...}

	async def get_session (self, sid=0, 猜幾個字=4, 可猜的字="0123456789") :
		if sid == 0 or sid not in self.Sessions:
			sid = int(time()*100)

		RMList=[]
		if sid not in self.Sessions:
			self.Sessions[sid] = 猜數字(猜幾個字,可猜的字);
		for k in self.Sessions:
			if sid - k > self.MaxGameLife :
				RMList.append(k)
		for k in RMList :
			del self.Sessions[k]
		return sid, self.Sessions[sid]

	async def handle (self, rio) :
		"""
		[Request]  curl --json '{"SID":123.456,"GS":"0123","CNT":4,"CS":"0123456789"}' http://localhost:40780/ABGame
		[Response] {"R":"OK","D":[0,0]}
		"""
		# assert "N" in rio.Session, "Violation"
		# print("path",rio.path)
		# s, dbn=[], rio.path.group(2)
		ct, arg, hdrs=rio.Req
		arg = loads(arg) if str == type(arg) else arg
		sid, ss = await self.get_session(
			arg["SID"]
		) if "SID" in arg else await self.get_session(
			0,
			int(arg["CNT"]) if "CNT" in arg else 4,
			arg["CS"] if "CS" in arg else "0123456789"
		)
		return rio.JSON({"R":"OK","SID":sid,"D":ss.比對(arg["GS"]) if "GS" in arg else [0,0]})
PHMClass=H
