# tkinter模块 GUI程序
# pack()包装，grid()网络，place()位置
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()  # pack最简单布局
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text="Hello,World!")
        self.helloLabel.pack()  # 把widget加到父容器
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text="Hello", command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or "World"
        messagebox.showinfo("Message", "Hello, %s" % name)


app = Application()
# 设置窗口标题
app.master.title("Hello World")
app.mainloop()  # 主消息循环
