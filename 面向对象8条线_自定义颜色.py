# 这是导入的包，没有意外不能动
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import random
df = pd.read_excel("2223fixed2.xlsx")
#设置画布尺寸
plt.figure(figsize=(8,6))
#定义类，类是面向对象的调用主体
class Draw():
    #定义一张画布上有几个图的方法
    def sp(self,row,pic,number):
        plt.subplot(row,pic,number)
    #定义数据的调用方法，用于画图
    def pic(self,y,color):
        plt.plot(df["Time"],df[y],label = y,linewidth = 0.5,color = color)
    #定义画图的坐标等方法
    def plot(self, xlable, title, fontsize, ylim1, ylim2):
        plt.xlabel(xlable)
        plt.title(title,font={'size':fontsize})
        x = [1, 2, 3, 4, 5, 6]
        x_index = [500, 750, 1000, 1500, 2000, 3000]
        plt.xticks(x,x_index)
        plt.ylim(ylim1,ylim2)
    #这是输出方法
    def output(self):
        plt.tight_layout(pad=1.08)
        plt.show()
        plt.legend()
# 这是用随机方法生成颜色
#def randomColor():
 #   colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  #  color = ''
   # for j in range(6):
    #    color += colorArr[random.randint(0,14)]
    #return '#'+ color
# 自定义颜色
colorArr = ["cadetblue","green","blue","black","orange","grey","purple","navy","peru","olive","red"]


# 这是调用，可以删，可以改
# 第一张图
a = Draw()
a.sp(1,1,1)
# 不同的线分配不同的颜色
for i in range(8):
    a.pic(f"Index N{i}",colorArr[i])

a.plot("Freq","Perforated_IMJ disconnected @ umbo \n Session 01, 9 measurements",10,0,0.24)

plt.savefig("./perforated_IMJ disconnected @ umbo.jpg")
a.output()
