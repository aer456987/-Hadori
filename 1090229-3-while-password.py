#第三次嘗試
you_password = "0123456789"
i = 3
while True:
	pwd = input("請輸入密碼: ")
	if pwd == you_password:
		print("歡迎登入。")
		break
	else:
		i = i - 1
		print("密碼錯誤,你還有", i, "次機會。")
		if i == 0:
			print("無緣byebye。")
			break