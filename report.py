from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import smtplib


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("900x600+200+20")

        self.var_hotelname = StringVar()
        self.var_hoteladdress = StringVar()
        self.var_yourname = StringVar()
        self.var_yourid = StringVar()
        self.var_about = StringVar()
        self.var_problem = StringVar()
        self.var_additional = StringVar()
        self.senderemail = "tabletruth47@gmail.com"
        self.senderpass = "gaurav4u77"
        self.recieveremail = "gauravupadhyay1813051019@gmail.com"

        lbl_title = Label(
            self.root,
            text="REPORT A PROBLEM",
            font=("times new roman", 17, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE,
        )
        lbl_title.place(x=0, y=0, width=900, height=50)

        labelframeleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            font=("times new roman", 11, "bold"),
            text="Report a problem",
            padx=2,
        )
        labelframeleft.place(x=5, y=50, width=300, height=300)

        ####labels####
        lblhname = Label(labelframeleft, text="Your Hotel Name",
                         font=("times new roman", 11, "bold"))
        lblhname.place(x=5, y=20)

        lblhname = ttk.Entry(labelframeleft, textvariable=self.var_hotelname)
        lblhname.place(x=140, y=20, width=150)

        lblhaddress = Label(labelframeleft, text="Hotel Address",
                            font=("times new roman", 11, "bold"))
        lblhaddress.place(x=5, y=60)

        lblhaddress = ttk.Entry(
            labelframeleft, textvariable=self.var_hoteladdress)
        lblhaddress.place(x=140, y=60, width=150)

        lblYourname = Label(labelframeleft, text="Your Name",
                            font=("times new roman", 11, "bold"))
        lblYourname.place(x=5, y=100)

        yourname = ttk.Entry(labelframeleft, textvariable=self.var_yourname)
        yourname.place(x=140, y=100, width=150)

        lblYourId = Label(labelframeleft, text="Your Id Number",
                          font=("times new roman", 11, "bold"))
        lblYourId.place(x=5, y=140)

        yourId = ttk.Entry(labelframeleft, textvariable=self.var_yourid)
        yourId.place(x=140, y=140, width=150)

        lblYourProblem = Label(labelframeleft, text="What's this about",
                               font=("times new roman", 11, "bold"))
        lblYourProblem.place(x=5, y=180)

        YourProb = ttk.Entry(labelframeleft, textvariable=self.var_about)
        YourProb.place(x=140, y=180, height=50, width=150)

        labelframeright = LabelFrame(self.root,
                                     bd=2,
                                     relief=RIDGE,
                                     font=("times new roman", 11, "bold"),
                                     text="Enter Your Problem here",
                                     padx=2,)

        labelframeright.place(x=310, y=50, width=300, height=300)

        lblproblem = Label(labelframeright, text="Enter here:",
                           font=("times new roman", 11, "bold"))
        lblproblem.place(x=5, y=10)

        probentry = ttk.Entry(labelframeright, textvariable=self.var_problem)
        probentry.place(x=9, y=40, width=270, height=230)

        labelframefarright = LabelFrame(self.root,
                                        bd=2,
                                        relief=RIDGE,
                                        font=("times new roman", 11, "bold"),
                                        text="Any Additional Messages",
                                        padx=2,)

        labelframefarright.place(x=615, y=50, width=270, height=300)

        lbladditional = Label(labelframefarright, text="Enter here:",
                              font=("times new roman", 11, "bold"))
        lbladditional.place(x=5, y=10)

        additionalentry = ttk.Entry(
            labelframefarright, textvariable=self.var_additional)
        additionalentry.place(x=9, y=40, width=230, height=230)

        submitbtn = Button(labelframeleft, text="Submit Report",
                           font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=4, relief=RAISED, command=self.report)
        submitbtn.place(x=12, y=236, width=270)

        lblframe = LabelFrame(self.root, text="Developer Details", font=("times new roman",
                                                                         11, "bold"), padx=2, bd=4, relief=RIDGE)
        lblframe.place(x=0, y=352, width=890, height=245)

        lblframe1 = LabelFrame(self.root, font=(
            "times new roman", 11, "bold"), padx=2, bd=6, relief=SUNKEN)
        lblframe1.place(x=20, y=376, width=355, height=208)

        lblframe2 = LabelFrame(self.root, font=(
            "times new roman", 11, "bold"), padx=2, bd=6, relief=RAISED)
        lblframe2.place(x=430, y=375, width=400, height=208)

        imgfoot = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\10.jpeg")
        imgfoot = imgfoot.resize((342, 197), Image.ANTIALIAS)
        self.photoimgfoot = ImageTk.PhotoImage(imgfoot)

        lblimgfoot = Label(
            self.root, image=self.photoimgfoot)
        lblimgfoot.place(x=27, y=383, width=342, height=197)

        lbl1 = Label(
            lblframe2, text="Made By:", font=("times new roman",
                                              15, "bold"))
        lbl1.place(x=10, y=10)

        lbl2 = Label(
            lblframe2, text="Gaurav Upadhyay", font=("times new roman",
                                                     15, "bold"))
        lbl2.place(x=130, y=10)

        lblimg3 = Label(
            lblframe2, text="Targeted Users:", font=("times new roman",
                                                     13, "bold"))
        lblimg3.place(x=10, y=50)

        lblimg4 = Label(
            lblframe2, text="Hotel Owners and Managers", font=("times new roman",
                                                               13, "bold"))
        lblimg4.place(x=140, y=50)

        lblimg5 = Label(
            lblframe2, text="Contact me:", font=("times new roman",
                                                 13, "bold"))
        lblimg5.place(x=10, y=90)

        lblimg6 = Label(
            lblframe2, text="9654494467", font=("times new roman",
                                                13, "bold"))
        lblimg6.place(x=130, y=90)

        lblimg52 = Label(
            lblframe2, text="Email me:", font=("times new roman",
                                               13, "bold"))
        lblimg52.place(x=10, y=130)

        lblimg62 = Label(
            lblframe2, text="gupadhyay8080@gmail.com", font=("times new roman",
                                                             13, "bold"))
        lblimg62.place(x=130, y=130)

        lblimg522 = Label(
            lblframe2, text="My Instagram:", font=("times new roman",
                                                   13, "bold"))
        lblimg522.place(x=10, y=170)

        lblimg622 = Label(
            lblframe2, text="@gauravupadhyayyy", font=("times new roman",
                                                       13, "bold"))
        lblimg622.place(x=130, y=170)

    def report(self):
        if self.var_hoteladdress.get() == "" or self.var_yourname.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required"
            )
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="gaurav4u7",
                    database="gaurav",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into report values(%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_hotelname.get(),
                        self.var_hoteladdress.get(),
                        self.var_yourname.get(),
                        self.var_yourid.get(),
                        self.var_about.get(),
                        self.var_problem.get(),
                        self.var_additional.get()
                    )
                )

                conn.commit()
                # self.fetch_data()
                conn.close()

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(self.senderemail, self.senderpass)

                # server.sendmail(self.senderemail, self.var_hotelname.get())
                server.sendmail(self.senderemail,
                                self.recieveremail, self.var_problem.get())

                messagebox.showinfo(
                    "success", "Report has been sent to developer"
                )

            except Exception as es:
                messagebox.showwarning(
                    "warning", f"Something went wrong:{str(es)}"
                )


if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()
