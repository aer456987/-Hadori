# 版本四:print內容調整；輸入錯誤增加提示；新增{集合}
import random

cpu_dic = {0:"剪刀", 1:"石頭", 2:"布"}
dic = {"剪刀", "石頭", "布"}    # 新增判讀用{集合}
cpu = cpu_dic[random.randint(0,2)]
num = int(input("輸入遊玩次數: "))    # number改成num
while True:
	player = input("你出的拳(剪刀/石頭/布): ")
	if player not in dic:    # 如果輸入內容不符要求,即出現提示,但不計入次數
		print("╔======================╗\n║ 只能輸入剪刀/石頭/布 ║\n╚======================╝\n")
	elif player in dic:    # 如果輸入內容符合要求，進入迴圈
		while num > 0:
			win = "╔==========╗\n║  你贏了  ║\n╚==========╝"  #優化程式顯示方式
			lose = "╔==========╗\n║  你輸了  ║\n╚==========╝"
			tie = "╔==========╗\n║ 雙方平手 ║\n╚==========╝"	
			print("電腦出的拳:", cpu)
			if player == cpu:
				print(tie)
			elif player == "剪刀" and cpu == "布":
				print(win)
			elif player == "石頭" and cpu == "剪刀" :
				print(win)
			elif player == "布" and cpu == "石頭":
				print(win)
			else:
				print(lose)
			if num > 0:
				num -= 1    # num = num - 1
				print("你還有", num, "次機會。")
				print("\n")
				break
		if num == 0:
			print("比賽結束")
			break