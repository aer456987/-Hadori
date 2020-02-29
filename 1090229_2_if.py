height = int(input("輸入身高(cm): "))
weight = int(input("輸入體重(kg): "))
height = height/100    # 身高(公分)/100=身高(公尺)
bmi = weight/(height**2)
print("你的BMI: ", bmi)
if bmi<18.5:
    print("體重過輕")
elif bmi>=18.5 and bmi<24:
    print("體重正常")
elif bmi>24 and bmi<27:
    print("體重過重")
elbmi>27 and bmi<30:if 
    print("輕度肥胖")
elif bmi>30 and bmi<35:
    print("中度肥胖")
else:
    print("重度肥胖")