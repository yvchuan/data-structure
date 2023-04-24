"""
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
"""



"""
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


"""
#插入排序
def insert_sort(li):
    for i in range(1,len(li)): #摸到牌的下标
        tem=li[i] #将遍历过的线性表li储存起来，防止被覆盖
        j=i-1 #手里的牌的下标
        while li[j]>tem and j>= 0:#手里的牌比摸到牌大，并且手里始终有牌
            li[j+1]=li[j] #将手中的牌的下表往前移动一个位置
            j-=1
        li[j+1]=tem #将之前遍历过的且已经有序的表与新的数值连接在一起
        print(f'step:{i}',end='')
        print(li)

li=[3,2,4,1,5,7,9,6,8]
print(li)
insert_sort(li)
print(li)
"""


