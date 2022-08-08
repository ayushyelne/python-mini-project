from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
import pymysql
from tkinter import messagebox

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Clock")
        self.root.geometry("1350x700")
        self.root.config(bg="#021e2f")

        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800,height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

        username = Label(login_frame, text="USERNAME", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=150)
        self.username_txt = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.username_txt.place(x=250, y=180, width=350, height=35)

        passwd = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=250)
        self.passwd = Entry(login_frame, show='*', font=("times new roman", 15), bg="lightgray")
        self.passwd.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, command=self.register_window, cursor="hand2", text="Register New Account?", font=("times new roman",14), bg="white", bd=0, fg="#B00857").place(x=250,y=320)
        btn_login = Button(login_frame, command=self.login_data, cursor="hand2", text="Login", font=("times new roman", 20, "bold"), fg="white", bg="#B00857").place(x=250, y=380, width=180, height=40)


        self.lbl = Label(self.root, bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()

    def register_window(self):
        self.root.destroy()
        import register

    def login_data(self):
        if self.username_txt.get() == "" or self.passwd.get() =="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="grocery")
                cur = conn.cursor()
                cur.execute("select * from register where email=%s and password=%s", (self.username_txt.get(), self.passwd.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid user or password", parent=self.root)

                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    
                    self.root.destroy()
                    import billingsystem
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 258, 35))
        draw = ImageDraw.Draw(clock)

        bg = Image.open("c.jfif")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))

        origin = 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="#DF005E", width=4)
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="white", width=3)
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="yellow", width=2)

        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360

        self.clock_image(hr, min_, sec_)

        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)


root = Tk()
obj = Login_window(root)
root.mainloop()