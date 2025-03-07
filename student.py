
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
from pymysql import MySQLError
from tkcalendar import DateEntry
import cv2



#import mysql.connector
#from mysql.connector import Error

conn = None
# Testing Connection


try:
    # Establishing the connection
    conn = pymysql.connect(
        user='root',
        password='root',
        host='localhost',
        database='face_recognition',
        port=3306
    )

    if conn.open:
        #print('Connected to MySQL database')

        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute("SHOW DATABASES")

        # Fetch all the databases
        data = cursor.fetchall()

        # Print the databases
        for db in data:
            print(db)

except MySQLError as e:
    print(f"Error: {e}")

finally:
    if conn and conn.open:
        cursor.close()
        conn.close()
        #print('MySQL connection is closed')
        


class Student:
    def __init__(self,root):
        self.root=root

        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_batch = StringVar()
        self.var_semester = StringVar()
        self.var_std_regdno = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mob = StringVar()
        self.var_address = StringVar()
        self.var_proctor = StringVar()
        #
        btn_frame = Frame(root)
        btn_frame.pack()
        #


        # This part is image labels setting start
        # first header image
        img=Image.open(r"C:\xampp\htdocs\Face Recognition System\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image
        bg1 = Image.open(r"C:\xampp\htdocs\Face Recognition System\Images_GUI\bg3.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome to Student Pannel", font=("verdana", 30, "bold"), bg="white",fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Creating Frame
        main_frame = Frame(bg_img, bd=2, bg="white")  # bd mean border
        main_frame.place(x=5, y=55, width=1355, height=510)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",font=("verdana", 12, "bold"), fg="navyblue")
        left_frame.place(x=10, y=10, width=660, height=480)

        # Current Course `
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course",font=("verdana", 12, "bold"), fg="navyblue")
        current_course_frame.place(x=10, y=5, width=635, height=150)

        # label Department
        dep_label = Label(current_course_frame, text="Department", font=("verdana", 12, "bold"), bg="white", fg="navyblue")
        dep_label.grid(row=0, column=0, padx=5, pady=15)

        # combo box
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, width=15, font=("verdana", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "CIVIL", "ETC", "MECH", "EL")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)
        # -----------------------------------------------------

        # label Course
        cou_label = Label(current_course_frame, text="Course", font=("verdana", 12, "bold"), bg="white", fg="navyblue")
        cou_label.grid(row=0, column=2, padx=5, pady=15)

        # combo box
        cou_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, width=15,font=("verdana", 12, "bold"), state="readonly")
        cou_combo["values"] = ("Select Course", "DIPLOMA", "POST DIPLOMA")
        cou_combo.current(0)
        cou_combo.grid(row=0, column=3, padx=5, pady=15, sticky=W)
        # -------------------------------------------------------------

        # label Year
        year_label = Label(current_course_frame, text="Batch", font=("verdana", 12, "bold"), bg="white", fg="navyblue")
        year_label.grid(row=1, column=0, padx=5, sticky=W)

        # combo box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_batch, width=15,
                                  font=("verdana", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select batch", "2022-25", "2023-26", "2024-27")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=15, sticky=W)

        # label Semester
        year_label = Label(current_course_frame, text="Semester", font=("verdana", 12, "bold"), bg="white",fg="navyblue")
        year_label.grid(row=1, column=2, padx=5, sticky=W)

        # combo box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, width=15, font=("verdana", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=5, pady=15, sticky=W)

        # Class Student Information
        class_Student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("verdana", 12, "bold"), fg="navyblue")
        class_Student_frame.place(x=10, y=160, width=635, height=230)

        # Student id
        studentId_label = Label(class_Student_frame, text="Regd.No:", font=("verdana", 12, "bold"), fg="navyblue",
                                bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_regdno, width=15,
                                    font=("verdana", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Student name
        student_name_label = Label(class_Student_frame, text="Name:", font=("verdana", 12, "bold"), fg="navyblue",
                                   bg="white")
        student_name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_name, width=15,
                                       font=("verdana", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Class Didvision
        student_div_label = Label(class_Student_frame, text="Class Division:", font=("verdana", 12, "bold"),
                                  fg="navyblue", bg="white")
        student_div_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, width=13, font=("verdana", 12, "bold"),
                                 state="readonly")
        div_combo["values"] = ("1st Half", "2nd Half")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Roll No
        student_roll_label = Label(class_Student_frame, text="Roll-No:", font=("verdana", 12, "bold"), fg="navyblue",
                                   bg="white")
        student_roll_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=15,
                                       font=("verdana", 12, "bold"))
        student_roll_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        student_gender_label = Label(class_Student_frame, text="Gender:", font=("verdana", 12, "bold"), fg="navyblue",
                                     bg="white")
        student_gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        # combo box
        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, width=13,
                                    font=("verdana", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        # Date of Birth
        student_dob_label = Label(class_Student_frame, text="DOB:", font=("verdana", 12, "bold"), fg="navyblue",bg="white")
        student_dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        student_dob_entry = DateEntry(class_Student_frame, textvariable=self.var_dob, width=15,font=("verdana", 12, "bold"), date_pattern="yyyy-mm-dd")
        student_dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)
        """
        student_dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=15,font=("verdana", 12, "bold"))
        student_dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)
        """

        # Email
        student_email_label = Label(class_Student_frame, text="Email:", font=("verdana", 12, "bold"), fg="navyblue",
                                    bg="white")
        student_email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=15,
                                        font=("verdana", 12, "bold"))
        student_email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone Number
        student_mob_label = Label(class_Student_frame, text="Mob:", font=("verdana", 12, "bold"), fg="navyblue",
                                  bg="white")
        student_mob_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_mob, width=15,
                                      font=("verdana", 12, "bold"))
        student_mob_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        student_address_label = Label(class_Student_frame, text="Address:", font=("verdana", 12, "bold"), fg="navyblue",
                                      bg="white")
        student_address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=15,
                                          font=("verdana", 12, "bold"))
        student_address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher Name
        student_tutor_label = Label(class_Student_frame, text="Proctor Name:", font=("verdana", 12, "bold"),
                                    fg="navyblue", bg="white")
        student_tutor_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame, textvariable=self.var_proctor, width=15,
                                        font=("verdana", 12, "bold"))
        student_tutor_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)
        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame, text="Take Photo Sample", variable=self.var_radio1,
                                    value="Yes")
        radiobtn1.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        radiobtn1 = ttk.Radiobutton(class_Student_frame, text="No Photo Sample", variable=self.var_radio1, value="No")
        radiobtn1.grid(row=5, column=1, padx=5, pady=5, sticky=W)
        # Button Frame
        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=390, width=635, height=60)
        # Button Frame
        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=390, width=635, height=60)
        # Save button
        save_btn = Button(btn_frame,command=self.add_data, text="Save", width=7, font=("verdana", 12, "bold"),fg="white", bg="navyblue")
        save_btn.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        # update button
        update_btn = Button(btn_frame,command=self.update_data ,text="Update", width=7, font=("verdana", 12, "bold"),fg="white", bg="navyblue")
        update_btn.grid(row=0, column=1, padx=5, pady=8, sticky=W)

        # delete button
        del_btn = Button(btn_frame,command=self.delete_data,  text="Delete", width=7, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        del_btn.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        # reset button
        reset_btn = Button(btn_frame,command=self.reset_data, text="Reset", width=7, font=("verdana", 12, "bold"),   fg="white", bg="navyblue")
        reset_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # take photo button
        take_photo_btn = Button(btn_frame,  text="Take Pic", width=9,  font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        take_photo_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        # update photo button
        update_photo_btn = Button(btn_frame, text="Update Pic", width=9, font=("verdana", 12, "bold"), fg="white",  bg="navyblue")
        update_photo_btn.grid(row=0, column=5, padx=5, pady=10, sticky=W)

        #def add_data(self):
        # Define the functionality you want when the Save button is clicked
        #print("Data saved successfully")




        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",font=("verdana", 12, "bold"), fg="navyblue")
        right_frame.place(x=680, y=10, width=660, height=480)

        # Searching System in Right Label Frame
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font=("verdana", 12, "bold"), fg="navyblue")
        search_frame.place(x=10, y=5, width=635, height=80)
        # Phone Number
        search_label = Label(search_frame, text="Search:", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.var_searchTX = StringVar()
        # combo box
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchTX, width=12, font=("verdana", 12, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Roll-No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=12, font=("verdana", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame,  text="Search", width=9,font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        search_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        showAll_btn = Button(search_frame, text="Show All", width=8,font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        showAll_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        # Table Frame
        # Searching System in Right Label Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=90, width=635, height=360)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # create table
        self.student_table = ttk.Treeview(table_frame, column=("Regd_no", "Name", "Dep", "Course", "Batch", "Sem", "Divi", "Gender", "DOB", "Mob", "Address", "Roll", "Email", "Proctor", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Regd_no", text="Regd_no")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Batch", text="Batch")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Divi", text="Division")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Mob", text="Mob")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Roll", text="RollNo")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Proctor", text="Proctor")
        self.student_table.heading("Photo", text="PhotoSample")
        self.student_table["show"] = "headings"

        # Set Width of Colums
        self.student_table.column("Regd_no", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Batch", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Divi", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Mob", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Proctor", width=100)
        self.student_table.column("Photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


        # ==================Function Decleration==============================
    def add_data(self):
            if self.var_dep.get() == "Select Department" or self.var_course.get == "Select Course" or self.var_batch.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_regdno.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "" or self.var_proctor.get() == "":
                messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
            else:
                try:
                    conn = pymysql.connect(
                        user='root',
                        password='root',
                        host='localhost',
                        database='face_recognition',
                        port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_std_regdno.get(),
                        self.var_std_name.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_batch.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_mob.get(),
                        self.var_address.get(),
                        self.var_roll.get(),
                        self.var_email.get(),
                        self.var_proctor.get(),
                        self.var_radio1.get()
                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "All Records are Saved!", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

# ===========================Fetch data form database to table ================================

    def fetch_data(self):
                 conn = pymysql.connect(
                            user='root',
                            password='root',
                            host='localhost',
                            database='face_recognition',
                            port=3306)

                 mycursor = conn.cursor()

                 mycursor.execute("select *from student")
                 data = mycursor.fetchall()

                 if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                 conn.close()

                 # ================================get cursor function=======================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_regdno.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_batch.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_proctor.set(data[13]),
        self.var_radio1.set(data[14])

    def update_data(self):
            if self.var_dep.get() == "Select Department" or self.var_course.get == "Select Course" or self.var_batch.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_regdno.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "" or self.var_proctor.get() == "":
                messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
            else:
                try:
                    Update = messagebox.askyesno("Update", "Do you want to Update this Student Details!",parent=self.root)
                    if Update > 0:
                        conn = pymysql.connect(
                            user='root',
                            password='root',
                            host='localhost',
                            database='face_recognition',
                            port=3306
                        )
                        mycursor = conn.cursor()
                        mycursor.execute(
                            "update student set Name=%s,Dep=%s,Course=%s,Batch=%s,Sem=%s,Divi=%s,Gender=%s,DOB=%s,Mob=%s,Address=%s,Roll=%s,Email=%s,Proctor=%s,Photo=%s where Regd_no=%s",
                            (
                                self.var_std_name.get(),
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_batch.get(),
                                self.var_semester.get(),
                                self.var_div.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_mob.get(),
                                self.var_address.get(),
                                self.var_roll.get(),
                                self.var_email.get(),
                                self.var_proctor.get(),
                                self.var_radio1.get(),
                                self.var_std_regdno.get()
                            ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success", "Successfully Updated!", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            # ==============================Delete Function=========================================

    def delete_data(self):
        if self.var_std_regdno.get() == "":
            messagebox.showerror("Error", "Student Id Must be Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root)
                if delete > 0:
                    conn = pymysql.connect(
                        user='root',
                        password='root',
                        host='localhost',
                        database='face_recognition',
                        port=3306)
                    mycursor = conn.cursor()
                    sql = "delete from student where Regd_no=%s"
                    val = (self.var_std_regdno.get(),)
                    mycursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully Deleted!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

                # Reset Function

    def reset_data(self):
                self.var_std_regdno.set(""),
                self.var_std_name.set(""),
                self.var_dep.set("Select Department"),
                self.var_course.set("Select Course"),
                self.var_batch.set("Select Year"),
                self.var_semester.set("Select Semester"),
                self.var_div.set("Morning"),
                self.var_gender.set("Male"),
                self.var_dob.set(""),
                self.var_mob.set(""),
                self.var_address.set(""),
                self.var_roll.set(""),
                self.var_email.set(""),
                self.var_proctor.set(""),
                self.var_radio1.set("")


            # main class object

if __name__ == "__main__":
        root = Tk()
        obj = Student(root)
        root.mainloop()
