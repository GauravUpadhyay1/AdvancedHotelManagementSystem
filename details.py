from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Detailsroom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1070x600")

        lbl_title = Label(
            self.root,
            text="ROOM DETAILS",
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

        img5 = Image.open(
            r"E:\Python\Final Project\Hotel Management System\img\imgdet.jpg"
        )
        img5 = img5.resize((1150, 210), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(self.root, image=self.photoimg5, bd=0, relief=RIDGE)
        lblimg5.place(x=0, y=393, width=1150, height=210)

        ##########label frame############

        labelframeleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            font=("times new roman", 11, "bold"),
            text="Add New Room",
            padx=2,
        )
        labelframeleft.place(x=5, y=50, width=530, height=340)

        ####floor####
        lbl_floor = Label(
            labelframeleft,
            text="Floor",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_floor.grid(row=0, column=0, sticky=W)
        self.var_floor = StringVar()

        entry_floor = ttk.Entry(
            labelframeleft,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_floor

        )
        entry_floor.grid(row=0, column=1, sticky=W)

        ####roomno####
        lbl_roomNo = Label(
            labelframeleft,
            text="Room No",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_roomNo.grid(row=1, column=0, sticky=W)

        self.var_roomno = StringVar()

        entry_roomNo = ttk.Entry(
            labelframeleft,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_roomno

        )
        entry_roomNo.grid(row=1, column=1, sticky=W)

        ####roomType####
        lbl_roomType = Label(
            labelframeleft,
            text="Room Type",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_roomType.grid(row=2, column=0, sticky=W)

        self.var_roomtype = StringVar()

        entry_roomType = ttk.Entry(
            labelframeleft,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.var_roomtype

        )
        entry_roomType.grid(row=2, column=1, sticky=W)

        ###buttons####

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=190, width=393, height=40)

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

        ########tableFrame search system###########
        tableframe = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            font=("times new roman", 11, "bold"),
            text="Show Room Details",
            padx=2,
        )
        tableframe.place(x=550, y=50, width=500, height=338)

        ###scroll###
        Scroll_x = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)

        self.room_table = ttk.Treeview(
            tableframe,
            column=(
                "floor",
                "roomno",
                "roomtype",
            ),
            xscrollcommand=Scroll_x.set,
            yscrollcommand=Scroll_y.set,
        )

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="RoomNo")
        self.room_table.heading("roomtype", text="RoomType")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        ####add data#

    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "":
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
                    "insert into details values(%s,%s,%s)",
                    (
                        self.var_floor.get(),
                        self.var_roomno.get(),
                        self.var_roomtype.get(),
                    ),
                )

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "success", "New Room has been added", parent=self.root
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
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])

    def update(self):
        if self.var_floor.get() == "":
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
                "UPDATE details SET Floor= %s , RoomType = %s WHERE RoomNo = %s",
                (
                    self.var_floor.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get(),
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
            "Do you want to delete these room details",
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
            query = "delete from details where RoomNo=%s"
            value = (self.var_roomno.get(),)
            my_cursor.execute(query, value)

        else:
            if not nDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")
        # self.var_roomtype.set()


if __name__ == "__main__":
    root = Tk()
    obj = Detailsroom(root)
    root.mainloop()
