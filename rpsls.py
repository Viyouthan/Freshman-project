#coding:gbk
"""
�������RPSLS��Ϸ
���ߣ�̷ޱ
"""
import random
comp_number=random.randint(0,5)
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	if name=="ʯͷ":
		return 0
	elif name=="ʷ����":
		return 1
	elif name=="ֽ":
		return 2
	elif name=="����":
		return 3
	elif name=="����":
		return 4
	else:
		print("Error: No Correct Name")
		
						
						
def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""
	if number==0:
		return "ʯͷ"
	elif number==1:
		return "ʷ����"
	elif number==2:
		return "ֽ"
	elif number==3:
		return "����"
	elif number==4:
		return "����"
		
		
		
def rpsls(player_choice):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

	"""
	player_number=name_to_number(player_choice)
	
	if comp_number==1 and player_number==0:
		print("����Ӯ��")
	if comp_number==2 and player_number==0:
		print("����Ӯ��")
	if comp_number==3 and player_number==0:
		print("��Ӯ��")
	if comp_number==4 and player_number==0:
		print("��Ӯ��")
	if comp_number==0 and player_number==1:
		print("��Ӯ��")
	if comp_number==2 and player_number==1:
		print("����Ӯ��")
	if comp_number==3 and player_number==1:
		print("����Ӯ��")
	if comp_number==4 and player_number==1:
		print("��Ӯ��")
	if comp_number==0 and player_number==2:
		print("��Ӯ��")
	if comp_number==1 and player_number==2:
		print("��Ӯ��")
	if comp_number==3 and player_number==2:
		print("����Ӯ��")
	if comp_number==4 and player_number==2:
		print("����Ӯ��")
	if comp_number==0 and player_number==3:
		print("����Ӯ��")
	if comp_number==1 and player_number==3:
		print("��Ӯ��")
	if comp_number==2 and player_number==3:
		print("��Ӯ��")
	if comp_number==4 and player_number==3:
		print("����Ӯ��")
	if comp_number==0 and player_number==4:
		print("����Ӯ��")
	if comp_number==1 and player_number==4:
		print("����Ӯ��")
	if comp_number==2 and player_number==4:
		print("��Ӯ��")
	if comp_number==3 and player_number==4:
		print("��Ӯ��")
	if comp_number==player_number:
		print("ƽ��")
		
	
#�Գ�����в���
print("����������ѡ��")
player_choice=input()#�û�����ѡ�񣬸�ֵ��player_choice
print("--------")#�ָ���
print("����ѡ��Ϊ",player_choice)#����������û���ѡ��
comp_choice=number_to_name(comp_number)#���ú���number_to_name������Ӧ������
print("�������ѡ��Ϊ",comp_choice)#����Ļ����ʾ�����ѡ����������
rpsls(player_choice)#����RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��



