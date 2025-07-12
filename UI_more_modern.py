import customtkinter
import customtkinter as ctk
from tkinter import *

from UI_desgin import Desgin
# 设置全局外观
ctk.set_appearance_mode("system")

class ModernDesgin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title ("Blood Alcohol")
        self.geometry("500x1000")

        self.entries = {}
        self.vars = {}
        self.text = "hello world "
        self.symptoms_var = StringVar()
        self.legal_var = StringVar()
        self.recommendation_var = StringVar()
        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.gender_var = ctk.StringVar(value="              male") # 默认值
        self.name = ctk.StringVar(value="")
        self.volume = ctk.DoubleVar(value=0.0)
        self.fraction = ctk.DoubleVar(value=0.0)
        self.weight = ctk.DoubleVar(value=0.0)
        #self.textbox.grid(row=0, column=0, sticky="nsew")
        #self.textbox.insert("0.0", "Some example text!\n" * 50)
        self.ui()

    def ui (self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        font = ctk.CTkFont(family="Times New Roman", size=15)

        # Wine Name
        self.label01 = ctk.CTkLabel(self, text="Wine Name", fg_color="black", text_color="white", corner_radius=10,
                                    width=200,height=45,font=font)
        self.label01.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.textbox = ctk.CTkTextbox(self, width=200, height=45, corner_radius=10)
        self.textbox.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        # 变量赋值 Wine Name
        self.entry = ctk.CTkEntry(self, textvariable=self.name)
        self.vars["name"] = ctk.StringVar()
        #self.entries["weight"].grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Volume
        self.label02 = ctk.CTkLabel(self, text="Volume", fg_color="black", text_color="white", corner_radius=10,
                                    width=200,height=45,font=font)
        self.label02.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.textbox1 = ctk.CTkTextbox(self, width=200, height=45, corner_radius=10)
        self.textbox1.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        # 变量赋值 Volume
        self.enty1 = ctk.CTkEntry(self, textvariable=self.volume)


        # Fraction Wine
        self.label03 = ctk.CTkLabel(self, text="Fraction Wine", fg_color="black", text_color="white", corner_radius=10,
                                    width=200,height=45,font=font)
        self.label03.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.textbox2 = ctk.CTkTextbox(self, width=200, height=45, corner_radius=10)
        self.textbox2.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        # 赋值给Fraction Wine
        self.entry2 = ctk.CTkEntry(self, textvariable=self.fraction)

        # Weight
        self.label04 = ctk.CTkLabel(self, text="Weight", fg_color="black", text_color="white", corner_radius=10,
                                    width=200, height=45,font=font)
        self.label04.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.textbox3 = ctk.CTkTextbox(self, width=200, height=45, corner_radius=10)
        self.textbox3.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        #赋值给weight
        self.entry3 = ctk.CTkEntry(self, textvariable=self.weight)

        # Gender
        self.label05 = ctk.CTkLabel(self, text="Gender", fg_color="black", text_color="white", corner_radius=10,width=200, height=45,font=font)
        self.label05.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.gender_var = ctk.StringVar(value="                        male                        ")
        self.gender_menu = ctk.CTkOptionMenu(self, values=["                        male                        ", "                        female                        ", "                        other                        "], variable=self.gender_var,
                                             width=200, font=font,height=45)
        self.gender_menu.grid(row=4, column=1, padx=10, pady=10, sticky="ew",)
        # 给gender赋值
        self.entry4 = ctk.CTkEntry(self, textvariable=self.gender_var)

        # 用来显示计算结果
        self.label06 = ctk.CTkLabel(self, text="Symptoms", fg_color="black", text_color="white", corner_radius=10,width=200, height=45,font=font )
        self.label06.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
        self.label10 = ctk.CTkLabel(self,  textvariable=self.symptoms_var, fg_color="black", text_color="white", corner_radius=10,width=200, height=45 )
        self.label10.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
        self.label07 = ctk.CTkLabel(self, text="Legal Implications", fg_color="black", text_color="white", corner_radius=10,width=200, height=45,font=font )
        self.label07.grid(row=7, column=0, padx=10, pady=10, sticky="ew")
        self.label11 = ctk.CTkLabel(self, textvariable=self.legal_var, fg_color="black", text_color="white", corner_radius=10, width=200, height=45)
        self.label11.grid(row=7, column=1, padx=10, pady=10, sticky="ew")
        self.label08 = ctk.CTkLabel(self, text="Recommendation", fg_color="black", text_color="white", corner_radius=10,width=200, height=45,font=font  )
        self.label08.grid(row=8, column=0, padx=10, pady=10, sticky="ew")
        self.label12 = ctk.CTkLabel(self,textvariable=self.recommendation_var, fg_color="black", text_color="white", corner_radius=10, width=200,height=45)
        self.label12.grid(row=8, column=1, padx=10, pady=10, sticky="ew")


        # Calculate Button
        self.button = ctk.CTkButton(self, text="Calculate", fg_color="black", text_color="white", command=self.button_1,
                                    width=400, height=45, font=font)
        self.button.grid(row=10, column=0, columnspan=2, padx=10, pady=20, sticky="ew")



    def button_1 (self):
        name = self.textbox.get("0.0", "end").strip()  # ← 获取文本框输入
        volume = self.textbox1.get("0.0", "end").strip()
        fraction = self.textbox2.get("0.0", "end").strip()
        weight = self.textbox3.get("0.0", "end").strip()
        gender = self.gender_var.get()
        self.entries["name"] = name
        self.entries["volume"] = volume
        self.entries["fraction"] = fraction
        self.entries["weight"] = weight
        self.entries["gender"] = gender
        print(self.entries)







