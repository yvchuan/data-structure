"""
import turtle
turtle.color('red', 'red')
turtle.pensize(2)
turtle.pendown()
turtle.setheading(150)
turtle.begin_fill()
turtle.fd(50)
turtle.circle(50 * -3.745, 45)
turtle.circle(50 * -1.431, 165)
turtle.left(120)
turtle.circle(50 * -1.431, 165)
turtle.circle(50 * -3.745, 45)
turtle.fd(50)
turtle.end_fill()
turtle.done

"""

"""
#奥运五环绘制
import turtle as t
radius = int(input())
ra1=radius/2
t.setup(1000.800)
t.width(5)
t.speed(5)

# 绘制一个半径为radius，颜色为“红色”的圆
t.color("red")
t.circle(radius)
t.penup()
t.goto(2 * radius + 20, 0)
t.pendown()
#绘制一个半径为radius，颜色为“蓝色”的圆
t.color("blue")
t.circle(radius)
t.penup()
t.goto(4*radius+40,0)
t.pendown()
#绘制一个半径为radius,颜色为“绿色”的圆
t.color("green")
t.circle(radius)
t.penup()
t.goto(radius+5, -50)
t.pendown()
#黄色
t.color("yellow")
t.circle(radius)
t.penup()
t.goto(radius*3+30,-50)
t.pendown()

t.color("black")
t.circle(radius)
t.done()
"""

'''
#贪吃蛇（just一条snake）
import turtle as t

t.Screen().setup(650, 350, 200, 200)
t.tracer(False)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("purple")
t.seth(-40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80 / 2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2 / 3)
t.hideturtle()
t.dot(10, "red")
t.write("PYTHON")
t.done()
'''

'''
#太极图
import turtle as t
t.setup(1000,800,10,20)
t.width(2)
t.fillcolor("white")
t.begin_fill()
t.circle(-180, -180)
t.circle(-90, 180)
t.circle(90, 180)
t.end_fill()
#(给太极图填充白色)
t.penup()
t.left(90)
t.fd(90)
t.pendown()
t.dot(45, "black")

t.penup()
t.right(180)
t.fd(90)
t.pendown()
t.right(90)
t.fillcolor("black")
t.begin_fill()
t.circle(-90,180)
t.circle(90,180)
t.circle(180,180)
t.end_fill()
t.circle(180,-180)

t.penup()
t.left(90)
t.fd(90)
t.pendown()
t.dot(45,"white")
t.penup()
t.fd(60)
t.pendown()
t.done()
'''
'''
# 钢琴键
import turtle as t

t.setup(1000, 500)
t.speed(10)


for i in range(7):
    t.fillcolor('white')
    t.begin_fill()
    t.fd(40)
    t.left(90)
    t.fd(200)
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(200)
    t.left(90)
    t.fd(42)
    t.end_fill()
# 创立钢琴四个白色色阶
t.right(180)
t.fd(168)
t.right(90)
t.fd(200)
t.right(90)
t.fd(20)

for i in range(3):
    t.fillcolor("black")
    t.begin_fill()
    t.fd(35)
    t.right(90)
    t.fd(93)
    t.right(90)
    t.fd(35)
    t.right(90)
    t.fd(93)
    t.right(90)
    t.fd(40)
    t.end_fill()
t.done()

'''

