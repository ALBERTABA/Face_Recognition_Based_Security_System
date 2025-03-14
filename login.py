from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
# --------------------------
from train import Train
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
import os


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1250x700+0+0")

        # variables 
        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\loginBg1.jpg")
        
        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(self.root, bg="#002B53")
        frame1.place(x=500, y=120, width=340, height=450)

        img1 = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\log1.png")
        img1 = img1.resize((100,100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1, bg="#002B53")
        lb1img1.place(x=620, y=125, width=100, height=100)

        get_str = Label(frame1, text="Login", font=("times new roman",20,"bold"), fg="white", bg="#002B53")
        get_str.place(x=100, y=100)

        # label1 
        username = Label(frame1, text="Email:", font=("times new roman",15,"bold"), fg="white", bg="#002B53")
        username.place(x=30, y=160)

        # entry1 
        self.txtuser = ttk.Entry(frame1, font=("times new roman",15,"bold"))
        self.txtuser.place(x=33, y=190, width=270)

        # label2 
        pwd = Label(frame1, text="Password:", font=("times new roman",15,"bold"), fg="white", bg="#002B53")
        pwd.place(x=30, y=230)

        # entry2 
        self.txtpwd = ttk.Entry(frame1, font=("times new roman",15,"bold"), show="*")
        self.txtpwd.place(x=33, y=260, width=270)

        # Creating Button Login
        loginbtn = Button(frame1, command=self.login, text="Login", font=("times new roman",15,"bold"), bd=0, relief=RIDGE, fg="#002B53", bg="white", activeforeground="white", activebackground="#007ACC")
        loginbtn.place(x=33, y=320, width=270, height=35)

        # Creating Button Registration
        loginbtn = Button(frame1, command=self.reg, text="Register", font=("times new roman",10,"bold"), bd=0, relief=RIDGE, fg="white", bg="#002B53", activeforeground="orange", activebackground="#002B53")
        loginbtn.place(x=33, y=370, width=50, height=20)

        # Creating Button Forget
        loginbtn = Button(frame1, command=self.forget_pwd, text="Forgot Password", font=("times new roman",10,"bold"), bd=0, relief=RIDGE, fg="white", bg="#002B53", activeforeground="orange", activebackground="#002B53")
        loginbtn.place(x=90, y=370, width=100, height=20)

    # This function is for open register window
    def reg(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if (self.txtuser.get() == "" or self.txtpwd.get() == ""):
            messagebox.showerror("Error", "All fields are required!")
        elif(self.txtuser.get() == "admin" and self.txtpwd.get() == "admin"):
            messagebox.showinfo("Successfully", "Welcome to the Face Recognition Attendance Management System")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='admin', host='localhost', database='face_recognizer', port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s", (
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid email or password!")
            else:
                open_min = messagebox.askyesno("Admin", "Admin access only")
                if open_min > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()

    #=======================Reset Password Function=============================
    def reset_pass(self):
        if self.var_ssq.get() == "Select":
            messagebox.showerror("Error", "Select a security question!", parent=self.root2)
        elif(self.var_sa.get() == ""):
            messagebox.showerror("Error", "Please enter the answer!", parent=self.root2)
        elif(self.var_pwd.get() == ""):
            messagebox.showerror("Error", "Please enter a new password!", parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='admin', host='localhost', database='face_recognizer', port=3306)
            mycursor = conn.cursor()
            query = ("select * from regteach where email=%s and s_que=%s and s_ans=%s")
            value = (self.txtuser.get(), self.var_ssq.get(), self.var_sa.get())
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please provide the correct answer!", parent=self.root2)
            else:
                query = ("update regteach set pwd=%s where email=%s")
                value = (self.var_pwd.get(), self.txtuser.get())
                mycursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Success! Your password has been reset. Please log in with the new password!", parent=self.root2)
                
# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter your email ID to reset your password!")
        else:
            conn = mysql.connector.connect(username='root', password='admin', host='localhost', database='face_recognizer', port=3306)
            mycursor = conn.cursor()
            query = ("select * from regteach where email=%s")
            value = (self.txtuser.get(),)
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please enter a valid email ID!")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+610+170")
                l = Label(self.root2, text="Forgot Password", font=("times new roman",30,"bold"), fg="#002B53", bg="#fff")
                l.place(x=0, y=10, relwidth=1)
                # -------------------fields-------------------
                # label1 
                ssq = Label(self.root2, text="Select security question:", font=("times new roman",15,"bold"), fg="#002B53", bg="#F2F2F2")
                ssq.place(x=70, y=80)

                # Combo Box1
                self.combo_security = ttk.Combobox(self.root2, textvariable=self.var_ssq, font=("times new roman",15,"bold"), state="readonly")
                self.combo_security["values"] = ("Select", "Date of Birth", "Nickname", "Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70, y=110, width=270)

                # label2 
                sa = Label(self.root2, text="Answer:", font=("times new roman",15,"bold"), fg="#002B53", bg="#F2F2F2")
                sa.place(x=70, y=150)

                # entry2 
                self.txtpwd = ttk.Entry(self.root2, textvariable=self.var_sa, font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70, y=180, width=270)

                # label2 
                new_pwd = Label(self.root2, text="New Password:", font=("times new roman",15,"bold"), fg="#002B53", bg="#F2F2F2")
                new_pwd.place(x=70, y=220)

                # entry2 
                self.new_pwd = ttk.Entry(self.root2, textvariable=self.var_pwd, font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70, y=250, width=270)

                # Creating Button New Password
                loginbtn = Button(self.root2, command=self.reset_pass, text="Reset Password", font=("times new roman",15,"bold"), bd=0, relief=RIDGE, fg="#fff", bg="#002B53", activeforeground="white", activebackground="#007ACC")
                loginbtn.place(x=70, y=300, width=270, height=35)


# =====================main program Face recognition system====================

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title("Face Recognition Attendance Management System")

        # This part is image labels setting start 
        # first header image  
        img = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\banner.jpg")
        img = img.resize((1366,130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1250, height=120)

        # background image 
        bg1 = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\bg3.jpg")
        bg1 = bg1.resize((1250,768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1250, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Face Recognition Attendance Management System", font=("verdana",20,"bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1250, height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\std1.jpg")
        std_img_btn = std_img_btn.resize((180,180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
        std_b1.place(x=220, y=100, width=180, height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Registered Individuals",cursor="hand2",font=("tahoma",11,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=220,y=250,width=180,height=40)

        # Detect Face button 2
        det_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\det1.jpg")
        det_img_btn = det_img_btn.resize((180,180), Image.LANCZOS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.face_rec, image=self.det_img1, cursor="hand2")
        det_b1.place(x=450, y=100, width=180, height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text=" Criminal Detection",cursor="hand2",font=("tahoma",13,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=450,y=250,width=180,height=40)

        # Attendance System button 3
        att_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\att.jpg")
        att_img_btn = att_img_btn.resize((180,180), Image.LANCZOS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.attendance_pannel, image=self.att_img1, cursor="hand2")
        att_b1.place(x=680, y=100, width=180, height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Criminal Records",cursor="hand2",font=("tahoma",13,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=680,y=250,width=180,height=40)

        # Help Support button 4
        hlp_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\hlp.jpg")
        hlp_img_btn = hlp_img_btn.resize((180,180), Image.LANCZOS)
        self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img, command=self.helpSupport, image=self.hlp_img1, cursor="hand2")
        hlp_b1.place(x=910, y=100, width=180, height=180)

        hlp_b1_1 = Button(bg_img,command=self.helpSupport,text="Law Enforcement Assistance",cursor="hand2",font=("tahoma",9,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=910,y=250,width=180,height=40)
        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
        # Train button 5
        tra_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\tra1.jpg")
        tra_img_btn = tra_img_btn.resize((180,180), Image.LANCZOS)
        self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img, command=self.train_pannels, image=self.tra_img1, cursor="hand2")
        tra_b1.place(x=220, y=300, width=180, height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Update Criminal Database",cursor="hand2",font=("tahoma",9,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=220,y=450,width=180,height=40)

        # Photo button 6
        pho_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\qr1.png")
        pho_img_btn = pho_img_btn.resize((180,180), Image.LANCZOS)
        self.pho_img1 = ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img, command=self.open_img, image=self.pho_img1, cursor="hand2")
        pho_b1.place(x=450, y=300, width=180, height=180)


        pho_b1_1 = Button(bg_img,command=self.open_img,text="QR CODE",cursor="hand2",font=("tahoma",11,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=450,y=450,width=180,height=40)

        # Developers button 7
        dev_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\dev.jpg")
        dev_img_btn = dev_img_btn.resize((180,180), Image.LANCZOS)
        self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img, command=self.developr, image=self.dev_img1, cursor="hand2")
        dev_b1.place(x=680, y=300, width=180, height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="System Administrators",cursor="hand2",font=("tahoma",11,"bold"),bg="white",fg="navyblue")
        dev_b1_1.place(x=680,y=450,width=180,height=40)

        # Exit button 8
        exi_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\exi.jpg")
        exi_img_btn = exi_img_btn.resize((180,180), Image.LANCZOS)
        self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img, command=self.Close, image=self.exi_img1, cursor="hand2")
        exi_b1.place(x=910, y=300, width=180, height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Shutdown Security System",cursor="hand2",font=("tahoma",10,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=910,y=450,width=180,height=40)

# ==================Function for Open Images Folder==================
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

    def open_img(self):
        os.startfile("dataset")
    

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
