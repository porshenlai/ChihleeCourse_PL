from piers.AIO.Web import WebHome
from json import loads
from lib import 費率

class H (WebHome.PostHandler) :
	def __init__ (self, args) :
		super().__init__(args)
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
		距離 = float(arg["Dist"]) if str == type(arg["Dist"]) else arg["Dist"]
		停等 = float(arg["Wait"]) if str == type(arg["Wait"]) else arg["Wait"]
		計算器 = getattr(費率,arg["Area"]+"計程車")()
		return rio.JSON({"R":"OK","D":計算器.費率試算(1000*距離,停等)})
PHMClass=H
