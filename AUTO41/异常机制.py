# 异常机制
# 2020/9/14
try:
    a=int(input('输入一个数字'))
    print(1/a)
except ValueError:
    print('您输入的不是数字')
except ZeroDivisionError:
    print('0不能作为分母')
except:
    print('程序出现未知错误')