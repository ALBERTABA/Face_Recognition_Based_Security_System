from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1250x700+0+0")

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

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\bgReg.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=100,y=40,width=900,height=560)
        
        get_str = Label(frame,text="Register",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=100)

        # First Name
        fname = Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)

        # Last Name
        lname = Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=270)
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)

        # Contact Number
        cnum = Label(frame,text="Contact Number:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=200)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=225,width=270)

        # Email
        email = Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)

        # Security Question
        ssq = Label(frame,text="Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=100,y=350)
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Date of Birth","Nick Name","Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)

        # Security Answer
        sa = Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=100,y=420)
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=445,width=270)

        # Password
        pwd = Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=350)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"), show="*")
        self.txtuser.place(x=533,y=375,width=270)

        # Confirm Password
        cpwd = Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=420)
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"), show="*")
        self.txtpwd.place(x=533,y=445,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="Agree to Terms and Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)

        # Register Button
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)

        # Login Button
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=533,y=510,width=270,height=35)

    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All fields are required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Password and Confirm Password must be the same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please agree to the Terms and Conditions!")
        else:
            try:
                conn = mysql.connector.connect(username='root', password='admin',host='localhost',database='face_recognizer',port=3306)
                mycursor = conn.cursor()
                query=("select * from regteach where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exists, please try a different email")
                else:
                    mycursor.execute("insert into regteach (fname, lname, cnum, email, ssq, sa, pwd) values (%s,%s,%s,%s,%s,%s,%s)",(
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
                    messagebox.showinfo("Success","Registration Successful!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
