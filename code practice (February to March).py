# # 欢迎你
# name = input("")
# print('欢迎你,', name, sep='')
# print('欢迎你,', name, sep='')
# print('欢迎你' + ',' + name, sep='')
# print(f'欢迎你,{name}')
# print('欢迎你,%s' % (name))

# Python初体验 之 基础语法 four
# a = int(input())
# b = int(input())
# print("%d + %d = %d" % (a, b, a + b))
# print("%d - %d = %d" % (a, b, a - b))
# print("%d * %d = %d" % (a, b, a * b))
# print("%d / %d = %f" % (a, b, a / b))
# print("%d // %d = %d" % (a, b, a // b))
# print("{} % {} = {}".format(a, b, a % b))
# print("%d ** %d = %d" % (a, b, a ** b))

# Python初体验 之 Hello World  second
# name = input("请输入一个人的名字：")
# country = input("请输入一个国家的名字：")
# print("世界那么大，{}想去{}看看。".format(name, country))

# 欢迎你
# temp=input()
# temp=temp.replace(" ","")
# temp1=eval(temp)
# print("{}={:.2f}".format(temp,temp1))

# 数值运算
# temp = input()
# temp1 = eval(temp)
# print("{}={:.2f}".format(temp, temp1))

# 九九乘法表输出
# for a in range(1, 10):
#     for b in range(1, a + 1):
#         print("{0}*{1}={2:<2d}".format(b, a, b * a), end=" ")
#     print()

# 等腰三角形输出
# for i in range(5):
#     for j in range(0, 5 - i):
#         print(' ', end="")
#     for k in range(0, 2 * i + 1):
#         print('*', end='')
#     print()

# s = input()
# a = "*"
# sum = 2 * eval(s) + 1
# for i in range(1, eval(s) + 1):
#     print("{:^{}}".format(a * ((2 * i) - 1), sum))
'''
import turtle as t

t.setup(300, 300)
t.goto(100, 100)
t.goto(100, -100)
t.goto(-100, -100)
t.goto(-100, 100)
t.goto(0, 0)
t.done()
'''

'''
import turtle as t
t.left(135)
t.fd(45)
t.right(90)
t.fd(90)
t.done()

'''

'''
# 画一个边长为n的五边形
n = int(input())
import turtle as t
t.pencolor("blue")
t.fd(n)
t.right(60)
t.fd(n)
t.right(60)
t.fd(n)
t.right(60)
t.fd(n)
t.right(60)
t.fd(n)
t.right(60)
t.fd(n)
t.done()
'''

'''
#画一个边长为n的三角形
n = int(input())
import turtle as t
t.pencolor("blue")
t.right(120)
t.fd(n)
t.right(120)
t.fd(n)
t.right(120)
t.fd(n)
t.done()
'''
'''
#画一个绿色的圆
import turtle as t
t.pencolor("green")
t.width(3)
t.circle(80, 360)
t.done()

'''



#画一个钢琴键
import turtle as t

t.setup(500, 300)
t.speed(9)
t.penup()
t.goto(-180, -50)
t.pendown()


def Drawrect():
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(120)
    t.penup()
    t.left(90)
    t.fd(42)
    t.pendown()


for i in range(7):
    Drawrect()
t.penup()
t.goto(-150, 0)
t.pendown()


def DrawRectBlack():
    t.color('black')
    t.begin_fill()
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.left(90)
    t.fd(30)
    t.left(90)
    t.fd(70)
    t.end_fill()
    t.penup()
    t.left(90)
    t.fd(40)
    t.pendown()


DrawRectBlack()
DrawRectBlack()
t.penup()
t.fd(48)
t.pendown()
DrawRectBlack()
DrawRectBlack()
DrawRectBlack()
t.hideturtle()
t.done()




