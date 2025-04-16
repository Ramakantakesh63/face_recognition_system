from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
from pymysql import MySQLError

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\manoj\PycharmProjects\pythonProject2\Images_GUI\bgReg.jpg")

        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="#F2F2F2")
        frame.place(x=100, y=80, width=900, height=580)

        # img1=Image.open(r"C:\Users\Muhammad Waseem\Documents\Python_Test_Projects\Images_GUI\reg1.png")
        # img1=img1.resize((450,100),Image.llllllllll
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=300,y=100, width=500,height=100)

        get_str = Label(frame, text="Registration", font=("times new roman", 30, "bold"), fg="#002B53", bg="#F2F2F2")
        get_str.place(x=350, y=130)

        # label1
        fname = lb1 = Label(frame, text="First Name:", font=("times new roman", 15, "bold"), fg="#002B53", bg="#F2F2F2")
        fname.place(x=100, y=200)

        # entry1
        self.txtuser = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=103, y=225, width=270)

        # label2
        lname = lb1 = Label(frame, text="Last Name:", font=("times new roman", 15, "bold"), fg="#002B53", bg="#F2F2F2")
        lname.place(x=100, y=270)

        # entry2
        self.txtpwd = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=103, y=295, width=270)

        # ==================== section 2 -------- 2nd Columan===================

        # label1
        cnum = lb1 = Label(frame, text="Contact No:", font=("times new roman", 15, "bold"), fg="#002B53", bg="#F2F2F2")
        cnum.place(x=530, y=200)

        # entry1
        self.txtuser = ttk.Entry(frame, textvariable=self.var_cnum, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=533, y=225, width=270)

        # label2
        email = lb1 = Label(frame, text="Email:", font=("times new roman", 15, "bold"), fg="#002B53", bg="#F2F2F2")
        email.place(x=530, y=270)

        # entry2
        self.txtpwd = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=533, y=295, width=270)

        # ========================= Section 3 --- 1 Columan=================

        # label1
        ssq = lb1 = Label(frame, text="Select Security Question:", font=("times new roman", 15, "bold"), fg="#002B53",
                          bg="#F2F2F2")
        ssq.place(x=100, y=350)

        # Combo Box1
        self.combo_security = ttk.Combobox(frame, textvariable=self.var_ssq, font=("times new roman", 15, "bold"),
                                           state="readonly")
        self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103, y=375, width=270)

        # label2
        sa = lb1 = Label(frame, text="Security Answer:", font=("times new roman", 15, "bold"), fg="#002B53",
                         bg="#F2F2F2")
        sa.place(x=100, y=420)

        # entry2
        self.txtpwd = ttk.Entry(frame, textvariable=self.var_sa, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=103, y=445, width=270)

        # ========================= Section 4-----Column 2=============================

        # label1
        pwd = lb1 = Label(frame, text="Password:", font=("times new roman", 15, "bold"), fg="#002B53", bg="#F2F2F2")
        pwd.place(x=530, y=350)

        # entry1
        self.txtuser = ttk.Entry(frame, textvariable=self.var_pwd,show= '*', font=("times new roman", 15, "bold"))
        self.txtuser.place(x=533, y=375, width=270)

        # label2
        cpwd = lb1 = Label(frame, text="Confirm Password:", font=("times new roman", 15, "bold"), fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530, y=420)

        # entry2
        self.txtpwd = ttk.Entry(frame, textvariable=self.var_cpwd, font=("times new roman", 15, "bold"))
        self.txtpwd.place(x=533, y=445, width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree the Terms & Conditions",font=("times new roman", 13, "bold"), fg="#002B53", bg="#F2F2F2")
        checkbtn.place(x=100, y=480, width=270)

        # Creating Button Register
        loginbtn = Button(frame, command=self.reg, text="Register", font=("times new roman", 15, "bold"), bd=0, relief=RIDGE, fg="#fff", bg="#002B53", activeforeground="white", activebackground="#007ACC")
        loginbtn.place(x=103, y=510, width=270, height=35)

        # Creating Button Login
        loginbtn = Button(frame, text="Login",command=self.login, font=("times new roman", 15, "bold"), bd=0, relief=RIDGE, fg="#fff", bg="#002B53", activeforeground="white", activebackground="#007ACC")
        loginbtn.place(x=533, y=510, width=270, height=35)



    def reg(self):
        if (
                self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_cnum.get() == "" or self.var_email.get() == "" or self.var_ssq.get() == "Select" or self.var_sa.get() == "" or self.var_pwd.get() == "" or self.var_cpwd.get() == ""):
            messagebox.showerror("Error", "All Field Required!")
        elif (self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error", "Please Enter Password & Confirm Password are Same!")
        elif (self.var_check.get() == 0):
            messagebox.showerror("Error", "Please Check the Agree Terms and Conditons!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = pymysql.connect(user='root',
                    password='root',
                    host='localhost',
                    database='face_recognition',
                    port=3306)
                mycursor = conn.cursor()
                query = ("select * from regteach where email=%s")
                value = (self.var_email.get(),)
                mycursor.execute(query, value)
                row = mycursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exist,please try another email")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_cnum.get(),
                        self.var_email.get(),
                        self.var_ssq.get(),
                        self.var_sa.get(),
                        self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Successfully Registerd!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    def login(self):
        if self.txtuser.get() == "" or self.txtpwd.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        elif self.txtuser.get() == "admin" and self.txtpwd.get() == "admin":
            messagebox.showinfo("Success", "Welcome to Attendance Management System Using Facial Recognition")
            self.root.destroy()  # Close login window
            new_root = Tk()
            app = Face_Recognition_System(new_root)
            new_root.mainloop()
        else:
            try:
                conn = pymysql.connect(
                    user='root',
                    password='root',
                    host='localhost',
                    database='face_recognition',
                    port=3306
                )
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM regteach WHERE email=%s AND password=%s", (
                    self.txtuser.get(),
                    self.txtpwd.get()
                ))
                row = mycursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid username or password!")
                else:
                    open_min = messagebox.askyesno("Access Confirmation", "Access only for admin. Proceed?")
                    if open_min:
                        self.root.destroy()  # Close login window
                        new_root = Tk()
                        app = Face_Recognition_System(new_root)
                        new_root.mainloop()

            except Exception as e:
                messagebox.showerror("Error", f"Database error: {str(e)}")
            finally:
                if conn:
                    conn.close()

