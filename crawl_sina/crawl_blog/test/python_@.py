#-*-coding:utf-8-*-

#def f1(arg):
#	print 'f1'
#	r1 = arg()
#	print 'r1 = %s' % r1
#	return r1 + 'f1'
#
##f2 = f1(f2())
#@f1
#def f2(arg='123'):
#	print 'f2'
#	return arg + 'f2r'
#
#print 'start'
#print f2
#
##print f2('1')

class Decorator(object):
	def __init__(self, f):
		print 'inside Decorator.__init__()'
		self.f = f

	def __call__(self):
		print 'inside Decorator.__call__()'
		self.f()

@Decorator
def a_function():
	print 'inside a_function()'

print 'Finished decorator a_function()'

a_function()


