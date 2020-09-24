# 循环与注释
# 2020/9/14

# a=9
# def fun1():
#     global b
#     b=5
#     return b**2
# fun1()
# print(b)

#打印1到10
i=1
while i <=10:
    if i==10:
        print(i)
    else:
        print(i,end=',')
    i+=1

for i in range(1,11,3):
        print(i)

list1=['关于','赵云','machao','huangzhong']
print(len(list1))
for i in range(0,len(list1)):
    print(list1[i])

