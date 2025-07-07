import tkinter
from pyexpat.errors import messages
from tkinter import *
from tkinter import messagebox

class Desgin(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.result_var = StringVar(value = "BAC == -- g/l")
        self.pack(padx = 20 , pady = 20)
        self.create_widgets()
        self.mybd = None
        self.cursor = None
        self.r_boy = 0.68
        self.r_girl = 0.55


    def create_widgets(self):
        # weight
        Label(self, text="Weight (kg)").pack()
        self.entries["weight"] = Entry(self)
        self.entries["weight"].pack()

        # wine name
        Label(self, text="Wine name").pack()
        self.entries["wine_name"] = Entry(self)
        self.entries["wine_name"].pack()

        # volume
        Label(self, text="Volume (ml)").pack()
        self.entries["volume"] = Entry(self)
        self.entries["volume"].pack()

        # alcohol %
        Label(self, text="Alcohol fraction (%)").pack()
        self.entries["abv"] = Entry(self)
        self.entries["abv"].pack()

        # gender
        Label(self, text="Gender").pack()
        gender_var = StringVar(value="male")
        self.entries["gender"] = gender_var
        OptionMenu(self, gender_var, "male", "female").pack()

        # 结果标签
        Label(self, textvariable=self.result_var,
              fg="white", font=("Arial", 12, "bold")).pack(pady=8)

        # 这两个按钮只放句柄，不把 pack() 赋回去
        self.debug_btn = Button(self, text="Show raw data")
        self.debug_btn.pack(side="left", padx=5)

        self.calc_btn = Button(self, text="Calculate")
        self.calc_btn.pack(side="left", padx=5)

    def on_click(self):
        data = {}
        for key, entry in self.entries.items() :
            data[key] = entry.get()
        print("表格数据为： ", data)

    #表格数据为：  {'weight': 'fdf', 'wine_name': 'fdfd', 'volume': 'fdfd', 'abv': 'dfd', 'gender': 'male'}