from pyexpat.errors import messages
from tkinter import *
from tkinter import messagebox

class Desgin(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.label = Label(self, text="Please enter you weight (kg) : ")
        self.label.pack()

        #添加一个输入框
        self.entry = Entry(self)
        self.entry.pack()

        #创建一个按钮
        self.button = Button(self , text = "confirm" , command= self.on_click)
        self.button.pack()

    def on_click(self):
        weight = self.entry.get()
        messagebox.showinfo("Weight Result" ,f"Your weight is {weight} kg")




if __name__ == '__main__':
    root = Tk()
    root.geometry("600x600+700+300")
    root.title("Calculate blood alcohol")
    app = Desgin(master=root)
    root.mainloop()