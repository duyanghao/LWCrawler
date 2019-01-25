import tempfile
import os

filename = "./tmp/tmp_%s.txt" % (os.getpid())
temp = open(filename, 'w+b')
try:
	print "temp:", temp
	print "temp.name:", temp.name
finally:
	temp.close()
	os.remove(filename)

print 
print "TemporaryFile:"
temp = tempfile.TemporaryFile()

try:
	print "temp:", temp
	print "temp.name:", temp.name
finally:
	temp.close()

#temp file
temp = tempfile.TemporaryFile()
try:
	temp.write("Some data")
	temp.seek(0)
	
	print temp.read()
finally:
	temp.close()

#temp dir
directory_name = tempfile.mkdtemp()
print directory_name
os.removedirs(directory_name)

if not os.path.isdir("./tmp/name"):
	os.makedirs("./tmp/name")

if not os.path.isdir("./tmp/name"):
	raise Exception("./tmp/name" + " dir does not exist" + "you need to set this for image")

level, path = tempfile.mkstemp(dir="./tmp/name/")
print level
print path
