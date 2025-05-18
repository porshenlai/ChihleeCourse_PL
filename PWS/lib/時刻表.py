from re import compile
from pytz import timezone
from datetime import datetime
from pandas import read_html
from urllib.parse import urlencode

class 臺鐵:
	"""
	tf=臺鐵()

	#print(tf.取得車站時刻表("1020-板橋"))
	#["1000-臺北","1020-板橋","1040-樹林","3300-臺中","4080-嘉義","4220-臺南","4400-高雄"]
	#["自強","普悠瑪","太魯閣","自強(3000)","莒光","區間快","區間"]

	tf.查詢("1040-樹林","4080-嘉義",["自強","普悠瑪","自強(3000)","區間"])
	"""
	Rdr=compile(r"(.*[^0-9])([0-9]+)\s*\(\s*([^\s]*)\s*→\s*([^\s]*)\s*\)\s*")
	def __init__ (self) :
		self.Cache={}

	def 時刻表格式轉換(self, 表格) :
		Schedule={}
		for 索引,列車 in 表格.iterrows() :
			info = 臺鐵.Rdr.match(列車["車種車次 (始發站 → 終點站)"])
			if not info :
				continue
			Schedule[info.group(2)]={
				"C":info.group(1),
				"R":(info.group(3),info.group(4)),
				"T":列車["出發時間"]
			}
		return Schedule

	def 取得車站時刻表 (self, 車站代碼) :
		日期代碼 = format(datetime.now(timezone("Asia/Taipei")),"%Y/%m/%d")
		if 日期代碼 not in self.Cache :
			self.Cache[日期代碼] = {}
		if 車站代碼 not in self.Cache[日期代碼] :
			tables=read_html(
				"https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystationblank?"+urlencode({
					"rideDate":日期代碼,
					"station":車站代碼
				})
			)
			tables[0] = self.時刻表格式轉換(tables[0])
			tables[1] = self.時刻表格式轉換(tables[1])
			self.Cache[日期代碼][車站代碼] = tables
		return self.Cache[日期代碼][車站代碼]

	def 計算時間間隔(self, t1, t2) :
		t1=t1.split(":")
		t1=int(t1[0])*60+int(t1[1])
		t2=t2.split(":")
		t2=int(t2[0])*60+int(t2[1])
		return t2-t1

	def 查詢 (self, 起站, 迄站, 車種=None) :
		起站時刻表 = self.取得車站時刻表(起站)
		迄站時刻表 = self.取得車站時刻表(迄站)

		result = []

		for route in range(0,2) :
			for tid in 起站時刻表[route] :
				if tid in 迄站時刻表[route] :
					乘車時間=self.計算時間間隔(起站時刻表[route][tid]["T"],迄站時刻表[route][tid]["T"])
					if 乘車時間 < 0 or 乘車時間 > 720 :
						continue
					if 車種 and 起站時刻表[route][tid]["C"] not in 車種 :
						continue;
					result.append({
						"ID":tid,
						"TT":起站時刻表[route][tid]["C"],
						"SE":起站時刻表[route][tid]["R"],
						"ST":起站時刻表[route][tid]["T"],
						"ET":迄站時刻表[route][tid]["T"],
						"DUR":乘車時間
					})
		return result

	def 格式化輸出 (self, r) :
		return "{3} - {4}[{5:>3d}] {0:>6s} {1} ({2})".format(
			r["ID"], r["TT"], " > ".join(r["SE"]), r["ST"], r["ET"], r["DUR"]
		);
