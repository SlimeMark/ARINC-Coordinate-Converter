print("目前仅可接受整数经纬度 请按格式输入 例：50N140W 50S040E")
print("警告：仅供模拟飞行使用")
"""
初始化部分结束
"""
while True:
	latlon = input("在此输入原始经纬度: ")
	latnum = latlon[0:2]#选取纬度数字
	latnum = int(latnum)#转换为整数
	latdir = latlon[2]#选取南/北纬
	lonnum1 = latlon[3:6]#选取经度数字
	lonnum1 = int(lonnum1)#转换为整数
	lonnum = latlon[4:6]#ARINC格式输出只取经度最后两位数
	lonnum = int(lonnum)#转换为整数
	londir = latlon[6]#选取西/东经
	result = ""


	if latdir == "N" and lonnum1<100 and londir == "W":
		latnum=str(latnum)
		lonnum=str(lonnum)
		print(latnum.rstrip()+lonnum.rstrip()+latdir.rstrip())
	elif latdir == "N" and lonnum1>=100 and londir == "W":
		latnum=str(latnum)
		lonnum=str(lonnum)
		print(latnum.rstrip()+latdir.rstrip()+lonnum.rstrip())
	elif latdir == "S" and lonnum1<100 and londir == "W":
		latnum=str(latnum)
		lonnum=str(lonnum)
		print(latnum.rstrip()+lonnum.rstrip()+londir.rstrip())
	elif latdir == "S" and lonnum1>=100 and londir == "W":
		latnum=str(latnum)
		lonnum=str(lonnum)
		print(latnum.rstrip()+londir.rstrip()+lonnum.rstrip())
	elif latdir == "N" and lonnum1<100 and londir == "E":
		latnum=str(latnum)
		lonnum=str(lonnum)
		print(latnum.rstrip()+lonnum.rstrip()+londir.rstrip())
	elif latdir == "N" and lonnum1>=100 and londir == "E":
		latnum=str(latnum)
		lonnum=str(lonnum)
		print(latnum.rstrip()+londir.rstrip()+lonnum.rstrip())
	elif latdir == "S" and lonnum1<100 and londir == "E":
		latnum=str(latnum)
		lonnum=str(lonnum)
		print(latnum.rstrip()+lonnum.rstrip()+latdir.rstrip())
	elif latdir == "S" and lonnum1>=100 and londir == "E":
		latnum=str(latnum)
		lonnum=str(lonnum)
		print(latnum.rstrip()+latdir.rstrip()+lonnum.rstrip())
	else:
		print("无法转换，请确认是否按格式输入且经纬度字母是否为大写")
		print(result)
	continue
