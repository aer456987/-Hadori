country = input("輸入你的國家: ")
age = int(input("輸入你的年齡: "))
if country == "台灣":
	if age >= 18:
		print("符合", country, "考駕照資格。")
	else:
		print("不符合", country,"駕照資格。")
elif country == "美國":
	if age >= 16:
		print("符合", country,"考駕照資格。")
	else:
		print("不符合", country,"駕照資格。")
else:
	print("請自行參考各國考駕照資格規範。")