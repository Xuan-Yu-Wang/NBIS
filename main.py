#!/usr/bin/env python3  #告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-  #告诉Python解释器，按照UTF-8编码读取源代码

from Functions import CusService
import numpy as np

#IO测试
name = input('Please enter your name:')
print('Welcome!', name)
num1 = int(input('Please enter your account:'))
num2 = int(input('Please enter your passport:')) #input函数传递为字符串数据，因此可使用int()等转化格式，其格式为class int(x, base=10)
#字符串输出测试
print('Account:', num1, '\n''Passport:', num2, '\n') #输出单行换行利用'\n'，注意函数结束后自动换行，因此如果print函数最后还包含\n就会加换一行
print('''Welcome to BANK LIMTED Co Ltd.
Please wait for a minute
Processing...''') 
print(r'''Welcome to BANK LIMTED Co Ltd.
Please wait for a minute
Processing...''') #输出多行换行格式直接为print('''  ''')或print(r'''  '''),中间各元素前无需省略号作为提示符，直接换行就可以
#字符串格式化及算数运算符测试
org_amount = 2000
year = 3
print('Hi! %s, \nDeposite is: $%.2f, per year growth is: $%.2f.' % (name, float(org_amount**year), float(org_amount/year)))
print(org_amount//year) #取模 - 返回除法的余数
print(org_amount%year) #取整除 - 返回商的整数
#list测试
account = []
account.append(name)
account.append(int(org_amount/year))
account.insert(1, int(org_amount**year))
print('Hi! %s, \nDeposite is: $%d, per year growth is: $%d.' % (account[0], account[1], account[2]))

"""
if __name__=='__main__': 
    #if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    #补充说明：当运行此程序时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方作为模块导入此文件时，不再是main，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
    test()
"""