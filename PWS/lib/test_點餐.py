from sys import path as incpath
incpath.append(".")
from 點餐 import 早餐店

美而美 = 早餐店()
訂單 = []
餐點名稱 = "豆漿" #@param ["豆漿","火腿蛋吐司","玉米蛋餅"]
餐點數量 = 1 #@param {type:"slider", min:0, max:10, step:1}
選項 = []
for 候選 in 美而美.菜單[餐點名稱]["選項"] :
	if input("輸入 y 加註 %s :" % (候選)) == 'y' :
		選項.append(候選)
訂單.append({"名稱":餐點名稱, "數量":餐點數量, "選項":選項})

美而美.試算(訂單)
