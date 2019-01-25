#-*-coding:utf-8-*-
import re

#[] 
# 元字符在其中不起作用
# . ^ $ * + ? {} [] \ | ()
# ^ $ 行首和行尾
# . 字符
# * + ? {} 重复次数
# \ 转义
# () 组
# | 或
# 
src = r'abc'
print re.findall(src, 'aabcaaabcaa')

st = 'top tip tmp tap tzp'
print re.findall(r'top', st)
print re.findall(r't[io]p', st)

# ^ in the begin [] function
print re.findall(r't[i^o]p', st)

s = 'hello world, hello boy'
print re.findall(r'^hello', s)

print re.findall(r'[-^]?abc', '^abc abc ^^abc')

#\d == [0-9]
#\D == [^0-9]
print re.findall(r'\d', '12345ad')
print re.findall(r'\D', '12345ad')

#\s == [\t\n\r\f\v]
#\S == [\t\n\r\f\v]
#匹配任何空白或者非空白字符
#


#\w == [a-zA-Z0-9_]
#\W == [^a-zA-Z0-9_]


r1 = '\d{3,4}-?\d{8}'
p_tel = re.compile(r1)
print p_tel	
print p_tel.findall("010-00000000")


csvt_re = re.compile(r'csvt', re.I)
print csvt_re.findall('CSVT')

# 字符串前加r 反斜杠就不会被任何特殊方式处理
# r'' function
print "r'regex pattern' ..." 
print re.findall('\\\\msection', '\\\\msection, \sectiona')
print re.findall(r'\\\\msection', '\\\\msection, \sectiona')

# match 在开头匹配, 决定在字符串刚开始的位置匹配
# return MatchObj
print 'match funciton...'
print csvt_re.match('csvt hello')
print csvt_re.match('hello csvt')

# search 扫描字符串，找到这个RE匹配的位置
# print csvt_re.search('csvt hello')
# return MatchObj
x =  csvt_re.search('hello csvt Csvt')
print "search function..."
print x.group()
print x.start()
print x.end()
print x.span()
print csvt_re.search('csvt hello')

# findall 
print 'findall function...'
print csvt_re.findall("hello csvt Csvt")

#re split
print 'split function...'
s  = '123+456-678'

print re.split(r'[-+*]', s)


