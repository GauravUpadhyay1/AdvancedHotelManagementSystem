from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1070x600")

        ####variables####
        self.var_Contact = StringVar()
        self.var_Checkin = StringVar()
        self.var_Checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        lbl_title = Label(
            self.root,
            text="ROOM BOOKING",
            font=("times new roman", 17, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE,
        )
        lbl_title.place(x=0, y=0, width=1070, height=50)

        ######LOGO############
        img2 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\grand-hotel-logo-inspiration-luxury-hotel-logo-template-inspiration-idea-grand-hotel-logo-inspiration-luxury-hotel-logo-template-169469853.jpg"
        )
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        ##########label frame############

        labelframeleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            font=("times new roman", 11, "bold"),
            text="Room Booking Details",
            padx=2,
        )
        labelframeleft.place(x=5, y=50, width=400, height=480)

        ####cust ref####
        lbl_cust_contact = Label(
            labelframeleft,
            text="Customer Contact",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(
            labelframeleft,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_Contact
        )
        entry_contact.grid(row=0, column=1, sticky=W)

        # fetch data button
        btnfetchdata = Button(
            labelframeleft,
            text="Fetch Data",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.fetch_contact

        )
        btnfetchdata.place(x=290, y=0)

        # checkin date

        lbl_checkin_date = Label(
            labelframeleft,
            text="Check_In_Date",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_checkin_date.grid(row=1, column=0, sticky=W)

        entry_checkin = ttk.Entry(
            labelframeleft,
            width=25,
            font=("times new roman", 11, "bold"), textvariable=self.var_Checkin
        )
        entry_checkin.grid(row=1, column=1)

        # checkout date
        lbl_checkout_date = Label(
            labelframeleft,
            text="Check_Out_Date",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_checkout_date.grid(row=2, column=0, sticky=W)

        entry_checkout = ttk.Entry(
            labelframeleft,
            width=25,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_Checkout
        )
        entry_checkout.grid(row=2, column=1)

        # room type
        room_type = Label(
            labelframeleft, text="Room Type:", font=("arial", 11, "bold"), padx=2, pady=5
        )
        room_type.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="gaurav4u7", database="gaurav"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = my_cursor.fetchall()

        combo_roomType = ttk.Combobox(
            labelframeleft,
            font=("arial", 11, "bold"),
            width=23,
            state="readonly",
            textvariable=self.var_roomtype
        )
        combo_roomType["value"] = ide
        combo_roomType.current(0)
        combo_roomType.grid(row=3, column=1)

        # Available room
        lblRoomAvailable = Label(
            labelframeleft,
            text="Available Rooms:",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        # entry_roomavailable = ttk.Entry(
        #     labelframeleft,
        #     width=25,
        #     font=("times new roman", 11, "bold"),
        #     textvariable=self.var_roomavailable
        # )
        # entry_roomavailable.grid(row=4, column=1)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="gaurav4u7", database="gaurav"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(
            labelframeleft,
            font=("arial", 11, "bold"),
            width=23,
            state="readonly",
            textvariable=self.var_roomavailable
        )
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # meal
        lblmeal = Label(
            labelframeleft,
            text="Meal:",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lblmeal.grid(row=5, column=0, sticky=W)

        entry_meal = ttk.Entry(
            labelframeleft,
            width=25,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_meal
        )
        entry_meal.grid(row=5, column=1)

        # number of days

        lbl_NumberOFdays = Label(
            labelframeleft,
            text="NO. Of Days:",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_NumberOFdays.grid(row=6, column=0, sticky=W)

        entry_NoOfDays = ttk.Entry(
            labelframeleft,
            width=25,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_noofdays
        )
        entry_NoOfDays.grid(row=6, column=1)

        # paid tax

        lbl_paidtax = Label(
            labelframeleft,
            text="Paid Tax:",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_paidtax.grid(row=7, column=0, sticky=W)

        entry_paidtax = ttk.Entry(
            labelframeleft,
            width=25,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_paidtax
        )
        entry_paidtax.grid(row=7, column=1)

        # subtotal
        lbl_subTotal = Label(
            labelframeleft,
            text="Sub Total:",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_subTotal.grid(row=8, column=0, sticky=W)

        entry_Subtotal = ttk.Entry(
            labelframeleft,
            width=25,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_actualtotal
        )
        entry_Subtotal.grid(row=8, column=1)

        # total cost

        lbl_totalcost = Label(
            labelframeleft,
            text="Total Cost",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_totalcost.grid(row=9, column=0, sticky=W)

        entry_totalcost = ttk.Entry(
            labelframeleft,
            width=25,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_total
        )
        entry_totalcost.grid(row=9, column=1)

        ####bill button######
        btnbill = Button(
            labelframeleft,
            text="Bill",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.total

        )
        btnbill.grid(row=10, column=0, padx=1, sticky=W)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=380, width=393, height=40)

        btnadd = Button(
            btn_frame,
            text="Add",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.add_data

        )
        btnadd.grid(row=0, column=0)

        btnUpdate = Button(
            btn_frame,
            text="Update",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.update

        )
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(
            btn_frame,
            text="Delete",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.nDelete

        )
        btnDelete.grid(row=0, column=2)

        btnReset = Button(
            btn_frame,
            text="Reset",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.reset

        )
        btnReset.grid(row=0, column=3)

        #right side image###

        img3 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\right.jpg"
        )
        img3 = img3.resize((315, 250), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg3.place(x=750, y=50, width=315, height=250)

        ########tableFrame search system###########
        tableframe = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            font=("times new roman", 11, "bold"),
            text="View Details And Search System",
            padx=2,
        )
        tableframe.place(x=400, y=280, width=665, height=250)

        lbl_searchby = Label(
            tableframe,
            text="Search By:",
            font=("arial", 11, "bold"),
            bg="red",
            fg="white",
        )
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(
            tableframe,
            font=("arial", 11, "bold"),
            width=16,
            state="readonly",
            textvariable=self.search_var,
        )
        combo_search["value"] = "Contact"
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        self.txt_search = StringVar()

        search = ttk.Entry(
            tableframe,
            width=20,
            textvariable=self.txt_search,
            font=("times new roman", 11, "bold"),
        )
        search.grid(row=0, column=2, padx=2)

        btnsearch = Button(
            tableframe,
            text="Search",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.search

        )
        btnsearch.grid(row=0, column=3, padx=2)

        btnshowall = Button(
            tableframe,
            text="Show All",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.fetch_data

        )
        btnshowall.grid(row=0, column=4, padx=2)

        ###show data###

        detailstable = Frame(tableframe, bd=2, relief=RIDGE)
        detailstable.place(x=5, y=50, width=652, height=175)

        Scroll_x = ttk.Scrollbar(detailstable, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(detailstable, orient=VERTICAL)

        self.room_table = ttk.Treeview(
            detailstable,
            column=(
                "contact",
                "checkin",
                "checkout",
                "roomtype",
                "roomavailable",
                "meal",
                "noOfdays",
            ),
            xscrollcommand=Scroll_x.set,
            yscrollcommand=Scroll_y.set,
        )

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Checkin")
        self.room_table.heading("checkout", text="Checkout")
        self.room_table.heading("roomtype", text="Roomtype")
        self.room_table.heading("roomavailable", text="RoomAvailable")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if self.var_Contact.get() == "" or self.var_Checkin.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
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
                    "insert into room values(%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_Contact.get(),
                        self.var_Checkin.get(),
                        self.var_Checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get()
                    ),
                )

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "success", "Room has been booked", parent=self.root
                )
            except Exception as es:
                messagebox.showwarning(
                    "warning", f"Something went wrong:{str(es)}", parent=self.root
                )

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="gaurav4u7", database="gaurav"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(
                *self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)

            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_rows = self.room_table.focus()
        content = self.room_table.item(cursor_rows)
        row = content["values"]

        self.var_Contact.set(row[0])
        self.var_Checkin.set(row[1])
        self.var_Checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

        # update

    def update(self):
        if self.var_Contact.get() == "":
            messagebox.showerror(
                "Error", "Please Enter Your Mobile Number", parent=self.root
            )

        else:

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="gaurav4u7",
                database="gaurav",
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE room SET checkin= %s , checkout = %s,roomtype = %s, roomavailable = %s  , meal = %s, noofdays = %s WHERE Contact = %s",
                (
                    self.var_Checkin.get(),
                    self.var_Checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_Contact.get(),
                ),
            )

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "update",
                "Room details have been updated successfully",
                parent=self.root,
            )

    def nDelete(self):
        nDelete = messagebox.askyesno(
            "Hotel Management System",
            "Do you want to delete this customer",
            parent=self.root,
        )
        if nDelete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="gaurav4u7",
                database="gaurav",
            )
            my_cursor = conn.cursor()
            query = "delete from room where Contact=%s"
            value = (self.var_Contact.get(),)
            my_cursor.execute(query, value)

        else:
            if not nDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_Contact.set("")
        self.var_Checkin.set("")
        self.var_Checkout.set("")
        # self.var_roomtype.set()
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

        #######all data#########

    def fetch_contact(self):
        if self.var_Contact.get() == "":
            messagebox.showerror(
                "Error", "Please Enter the Contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="gaurav4u7",
                database="gaurav",
            )
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile = %s")
            value = (self.var_Contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "This number is not found", parent=self.root)

            else:
                conn.commit
                conn.close

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=405, y=55, width=340, height=230)

                lblname = Label(showDataFrame, text="Name:",
                                font=("arial", 12, "bold"))
                lblname.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row,
                            font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="gaurav4u7",
                    database="gaurav",
                )
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile = %s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataFrame, text="Gender:",
                                  font=("arial", 12, "bold"))
                lblgender.place(x=0, y=30)

                lblg = Label(showDataFrame, text=row,
                             font=("arial", 12, "bold"))
                lblg.place(x=90, y=30)

                ###email###

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="gaurav4u7",
                    database="gaurav",
                )
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile = %s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataFrame, text="Email:",
                                 font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)

                lble = Label(showDataFrame, text=row,
                             font=("arial", 12, "bold"))
                lble.place(x=90, y=60)

                ###nationality###

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="gaurav4u7",
                    database="gaurav",
                )
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile = %s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblnation = Label(showDataFrame, text="Nationality:",
                                  font=("arial", 12, "bold"))
                lblnation.place(x=0, y=90)

                lbln = Label(showDataFrame, text=row,
                             font=("arial", 12, "bold"))
                lbln.place(x=90, y=90)

                ###address###

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="gaurav4u7",
                    database="gaurav",
                )
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile = %s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataFrame, text="Address:",
                                   font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=120)

                lbladd = Label(showDataFrame, text=row,
                               font=("arial", 12, "bold"))
                lbladd.place(x=90, y=120)

    ###search system#####

    def search(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="gaurav4u7",
            database="gaurav",
        )
        my_cursor = conn.cursor()

        my_cursor.execute(
            "select * from room where "
            + str(self.search_var.get())
            + " LIKE '%"
            + str(self.txt_search.get())
            + "%'"
        )

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_Checkin.get()
        outDate = self.var_Checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")

        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get() == "Breakfast" and self.var_roomtype.get()
                == "Luxury"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get()
                == "Luxury"):
            q1 = float(400)
            q2 = float(800)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get()
                == "Luxury"):
            q1 = float(500)
            q2 = float(900)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get()
                == "Double"):
            q1 = float(150)
            q2 = float(550)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get()
                == "Double"):
            q1 = float(200)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get()
                == "Double"):
            q1 = float(250)
            q2 = float(500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get()
                == "Single"):
            q1 = float(200)
            q2 = float(300)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get()
                == "Single"):
            q1 = float(200)
            q2 = float(400)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get()
                == "Single"):
            q1 = float(150)
            q2 = float(200)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get()
                == "Duplex"):
            q1 = float(550)
            q2 = float(800)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            tax = "Rs" + str("%.2f" % ((q5)*0.1))
            stotal = "Rs" + str("%.2f" % ((q5)))
            Ttotal = "Rs" + str("%.2f" % (q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(stotal)
            self.var_total.set(Ttotal)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
