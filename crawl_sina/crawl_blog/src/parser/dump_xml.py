#-*-coding:utf-8-*-
import lxml.html
import sys
from lxml import etree
reload(sys)
sys.setdefaultencoding('utf-8')

class DumpXml(object):
	
	@classmethod
	def drop_tag(self, nodes):
		if isinstance(nodes, list):
			for node in nodes:
				node.drop.tag()
		else:
			nodes.drop_tag()

	@classmethod
	def fromstring(self, html):
		self.doc = lxml.html.fromstring(html)
		return self.doc
	
	@classmethod
	def node_to_string(self, node, encode='utf-8', pretty_format=True):
		return etree.tostring(node, encoding=encode, pretty_print=pretty_format)
	
	@classmethod
	def replace_tag(self, node, tag):
		node.tag = tag	
		
	# delete all element with the provided tag names
	# merge the text and tail and children element to into its parent
	# ******there some fault in this funtion when debug ******
	@classmethod
	def strip_tags(self, node, *tags):
		etree.strip_tags(node, *tags)

	@classmethod
	def get_element_by_id(self, node, id):
		selector = '//*[@id="%s"]' %id
		elems = node.xpath(selector)
		if elems:
			return elems[0]
		return None

	@classmethod
	def append_child(self, node, child):
		node.append(child)

	@classmethod
	def child_nodes(self, node):
		return list(node)
	
	# ******this function is not debug ******
	@classmethod
	def child_nodes_with_text(self, node):
		root = node
		if root.text:
			t = lxml.html.HtmlElement()
			t.text = root.text
			t.tag = 'text'
			root.text = None
			root.insert(0, t)
		#loop child
		for c, n in enumerate(list(root)):
			idx = root.index(n)
			#do not process texts nodes
			if n.tag == 'text':
				continue
			#create a text node for tail
			if n.tail:
				t = self,create_element(tag='text', text=n.tail, tail=None)
				root.insert(idx + 1, t)

		return list(root)
			
	@classmethod
	def get_children(self, node):
		return node.getchildren()

	@classmethod
	def get_element_by_tags(self, node, tags):
		pass

	@classmethod
	def create_element(self, tag='P', text=None, tail=None):
		t = lxml.html.HtmlElement()
		t.tag = tag
		t.text = text
		t.tail = tail
		return t

	@classmethod
	def get_parent(self, node):
		return node.getparent()

	@classmethod
	def remove(self, node):
		parent = node.getparent()
		if parent is not None:
			if node.tail:
				prev = node.getprevious()
				if prev is None:
					if not parent.text:
						parent.text = ''
					parent.text += u' ' + node.tail
				else:
					if not prev.tail:
						prev.tail = ''
					prev.tail += u' ' + node.tail

			node.clear()
			parent.remove(node)

	@classmethod
	def get_tag(self, node):
		return node.tag

	@classmethod
	def get_text(self, node):
		return node.text 		
	
	#node attribute operation
	@classmethod
	def get_attribute(self, node, attr=None):
		if attr:
			return node.attrib.get(attr, None)
		return attr		

	@classmethod
	def del_attribute(self, node, attr=None):
		if attr:
			ret_attr = node.attrib.get(attr, None)
			if ret_attr:
				del node.attrib[attr]

	@classmethod
	def set_attribute(self, node, attr=None, value=None):
		if attr and value:
			node.set(attr, value)



if __name__ == '__main__':
	#html = '<root><data id="1"><topic></topic><subtitle><subtitle><readcnt></readcnt></data></root>'
	#doc = DumpXml.fromstring(html)	
	#print type(doc)
	#print DumpXml.node_to_string(doc)
	#node1 =  DumpXml.get_element_by_id(doc, '1')
	#print DumpXml.node_to_string(node1)
	#for item in doc.getchildren():
	#	print DumpXml.node_to_string(item)
	root_node = DumpXml.create_element(tag='root')
	print DumpXml.node_to_string(root_node)	
	data_node = DumpXml.create_element(tag='data', text=u'#明星#')
	content_node = DumpXml.create_element(tag='content', text=u'我是中国人')
	DumpXml.set_attribute(data_node, 'id', '1')
	DumpXml.append_child(root_node, data_node)
	DumpXml.append_child(root_node, content_node)
	
	#DumpXml.del_attribute(data_node, 'id')
	#print DumpXml.get_attribute(data_node, 'name')
	#print DumpXml.get_text(data_node)
	#DumpXml.drop_tag(data_node)
	print DumpXml.node_to_string(root_node)
	#DumpXml.strip_tags(root_node, 'content', 'data')	
	#DumpXml.replace_tag(data_node, 'topic')
	node_id_1 = DumpXml.get_element_by_id(root_node, '1')
	print node_id_1.tag
	for item in DumpXml.child_nodes(root_node):
		print item.tag

	print DumpXml.node_to_string(root_node)
	pass

