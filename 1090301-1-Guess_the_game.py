import random
i = 3
while True:
	cpu_dic = {0:"剪刀", 1:"石頭", 2:"布"}
	player = input("輸入剪刀/石頭/布：")
	cpu = cpu_dic[random.randint(0,2)]
	print("\n")
	print("你出的拳:", player)
	print("電腦出的拳:", cpu)
	dic = {"剪刀":0, "石頭":1, "布":2}
	player = dic[player]
	cpu = dic[cpu]
	# win = "你贏了!"
	# loser = "你輸了!"
	# tie = "雙方平手。"

	while i > 0:
		if player == cpu:
			print("╔==========╗")
			print("║ 雙方平手 ║")
			print("╚==========╝")
		elif player == 0 and cpu == 2:
			print("╔==========╗")
			print("║  你贏了  ║")
			print("╚==========╝")
		elif player == 1 and cpu == 0:
			print("╔==========╗")
			print("║  你贏了  ║")
			print("╚==========╝")
		elif player == 2 and cpu == 1:
			print("╔==========╗")
			print("║  你贏了  ║")
			print("╚==========╝")
		else:
			print("╔==========╗")
			print("║  你輸了  ║")
			print("╚==========╝")
		if i > 0:
			i = i - 1
			print("你還有", i, "次機會。")
			print("\n")
			break
	if i == 0:
		print("比賽結束")
		break