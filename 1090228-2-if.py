# if練習_1
number = int(input("EX1- 輸入數字(1~200): "))
if number>200:
    print("大於200!")
elif number>100:
    print("大於100,小於200!")
else:
    print("小於100!")


print("\n")
# if練習_2-輸入年份並比對與答案是否相符:
birthday_year = int(1991)
age = 29
this_year = int(input("EX2- 請輸入今年年分(西元): "))
now_age = this_year-birthday_year
if now_age == 29:
    print("是的,他今年", age, "!")
else:
    print("他今年是", age, "歲,不是", now_age, "歲喔!")


print("\n")
# if練習_3-猜歲數:
age = 29
keying = int(input("EX3- 猜猜他今年幾歲: "))
if keying == age:
    print("答對了,他今年", age, "!")
else:
    print("錯了,他今年是", age)