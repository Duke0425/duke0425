"""
open方法的另外一种写法
with open(文件路径, 读写方式, encoding=编码方式) as 文件对象:
    文件操作

-->打开文件,将文件存在文件对象中.当文件操作完成会自动关闭

"""
with open('files/nono', 'r', encoding='utf-8') as f:
    print(f.read())

print(f.closed)  # Ture


"""
普通的文本文档,也可以以二进制的形式读和写
2.二进制文件的读
只要将读写的方式设置为'br','rb'就可以了.读出来的数据就是二进制数据
注意: 二进制操作不能设置编码方式
"""

with open('files/was.jpg', 'rb') as f:
    content = f.read()

with open('imge.jpg', 'wb') as f:
    f.write(content)

"""
3.文件不存在
当以读的方式打开一个不存在的文件,会报'fileNotFindError'
当以写的方式打开一个不存在的文件,不会报错,并会创建这个文件
"""
with open('ddd.txt', 'a') as f:
    pass