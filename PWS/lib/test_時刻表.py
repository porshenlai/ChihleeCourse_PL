from sys import path as incpath
incpath.append(".")
from 時刻表 import 臺鐵

tf = 臺鐵()
result = tf.查詢("1040-樹林","4080-嘉義",["自強","普悠瑪","自強(3000)","區間"])
print(result)
