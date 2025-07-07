from pyexpat.errors import messages
from tkinter import *
from tkinter import messagebox

class Desgin(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.mybd = None
        self.cursor = None
        self.r_boy = 0.68
        self.r_girl = 0.55


    def create_widgets(self):

        self.entries = {}  # 用来存所有 Entry 控件 这是一个字典

        # weight
        self.label = Label(self, text="Please enter your weight (kg):")
        self.label.pack()
        self.entries["weight"] = Entry(self) #这里创建了一个输入框，并且把它保存到了一个字典里self.entries，键是“weight”
        self.entries["weight"].pack() #他调用了.pack() 把刚才创建的这个输入框显示到窗口中

        # wine name
        self.label01 = Label(self, text="Please enter the name of the wine:")
        self.label01.pack()
        self.entries["wine_name"] = Entry(self)
        self.entries["wine_name"].pack()

        # volume
        self.label02 = Label(self, text="Please enter the volume of the wine (ml):")
        self.label02.pack()
        self.entries["volume"] = Entry(self)
        self.entries["volume"].pack()

        # alcohol %
        self.label03 = Label(self, text="Please enter the alcohol fraction (%):")
        self.label03.pack()
        self.entries["abv"] = Entry(self)
        self.entries["abv"].pack()

        # gender
        self.label04 = Label(self, text="Please enter your gender (male or female):")
        self.label04.pack()

        # gender options
        self.gender_var = StringVar(value = "male") # 创建了一个标签，而StringVar这个函数是对一个变量的追踪
        self.entries["gender"] = self.gender_var #用来保存并自动追踪一个字符串值
        self.gender_options = ["male", "female"] #这是一个普通一个python列表，稍微会展开成参数
        self.gender_menu = OptionMenu(self, self.gender_var, *self.gender_options)
        self.gender_menu.pack() # OptionMenU这个函数是用来创建下拉框的，父容器是self，

        self.button = Button(self, text="Just show the data", command=self.on_click)
        self.button.pack()

        #entries这个字典储存了可以计算ABC的大部分信息


    def on_click(self):
        data = {}
        for key, entry in self.entries.items() :
            data[key] = entry.get()
        print("表格数据为： ", data)


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x600+700+300")
    root.title("Calculate blood alcohol")
    app = Desgin(master=root)
    root.mainloop()

    #表格数据为：  {'weight': 'fdf', 'wine_name': 'fdfd', 'volume': 'fdfd', 'abv': 'dfd', 'gender': 'male'}