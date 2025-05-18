from piers.AIO.Web import WebHome
from json import loads
from lib.時刻表 import 臺鐵

class H (WebHome.PostHandler) :
	def __init__ (self, args) :
		super().__init__(args)
		self.TimeTable=臺鐵()
	async def handle (self, rio) :
		"""
		[Request]  curl --json '{"ABC":123}' http://localhost:40780/APITEST
		[Response] {"R":"OK","A":{"ABC":123},"C":1}
		"""
		# assert "N" in rio.Session, "Violation"
		# print("path",rio.path)
		# s, dbn=[], rio.path.group(2)
		ct, arg, hdrs=rio.Req
		arg = loads(arg) if str == type(arg) else arg
		return rio.JSON({"R":"OK","D":self.TimeTable.查詢(
			arg["F"], arg["T"], arg["Trs"]
		)})
PHMClass=H
