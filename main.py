import mysql.connector
from typing import Any
from tkinter import Tk
from UI_desgin import Desgin

class Main (Desgin):
    def __init__(self):
        super().__init__()
        self.entries:dict[str, Any] = {} #这行代码同时做了两件事情，类型标注+实际赋值
        self.create_widgets()
        self.mydb = None
        self.cursor = None
        self.r_boy = 0.68
        self.r_girl = 0.55
        self.r = 0
        self.p = 0.789
        self.wine_name = ""
        self.volume = 0
        self.abv = 0
        self.weight = 0
        self.A = 0
        self.BAC_0 = 0
        self.gender = ""
        self.abv_1 = 0
        self.content_alcohol = 0
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",  # 如果你有密码，请填入
            database="blood_alcohol"
        )
        self.cursor = self.mydb.cursor()

#可以直接使用print函数来打印，但是使用for函数，比较美观

    def close_database(self):
        if self.cursor:
            self.cursor.close()

        if self.mydb:
            self.mydb.close()



    def get_wine_name(self):
        self.wine_name = input("Please enter the name of the wine: ")
        self.volume = input("Please enter the volume of the wine(unit is ml): ")
        self.abv = input("Please enter the fraction of the wine(unit is %): ")
        self.weight = input("Please enter your weight(unit is kg): ")
        self.gender = input("Please enter the gender（male or female）: ")
        print(f"Your the wine name is {self.wine_name}")
        print(f"Your volume is {self.volume}")
        print(f"Your abv is {self.abv}")
        print(f"Your weight is {self.weight}")
        print(f"Your gender is {self.gender}")
        if self.gender == "male" :
            self.r = self.r_boy
        else:
            self.r = self.r_girl

    def function_about_widmark(self):
        self.abv = self.entries["abv"]
        self.abv_1 = float(self.abv) /100
        self.volume = float(self.volume)
        self.content_alcohol = self.volume * self.abv_1
        self.A = self.p * self.content_alcohol
        self.weight = float(self.weight)
        self.BAC_0 = self.A / self.weight * self.r
        print(f"Your blood alcohol content is (excluding metabolic and theoretical value){self.BAC_0}")

    def show_data(self):
        self.cursor.execute("SELECT * FROM bac_levels")
        rows = self.cursor.fetchall()
        matched_row = None

        for row in rows:
            id, bac_range, g_per_l_range, symptoms, legal_implications, recommendation = row
            g_per_l_range = g_per_l_range.strip()

            if "–" in g_per_l_range:  # en dash
                lower, upper = g_per_l_range.split("–")
                lower = float(lower.strip())
                upper = float(upper.strip())

                if lower <= self.BAC_0 <= upper:
                    matched_row = row
                    break

            elif "≥" in g_per_l_range:
                lower = float(g_per_l_range.replace("≥", "").strip())
                if self.BAC_0 >= lower:
                    matched_row = row
                    break

        if matched_row:
            print(f"Your BAC is {self.BAC_0:.2f} g/L, which corresponds to:")
            print(f"Symptoms: {matched_row[3]}")
            print(f"Legal Implications: {matched_row[4]}")
            print(f"Recommendation: {matched_row[5]}")
        else:
            print("No matching BAC level found.")

        self.close_database()
# 运行
app = Main()
app.get_wine_name()
app.function_about_widmark()
app.show_data()