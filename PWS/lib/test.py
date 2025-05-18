from 遊戲 import 猜數字

猜幾個字 = 2 #@param{type:"slider","min":1,"max":8}
可猜的字 = "0123456789abcdef" #@param{type:"string"}
遊戲 = 猜字遊戲(猜幾個字,可猜的字)
遊戲.挑戰()
