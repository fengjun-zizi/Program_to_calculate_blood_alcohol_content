
import tkinter as tk       # ★ 必须有
import mysql.connector
from UI_desgin import Desgin
from tkinter import messagebox
# 其余代码保持不变 …

class Main (Desgin):
    def __init__(self , master=None):
        super().__init__(master)  #也就是在这里我已经把Desgin中的字典传递过来了

        # 绑定按钮
        self.debug_btn.config(command=self.print_raw_data)
        self.calc_btn.config(command=self.function_about_widmark)

        # 常量
        self.p       = 0.789         # 乙醇密度
        self.r_boy   = 0.68
        self.r_girl  = 0.55
        self.BAC_0   = 0             # 计算结果缓存

        # 数据库连接（可放到 try/except 里）
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="blood_alcohol"
        )
        self.cursor = self.mydb.cursor()

    def print_raw_data(self):
        data = {k: (v.get() if hasattr(v, "get") else v.get())
                for k, v in self.entries.items()}
        print("Debug data:", data)

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
        try:
            weight   = float(self.entries["weight"].get())
            volume   = float(self.entries["volume"].get())
            abv_pct  = float(self.entries["abv"].get())
            gender   = self.entries["gender"].get().lower()

            r = self.r_boy if gender == "male" else self.r_girl
            grams_ethanol = volume * (abv_pct / 100) * self.p
            self.BAC_0 = grams_ethanol / (weight * r)

            # 更新 UI
            self.result_var.set(f"BAC = {self.BAC_0:.2f} g/L")

            # 查数据库并弹窗
            self.show_data()

        except ValueError:
            messagebox.showerror("Input error",
                                 "所有数值字段必须填入可转换为数字的内容。")

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

    def destroy(self):
        self.close_database()
        super().destroy()
# 运行
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Widmark BAC Calculator")
    root.geometry("400x480")
    app = Main(master=root)
    root.mainloop()