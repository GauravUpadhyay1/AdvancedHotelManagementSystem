from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1070x600")

        ###########variables$#############
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()

        ##########title############
        lbl_title = Label(
            self.root,
            text="ADD CUST0MER DETAILS",
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
            text="Customer Details",
            padx=2,
        )
        labelframeleft.place(x=5, y=50, width=400, height=480)

        ########labels and entries########
        ####cust ref####
        lbl_cust = Label(
            labelframeleft,
            text="Customer Ref",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_cust.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(
            labelframeleft,
            textvariable=self.var_ref,
            width=20,
            font=("times new roman", 11, "bold"),
            state="readonly",
        )
        entry_ref.grid(row=0, column=1)

        ####cust name####
        cust_name = Label(
            labelframeleft,
            text="Customer Name",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        cust_name.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(
            labelframeleft,
            textvariable=self.var_name,
            width=20,
            font=("times new roman", 11, "bold"),
        )
        txtcname.grid(row=1, column=1)

        ####mother name####
        mother_name = Label(
            labelframeleft,
            text="Mothers Name",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        mother_name.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(
            labelframeleft,
            textvariable=self.var_mother,
            width=20,
            font=("times new roman", 11, "bold"),
        )
        txtmname.grid(row=2, column=1)

        ####gender combo box####
        gender = Label(
            labelframeleft, text="Gender", font=("arial", 11, "bold"), padx=2, pady=5
        )
        gender.grid(row=3, column=0, sticky=W)

        combo_Gender = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_gender,
            font=("arial", 11, "bold"),
            width=18,
            state="readonly",
        )
        combo_Gender["value"] = ("Male", "Female", "Other")
        combo_Gender.current(0)
        combo_Gender.grid(row=3, column=1)

        ####post code####
        lblpost_code = Label(
            labelframeleft, text="PostCode", font=("arial", 11, "bold"), padx=2, pady=5
        )
        lblpost_code.grid(row=4, column=0, sticky=W)

        txtpostcode = ttk.Entry(
            labelframeleft,
            textvariable=self.var_post,
            width=20,
            font=("times new roman", 11, "bold"),
        )
        txtpostcode.grid(row=4, column=1)

        ####mobile number####
        lblmob_Num = Label(
            labelframeleft,
            text="Mobile Number",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lblmob_Num.grid(row=5, column=0, sticky=W)

        txtMob = ttk.Entry(
            labelframeleft,
            textvariable=self.var_mobile,
            width=20,
            font=("times new roman", 11, "bold"),
        )
        txtMob.grid(row=5, column=1)

        ####email####
        lblemail = Label(
            labelframeleft, text="Email Id", font=("arial", 11, "bold"), padx=2, pady=5
        )
        lblemail.grid(row=6, column=0, sticky=W)

        txtemail = ttk.Entry(
            labelframeleft,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 11, "bold"),
        )
        txtemail.grid(row=6, column=1)

        ####Nationality####
        lbl_nation = Label(
            labelframeleft,
            text="Nationality",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_nation.grid(row=7, column=0, sticky=W)
        combo_nation = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_nationality,
            font=("arial", 11, "bold"),
            width=18,
            state="readonly",
        )
        combo_nation["value"] = ("Indian", "American", "British")
        combo_nation.current(0)
        combo_nation.grid(row=7, column=1)

        ####Id proof combobox####
        lbl_id = Label(
            labelframeleft,
            text="Id Proof Type",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_id.grid(row=8, column=0, sticky=W)

        combo_idproof = ttk.Combobox(
            labelframeleft,
            textvariable=self.var_idproof,
            font=("arial", 11, "bold"),
            width=18,
            state="readonly",
        )
        combo_idproof["value"] = ("AdharCard", "DriversLicence", "Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)

        ##Id number number####
        lbl_idNum = Label(
            labelframeleft, text="Id Number", font=("arial", 11, "bold"), padx=2, pady=5
        )
        lbl_idNum.grid(row=9, column=0, sticky=W)
        Idnum = ttk.Entry(
            labelframeleft,
            textvariable=self.var_idnumber,
            width=20,
            font=("times new roman", 11, "bold"),
        )
        Idnum.grid(row=9, column=1)

        ##address####
        lbl_Address = Label(
            labelframeleft, text="Address", font=("arial", 11, "bold"), padx=2, pady=5
        )
        lbl_Address.grid(row=10, column=0, sticky=W)
        txtAdd = ttk.Entry(
            labelframeleft,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 11, "bold"),
        )
        txtAdd.grid(row=10, column=1)

        #####buttons####
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=380, width=393, height=40)

        btnadd = Button(
            btn_frame,
            text="Add",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.add_data,
        )
        btnadd.grid(row=0, column=0)

        btnUpdate = Button(
            btn_frame,
            text="Update",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.Update,
        )
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(
            btn_frame,
            text="Delete",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.nDelete,
        )
        btnDelete.grid(row=0, column=2)

        btnReset = Button(
            btn_frame,
            text="Reset",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.reset,
        )
        btnReset.grid(row=0, column=3)

        ########tableFrame###########
        tableframe = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            font=("times new roman", 11, "bold"),
            text="View Details And Search System",
            padx=2,
        )
        tableframe.place(x=400, y=50, width=665, height=480)

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
        combo_search["value"] = "Mobile"
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
            command=self.search,
        )
        btnsearch.grid(row=0, column=3, padx=2)

        btnshowall = Button(
            tableframe,
            text="Show All",
            font=("times new roman", 11, "bold"),
            bg="black",
            fg="gold",
            width=10,
            command=self.fetch_data,
        )
        btnshowall.grid(row=0, column=4, padx=2)

        ###########show data table###########
        frameDetails = Frame(tableframe, bd=2, relief=RIDGE)
        frameDetails.place(x=5, y=50, width=652, height=350)

        Scroll_x = ttk.Scrollbar(frameDetails, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(frameDetails, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(
            frameDetails,
            column=(
                "ref",
                "name",
                "mother",
                "gender",
                "post",
                "mobile",
                "email",
                "nationality",
                "idproof",
                "idnumber",
                "address",
            ),
            xscrollcommand=Scroll_x.set,
            yscrollcommand=Scroll_y.set,
        )

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.Cust_Details_Table.xview)
        Scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_email.get() == "":
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
                    "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_ref.get(),
                        self.var_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_idproof.get(),
                        self.var_idnumber.get(),
                        self.var_address.get(),
                    ),
                )

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "success", "Customer has been added", parent=self.root
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
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_rows = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_rows)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])

    def Update(self):
        if self.var_mobile.get() == "":
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
                "UPDATE customer SET Name = %s, Mother= %s , Gender = %s, PostCode = %s,Mobile = %s, Email = %s  , Nationality = %s, Idproof = %s, Idnumber = %s, Address= %s WHERE Ref = %s",
                (
                    self.var_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_idproof.get(),
                    self.var_idnumber.get(),
                    self.var_address.get(),
                    self.var_ref.get(),
                ),
            )

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "update",
                "customer details have been updated successfully",
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
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)

        else:
            if not nDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set("")
        self.var_name.set("")
        self.var_mother.set("")
        # self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        # self.var_nationality.set("")
        # self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_address.set("")
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="gaurav4u7",
            database="gaurav",
        )
        my_cursor = conn.cursor()

        my_cursor.execute(
            "select * from customer where "
            + str(self.search_var.get())
            + " LIKE '%"
            + str(self.txt_search.get())
            + "%'"
        )

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
