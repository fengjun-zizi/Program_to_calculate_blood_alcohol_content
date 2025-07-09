
import tkinter as tk
import mysql.connector
from UI_desgin import Desgin
from tkinter import messagebox
from tkinter import ttk
import re
class Main (Desgin):
    def __init__(self , master=None):
        super().__init__(master)  #也就是在这里我已经把Desgin中的字典传递过来了

        # 绑定按钮
        #self.debug_btn.config(command=self.print_raw_data)
        self.calc_btn.config(command=self.function_about_widmark)
        #self.load_btn.config(command=self.load_data_from_db)

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

            self.load_data_from_db(only_match = True)

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

    def load_data_from_db(self , only_match = False):
        try:
            self.cursor.execute("SELECT * FROM bac_levels") # 尝试向数据库发送SELECT * FROM bac_levels这个SQL语句
            rows = self.cursor.fetchall() # 从数据库游标中获取查询结果的所有行，并且储存在rows
        except mysql.connector.Error as err:  # ← 统一用 err mysql.connector.Error这个语句是用来捕获所有的有关MySQL的错误
            messagebox.showerror("Database error", str(err))
            return  # 捕获异常后立刻返回
        # 清楚旧行
        for item in self.tree.get_children():
            self.tree.delete(item)
        # 插入
        for row in rows:
            march = self._row_match_bac(row)
            print("Debug row", row[0], "match?", march)

            if only_match and not self._row_match_bac(row) :
                continue
            self.tree.insert("" , "end" , values= (row[3] , row[4] , row[5]))
            self.symptoms_var.set(row[3])
            self.legal_var.set(row[4])
            self.recommendation_var.set(row[5])

    def _row_match_bac(self, row):

        g_range = row[2].strip() # 取出第三列g_per_1_range，去掉首尾空格
        val = self.BAC_0 # 把我算好的BAC的值，赋值到val

        \
        m = re.match(r'^\s*([0-9.]+)\s*[–-]\s*([0-9.]+)\s*$', g_range) #使用正则表达式，去匹配数据库里面的数据
        if m: # 如果匹配成功，这把前后界转成lo ,hi
            lo, hi = map(float, m.groups())
            return lo <= val <= hi


        m = re.match(r'^≥\s*([0-9.]+)\s*$', g_range)
        if m:
            lo = float(m.group(1))
            return val >= lo


        return False

    def destroy(self):
        self.close_database()
        super().destroy()
# 运行
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blood Alcohol Content Calculator")
    #root.attributes("-topmost", True)
    root.geometry("1000x800")
    app = Main(master=root)
    root.mainloop()