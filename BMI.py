height = input('請輸入你的身高: ')
weight = input('請輸入你的體重: ')
height = float(height)
weight = float(weight)
bmi = weight / ( height * height) * 10000
print(bmi)
if bmi < 18.5 :
	print('太瘦了吧, 吃多點!')
elif  18.5 <= bmi < 24 :
	print('唉唷,剛好喔, 維持住喔')
elif  24 >= bmi < 27 :
	print('過重了啦, 少吃點!')
elif 27 >= bmi < 30 :
	print('wow, 輕度肥胖的小胖子')
elif 30 >= bmi <35 :
	print('omg, 中度肥胖的中胖子')
else:
	print('重度肥胖, 建議您做腸胃繞道手術!!!!!!')