from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from hotel1 import HotelManagementSystem
from datetime import datetime

import cv2
import os
import numpy as np


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("1100x800")

        self.bg = ImageTk.PhotoImage(
            file=r"E:\Python\Final Project\Hotel Management System\img\loginmain.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=400, y=150, width=320, height=400)

        img1 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\loginicon.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1,
                       bg="black")
        lblimg.place(x=515, y=155, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=90, y=100)

        #####labels####
        username_lbl = Label(frame, text="Username", font=(
            "times new roman", 13, "bold"), fg="white", bg="black")

        username_lbl.place(x=65, y=148)

        self.txtuser = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), width=23)

        self.txtuser.place(x=45, y=180)

        password_lbl = Label(frame, text="Password", font=(
            "times new roman", 13, "bold"), fg="white", bg="black")

        password_lbl.place(x=65, y=218)

        self.passuser = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), width=23)

        self.passuser.place(x=45, y=240)

        #######icon images######

        img2 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\username.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(frame, image=self.photoimg2,
                        bg="black")
        lblimg2.place(x=40, y=148, width=25, height=25)

        img3 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\password.png")
        img3 = img3.resize((23, 20), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(frame, image=self.photoimg3,
                        bg="black")
        lblimg3.place(x=40, y=217, width=23, height=20)

        #######login########
        btnlogin = Button(frame, text="Login", command=self.login, font=(
            "times new roman", 13, "bold"), bd=4, relief=RIDGE, fg="white", bg="cadetblue")
        btnlogin.place(x=90, y=290, width=120, height=30)

        #####register#####
        btnreg = Button(frame, text="Register New User", command=self.register_window, font=(
            "times new roman", 8, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        btnreg.place(x=5, y=335, width=155)

        #####password#####
        btnforg = Button(frame, text="Forget Password", font=(
            "times new roman", 8, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black", command=self.forgot_password_window)
        btnforg.place(x=0, y=355, width=155)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.passuser.get() == "":
            messagebox.showerror("Error", "all fields are required")

        elif self.txtuser.get() == "gaurav" and self.passuser.get() == "gaurav4u7":
            messagebox.showinfo("Success", "Login Successful")

        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="gaurav4u7",
                database="gaurav",
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email =%s and password =%s", (
                self.txtuser.get(),
                self.passuser.get()
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username and password")

            else:
                open_main = messagebox.askyesno("yesNo", "Acess Only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)

                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close

            # face_classifer = cv2.CascadeClassifier(
            #     "haarcascade_frontalface_default.xml")

            # def face_cropped(img):
            #     gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
            #     faces = face_classifer.detectMultiScale(gray, 1.3, 5)
            #     # scalingfactor=1.3
            #     # minimumneighbour = 5
            #     for (x, y, w, y) in faces:
            #         face_cropped = img[y:y+h, x:x+w]
            #         return face_cropped

            # cap = cv2.VideoCapture(0)
            # img_id = 0

            # while True:
            #     ret, my_frame = cap.read()
            #     if face_cropped(my_frame) is not None:
            #         img_id += 1
            #     face = cv2.resize(face_cropped(my_frame), (450, 450))
            #     face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            #     file_name_path = "data/user." + str(img_id) + "." + ".jpg"
            #     cv2.imwrite(file_name_path)
            #     cv2.putText(face, str(img_id),
            #                 cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
            #     cv2.imshow("Cropped Face", face)
            #     if cv2.waitKey(1) == 13 or int(img_id) == 10:
            #         break

            # cap.release()
            # cv2.destroyAllWindows()

            face_classifier = cv2.CascadeClassifier(
                'haarcascade_frontalface_default.xml')

            def takeImages():

                i = 0
                if (i == 0):

                    cam = cv2.VideoCapture(0)

                    sampleNum = 0
                    while(True):
                        ret, img = cam.read()
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                        for (x, y, w, h) in faces:
                            cv2.rectangle(
                                img, (x, y), (x+w, y+h), (255, 0, 0), 2)

                            sampleNum = sampleNum+1
                            now = datetime.now()
                            dt = now.strftime("%d-%m-%Y , %Hh;%Mm;%Ss")

                            cv2.imwrite("data\ " + str(dt) + "." + str(sampleNum) +
                                        ".jpeg", gray[y:y+h, x:x+w])

                            cv2.imshow("frame", img)

                        if cv2.waitKey(10) & 0xFF == ord('q'):
                            break

                        elif sampleNum > 5:
                            break

                    cam.release()
                    cv2.destroyAllWindows()
                    # messagebox.showinfo("welcome", "Welcome" parent= self.root)

                else:

                    messagebox.showerror("error", "cannot log you in")

            takeImages()

    def reset(self):
        if self.combo_secques.get() == "Select":
            messagebox.showerror(
                "Error", "Please select a security question", parent=self.root2)

        elif self.entrysecans.get() == "":
            messagebox.showerror(
                "Error", "Please enter the security answer", parent=self.root2)

        elif self.entrynewpassword.get() == "":
            messagebox.showerror(
                "Error", "Please enter the new password", parent=self.root2)

        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="gaurav4u7",
                database="gaurav",
            )
            my_cursor = conn.cursor()
            query = (
                "select * from register where email = %s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_secques.get(),
                     self.entrysecans.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Wrong answer", parent=self.root2)
            else:
                query = ("update register set password = %s where email = %s")
                value = (self.entrynewpassword.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "Password has been reset successfully", parent=self.root2)
                self.root2.destroy()

    #####forget password####

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Enter a valid Username")

        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="gaurav4u7",
                database="gaurav",
            )
            my_cursor = conn.cursor()
            query = ("select * from register where email =%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please enter a valid username")

            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+450+170")

                l = Label(self.root2, text="Forget Password", font=(
                    "times new roman", 15, "bold"), fg="cadetblue", bg="white")
                l.place(x=0, y=0, relwidth=1)

                secques = Label(self.root2, text="Select Security Question", font=(
                    "times new roman", 17, "bold"), bg="white")
                secques.place(x=50, y=50)

                self.combo_secques = ttk.Combobox(
                    self.root2,
                    font=("times new roman", 10, "bold"),
                    width=25,
                    state="readonly"
                )
                self.combo_secques["value"] = ("Select",
                                               "Your Girlfriend's Name", "Your Pet's Name", "Your Birth Place")
                self.combo_secques.current(0)
                self.combo_secques.place(x=75, y=90)

            # entrysecques = ttk.Entry(frame, font=(
            #     "times new roman", 13, "bold"))
            # entrysecques.place(x=330, y=195, width=220)

            ####forget password####
                secans = Label(self.root2, text="Select Security Answer", font=(
                    "times new roman", 17, "bold"), bg="white")
                secans.place(x=50, y=130)

                self.entrysecans = ttk.Entry(self.root2, font=(
                    "times new roman", 10, "bold"))
                self.entrysecans.place(x=75, y=170, width=200)

                newpassword = Label(self.root2, text="Enter New Password", font=(
                    "times new roman", 17, "bold"), bg="white")
                newpassword.place(x=50, y=210)

                self.entrynewpassword = ttk.Entry(self.root2, font=(
                    "times new roman", 10, "bold"))
                self.entrynewpassword.place(x=75, y=250, width=200)

                btnn = Button(self.root2, text="Reset", font=(
                    "times new roman", 15, "bold"), fg="white", bg="cadetblue", command=self.reset)
                btnn.place(x=130, y=310)


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
                         relief=RIDGE, borderwidth=0, cursor="hand2", bg="white", command=self.return_login)
        btnimg6.place(x=200, y=430, width=100, height=58)

        ##########func ######

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityA.get() == "Select":
            messagebox.showerror("Error", "All fields are required")

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

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
