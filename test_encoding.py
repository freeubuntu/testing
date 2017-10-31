何获得系统的默认编码？ 
#!/usr/bin/env python
#coding=utf-8
import sys
print sys.getdefaultencoding()  
该段程序在英文WindowsXP上输出为：ascii 
英文win10：utf-8
win7中文windows系统cmd编码格式为gbk

在某些IDE中，字符串的输出总是出现乱码，甚至错误，其实是由于IDE的结果输出控制台自身不能显示字符串的编码，而不是程序本身的问题。 

#!/usr/bin/env python  
#coding=utf-8  
s="中文"  
  
if isinstance(s, unicode):  
#s=u"中文"  
    print s.encode('gb2312')  
else:  
#s="中文"  
    print s.decode('utf-8').encode('gb2312') 
	
	
python读取文件时候要考虑文件编码格式