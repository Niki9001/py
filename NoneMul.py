import pandas as pd
import matplotlib.pyplot as plt
import random
from matplotlib import font_manager
import numpy as np
df = pd.read_excel("Nation&Province.xlsx")
k = df.iloc[0:3,3:4]
#print(k)
class Draw():
    #k = df.iloc[0:3,3:4]
    # k = df.iloc[0:3,4:10]
    # l = np.array(k)
    # j = l.tolist()
    # for number in range(8):
    #   print(number)
    #   a.pic(i,colorArr[number])
    def figurei(self,dpi):
        plt.figure(dpi=dpi)

    #定义一张画布上有几个图的方法
    def sp(self,row,pic,number):
        plt.subplot(row,pic,number)
    #定义数据的调用方法，用于画图
    def pic(self,y,z,color):
        x = [0,1,2,3]
        plt.plot(x,y,label = z,linewidth = 0.5,color = color)
    #定义画图的坐标等方法
    def plot(self, xlable, title, fontsize, ylim1, ylim2,csize):
        plt.xlabel(xlable)
        plt.title(title,font={'size':fontsize})
        x = [0,1, 2, 3,4]
        x_index = [2006, 2011, 2016, 2021,2022]
        plt.xticks(x,x_index,size = csize)
        plt.yticks(fontsize=csize)
        plt.ylim(ylim1,ylim2)
        plt.legend(loc='upper right')

    #这是输出方法
    def output(self):
        plt.tight_layout(pad=1.08)
        plt.show()
        #plt.legend()
    # 这是用随机方法生成颜色（如果需要可以调用）
    def randomColor(self):
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ''
        for j in range(6):
            color += colorArr[random.randint(0, 14)]
        return '#' + color
    def sRange(self,startRow,endRow,startCol,endCol):
        k = df.iloc[startRow:endRow, startCol:endCol]
        return k
    def Leg(self):
        k = df.iloc[0:56, 0:1]
        l = np.array(k)
        j = l.tolist()
        kk = []
        for i in range(56):
            if i % 4 == 0:
                kk.append(j[i])
        return kk

# 这是调用，可以删，可以改
# 颜色列表
colorSel = ["green","blue","black","orange","grey","purple","navy","olive","red","peru","cadetblue","green","blue","black"]
#创建实例
a = Draw()
a.figurei(600)
#调用sp()方法
# 第一张图（每新增一张图都可以复制下面的文字，注意b只能有一个，要用其他字母替换）
a.sp(1,1,1)
c=a.Leg()
#b = a.sRange(0,4,3,4)
#loc = [['Canada '], ['NF'], ['PEI'], ['NS'], ['NB'], ['QC'], ['ON'], ['MB'], ['SK'], ['AB'], ['BC'], ['YT'], ['NT'], ['NU']]
for number in range(14):
    b = a.sRange((number*4),4*(number+1),3,4)
    a.pic(b,c[number],a.randomColor())
    a.plot("Year","None",10,0,60,5)
# 第二张图
#a.sp(1,2,2)
#c = a.sRange(4,8,3,4)
#for number in range(0,1): #注意这个range，超过了会报错
#    a.pic(c,colorSel[number])
#a.plot("Freq","Perforated_IMJ disconnected @ umbo \n Session 01, 9 measurements",10,0,60,5)
# 输出
a.output()