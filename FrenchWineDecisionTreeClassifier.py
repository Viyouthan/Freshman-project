#coding:gbk
"""
���þ������㷨���з���
���ߣ�
���ڣ�
"""
import pandas as pd           # ������Ҫ�õĿ�
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb
#%matplotlib inline
# ��������
df = pd.read_csv('frenchwine.csv')
df.columns = ['species','alcohol', 'malic_acid', 'ash', 'alcalinity ash','magnesium' ]
# �鿴ǰ5������
df.head()
print(df.head()) 
# �鿴����������ͳ����Ϣ
df.describe()
print(df.describe())

def scatter_plot_by_category(feat, x, y): #���ݵĿ��ӻ� 
    alpha = 0.5
    gs = df.groupby(feat)
    cs = cm.rainbow(np.linspace(0, 1, len(gs)))
    for g, c in zip(gs, cs):
        plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)

plt.figure(figsize=(20,5))
plt.subplot(131)
scatter_plot_by_category('species', 'alcohol', 'malic_acid')
plt.xlabel('malic_acid')
plt.ylabel('alcohol')
plt.title('species')
plt.show()

plt.figure(figsize=(20, 10)) #����seaborn��������־Ʋ�ͬ����ͼ
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(3, 2, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# ���ȶ����ݽ����з֣������ֳ�ѵ�����Ͳ��Լ�
from sklearn.model_selection import train_test_split #����sklearn���н�����飬����ѵ�����Ͳ��Լ�
all_inputs = df[['alcohol', 'malic_acid',
                             'ash', 'alcalinity ash','magnesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.85, random_state=1)#85%������ѡΪѵ����

# ʹ�þ������㷨����ѵ��
from sklearn.tree import DecisionTreeClassifier #����sklearn���е�DecisionTreeClassifier������������
# ����һ������������
decision_tree_classifier = DecisionTreeClassifier()
# ѵ��ģ��
model = decision_tree_classifier.fit(X_train, Y_train)
# ���ģ�͵�׼ȷ��
print(decision_tree_classifier.score(X_test, Y_test)) 

list1_test=[[13.52,3.17,2.72,23.5,97],[12.42,2.55,2.27,22,90],[13.76,1.53,2.7,19.5,132]]
#����ѵ���õ�ģ�Ͷ�3��������5άָ������ݽ��з��࣬�ж���ֱ��������־��������Ʒ��
print(list1_test)#����3�����ݽ��в��ԣ���ȡ3��������Ϊģ�͵������
list1_predict=model.predict(list1_test)
list2=[]
for i in list1_predict:
	if i=="Zinfandel":
		list2.append("�ɷ���")
	elif i=="Sauvignon":
		list2.append("��ϼ��")
	elif i=="Syrah":
		list2.append("����")
print(list2)

#������ԵĽ���������ģ��Ԥ��Ľ��
 
