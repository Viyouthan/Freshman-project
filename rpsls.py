#coding:gbk
"""
程序：完成RPSLS游戏
作者：谭薇
"""
import random
comp_number=random.randint(0,5)
# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
def name_to_number(name):
	"""
	将游戏对象对应到不同的整数
	"""
	if name=="石头":
		return 0
	elif name=="史波克":
		return 1
	elif name=="纸":
		return 2
	elif name=="蜥蜴":
		return 3
	elif name=="剪刀":
		return 4
	else:
		print("Error: No Correct Name")
		
						
						
def number_to_name(number):
	"""
	将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	"""
	if number==0:
		return "石头"
	elif number==1:
		return "史波克"
	elif number==2:
		return "纸"
	elif number==3:
		return "蜥蜴"
	elif number==4:
		return "剪刀"
		
		
		
def rpsls(player_choice):
	"""
	用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

	"""
	player_number=name_to_number(player_choice)
	
	if comp_number==1 and player_number==0:
		print("机器赢了")
	if comp_number==2 and player_number==0:
		print("机器赢了")
	if comp_number==3 and player_number==0:
		print("您赢了")
	if comp_number==4 and player_number==0:
		print("您赢了")
	if comp_number==0 and player_number==1:
		print("您赢了")
	if comp_number==2 and player_number==1:
		print("机器赢了")
	if comp_number==3 and player_number==1:
		print("机器赢了")
	if comp_number==4 and player_number==1:
		print("您赢了")
	if comp_number==0 and player_number==2:
		print("您赢了")
	if comp_number==1 and player_number==2:
		print("您赢了")
	if comp_number==3 and player_number==2:
		print("机器赢了")
	if comp_number==4 and player_number==2:
		print("机器赢了")
	if comp_number==0 and player_number==3:
		print("机器赢了")
	if comp_number==1 and player_number==3:
		print("您赢了")
	if comp_number==2 and player_number==3:
		print("您赢了")
	if comp_number==4 and player_number==3:
		print("机器赢了")
	if comp_number==0 and player_number==4:
		print("机器赢了")
	if comp_number==1 and player_number==4:
		print("机器赢了")
	if comp_number==2 and player_number==4:
		print("您赢了")
	if comp_number==3 and player_number==4:
		print("您赢了")
	if comp_number==player_number:
		print("平局")
		
	
#对程序进行测试
print("请输入您的选择")
player_choice=input()#用户输入选择，赋值给player_choice
print("--------")#分割线
print("您的选择为",player_choice)#电脑上输出用户的选择
comp_choice=number_to_name(comp_number)#调用函数number_to_name将数对应到对象
print("计算机的选择为",comp_choice)#在屏幕上显示计算机选择的随机对象
rpsls(player_choice)#根据RPSLS游戏规则，在屏幕上输出对应的结果



