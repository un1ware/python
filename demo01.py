
'''
s = "我叫{name},我爱{lover},我师北京徐云的{name}"
print( s.format(name="刘大拿",lover="王晓静"))


#通过下标
s ="我叫{0[0]},我爱{0[1]},我师北京徐云的{0[0]},我还爱{1}"
print(s.format(["刘大拿","刘晓松"],"王晓静"))



print(1100000)
r ="我有{:,}".format(100000)



def digui(n):
    print("$" + str(n))

    if n >0:
        digui(n-1)
    else:
        print("=" * 20)
    print(n)

digui(3)





#统计文件大小
import os

def getdirpath(dirpath):
    total = 0
    allname = os.listdir(dirpath)

    for name in allname:
        fullpath = os.path.join(dirpath,name)
        if os.path.isfile(fullpath):
            total += os.path.getsize(fullpath)
        elif os.path.isdir(fullpath):
            total += getdirpath(fullpath)
    return total

size =getdirpath(r"/Users/mac/PycharmProjects/pythonProject7/")
print(size)

temp = input("输入0-100整数")

if temp.isdigit():
    temp =int(temp)
    if 1<=temp <=100:
        print("ok")
    else:
        print("no")
else:
    print("xxx")



print(int(3.4))


import random

secert = random.randint(1,100) # 生成一个随机数

times =3

while times:
    num = input("请输入数字")
    if num.isdigit():
        tmp =int(num)
        if tmp ==secert:
            print("你猜对了")
            break
        elif tmp < secert:
            print("猜小了!")
            times =times -1
        elif tmp > secert:
            print("猜大了!")
            times = times -1
    else:
        print("请输入数字")




passwd = "adc0123"

times = 3
while times:
    input_passwd = input("请输入密码")

    if '*' in input_passwd:
        print("密码中不能包含*号")
    else:
        if input_passwd == passwd:
            print("密码正确")
        else:
            print("密码正确")
            times -= 1



s1 =" 123 "
s2 = " wangxiaom "
s3 =s1+s2
print(s3)

print(s3[0])
print(s3[1])
print(s3[2])
print(s3[3])
print(s3[4])
print(s3[:5])
print(s3[6:])
print(s3[:])

l = [1,2,3,4,5,6,7,8,9,100]

l1 =l[:6]
print(l1)

l2 =l[:]

print(l2)





s = "i Lone wANGJING"

print(s.capitalize())




s = "1234123"

s1 ="123sw"

print(len(s))
print(len(s1))



s = "asdfasqewsdaasssdafwqe"
print(s.count('s'))


s = "  "
s1 = " a sd "
s3="12345"

print(s.isspace())
print(s1.isspace())
print(s3.isspace())



s ="I 够like dog"
s1 ="I个哦皮ldos"

print(s.isalpha())
print(s1.isalpha())



s="日照香炉生紫烟*疑是银河落九天"
list1 =s.split('*')
print(list1)

s = "今天吃的小炒肉，可好吃了"
table = s.maketrans("小炒肉","大白菜")
print(table)
print(s.translate(table))




a = (1,2,3,)
b = (1,)

print(a)
print(b)


#账号注册
user_pass = {"laotie":"password","huniu":"admin"}

def create_user(username,passwd):

    usernames = user_pass.keys()

    if username in usernames:
        print("被注册了")
    else:
        user_pass[username] =passwd
        print("恭喜你，已经成为了会员")
create_user("goudan","1234")

print(user_pass)


#登录
user_pass = {"laotie":"password","huniu":"admin"}

def login_user(username,passwd):
    usernames =user_pass.keys()

    if username not in usernames:
        print("不是会员")
    elif passwd !=user_pass[username]:
        print("密码错误")
    else:
        print("登录成功过")

login_user("laotie","admin")




list1 = ['a','b','c']

dict1 = {}.fromkeys(list1)
dict2 = {}.fromkeys(list1,3)
print(dict1,dict2)

dict1 = {'a':1,'b':2,'c':3}


在Python中，[]、{}和()有不同的用途：

[]：这是Python中的列表（List）符号。列表是Python中的一种数据结构，可以包含多个元素，这些元素可以是任意类型（数字、字符串、其他列表等）

{}：这是Python中的字典（Dictionary）符号。字典是Python中的一种数据结构，用于存储键值对。字典中的元素通过键来访问，而键可以是任意不可变类型（如字符串、数字、元组等）。




#控制行
for m in range(0,4):
    #控制列
    for n in range(0,5):
        print('*',end = " ")
    print("")
print("="*20)
for m in range(4):
    for n in range(5):
        if m==0 or m==3 or n==0 or n==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")






#打印一个矩形
#控制行
#把print 回车换行 替换为 空格
for i in range(1,5):
     #控制列
     for j in range(1,6):
         print("*",end=" ")
     #当第i行的5列输出完成后，进行换行，
     print()
#分割一下输出
print("="*20)





def digui(num):
    print(num)
    if num>0:
        digui(num-1)
    else:
        print("="*20)
    print(num)

digui(3)



tuplel = (1,2,3,4,5)
tuple2 = {1,2,3,4,5}
tulel3 =  [1,2,3,4,5]

print(tuplel.count(5))
#print(tuple2.count(5))
print(tulel3.count(5))



#清理整个字典
dict1 = {1,2,3,4,5}
dict1.clear()
print(dict1)


dict1 = {1,2,3,4,5}
dict2 =dict1.copy()
print(dict2)



dict1 = {'a':1,'b':2,"c":3,"d":4,"e":5}
print(dict1.get('a'))


dict1 = {'a':1,'b':2,"c":3,"d":4,"e":5}
dict2 =dict1.popitem()
print("dict1" + str(dict1.popitem()))
print("dict2" + str(dict2))

import math
print(1)

import keyword
print(keyword.kwlist)



import math

print(math.fsum([1,2.3,4,5,6]))

print(sum([1,2,4.6,5,6]))


import random

#random 获取0-1之间随机小数
for i in range(10):
    print(random.random())


class Student(object):
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_scores(self):
        return self.scores

zz = Student("周周",18,[80,100,90])
print(zz.get_name())
print(zz.get_age())
print(zz.get_scores())
print(max([100,299,499,500]))

print(min([100,299,499,500]))



class DictClass(object):

    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        if key not in self.dict.keys():
            return "key不存在字典"
        else:
            self.dict.pop(key)
            return "删除成功"

    def get_dict(self, key):
        if key not in self.dict.keys():
            return "not found"
        else:
            return self.dict[key]
    def get_key(self):
        return self.dict.keys()

    def update_dict(self,dict2):
        self.dict = dict(self.dict,**dict2)
        return self.dict.values()

d = DictClass({"a": 1, "b": 2})
print(d.get_dict("a"))
print(d.update_dict({"c":3}))



class ListInfo(object):

    def __init__(self,list_val):
        self.list = list_val

    def add_key(self,key_name):
        #添加的key必须是字符串或者数字
        if isinstance(key_name,(str,int)):
            self.list.append(key_name)
            print(self.list)
            return "OK"
        self.list.append(key_name)
        print(self.list)
        return "ok"

    def get_key(self,index):
        #判断传入的索引是否超过列表
        if index>=0 and index < len(self.list):
            return self.list[index]
        return "你输入的太多了"

    def update_list(self,new_list):
        self.list.extend(new_list)
        return self.list

    def del_key(self):
        #判断列表里面是否还有元素
        if len(self.list) >=0:
            return self.list.pop(-1)
        else:
            return "列表是空的"

list_info = ListInfo([1,2,3,4,5])

print(list_info.add_key(69))
#print(list_info.get_key(3))
#print(list_info.update_list([8,9,10]))
#print(list_info.del_key())




Course_list = []

class School(object):
    def __init__(self,school_name):
        self.school_name = school_name
        self.student_list = []
        self.teachers_list = []

        global Course_list

    def hire(self,obj):
        self.teachers_list.append(obj.name)
        print("我们现在聘请一个新老师{}".format(obj.name))

    def enroll(self,obj):
        self.student_list.append(obj.name)
        print("我们又来一个新学员{}".format(obj.name))

class Grade(School):
    def __init__(self,school_name,grade_code,grade_course):
        super(Grade,self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)

        print("现在我们有了{}".format(self,school_name,self.code,self.course))

    def course_info(self):
        print("课程大纲{}")

Python = Grade("BJ",3,"Python")
Linux = Grade("CD",1,"Linux")

class School_member(object):
    def __init__(self,name,age,sex,role):
        self.name =name
        self.age = age
        self.sex =sex
        self.role = role
        self.course_list=[]

        print("我叫{},我是一个{}".format(self.name,self.role))





class Ticket():
    def __init__(self,weekend=False,child=False):
        self.exp =100
        if weekend:
            self.inc = 1.2
        else:
            self.inc =1

        if child:
            self.discount =0.5
        else:
            self.discount = 1

    def cal_price(self,num):
        return self.exp * self.inc * self.discount * num

adult = Ticket()
child = Ticket (child=True)

print("两个成年人和一个小孩平日价格是{}".format(adult.cal_price(2)+child.cal_price(1)))



import random as r

class Turtle(object):
    def __init__(self):
        self.power = 100

        #初始化乌龟位置
        self.x = r.random(0,10)
        self.y = r.random(0,10)

    def move(self):
        new_x = r.choice([1,2,-1,-2]) + self.x
        new_y = r.choice([1,2,-1,-2]) + self.y

        #判断 乌龟移动速度是否超过边界




import math

class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Line(object):
    def __init__(self,p1,p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()

        self.len = math.sqrt(self.x*self.x + self.y*self.y)

    def get_len(self):
        return self.len

p1 = Point(2,3)
p2 = Point(5,7)
line = Line(p1,p2)
line.get_len()



import random
import math
num = input("请输入一个三位数：")

random_num = random.randrange(100,1000)

#输入函数返回的是字符串，不能与整数相比较，需要类型转换
if num.isdigit() and 100<=int(num) <=999:
    if int(num)>int(random_num):
        print(random_num)
    if int(num) == int(random_num):
        print(random_num)
    if int(num)< int(random_num):
        print(random_num)

else:
    print("请重新输入")



a =5
print(5/10)




for i in range(1,6):
    for k in range(6-i):
        print(" ",end="")
    for j in range(1,i+1):
        if i==1 or i==3 or j==1 or j==i:
             print("*",end=" ")
        else:
            print(" ",end="")
    print()

'''


import random
import tkinter










































