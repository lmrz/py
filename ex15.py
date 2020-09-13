#引入库
from sys import argv
#定义库
script, filename = argv

#将文件内容赋改txt对象
txt = open(filename)

#输出文件名/文件内容
print(f"Here's you file {filename}:")
print(txt.read())

#输入文件，“>" 开头
print("Type the filename again:")
file_again = input("> ")

#将输入的内容赋给txt_again
txt_again= open(file_again)
#输出内容
print(txt_again.read())
