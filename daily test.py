"""


F=0
W=0
for i in range(5):
    F=W+1
    W=F/2
print(W)

n=0
for i in range(5):
    n=n+1
    n=n/2
print(n)

###数列求和
##尽量使用for简写形式##
import math as m
n=eval(input())
sum=0
for i in range(1,n+1):
    sum=m.pow(2,i)-1
print(f'放到第{i}格时，需要{int(sum)}颗麦子')


n=eval(input())
sum=1
sum1=1
for i in range(2,n+1):
    sum=sum*2
    sum1=sum1+sum
print(f'放到第{n}格时，需要{sum1}颗麦子')

# N钱买N鸡
n=eval(input())
k=0
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if i*5+a*3+b/3==n and i+a+b==n:
                print(f'鸡翁{i}只，鸡母{a}只，鸡雏{b}只')
                k=1
if k ==0:
    print("无解")


sum=0
count=0
n=input().split(',')
r=0
for i in n:
    sum=sum+int(i)
    r+=1
    if int(i)>=60:
        count=count+1
average=sum/r
print(f'courage={average} count={count}')


#稳定的计算程序
try:
    import math as m
    x=int(input())
    a=m.pow((1/x),x)
    print(f'{a:.4f}')
except NameError:
    print("请输入数字")
except:
    print("输入异常")

import math as m
x=int(input())
a=m.pow((1/x),x)
print(f'{a:.4f}')

##个人所得税计算器
salary = float(input())                   # salary 应发工资薪金所得
five_one_insurance_fund = float(input())  # five_one_insurance_fund  五险一金
exemption = float(input())                # exemption 个税免征额
### 计算应缴税款及实发工资 ###
### BEGIN ###
y=0 #应纳税额
income=(salary-five_one_insurance_fund-y)  #实发工资
a=salary-five_one_insurance_fund-exemption
if salary<=0:
    print("error")
elif income<=3000:
    y=income*0.03
elif 3000<income<=12000:
    y=(income*0.1)-210
elif 12000<income<=25000:
    y=(income*0.2)-1410
elif 25000<income<=35000:
    y=(income*0.25)-2660
elif 35000<income<=55000:
    y=(income*0.3)-4410
elif 55000<income<=80000:
    y=(income*0.35)-7160
elif income>80000:
    y=(income*0.45)-15160
print(f'应缴税款{y:.2f},实发工资{income:.2f}')

### END ###

 ##密码修改##
password="123456"
a=input()
b=input()
if a==b:
    print(password)
    print("Overwrite Sucess")
    print(a)
else:
    print(password)
    print("Different Input")
    print(password)
"""

## 宝塔上的琉璃灯 ##
"""
import math as m
total=765
sum=0
for i in range(1,9):
    layer=m.pow(2,i-1)
    sum+=layer
first=total/sum
print(first)    #first=3.0

first=3
print("3")
for i in range(2,9):
    first=first*2
    print(first)

try:
    n = eval(input())

    count = 0
    if isinstance(n, float):
        end
    while n<1:
        # print("ERROR")
        end
    print(int(n), end=' ')
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            # numbers.append(n)
            # print(int(n), end=' ')
        else:
            n = (3 * n) + 1
            # numbers.append(n)
            # print(int(n), end=' ')
        count += 1
        print(int(n), end=' ')
    # print(numbers)
    print("\n", end="")  ##换行输出
    print(count)
except NameError:
    print("ERROR")



# 用户输入部分
N = int(input())

# 声明一个空列表
lst = []

try:
    for i in range(N):
        a = [i for i in input().split()]  # 输入的时间分割形成列表添加到lst中
        lst.append(a)
except:
    pass


# 睡眠函数
def bed_time(times):
    # ******Begin**********
    time1=a[0]
    time2=a[1]
    lst.
    print(time1)



    # ******End***********

print(bed_time(lst))



class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

import math
x=eval(input())
b=0.5 * math.log(x)
ans = int(math.exp(b))
print(b)
print(ans)

# 导入相应的库
# from PyQt5.QtWidgets import QApplication, QMessageBox
# from PyQt5 import uic
# from PyQt5 import QtCore
import os


# 设计stats类，实现BMI统计
# current_path=os.path.dirname(__file__)
class Stats:
    def __init__(self):
        # self.ui = uic.loadUi(current_path+'UI/BMI_stats.ui')
        self.ui = uic.loadUi('UI/BMI_stats.ui')
        # 单击事情处理
        self.ui.button.clicked.connect(self.BMICalc)
        # 从文件中加载UI定义
        # 从UI定义中动态 创建一个相应的窗口对象

    def BMICalc(self):
        weight = eval(self.ui.text_W.text())
        height = eval(self.ui.text_H.text())
        bmi = weight / pow(herght, 2)
        who = ""
        if bmi < 18.5:
            who = "偏瘦"
        elif 18.5 <= bmi < 25:
            who = "正常"
        elif 25 <= bmi < 30:
            who = "偏旁"
        else:
            who = "肥胖"
        QMessageBox.about(self.ui, '结果', f'您的BMI:{bmi:.3f}/您{who}')


# 程序入口
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()

##双分支结构
##判断输入的数是奇数还是偶数
num=int(input('请输入一整数:'))
#条件判断
if num %2==0:
    print()


def listnum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0]+listnum(numList[1:])

print(listnum([1,3,5,7,9]))

"""
"""
import random
#冒泡排序(改进版）
def bubble_sort(li):
    for i in range(len(li)-1):#第i趟
        exchange=False
        for j in range(len(li)-i-1):#第i趟内的第j个数字
            if li[j]>li[j+1]: #如果改成'<'则为降序排列
                li[j],li[j+1]=li[j+1],li[j] #交换数据
                exchange =True
            print(li)
            if not exchange:
                return


# li=[random.randint(0,10000) for i in range(1000)]
li=[8,1,2,3,4,5,6,7]
# print(li)
bubble_sort(li)
# print(li)



#选择排序
def select_sort_simple(li):
    new_list=[]
    for i in range(len(li)):
        # print(i) #说明i是从0开始计数的
        min_val=min(li) #寻找最小值
        new_list.append(min_val)#将li中的最小值添加到新列表中
        li.remove(min_val)#将列表li中的最小值删去
    return new_list
'''
上面的选择排序code不是很好，因为他内存占用率比较高，因为此选择排序新建立了两个列表,空间复杂度较高。
时间复杂度是O(n^2),虽说只有一层for循环，但是min(li)和remove操作的时间复杂度都是O(n)so 时间复杂度是平方
'''
def select_sort(li):
    for i in range(0,len(li)-1): # i:表示第i次循环i=0,1,2,3...
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]: #如果无序列表中第j个数的值小于有序列表中最小的数值则二者交换数据
                min_loc=j #交换位置
        li[i],li[min_loc]=li[min_loc],li[i] #交换数据
        print(li)

li=[3,4,2,1,5,6,8,7,9]
select_sort(li)
# print(li)
"""


































