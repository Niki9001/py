import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

df = pd.read_excel("20221222-20221223_Cadaveric data spreadsheet_20221224-01.xlsx")

class Draw():
    #定义一张画布上有几个图的方法
    def sp(self,row,pic,number):
        plt.subplot(row,pic,number)
    #定义数据的调用方法，用于画图
    def pic(self,y,color):
        plt.plot(y,label = y,linewidth = 0.5,color = color)
    #定义画图的坐标等方法
    def plot(self, xlable, title, fontsize, ylim1, ylim2):
        plt.xlabel(xlable)
        plt.title(title,font={'size':fontsize})
        x = [0,1, 2, 3, 4, 5]
        x_index = [500, 750, 1000, 1500, 2000, 3000]
        plt.xticks(x,x_index)
        plt.ylim(ylim1,ylim2)
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
        l = np.array(k)
        j = l.tolist()
        return j

# 这是调用，可以删，可以改
# 第一张图
colorArr = ["green","blue","black","orange","grey","purple","navy","olive","red","peru","cadetblue"]
a = Draw()
a.sp(1,1,1)
b = a.sRange(0,3,4,10)
for number in range(0,3):
    a.pic(b[number],colorArr[number])

a.plot("Freq","Perforated_IMJ disconnected @ umbo \n Session 01, 9 measurements",10,0,0.4)
a.output()


