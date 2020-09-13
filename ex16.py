from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("if you dont't want that, hit CTRL-C (^C).")
print("if you do want that, hit RUTURE.")

input("?")

print("Opening the file...")
# 通过w 写的方式给赋值
target =  open(filename,'w')

print("Truncating the file.  Goodbye!")
#截断文件，将之前的文件截断
target.truncate()

print("Now I'm going to ask you for there lines.")

#将输入的文件复制给line1/line2/line3
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#将line1内容写到目标文件中，换行
target.write(line1)
target.write("\n")
#将line2内容写到目标文件中，换行
target.write(line2)
target.write("\n")
#将line3内容写到目标文件中，换行
target.write(line3)
target.write("\n")


print("And finally , we  close  it.")
#结束，关闭文件读写
target.close()
