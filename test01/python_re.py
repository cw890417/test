# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/16

import re

p = re.compile('[a-z]+')
# 从开始匹配
obj = p.match("adf")
print(obj.group())
print(obj.start())
print(obj.end())
print(obj.span())

print('--------------')
# 搜索字符串
obj1 = p.search("!dsfa!")
print(obj1.group())
print(obj1.start())
print(obj1.end())
print(obj1.span())

print('***********')
# 遍历字符串，找到正则表达式匹配的所有位置，并以列表的形式返回
obj2 = p.findall("!dsasaaasd!afa!")
print(obj2)
print('***********')
# 遍历字符串，找到正则表达式匹配的所有位置，并以迭代器的形式返回
obj3 = p.finditer("!dsasaaasd!afa!")
for x in obj3:
    print(x.span())

print('***********')
# 下边例子中，class 只有在出现一个完整的单词 class 时才匹配；如果出现在别的单词中，并不会匹配。
print(re.search(r'\bclass\b', r'lkdj class df'))
print(re.search(r'\bclass\b', r'lkdjclass df'))

print('**********')
p = re.compile(r'(ab)*')
print(p.search("abababa").span())

print('**********')
# 子组的索引值是从左到右进行编号，子组也允许嵌套，因此我们可以通过从左往右来统计左括号 ( 来确定子组的序号。
p = re.compile(r'(a(b)c)d')
m = p.match('abcd')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(2, 1, 2))
print(m.groups())

print('**********')
p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search('(((Lots of punctuation)))')
print(m.group('word'))
print(m.group(0))
print(m.groups())
