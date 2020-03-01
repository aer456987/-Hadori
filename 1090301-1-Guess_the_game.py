# 版本二:
import random
top = " ╔==========╗\n"
win = "║  你贏了  ║"
loser = "║  你輸了  ║"
tie = "║ 雙方平手 ║"
down = "\n ╚==========╝"
i = 3    #剩餘次數
while True:
	cpu_dic = {0:"剪刀", 1:"石頭", 2:"布"}    # 建立cpu對照用字典,數字:文字
	player = input("輸入剪刀/石頭/布：")
	cpu = cpu_dic[random.randint(0,2)]
	print("\n")
	print("你出的拳:", player)
	print("電腦出的拳:", cpu)
	while i > 0:
		if player == cpu:
			print(top, tie, down)
		elif player == "剪刀" and cpu == "布":
			print(top, win, down)
		elif player == "石頭" and cpu == "剪刀" :
			print(top, win, down)
		elif player == "布" and cpu == "石頭":
			print(top, win, down)
		else:
			print(top, loser, down)
		if i > 0:
			i = i - 1
			print("你還有", i, "次機會。")
			print("\n")
			break
	if i == 0:
		print("比賽結束")
		break



# # 版本一:
# import random
# i = 3
# while True:
# 	cpu_dic = {0:"剪刀", 1:"石頭", 2:"布"}    # 建立cpu對照用字典,數字:文字
# 	player = input("輸入剪刀/石頭/布：")
# 	cpu = cpu_dic[random.randint(0,2)]
# 	print("\n")
# 	print("你出的拳:", player)
# 	print("電腦出的拳:", cpu)
# 	dic = {"剪刀":0, "石頭":1, "布":2}    # 轉換字典內容,文字:數字
# 	player = dic[player]
# 	cpu = dic[cpu]

# 	while i > 0:
# 		if player == cpu:
# 			print("╔==========╗")
# 			print("║ 雙方平手 ║")
# 			print("╚==========╝")
# 		elif player == 0 and cpu == 2:
# 			print("╔==========╗")
# 			print("║  你贏了  ║")
# 			print("╚==========╝")
# 		elif player == 1 and cpu == 0:
# 			print("╔==========╗")
# 			print("║  你贏了  ║")
# 			print("╚==========╝")
# 		elif player == 2 and cpu == 1:
# 			print("╔==========╗")
# 			print("║  你贏了  ║")
# 			print("╚==========╝")
# 		else:
# 			print("╔==========╗")
# 			print("║  你輸了  ║")
# 			print("╚==========╝")
# 		if i > 0:
# 			i = i - 1
# 			print("你還有", i, "次機會。")
# 			print("\n")
# 			break
# 	if i == 0:
# 		print("比賽結束")
# 		break
