import mysql.connector

class Main:
    def __init__(self):
        self.r_boy = 0.68
        self.r_girl = 0.55
        self.p = 0.789
        self.get_wine_name = ""
        self.volume = 0
        self.abv = 0
        self.weight = 0
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",  # 如果你有密码，请填入
            database="blood_alcohol"
        )

        self.cursor = self.mydb.cursor()

    def show_data(self):
        self.cursor.execute("SELECT * FROM bac_levels")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row) #可以直接使用print函数来打印，但是使用for函数，比较美观

    def close_database(self):
        self.cursor.close()
        self.mydb.close()

    def get_wine_name(self):
        wine_name = input("Please enter the name of the wine: ")
        volume = input("Please enter the volume of the wine: ")
        abv = input("Please enter the fraction of the wine: ")
        weight = input("Please enter the weight of the wine: ")
        pr(f"Your the wine name is "wine_name, volume, abv, weight)

    def calculate(self):


# 运行
app = Main()
app.show_data()