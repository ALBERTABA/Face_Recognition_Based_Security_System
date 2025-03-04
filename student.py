from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# Testing Connection 
"""
conn = mysql.connector.connect(username='root', password='admin',host='127.0.0.1',database='face_recognizer',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x700+0+0")
        self.root.title("Face Recognition-Based Security System")

        #-----------Variables-------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\banner.jpg")
        img=img.resize((1250,120),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1250,height=120)

        # background image 
        bg1=Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1250,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1250,height=768)


        # title section
        title_lb1 = Label(bg_img,text="Registered Individuals Management",font=("verdana",25,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1250,height=40)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd means border 
        main_frame.place(x=0,y=40,width=1250,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Individual Information",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        # Profile Details 
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Profile Details",font=("verdana",10,"bold"),fg="navyblue")
        current_course_frame.place(x=10,y=5,width=635,height=150)

        # Label for Category
        dep_label=Label(current_course_frame,text="Category",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=5,pady=15)

        # combo box for Category
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select","Theft","Assault","Fraud","Child abuse","Domestic abuse","Kidnapping","Other")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        # Label for Offense
        cou_label=Label(current_course_frame,text="Offense",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=0,column=2,padx=5,pady=15)

        # combo box for Offense
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("verdana",12,"bold"),state="readonly")
        cou_combo["values"]=("Select","Felonies","Infractions","Indictable offenses","Crimes against a person","Crimes against property","Crimes against society","Fraud","Other")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)
        

        # Label for Year (Incident Year)
        year_label=Label(current_course_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        # combo box for Year
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select","2025","2026","2027","2028","2029","2030")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        # Label for Status
        year_label=Label(current_course_frame,text="Status",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=2,padx=5,sticky=W)

        # combo box for Status
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select","Wanted","Cleared")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=15,sticky=W)

        # Profile Summary
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Profile Summary",font=("verdana",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=10,y=160,width=635,height=230)

        # ID
        studentId_label = Label(class_Student_frame,text="ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        # Name
        student_name_label = Label(class_Student_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        # Shift (Previously Class session)
        student_div_label = Label(class_Student_frame,text="Shift",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=13,font=("verdana",12,"bold"),state="readonly")
        div_combo["values"]=("Morning","Afternoon","Evening")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        # Record No (Previously Roll-No)
        student_roll_label = Label(class_Student_frame,text="Record No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        # Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        # combo box for Gender
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        # DOB
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # Email (Contact Email)
        student_email_label = Label(class_Student_frame,text="Contact Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        # Mobile
        student_mob_label = Label(class_Student_frame,text="Mobile:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        # Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        # Assigned Officer (Previously Lecturer)
        student_tutor_label = Label(class_Student_frame,text="Assigned Officer:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_tutor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("verdana",12,"bold"))
        student_tutor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        # Radio Buttons for photo capture
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take a photo",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn1=ttk.Radiobutton(class_Student_frame,text="No photo",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        # Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        # Save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        # Update button
        update_btn=Button(btn_frame,command=self.update_data,text="Edit",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        # Delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        # Reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        # Take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take a photo",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # Edit photo button
        update_photo_btn=Button(btn_frame,text="Edit Photo",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)

        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Records List",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)

        # Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=635,height=80)

        # Label for Search
        search_label = Label(search_frame,text="Search by:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        # combo box for search criteria
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Record No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        """ showAll_btn=Button(search_frame,command=self.fetch_data,text="Tất cả",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W) """

        # -----------------------------Table Frame-------------------------------------------------
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        # Scroll bars 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        # Create table 
        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","Dep","Course","Year","Sem","Div","Gender","DOB","Mob-No","Address","Roll-No","Email","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Dep",text="Category")
        self.student_table.heading("Course",text="Offense")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Status")
        self.student_table.heading("Div",text="Shift")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Mob-No",text="Mobile")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Roll-No",text="Record No")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Teacher",text="Officer")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        # Set width of columns 
        self.student_table.column("ID",width=20)
        self.student_table.column("Name",width=100)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Mob-No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Declarations==============================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please fill in all required fields!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='admin',host='127.0.0.1',database='face_recognizer',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All records have been saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data from database to table ================================
    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='admin',host='127.0.0.1',database='face_recognizer',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================Get cursor function=======================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please fill in all required fields!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to edit it again?",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='admin',host='127.0.0.1',database='face_recognizer',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where ID=%s",( 
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Updated Successfully!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete it?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='admin',host='127.0.0.1',database='face_recognizer',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where ID=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted Successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set(""),
        self.var_course.set(""),
        self.var_year.set(""),
        self.var_semester.set(""),
        self.var_div.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='admin',host='127.0.0.1',database='face_recognizer',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT ID,Name,Department,Course,Year,Semester,Division,Gender,DOB,Mobile_No,Address,Roll_No,Email,Teacher_Name,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please fill in all required fields!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='admin',host='127.0.0.1',database='face_recognizer',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where ID=%s",( 
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # convert to gray scale
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor 1.3, Minimum neighbor 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/stdudent."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset creation completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


# main class object
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