class Face_Recognition_System:
        def __init__(self, root):
            self.root = root
            self.root.geometry("1366x768+0+0")
            self.root.title("Face_Recogonition_System")

            # This part is image labels setting start
            # first header image
            img = Image.open(r"Images_GUI\banner.jpg")
            img = img.resize((1366, 130), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)

            # set image as lable
            f_lb1 = Label(self.root, image=self.photoimg)
            f_lb1.place(x=0, y=0, width=1366, height=130)

            # backgorund image
            bg1 = Image.open(r"Images_GUI\bg3.jpg")
            bg1 = bg1.resize((1366, 768), Image.LANCZOS)
            self.photobg1 = ImageTk.PhotoImage(bg1)

            # set image as lable
            bg_img = Label(self.root, image=self.photobg1)
            bg_img.place(x=0, y=130, width=1366, height=768)

            # title section
            title_lb1 = Label(bg_img, text="Attendance Managment System Using Facial Recognition",
                              font=("verdana", 30, "bold"), bg="white", fg="navyblue")
            title_lb1.place(x=0, y=0, width=1366, height=45)

            # Create buttons below the section
            # -------------------------------------------------------------------------------------------------------------------
            # student button 1
            std_img_btn = Image.open(r"Images_GUI\std1.jpg")
            std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
            self.std_img1 = ImageTk.PhotoImage(std_img_btn)

            std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
            std_b1.place(x=250, y=100, width=180, height=180)

            std_b1_1 = Button(bg_img, command=self.student_pannels, text="Student Pannel", cursor="hand2",
                              font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
            std_b1_1.place(x=250, y=280, width=180, height=45)

            # Detect Face  button 2
            det_img_btn = Image.open(r"Images_GUI\det1.jpg")
            det_img_btn = det_img_btn.resize((180, 180), Image.LANCZOS)
            self.det_img1 = ImageTk.PhotoImage(det_img_btn)

            det_b1 = Button(bg_img, command=self.face_rec, image=self.det_img1, cursor="hand2", )
            det_b1.place(x=480, y=100, width=180, height=180)

            det_b1_1 = Button(bg_img, command=self.face_rec, text="Face Detector", cursor="hand2",
                              font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
            det_b1_1.place(x=480, y=280, width=180, height=45)

            # Attendance System  button 3
            att_img_btn = Image.open(r"Images_GUI\att.jpg")
            att_img_btn = att_img_btn.resize((180, 180), Image.LANCZOS)
            self.att_img1 = ImageTk.PhotoImage(att_img_btn)

            att_b1 = Button(bg_img, command=self.attendance_pannel, image=self.att_img1, cursor="hand2", )
            att_b1.place(x=710, y=100, width=180, height=180)

            att_b1_1 = Button(bg_img, command=self.attendance_pannel, text="Attendance", cursor="hand2",
                              font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
            att_b1_1.place(x=710, y=280, width=180, height=45)

            # Help  Support  button 4
            hlp_img_btn = Image.open(r"Images_GUI\hlp.jpg")
            hlp_img_btn = hlp_img_btn.resize((180, 180), Image.LANCZOS)
            self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

            hlp_b1 = Button(bg_img, command=self.helpSupport, image=self.hlp_img1, cursor="hand2", )
            hlp_b1.place(x=940, y=100, width=180, height=180)

            hlp_b1_1 = Button(bg_img, command=self.helpSupport, text="Help Support", cursor="hand2",
                              font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
            hlp_b1_1.place(x=940, y=280, width=180, height=45)

            # Top 4 buttons end.......
            # ---------------------------------------------------------------------------------------------------------------------------
            # Start below buttons.........
            # Train   button 5
            tra_img_btn = Image.open(r"Images_GUI\tra1.jpg")
            tra_img_btn = tra_img_btn.resize((180, 180), Image.LANCZOS)
            self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)

            tra_b1 = Button(bg_img, command=self.train_pannels, image=self.tra_img1, cursor="hand2", )
            tra_b1.place(x=250, y=330, width=180, height=180)

            tra_b1_1 = Button(bg_img, command=self.train_pannels, text="Data Train", cursor="hand2",
                              font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
            tra_b1_1.place(x=250, y=510, width=180, height=45)

            # Photo   button 6
            pho_img_btn = Image.open(r"Images_GUI\kkp.jpg")
            pho_img_btn = pho_img_btn.resize((180, 180), Image.LANCZOS)
            self.pho_img1 = ImageTk.PhotoImage(pho_img_btn)

            pho_b1 = Button(bg_img, command=self.open_img, image=self.pho_img1, cursor="hand2", )
            pho_b1.place(x=480, y=330, width=180, height=180)

            pho_b1_1 = Button(bg_img, command=self.open_img, text="photos", cursor="hand2", font=("tahoma", 15, "bold"),
                              bg="white", fg="navyblue")
            pho_b1_1.place(x=480, y=510, width=180, height=45)

            # Developers   button 7
            dev_img_btn = Image.open(r"Images_GUI\dev.jpg")
            dev_img_btn = dev_img_btn.resize((180, 180), Image.LANCZOS)
            self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)

            dev_b1 = Button(bg_img, command=self.developr, image=self.dev_img1, cursor="hand2", )
            dev_b1.place(x=710, y=330, width=180, height=180)

            dev_b1_1 = Button(bg_img, command=self.developr, text="Developers", cursor="hand2",
                              font=("tahoma", 15, "bold"),
                              bg="white", fg="navyblue")
            dev_b1_1.place(x=710, y=510, width=180, height=45)

            # exit   button 8
            exi_img_btn = Image.open(r"Images_GUI\exi.jpg")
            exi_img_btn = exi_img_btn.resize((180, 180), Image.LANCZOS)
            self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

            exi_b1 = Button(bg_img, command=self.Close, image=self.exi_img1, cursor="hand2", )
            exi_b1.place(x=940, y=330, width=180, height=180)

            exi_b1_1 = Button(bg_img, command=self.Close, text="Exit", cursor="hand2", font=("tahoma", 15, "bold"),
                              bg="white", fg="navyblue")
            exi_b1_1.place(x=940, y=510, width=180, height=45)

        # ==================Funtion for Open Images Folder==================
        def open_img(self):
            os.startfile("data_img")

        # ==================Functions Buttons=====================
        def student_pannels(self):
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)

        def train_pannels(self):
            self.new_window = Toplevel(self.root)
            self.app = Train(self.new_window)

        def face_rec(self):
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition(self.new_window)

        def attendance_pannel(self):
            self.new_window = Toplevel(self.root)
            self.app = Attendance(self.new_window)

        def developr(self):
            self.new_window = Toplevel(self.root)
            self.app = Developer(self.new_window)

        def helpSupport(self):
            self.new_window = Toplevel(self.root)
            self.app = Helpsupport(self.new_window)

        def Close(self):
            root.destroy()

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()