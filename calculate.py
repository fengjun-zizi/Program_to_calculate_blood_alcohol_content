from pyexpat.errors import messages

import mysql.connector
from UI_more_modern import ModernDesgin
import tkinter as messagebox
import re

class Calculator (ModernDesgin):
    def __init__(self , master=None):
        super().__init__()

        self.r = 0.00
        # 常量
        self.p       = 0.789         # 乙醇密度
        self.r_boy   = 0.68
        self.r_girl  = 0.55
        self.BAC_0   = 0

        # 计算结果缓存

        # 连接数据库
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="blood_alcohol"
        )
        self.cursor = self.mydb.cursor()

        self.run()

    def run(self):

        
        
            self.ui()


            def validate_and_calculate():
                name = self.vars["name"].get().strip()
                volume = self.volume.get()
                fraction = self.fraction.get()
                weight = self.weight.get()

                if name == "" or self.volume == 0.0 or fraction == 0.0 or weight == 0.0:
                    messagebox.showerror("Input Error", "All fields must be filled with valid values.")
                    return
                else:
                    self.calculate()

            # 设置按钮的 command
            self.button.configure(command=validate_and_calculate)


    def print_raw_data(self):
        data = {k: (v.get() if hasattr(v, "get") else v.get())
                for k, v in self.entries.items()}
        print("Debug data:", data)



    def close_database(self):
        if self.cursor:
            self.cursor.close()

        if self.mydb:
            self.mydb.close()


    def get_data(self):
        print(f"Your the wine name is {self.name}")
        print(f"Your volume is {self.volume}")
        print(f"Your fraction is {self.fraction}")
        print(f"Your weight is {self.weight}")
        print(f"Your gender is {self.gender_var}")

        if self.gender_var == "male":
            self.r = self.r_girl
        else :
            self.r = self.r_boy

    def calculate(self):
        try :
            print("run successfully")
            #weight = float(self.entries["weight"].get())
            volume = float(self.entries["volume"].get())
            abv_pct = float(self.entries["fraction"].get())
            gender = self.entries["gender"].get().lower().strip()
            self.r = self.r_boy
            if gender == "male" :
                self.r = self.r_boy
            else :
                self.r = self.r_girl


            grams_ethanol = volume * (abv_pct / 100) * self.p
            print(f"Your volume is {volume} ml")
            print(f"Your alcohol fraction is {abv_pct} %")
            print(f"Your p is {self.p} g/ml")
            print("上面的的结果和grams_ethanol有关")
            #print(f"Your weight is {self.weight}")
            #print(f"Your weight is {weight}")
            weight = self.entries["weight"].get()
            if weight == " " :
                messagebox.showerror("Input Error" , "All weights must be filled with content that can be converted to a number")
                return

            weight = float(weight)
            print(weight)
            print(self.r)
            self.BAC_0 = grams_ethanol / (weight * self.r)
            print(f"Your BAC is {self.BAC_0:.2f} g/L")
            print(f"gram_ethanol is {grams_ethanol:.2f} g")
            print(f"weight is {weight:.2f} kg")
            print(f"r is {self.r:.2f} L/kg")


            self.show_data()

        except ValueError:
            messagebox.showerror("Input Error" , "All numeric fields must be filled with content that can be converted to a number")

        # self.load_data_from_db()


    def show_data(self):
        """根据计算的 BAC 值，从数据库中查询对应的症状、法律后果和建议，并显示在界面上"""
        self.cursor.execute("SELECT * FROM bac_levels")  # 从数据库中选择所有的行
        rows = self.cursor.fetchall() # 获取所有行数据，以列表的形式保存在 rows 中
        matched_row = None

        for row in rows:
            id, bac_range, g_per_l_range, symptoms, legal_implications, recommendation = row
            g_per_l_range = g_per_l_range.strip()

            if "–" in g_per_l_range:  # en dash
                lower, upper = g_per_l_range.split("–") # 给 lower 和 upper 赋值
                # 去掉首尾空格，并转换为 float
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


        self.load_data_from_db()
        


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

            if march:
            # 如果匹配成功，插入到表格中
                self.tree.insert("" , "end" , values= (row[3] , row[4] , row[5]))
                self.symptoms_var.set(row[3])
                self.legal_var.set(row[4])
                self.recommendation_var.set(row[5])
                print(f"symptoms: {self.symptoms_var.get()}")
                print(f"legal: {self.legal_var.get()}")
                print(f"recommendation: {self.recommendation_var.get()}")


    def _row_match_bac(self, row):

        g_range = row[2].strip() # 取出第三列g_per_1_range，去掉首尾空格
        val = self.BAC_0 # 把我算好的BAC的值，赋值到val


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



if __name__ == "__main__":

    app = Calculator()
    #app.resizable(False, False)
    app.mainloop()
