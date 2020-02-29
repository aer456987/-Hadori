you_password = "0123456789"
x = input("請輸入密碼: ")
while True:
	if you_password == x:
		print("歡迎登入。")
		break
	elif you_password != x:
		print("你還有兩次機會。")
		x = input("請輸入密碼: ")
		if you_password != x:
			print("你還有一次機會。")
			x = input("請輸入密碼: ")
			if you_password != x:
				print("無緣byebye。")
				break