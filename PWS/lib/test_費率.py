from sys import path as incpath
incpath.append(".")
import 費率

搭車地區="桃園" # @param ["桃園","高雄","台北"]
搭車距離=5.5 # @param {"type":"number"}
停等時間=0  # @param {"type":"number"}

計費器 = getattr(費率,搭車地區+"計程車")()
print("在%s搭車，%d公里，停等%d秒，需花費 %d NTD" % (搭車地區,搭車距離,停等時間,計費器.費率試算(1000*搭車距離,停等時間)) )
