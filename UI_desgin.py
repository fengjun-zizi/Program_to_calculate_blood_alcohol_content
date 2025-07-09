import tkinter
from pyexpat.errors import messages
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
class Desgin(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.result_var = StringVar(value = "BAC == -- g/l")
        self.pack(padx = 20 , pady = 20)
        self.cols = ("symptoms", "legal_implications", "recommendation")
        self.tree= ttk.Treeview(self , columns=self.cols , show="headings" , height="5")
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


        # 创建提示显示区域
        # 创建用于显示详细信息的 Frame
        # 在 __init__ 或 create_widgets 中：
        self.detail_frame = Frame(self)
        self.detail_frame.pack(pady=10)

        self.symptoms_var = StringVar()
        self.legal_var = StringVar()
        self.recommendation_var = StringVar()

        Label(self.detail_frame, text="Symptoms:", anchor="e", fg="white", width=18).grid(row=0, column=0, sticky="e",
                                                                                          padx=5, pady=3)
        Label(self.detail_frame, textvariable=self.symptoms_var, anchor="w", fg="white", bg="#222",
              wraplength=500, justify="left", relief="sunken", width=50).grid(row=0, column=1, sticky="w", padx=5,
                                                                              pady=3)

        Label(self.detail_frame, text="Legal Implications:", anchor="e", fg="white", width=18).grid(row=1, column=0,
                                                                                                    sticky="e", padx=5,
                                                                                                    pady=3)
        Label(self.detail_frame, textvariable=self.legal_var, anchor="w", fg="white", bg="#222",
              wraplength=500, justify="left", relief="sunken", width=50).grid(row=1, column=1, sticky="w", padx=5,
                                                                              pady=3)

        Label(self.detail_frame, text="Recommendation:", anchor="e", fg="white", width=18).grid(row=2, column=0,
                                                                                                sticky="e", padx=5,
                                                                                                pady=3)
        Label(self.detail_frame, textvariable=self.recommendation_var, anchor="w", fg="white", bg="#222",
              wraplength=500, justify="left", relief="sunken", width=50).grid(row=2, column=1, sticky="w", padx=5,
                                                                              pady=3)

       # self.detail_frame = Frame(self)
       # self.detail_frame.pack(pady=10)

       # self.symptoms_var = StringVar()
       # self.legal_var = StringVar()
       # self.recommendation_var = StringVar()
        # 显示区域的创建
        #Label(self.detail_frame, text="Symptoms:", anchor="w", fg="white").grid(row=0, column=0, sticky="w")
       # Label(self.detail_frame, textvariable=self.symptoms_var, anchor="w", fg="white", wraplength=600,
          #    justify="left").grid(row=0, column=1, sticky="w")

        #Label(self.detail_frame, text="Legal Implications:", anchor="w", fg="white").grid(row=1, column=0, sticky="w")
       # Label(self.detail_frame, textvariable=self.legal_var, anchor="w", fg="white", wraplength=600,
          #    justify="left").grid(row=1, column=1, sticky="w")

       # Label(self.detail_frame, text="Recommendation:", anchor="w", fg="white").grid(row=2, column=0, sticky="w")
      #  Label(self.detail_frame, textvariable=self.recommendation_var, anchor="w", fg="white", wraplength=600,
         #     justify="left").grid(row=2, column=1, sticky="w")


      #  for col in self.cols :
           # self.tree.heading(col , text = col.replace("-" , " ").title())
          #  self.tree.column(col , width = 200)

        #self.tree.pack(pady = 10)

        # 创建一个新的框架用来水平排列按钮
        button_frame = Frame(self)
        button_frame.pack(pady = 10)

        #添加一个按钮
        #self.debug_btn = Button(self, text="Show raw data")
        #self.debug_btn.pack(side= "left" ,padx=10 , expand=True)
        self.calc_btn = Button(self, text="Calculate")
        self.calc_btn.pack(side = "left" ,padx=9 , expand=True)
        #self.load_btn = Button (self , text="Load data" , command = self.load_data_from_db)
        #self.load_btn.pack(side = "left" ,padx=9 , expand=True)

    #def show_record(self,data):
       # labels = self.cols
       # for i in range (len(labels):
         #  Label(self, text=labels[i], anchor="e", width=20, bg="#333", fg="white").grid(row=i, column=0, padx=5,
          #                                                                                pady=2, sticky="e")
          # Label(self, text=data[i], anchor="w", width=60, bg="#222", fg="white").grid(row=i, column=1, padx=5, pady=2,
                                                                              #      sticky="w")


    def on_click(self):
        data = {}
        for key, entry in self.entries.items() :
            data[key] = entry.get()
        print("表格数据为： ", data)

    #表格数据为：  {'weight': 'fdf', 'wine_name': 'fdfd', 'volume': 'fdfd', 'abv': 'dfd', 'gender': 'male'}