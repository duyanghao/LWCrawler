#-*-coding:utf-8-*-

from lxml.html import soupparser
from lxml import etree
from copy import deepcopy

if __name__ == '__main__':
	root = etree.Element("root")
	print root.tag
	root.append(etree.Element('child1'))
	#etree.SubElement(root, 'child2')
	#etree.SubElement(root, 'child3')
	root.append(etree.Element('child2'))
	root.append(etree.Element('child3'))
	#******etree tostring ******# 	
	print etree.tostring(root, pretty_print=True)

	#******Elements are lists ******#
	#******元素的子进行操作******#
	child1 = root[0]
	print child1.tag
	print len(root)
	for child in root:
		print child.tag
	
	root.insert(0, etree.Element('child0'))	
	child = root[0]
	print child.tag
	
	print etree.iselement('root')

	element = etree.Element('neu')
	element.append(deepcopy(root[1]))
	print element[0].tag	
	
	print ([c.tag for c in root])
	
	if root[0] == root[1].getprevious():
		print "success"
	
	if root[1] == root[0].getnext():
		print root[1].tag, root[0].tag

	#对elment元素中的属性进行操作	
	root = etree.Element('root', interesting = 'totally')
	print etree.tostring(root)

	print root.get("interesting")
	print root.get("hello")
	
	root.set("hello", "HUHU")
	print etree.tostring(root)
	
	print sorted(root.keys())
	for name, value in root.items():
		print '%s=%r' %(name, value)

	attributes = root.attrib
	print attributes['interesting']
	print attributes['hello']
	
	#******Element contain text******#
	#元素中含有文本
	root = etree.Element('root')
	root.text = 'text'
	print root.text

	print etree.tostring(root)

	html = etree.Element('html')
	#html.append(etree.Element('body'))
	#html[0].text = 'text'
	#print etree.tostring(html)	
	body = etree.SubElement(html, 'body')
	body.text = 'text'
	br = etree.SubElement(body, 'br')
	#br.text = 'text'	
	br.tail = 'tail'
	print etree.tostring(html)	
	
	#******xpath 获得文本内容******#
	print html.xpath("string()")
	print html.xpath("//text()")
	
	build_text_list = etree.XPath("//text()")
	print build_text_list(html)
	
	texts = build_text_list(html)
	for text in texts:
		print text.getparent().tag
	
	#****** tree 迭代器 ******#
	root = etree.Element('root')
	etree.SubElement(root, 'child').text = 'child 1'
	etree.SubElement(root, 'child').text = 'child 2'
	etree.SubElement(root, 'another').text = 'child 3'
	print etree.tostring(root, pretty_print = True)	 
	for item in root.iter():
		print '%s-%s' %(item.tag, item.text)

	for item in root.iter('child'):
		print '%s-%s' %(item.tag, item.text)
	
			



	pass
