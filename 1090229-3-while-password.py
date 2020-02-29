# 第五次嘗試
you_password = "012345"
i = 3
while i > 0:
	i = i - 1
	pwd = input("請輸入密碼: ")
	if pwd == you_password:
		print("歡迎登入。")
		break
	else:
		print("密碼錯誤")
		if i > 0:
			print("你還有", i, "次機會。")
		else:
			print("無緣byebye。")
			break