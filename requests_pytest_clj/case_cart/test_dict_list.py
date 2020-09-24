# def partition(arr,low,high):
#     i = ( low-1 )         # 最小元素索引
#     pivot = arr[high]
#
#     for j in range(low , high):
#
#         # 当前元素小于或等于 pivot
#         if   arr[j] <= pivot:
#
#             i = i+1
#             arr[i],arr[j] = arr[j],arr[i]
#
#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return ( i+1 )
#
#
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
#
# # 快速排序函数
# def quickSort(arr,low,high):
#     if low < high:
#
#         pi = partition(arr,low,high)
#
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)
#
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# print(n)
# quickSort(arr,0,n-1)
# print ("排序后的数组:")
# for i in range(n):
#     print ("%d" %arr[i])


# lst = [10, 11, 12, 13, 14, 15]
# str='Runoob'
# bb = reversed(lst)#不改变原序列
# print(list(bb),lst)
# aa =lst.reverse()
# print(aa,lst)
#print(''.join(reversed(str)))

# s_list = ["bbb","ccc","bac","a","ba"]
# s_list.sort(key=len) # key=len 指定排序规则按长度排序
# print(s_list)
# student = [{"name": "小C", "age": 12, "score": 90},
#            {"name": "小D", "age": 13, "score": 84},
#            {"name": "小A", "age": 14, "score": 85},
#            {"name": "小E", "age": 15, "score": 89},
#            {"name": "小F", "age": 12, "score": 88}]
# student.sort(key=lambda a: a["age"])
# # 此方法是对list的元素进行排序,每一个元素是一个字典,按字典中的age进行排序,但不能直接对字典进行排序,sort的操作对象只能是list
# print(student)
# a = { "b": 5, "c": 2,"a": 4, "d": 1}
# #对字典按值（value）进行排序（默认由小到大）
# test_2=sorted(a.items(),key=lambda x:x[1])
# #输出结果
# print(test_2)


# s_tuples = [('john', 'A', 15),
#                   ('jane', 'B', 12),
#                   ('dave', 'B', 10)]
# new_tuples = sorted(s_tuples , key=lambda student: student[2])
# # student[2]表示按照列表中的元组中的第三个元素的大小进行排序
# print(s_tuples )
# print(new_tuples)

# 计算出以下字符串，每个字符出现的次数
# a = "hello,world!"
# print('a=',a)
#
# #办法1
# print ("统计a中各项的个数，办法1（字典）：")
# dicta = {}
# for i in a:
#     dicta[i] = a.count(i)
# print (dicta)
#
#
# # 办法2
# print ("统计a中各项的个数，办法2（collections的counter）：")
# from collections import Counter
# print(Counter(a))
#
#
# # 办法3
# print ("统计a中各项的个数，办法3（count方法）：")
# for i in a:
#     print("%s:%d" %(i,a.count(i)))    #用count方法计算各项数量，简单打印出来而已
#
# # 办法4（结果同3）
# print ("统计a中各项的个数，办法4（列表count方法）：")
# lista = list(a)                           #字符串转为列表
# print ('lista:',lista)
# for i in lista:
#     print("%s:%d" %(i,lista.count(i)))    #用列表的count方法计算各项数量


# #列表转字符串：将列表中的内容拼接成一个字符串
# l = ['a','b','c']
# a = ''.join(l)
# print(type(a),a)
#列表准字符串：将列表中的值转成字符串
# l = ['a',1,'b',2]
# aa = [str(i) for i in l]
# print(type(aa),aa)
#字符串转列表：eval转换
#s = "['a','b','c']"
# eval(s)
# print(s)
#将字符串每个字符转成列表中的值
# s = 'abc'
# print(list(s))
#将字符串按分割成列表
# s = 'a,b,c'
# print(s.split(','))
#列表与字典转换:将2个列表转成字典:
## zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
# l = ['a','b','c']
# t = [1,2,3]
# a = list(zip(l,t))
# print(a)
#将嵌套列表转为字典
# l = [['a',1],['b',2],['c',3]]
# a = dict(l)
# print(a)
#字典转列表：
# a = {'a':1,'b':2}
# b = list(a.items())
# print(b)
# c = list(a.keys())
# print(c)
# d = list(a.values())
# print(d)
#字符串转字典：
# a = "{'d':1,'b':2}"
# aa = eval(a)
# print(aa)
#字符串转字典：
import json
# a = '{"d":1,"b":2}'
# #aa = json.loads(a)
# aa = eval(a)
# print(aa)
#字典转字符串
# d = {'a':1,'b':2}
# dd = json.dumps(d)
# print(dd,type(dd))
d = {'a':1,'b':2}
dd = str(d)
print(dd,type(dd))





