from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1100x800")

        #####variables####
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        ####bglogo#####

        self.bg = ImageTk.PhotoImage(
            file=r"E:\Python\Final Project\Hotel Management System\img\reg1.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        ###left image####
        self.bg2 = ImageTk.PhotoImage(
            file=r"E:\Python\Final Project\Hotel Management System\img\food.jpg")

        lbl_bg2 = Label(self.root, image=self.bg2)
        lbl_bg2.place(x=10, y=90, width=400, height=500)

        #####mainframe#####

        frame = Frame(self.root, bg="white")
        frame.place(x=410, y=90, width=680, height=500)

        lblreg = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="green", bg="white")
        lblreg.place(x=10, y=10)

        ########labels##########

        fname = Label(frame, text="First Name", font=(
            "times new roman", 17, "bold"), bg="white")
        fname.place(x=30, y=80)

        self.entryname = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_fname)
        self.entryname.place(x=30, y=115, width=220)

        ####lastname####
        flastname = Label(frame, text="Last Name", font=(
            "times new roman", 17, "bold"), bg="white")
        flastname.place(x=330, y=80)

        self.entrylname = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_lname)
        self.entrylname.place(x=330, y=115, width=220)

        ####contact####
        contact = Label(frame, text="Contact Number", font=(
            "times new roman", 17, "bold"), bg="white")
        contact.place(x=30, y=160)

        self.entrycontact = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_contact)
        self.entrycontact.place(x=30, y=195, width=220)

        ####email####
        email = Label(frame, text="Email", font=(
            "times new roman", 17, "bold"), bg="white")
        email.place(x=330, y=160)

        self.entryemail = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_email)
        self.entryemail.place(x=330, y=195, width=220)

        ####security question####
        secques = Label(frame, text="Select Security Question", font=(
            "times new roman", 17, "bold"), bg="white")
        secques.place(x=30, y=240)

        self.combo_secques = ttk.Combobox(
            frame,
            font=("times new roman", 10, "bold"),
            width=25,
            state="readonly", textvariable=self.var_securityQ
        )
        self.combo_secques["value"] = ("Select",
                                       "Your Girlfriend's Name", "Your Pet's Name", "Your Birth Place")
        self.combo_secques.current(0)
        self.combo_secques.place(x=30, y=275)

        # entrysecques = ttk.Entry(frame, font=(
        #     "times new roman", 13, "bold"))
        # entrysecques.place(x=330, y=195, width=220)

        ####security Answer####
        secans = Label(frame, text="Security Answer", font=(
            "times new roman", 17, "bold"), bg="white")
        secans.place(x=330, y=240)

        self.entrysecans = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_securityA)
        self.entrysecans.place(x=330, y=275, width=220)

        #####password###
        password = Label(frame, text="Password", font=(
            "times new roman", 17, "bold"), bg="white")
        password.place(x=30, y=320)

        self.entrypassword = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_pass)
        self.entrypassword.place(x=30, y=355, width=220)

        #####confirm  password###
        conpassword = Label(frame, text="Confirm Password", font=(
            "times new roman", 17, "bold"), bg="white")
        conpassword.place(x=330, y=320)

        self.entryconpassword = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_confpass)
        self.entryconpassword.place(x=330, y=355, width=220)

        #####checkbutton#####
        self.var_check = IntVar()

        self.checkbtn = Checkbutton(
            frame, text="I Agree To The Terms And Conditions", font=("times new roman", 10, "bold"), variable=self.var_check, onvalue=1, offvalue=0)
        self.checkbtn.place(x=30, y=395)

        ###buttons####

        img5 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\regbtn.png"
        )
        img5 = img5.resize((100, 40), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btnimg5 = Button(frame, image=self.photoimg5, bd=0,
                         relief=RIDGE, borderwidth=0, cursor="hand2", bg="white", command=self.register_data)
        btnimg5.place(x=70, y=430, width=100, height=58)

        img6 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\login.png"
        )
        img6 = img6.resize((100, 40), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btnimg6 = Button(frame, image=self.photoimg6, bd=0,
                         relief=RIDGE, borderwidth=0, cursor="hand2", bg="white")
        btnimg6.place(x=200, y=430, width=100, height=58)

        ##########func ######

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityA.get() == "Select":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)

        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords Do Not Match")

        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please Accept the Terms and Condition")

        else:

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="gaurav4u7",
                database="gaurav",
            )
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "Email already exists, Please try another")

            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            # self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful")


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
