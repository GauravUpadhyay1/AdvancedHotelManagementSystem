from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking
from details import Detailsroom
from report import Report
from chatbot import ChatBot
from time import strftime
from datetime import date


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        ##########1st Image############
        img1 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\hotel1.png")
        img1 = img1.resize((1350, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        ##########2nd Image############

        img2 = Image.open(r"E:\Python\Final Project\Hotel Management System\img\grand-hotel-logo-inspiration-luxury-hotel-logo-template-inspiration-idea-grand-hotel-logo-inspiration-luxury-hotel-logo-template-169469853.jpg")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

        ##########title############
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(
            "times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1350, height=50)

        ##########title############

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1350, height=600)

        #####menu###########
        lbl_menu = Label(main_frame, text="MENU", font=(
            "times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        ########btn frame###########
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=160)

        cust_btn = Button(btn_frame, text="CUSTOMER", width=24, command=self.cust_Details, font=(
            "times new roman", 12, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", width=24, font=("times new roman", 12, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand1", command=self.Roombooking)
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=24, font=("times new roman", 12, "bold"), bg="black",
                             fg="gold", bd=0, cursor="hand1", command=self.DetailsRoom)
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=24, font=("times new roman", 12, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand1", command=self.Reportprob)
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=24, font=("times new roman", 12, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand1", command=self.logout)
        logout_btn.grid(row=4, column=0, pady=1)

        ###########right side image#############

        img3 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\1503534990218.jpeg")
        img3 = img3.resize((1100, 550), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1040, height=452)

        ########down images################

        img4 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\download.jpg")
        img4 = img4.resize((230, 130), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=190, width=230, height=130)

        img5 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\fpp.jpg")
        img3 = img5.resize((230, 130), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=320, width=230, height=130)

        # chatbot button

        chatbot_btn = Button(lblimg3, text="Help Desk", width=15, font=("times new roman", 12, "bold"), bg="black",
                             fg="gold", bd=3, cursor="hand1", command=self.chatbot)
        chatbot_btn.place(x=880, y=405)

        # time
        def time():
            sting = strftime("%H:%M:%S %p")
            labeltime.config(text=sting)
            labeltime.after(1000, time)

        labeltime = Label(self.root, font=(
            "ds-digital", 19), bg="black", fg="gold")
        labeltime.place(x=1105, y=149)
        time()

        def ndate():
            std = date.today()
            labeldate.config(text=std)
            labeldate.after(1000, ndate)

        labeldate = Label(self.root, font=(
            "ds-digital", 19), bg="black", fg="gold")
        labeldate.place(x=25, y=149)
        ndate()

    def cust_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def Roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def DetailsRoom(self):
        self.new_window = Toplevel(self.root)
        self.app = Detailsroom(self.new_window)

    def Reportprob(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)

    def logout(self):
        self.root.destroy()

    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
