# 第四次嘗試
you_password = "0123456789"
i = 3
while i > 0:
	pwd = input("請輸入密碼: ")
	if pwd == you_password:
		print("歡迎登入。")
		break
	else:
		i = i - 1
		print("密碼錯誤,你還有", i, "次機會。")