# -*- encoding: utf-8 -*-

from xml.dom import minidom
import xml.etree.ElementTree as ET
import os

filepath = "/Users/WorkStation/py_learning/function/"
filename = 'xmltest.xml'

xsi="http://www.w3.org/2001/XMLSchema-instance"
xsd="http://www.w3.org/2001/XMLSchema"

impl = minidom.getDOMImplementation()
doc = impl.createDocument(None,None,None)

rootElement = doc.createElement("根节点名")
rootElement.setAttribute('属性1',"设置属性1")
rootElement.setAttribute('属性2',"设置属性2")
rootElement.setAttribute('属性N',"设置属性...")

moduleElement1 = doc.createElement("子节点1名")
moduleElement1.setAttribute('属性1',"设置属性1")
moduleElement1.setAttribute('属性2',"设置属性2")
# 将节点添加到上一个节点下
rootElement.appendChild(moduleElement1)

moduleElement2 = doc.createElement("子节点2名")
moduleElement2.setAttribute('属性',None)
rootElement.appendChild(moduleElement2)

itemElement = doc.createElement("孙节点1名")
psElement = doc.createTextNode("孙节点注释")
itemElement.setAttribute('属性1',"设置属性")
itemElement.appendChild(psElement)
moduleElement1.appendChild(itemElement)

comentElement = doc.createTextNode("文本内容")
moduleElement2.appendChild(comentElement)

# 文件最后加入后半标签
doc.appendChild(rootElement)

# 如果文件已存在就先备份
if os.path.exists(filename):
    if os.path.exists(filename+".backup.xml"):
        os.remove(filename+".backup.xml")
    os.rename(filename, filename + ".backup.xml")

# 打开xmltest.xml文件 准备写入
f = open(filename, 'a', encoding='utf-8')
# 写入文件 子节点缩进，新行换行
doc.writexml(f,encoding='utf-8',addindent='\t',newl='\n')
# 关闭
f.close()
