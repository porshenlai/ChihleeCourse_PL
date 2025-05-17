from lib.臺鐵 import 時刻表

tf=時刻表()
for result in tf.查詢("1040-樹林","4080-嘉義",["自強","普悠瑪","自強(3000)","莒光","區間"]) :
	print(tf.格式化輸出(result))
