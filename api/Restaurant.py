from piers.AIO.Web import WebHome
from json import loads
from lib.點餐 import 早餐店

class H (WebHome.PostHandler) :
	def __init__ (self, args) :
		super().__init__(args)
        self.美而美 = 早餐店()
	async def handle (self, rio) :
		"""
		[Request]  curl --json '{"Area":"高雄","Dist":5.5,"Wait":30}' http://localhost:40780/Taxi
		[Response] {"R":"OK","D":1234}
		"""
		# assert "N" in rio.Session, "Violation"
		# print("path",rio.path)
		# s, dbn=[], rio.path.group(2)
		ct, arg, hdrs=rio.Req
		arg = loads(arg) if str == type(arg) else arg
        訂單 = arg["Orders"]
		return rio.JSON({"R":"OK","D":self.美而美.試算(訂單)})
PHMClass=H
