from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import getpass
import pymysql


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registeration Window")
        self.root.geometry("1181x700+100+50")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="grocery.jfif")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=250, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(
            x=50, y=30)

        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370,
                                                                                                                y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        gender = Label(frame1, text="Gender", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50,
                                                                                                                  y=240)
        self.txt_gender = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_gender.place(x=50, y=270, width=250)

        address = Label(frame1, text="City", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=370,
                                                                                                                 y=240)
        self.txt_address = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_address.place(x=370, y=270, width=250)

        passwd = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=50, y=310)
        self.txt_password = Entry(frame1, show='*', font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        confirm_password = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                               fg="black").place(x=370, y=310)
        self.txt_confirmpassword = Entry(frame1, show='*', font=("times new roman", 15), bg="lightgray")
        self.txt_confirmpassword.place(x=370, y=340, width=250)

        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I agree the terms and conditions", variable=self.var_chk, onvalue=1, offvalue=0,
                          bg="white", font=("times new roman", 12)).place(x=50, y=380)

        btn_register = Button(frame1, cursor="hand2", command=self.register_data, text="REGISTER",
                              font=("times new roman", 20, "bold"), fg="white", bg="#B00857").place(x=150, y=420,
                                                                                                    width=180,
                                                                                                    height=40)
        btn_login = Button(frame1, command=self.login_window, cursor="hand2", text="SIGN IN",
                              font=("times new roman", 20, "bold"), fg="white", bg="#B00857").place(x=400, y=420,
                                                                                                    width=180,
                                                                                                    height=40)

    def login_window(self):
        self.root.destroy()
        import login

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact.get() =="" or self.txt_email == "" or self.txt_gender.get() == "" or self.txt_address.get() == "" or self.txt_password.get() == "" or self.txt_confirmpassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        elif self.txt_password.get() != self.txt_confirmpassword.get():
            messagebox.showerror("Error", "Password doesn't match", parent=self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="grocery")
                cur = conn.cursor()
                cur.execute(
                    "insert into register (f_name, l_name, contact, email, gender, city, password) values (%s, %s, %s, %s, %s, %s, %s)",
                    (self.txt_fname.get(),
                     self.txt_lname.get(),
                     self.txt_contact.get(),
                     self.txt_email.get(),
                     self.txt_gender.get(),
                     self.txt_address.get(),
                     self.txt_password.get()
                     ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                 

            except Exception as es:
                messagebox.showinfo("Error", f"Error due to {str(es)}", parent=self.root)


root = Tk()
obj = Register(root)
root.mainloop()
