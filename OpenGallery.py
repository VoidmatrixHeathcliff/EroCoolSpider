import os

name = input("请输入需要打开的画册名字：")
os.system("explorer \"" + os.getcwd() + "\\Gallery\\" + name + "\"")