'''
#网上的皮卡丘代码
import turtle


def getPosition(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)


class Pikachu:

    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(3)
        t.speed(9)
        t.ondrag(getPosition)

    def noTrace_goto(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def leftEye(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.noTrace_goto(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.noTrace_goto(x + 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def rightEye(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.noTrace_goto(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.noTrace_goto(x - 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mouth(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t

        t.fillcolor('#88141D')
        t.begin_fill()

        # Lower Lip
        l1 = []
        l2 = []
        t.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.right(3)
            t.fd(a)
            l1.append(t.position())

        self.noTrace_goto(x, y)

        t.seth(10)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.left(3)
            t.fd(a)
            l2.append(t.position())

        # Upper Lip
        t.seth(10)
        t.circle(50, 15)
        t.left(180)
        t.circle(-50, 15)

        t.circle(-50, 40)
        t.seth(233)
        t.circle(-50, 55)
        t.left(180)
        t.circle(50, 12.1)
        t.end_fill()

        # Tongue
        self.noTrace_goto(17, 54)
        t.fillcolor('#DD716F')
        t.begin_fill()
        t.seth(145)
        t.circle(40, 86)
        t.penup()
        for pos in reversed(l1[:20]):
            t.goto(pos[0], pos[1] + 1.5)
        for pos in l2[:20]:
            t.goto(pos[0], pos[1] + 1.5)
        t.pendown()
        t.end_fill()

        # Nose
        self.noTrace_goto(-17, 94)
        t.seth(8)
        t.fd(4)
        t.back(8)

    # Red Cheeks
    def leftCheek(self, x, y):
        turtle.tracer(False)
        t = self.t
        self.noTrace_goto(x, y)
        t.seth(300)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def rightCheek(self, x, y):
        t = self.t
        turtle.tracer(False)
        self.noTrace_goto(x, y)
        t.seth(60)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def colorLeftEar(self, x, y):
        t = self.t
        self.noTrace_goto(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(330)
        t.circle(100, 35)
        t.seth(219)
        t.circle(-300, 19)
        t.seth(110)
        t.circle(-30, 50)
        t.circle(-300, 10)
        t.end_fill()

    def colorRightEar(self, x, y):
        t = self.t
        self.noTrace_goto(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(300)
        t.circle(-100, 30)
        t.seth(35)
        t.circle(300, 15)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 17)
        t.end_fill()

    def body(self):
        t = self.t

        t.fillcolor('#F6D02F')
        t.begin_fill()
        # Right face contour
        t.penup()
        t.circle(130, 40)
        t.pendown()
        t.circle(100, 105)
        t.left(180)
        t.circle(-100, 5)

        # Right ear
        t.seth(20)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 36)

        # Upper profile
        t.seth(150)
        t.circle(150, 70)

        # Left ear
        t.seth(200)
        t.circle(300, 40)
        t.circle(30, 50)
        t.seth(20)
        t.circle(300, 35)
        #print(t.pos())

        # Left face contour
        t.seth(240)
        t.circle(105, 95)
        t.left(180)
        t.circle(-105, 5)

        # Left hand
        t.seth(210)
        t.circle(500, 18)
        t.seth(200)
        t.fd(10)
        t.seth(280)
        t.fd(7)
        t.seth(210)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(220)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(240)
        t.fd(12)
        t.seth(0)
        t.fd(13)
        t.seth(240)
        t.circle(10, 70)
        t.seth(10)
        t.circle(10, 70)
        t.seth(10)
        t.circle(300, 18)

        t.seth(75)
        t.circle(500, 8)
        t.left(180)
        t.circle(-500, 15)
        t.seth(250)
        t.circle(100, 65)

        # Left foot
        t.seth(320)
        t.circle(100, 5)
        t.left(180)
        t.circle(-100, 5)
        t.seth(220)
        t.circle(200, 20)
        t.circle(20, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(300)
        t.circle(10, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(10)
        t.circle(100, 60)

        # Horizontal
        t.seth(180)
        t.circle(-100, 10)
        t.left(180)
        t.circle(100, 10)
        t.seth(5)
        t.circle(100, 10)
        t.circle(-100, 40)
        t.circle(100, 35)
        t.left(180)
        t.circle(-100, 10)

        # Right foot
        t.seth(290)
        t.circle(100, 55)
        t.circle(10, 50)

        t.seth(120)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(0)
        t.circle(10, 50)

        t.seth(110)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(30)
        t.circle(20, 50)

        t.seth(100)
        t.circle(100, 40)

        # Right body contour
        t.seth(200)
        t.circle(-100, 5)
        t.left(180)
        t.circle(100, 5)
        t.left(30)
        t.circle(100, 75)
        t.right(15)
        t.circle(-300, 21)
        t.left(180)
        t.circle(300, 3)

        # Right hand
        t.seth(43)
        t.circle(200, 60)

        t.right(10)
        t.fd(10)

        t.circle(5, 160)
        t.seth(90)
        t.circle(5, 160)
        t.seth(90)

        t.fd(10)
        t.seth(90)
        t.circle(5, 180)
        t.fd(10)

        t.left(180)
        t.left(20)
        t.fd(10)
        t.circle(5, 170)
        t.fd(10)
        t.seth(240)
        t.circle(50, 30)

        t.end_fill()
        self.noTrace_goto(130, 125)
        t.seth(-20)
        t.fd(5)
        t.circle(-5, 160)
        t.fd(5)

        # Fingers
        self.noTrace_goto(166, 130)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)

        # Tail
        self.noTrace_goto(168, 134)
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(40)
        t.fd(200)
        t.seth(-80)
        t.fd(150)
        t.seth(210)
        t.fd(150)
        t.left(90)
        t.fd(100)
        t.right(95)
        t.fd(100)
        t.left(110)
        t.fd(70)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)

        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        #print(t.pos())
        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(70)
        t.right(100)
        t.fd(80)
        t.left(100)
        t.fd(46)
        t.seth(66)
        t.circle(200, 38)
        t.right(10)
        t.fd(10)
        t.end_fill()

        # Tail Pattern
        t.fillcolor('#923E24')
        self.noTrace_goto(126.82, -156.84)
        t.begin_fill()

        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(40)
        t.pencolor('#923e24')
        t.seth(-30)
        t.fd(30)
        t.left(140)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(150)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(130)
        t.fd(18)
        t.pencolor('#000000')
        t.seth(-45)
        t.fd(67)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)
        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        t.end_fill()

        # Hat, Eye, Mouth, Cheek
        self.cap(-134.07, 147.81)
        self.mouth(-5, 25)
        self.leftCheek(-126, 32)
        self.rightCheek(107, 63)
        self.colorLeftEar(-250, 100)
        self.colorRightEar(140, 270)
        self.leftEye(-85, 90)
        self.rightEye(50, 110)
        t.hideturtle()

    def cap(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.fillcolor('#CD0000')
        t.begin_fill()
        t.seth(200)
        t.circle(400, 7)
        t.left(180)
        t.circle(-400, 30)
        t.circle(30, 60)
        t.fd(50)
        t.circle(30, 45)
        t.fd(60)
        t.left(5)
        t.circle(30, 70)
        t.right(20)
        t.circle(200, 70)
        t.circle(30, 60)
        t.fd(70)
        #print(t.pos())
        t.right(35)
        t.fd(50)
        t.circle(8, 100)
        t.end_fill()
        self.noTrace_goto(-168.47, 185.52)
        t.seth(36)
        t.circle(-270, 54)
        t.left(180)
        t.circle(270, 27)
        t.circle(-80, 98)

        t.fillcolor('#444444')
        t.begin_fill()
        t.left(180)
        t.circle(80, 197)
        t.left(58)
        t.circle(200, 45)
        t.end_fill()

        self.noTrace_goto(-58, 270)
        t.pencolor('#228B22')
        t.dot(35)

        self.noTrace_goto(-30, 280)
        t.fillcolor('#228B22')
        t.begin_fill()
        t.seth(100)
        t.circle(30, 180)
        t.seth(190)
        t.fd(15)
        t.seth(100)
        t.circle(-45, 180)
        t.right(90)
        t.fd(15)
        t.end_fill()
        t.pencolor('#000000')

    def start(self):
        self.body()


def main():
    print('Painting the Pikachu... ')
    wn = turtle.Screen()
    wn.setup(width=600, height=800)
    pikachu = Pikachu()
    pikachu.start()
    turtle.mainloop()


if __name__ == '__main__':
    main()


'''
"""
#三角形周长及面积
import math
z=input()
a=eval(z.split(' ')[0])
b=eval(z.split(" ")[1])
c=eval(z.split(' ')[2])
d=a+b+c
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'周长={d:.2f}')
print("面积={:.2f}".format(area))

##身份证号基本信息
a=input()
year=a[6:10]
month=a[10:12]
day=a[12:14]
sex=eval(a[16])
if sex%2==0:
    print("出生：{}年{}月{}日".format(year,month,day))
    print(f'性别：女')
else:
    print("出生：{}年{}月{}日".format(year,month,day))
    print(f'性别：男')




#复读机相加（mathod two)
import math
a=int(input())#输入的数
n=int(input())#加几次的数字
ans=0
b=a
for i in range(1,n+1):
    ans=ans+a
    a=a*10+b
    #应该做到每一次循环结束便是得到第一个数字的值

print("结果是：{}".format(ans))


##复读机相加(mathod one)
import math

a = int(input())#被加数字
n = int(input())#加几次的数字
b = 0
i = n
sum = 0
ans=0
while i > 0:
    b=2*(math.pow(10,i-1))
    i=i-1
    sum = sum + b
while sum>0:
    ans+=sum
    sum = int(sum / 10)

ans=ans+sum
print("结果是{}".format(ans))
print(ans)

#温度转换
a=input()
if a[-1] in ['F','f']:
    C=(eval(a[0:-1])-32)/1.8
    # C=eval((a[0,-1]-32)/1.8)
    print(f'{C:.2f}C')
elif a[-1] in ['C','c']:
    F=(eval(a[0:-1])*1.8)+32
    # F=eval((a[0,-1]*1.8)+32)
    print("{:.2f}F".format(F))
else :
    print("输入格式错误")

#温度转换 II
a=input()
if a[0] in ['C']:
    F=(eval(a[1:])*1.8)+32
    print(f'F{F:.2f}')
elif a[0] in ['F']:
    C=(eval(a[1:])-32)/1.8
    print("C{:.2f}".format(C))


#数字形式转换 1
template="零一二三四五六七八九"
a=input()
for i in a:
    print(template[eval(i)],end="")


#货币转换 I
money=input()
if money[0:3] =="RMB":
    USD=eval(money[3:])/6.78
    print(f'USD{USD:.2f}')
elif money[0:3]=="USD":
    RMB=6.78*eval(money[3:])
    print("RMB{:.2f}".format(RMB))

str1 = "hello world"     # 空格也算一个字符
print(str1.find("o"))
print(str1.count("h"))
print(str1.count("l", 2, 9))
"""
"""
#学习-python字符串常用操作之一
str1 = "hello world"     # 空格也算一个字符
print(str1.find("w"))
print(str1.find("wo"))
print(str1.find("l", 4, 10))
print(str1.find("e", 3))

print(str1.rfind("l"))
print(str1.rfind("l", 4, 10))
print(str1.rfind("e", 3))

print(str1.index("l",4,10))
print(str1.count("l"))

#绘制蟒蛇
import  turtle as t
#建一个宽为650，高为350的窗口，同时窗口左侧与左屏幕的像素距离为200，窗口顶部与屏幕顶部的距离为210的像素距离
t.setup(650,350,200,210)
#抬起笔
t.penup()
#将画笔向后移动250的像素距离
t.fd(-250)
#落笔
t.pendown()
#设置画笔尺寸为20
t.pensize(20)
#设置画笔颜色为“紫色”
t.pencolor("purple")
#将小海龟方向顺时针旋转40°
t.seth(-40)
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)
t.done()

IP地址转换
ip=input()
if len(ip)==32:
    print(int(ip[0:8],2),end='.')
    print(int(ip[8:16],2),end='.')
    print(int(ip[16:24],2),end='.')
    print(int(ip[24:32],2),end='')
else:
    print("data error")
    
#换披萨
import math
m=int(input())
n=int(input())
cm_m=float(2.54*m)
cm_n=float(2.54*n)
s_m=math.pi*math.pow(cm_m/2,2)
s_n=math.pi*math.pow(cm_n/2,2)
numbers=int(s_m/s_m)
if s_m%s_n==0:
    print(numbers)
else:
    print(numbers+1)
    

# 高空落球
# import math
h = 50.0
t = 100
for i in range(1, 11):
    print("第{}次反弹的高度为{}米".format(i, h))
    t = t + h * 2.0
    # t=100*(1-math.pow((1/2),i))+100
    h = h / 2
print(f'第10次落地共经过{t-(0.09765625*2)}米')


a,b = eval(input())
x = (-b+math.sqrt(2 * a * math.sin(math.pi / 3)*math.cos(math.pi / 3)))/(2 * a)  #sin()函数的参数以弧度为单位
print(x)


"""


import turtle as t
t.setup(900,900,200,200)
t.pensize(4)
t.penup()
t.goto(-50,-100)
t.pendown()
for i in range(9):
    t.fd(100)
    t.right(80)

t.done()