import re
from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

# Global variable for importCsv Function 
mydata = []

class Attendance:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title("Face Recognition Based Security System")

        # -----------Variables-------------------
        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attend = StringVar()

        # This part is image labels setting start 
        # first header image  
        img = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\banner.jpg")
        img = img.resize((1250, 120), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1250, height=120)

        # background image 
        bg1 = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\bg3.jpg")
        bg1 = bg1.resize((1250, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1250, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Face Recognition Based Security System", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1250, height=40)

        # ========================Section Creating==================================
        # Creating Frame 
        main_frame = Frame(bg_img, bd=2, bg="white")  # bd means border 
        main_frame.place(x=0, y=40, width=1300, height=480)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student", font=("verdana", 12, "bold"), fg="navyblue")
        left_frame.place(x=10, y=10, width=660, height=480)

        # ==================================Text boxes and Combo Boxes====================
        # Student id
        studentId_label = Label(left_frame, text="ID:", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentId_entry = ttk.Entry(left_frame, textvariable=self.var_id, width=15, font=("verdana", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Student Roll
        student_roll_label = Label(left_frame, text="Roll.No:", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        student_roll_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        student_roll_entry = ttk.Entry(left_frame, textvariable=self.var_roll, width=15, font=("verdana", 12, "bold"))
        student_roll_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Student Name
        student_name_label = Label(left_frame, text="Name:", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        student_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        student_name_entry = ttk.Entry(left_frame, textvariable=self.var_name, width=15, font=("verdana", 12, "bold"))
        student_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Time
        time_label = Label(left_frame, text="Time:", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        time_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        time_entry = ttk.Entry(left_frame, textvariable=self.var_time, width=15, font=("verdana", 12, "bold"))
        time_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Date 
        date_label = Label(left_frame, text="Date:", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        date_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        date_entry = ttk.Entry(left_frame, textvariable=self.var_date, width=15, font=("verdana", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Attendance
        student_attend_label = Label(left_frame, text="Status:", font=("verdana", 12, "bold"), fg="navyblue", bg="white")
        student_attend_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        attend_combo = ttk.Combobox(left_frame, textvariable=self.var_attend, width=13, font=("verdana", 12, "bold"), state="readonly")
        attend_combo["values"] = ("Status", "Cleared", "Wanted")
        attend_combo.current(0)
        attend_combo.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # ===============================Table Sql Data View==========================
        table_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=100, width=635, height=310)

        # Scroll bar 
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Create table 
        self.attendanceReport_left = ttk.Treeview(table_frame, column=("ID", "Roll_No", "Name", "Time", "Date", "Attend"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("ID", text="ID")
        self.attendanceReport_left.heading("Roll_No", text="Roll.No")
        self.attendanceReport_left.heading("Name", text="Name")
        self.attendanceReport_left.heading("Time", text="Time")
        self.attendanceReport_left.heading("Date", text="Date")
        self.attendanceReport_left.heading("Attend", text="Status")
        self.attendanceReport_left["show"] = "headings"

        # Set Width of Columns 
        self.attendanceReport_left.column("ID", width=100)
        self.attendanceReport_left.column("Roll_No", width=100)
        self.attendanceReport_left.column("Name", width=100)
        self.attendanceReport_left.column("Time", width=100)
        self.attendanceReport_left.column("Date", width=100)
        self.attendanceReport_left.column("Attend", width=100)
        
        self.attendanceReport_left.pack(fill=BOTH, expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>", self.get_cursor_left)

        # =========================button section========================
        # Button Frame
        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=390, width=635, height=60)

        # Import button
        save_btn = Button(btn_frame, command=self.importCsv, text="Import CSV", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        save_btn.grid(row=0, column=0, padx=6, pady=10, sticky=W)

        # Export button
        update_btn = Button(btn_frame, command=self.exportCsv, text="Export CSV", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        update_btn.grid(row=0, column=1, padx=6, pady=8, sticky=W)

        # Update button
        del_btn = Button(btn_frame, command=self.action, text="Edit", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        del_btn.grid(row=0, column=2, padx=6, pady=10, sticky=W)

        # Reset button
        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        reset_btn.grid(row=0, column=3, padx=6, pady=10, sticky=W)

        # Export Student Data button
        export_student_btn = Button(btn_frame, command=self.export_student_data_to_csv, text="Export Student Data", width=20, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        export_student_btn.grid(row=0, column=4, padx=6, pady=10, sticky=W)

        # Right section=======================================================
        # Right Label Frame 
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Details", font=("verdana", 12, "bold"), fg="navyblue")
        right_frame.place(x=680, y=10, width=660, height=480)

        # -----------------------------Table Frame-------------------------------------------------
        # Table Frame 
        # Searching System in Right Label Frame 
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=70, width=580, height=360)

        # Scroll bar 
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Create table 
        self.attendanceReport = ttk.Treeview(table_frame, column=("ID", "Roll_No", "Name", "Time", "Date", "Attend"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID", text="ID")
        self.attendanceReport.heading("Roll_No", text="Roll.No")
        self.attendanceReport.heading("Name", text="Name")
        self.attendanceReport.heading("Time", text="Time")
        self.attendanceReport.heading("Date", text="Date")
        self.attendanceReport.heading("Attend", text="Status")
        self.attendanceReport["show"] = "headings"

        # Set Width of Columns 
        self.attendanceReport.column("ID", width=30)
        self.attendanceReport.column("Roll_No", width=70)
        self.attendanceReport.column("Name", width=100)
        self.attendanceReport.column("Time", width=75)
        self.attendanceReport.column("Date", width=80)
        self.attendanceReport.column("Attend", width=120)
        
        self.attendanceReport.pack(fill=BOTH, expand=1)
        self.attendanceReport.bind("<ButtonRelease>", self.get_cursor_right)
        self.fetch_data()

        # =================================update for mysql button================
        # Update button
        del_btn = Button(right_frame, command=self.update_data, text="Edit", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        del_btn.grid(row=0, column=1, padx=6, pady=10, sticky=W)

        # Update button
        del_btn = Button(right_frame, command=self.delete_data, text="Delete", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        del_btn.grid(row=0, column=2, padx=6, pady=10, sticky=W)

    # ===============================Fetch Data from MySQL===============================
    def fetch_student_data(self, student_id):
        conn = mysql.connector.connect(username='root', password='admin', host='127.0.0.1', database='face_recognizer', port=3306)
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM student WHERE ID=%s", (student_id,))
        student_data = mycursor.fetchone()
        conn.close()
        return student_data

    # =============================Action Method to Record Attendance========================
    def action(self):
        if self.var_id.get() == "" or self.var_roll.get() == "" or self.var_name.get() == "" or self.var_time.get() == "" or self.var_date.get() == "" or self.var_attend.get() == "Status":
            messagebox.showerror("Error", "Please fill in all required fields!", parent=self.root)
        else:
            try:
                # Record attendance in the database
                conn = mysql.connector.connect(username='root', password='admin', host='127.0.0.1', database='face_recognizer', port=3306)
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO stdattendance VALUES (%s, %s, %s, %s, %s, %s)", (
                    self.var_id.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get()
                ))
                conn.commit()
                conn.close()

                # Fetch student data
                student_data = self.fetch_student_data(self.var_id.get())
                if student_data:
                    # Prepare CSV data
                    csv_data = [student_data]  # Wrap in a list to write multiple rows if needed
                    self.export_to_csv(csv_data)

                messagebox.showinfo("Success", "All records have been saved in the database!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ===========================Export to CSV========================
    def export_to_csv(self, data):
        try:
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                exp_write.writerow(["ID", "Roll No", "Name", "Time", "Date", "Attendance"])  # Header
                for row in data:
                    exp_write.writerow(row)
                messagebox.showinfo("Success", "Data exported successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ===============================Update Function for MySQL=================
    def update_data(self):
        if self.var_id.get() == "" or self.var_roll.get() == "" or self.var_name.get() == "" or self.var_time.get() == "" or self.var_date.get() == "" or self.var_attend.get() == "Status":
            messagebox.showerror("Error", "Please fill in all required fields!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student's attendance score?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='admin', host='127.0.0.1', database='face_recognizer', port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("UPDATE stdattendance SET std_id=%s, std_roll_no=%s, std_name=%s, std_time=%s, std_date=%s, std_attendance=%s WHERE std_id=%s", (
                        self.var_id.get(),
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_time.get(),
                        self.var_date.get(),
                        self.var_attend.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Update successful!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # =============================Delete Attendance from MySQL============================
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID is required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete it?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(username='root', password='admin', host='127.0.0.1', database='face_recognizer', port=3306)
                    mycursor = conn.cursor()
                    sql = "DELETE FROM stdattendance WHERE std_id=%s"
                    val = (self.var_id.get(),)
                    mycursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Deleted successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ===========================Fetch Data from MySQL Attendance===========
    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='admin', host='127.0.0.1', database='face_recognizer', port=3306)
        mycursor = conn.cursor()

        mycursor.execute("SELECT * FROM stdattendance")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("", END, values=i)
            conn.commit()
        conn.close()

    # =============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # =========================Fetch Data Import data ===============
    def fetchData(self, rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("", END, values=i)
            print(i)

    def importCsv(self):
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    # ==================Export CSV=============
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No Data Found!", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfully", "Data export successful!")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # =============Cursor Function for CSV========================
    def get_cursor_left(self, event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])  

    # =============Cursor Function for MySQL========================
    def get_cursor_right(self, event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])    

    # =========================Export Student Data to CSV========================
    def export_student_data_to_csv(self):
        try:
            # Open a file dialog to save the CSV file
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            
            # Open the file in write mode
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                # Write the header
                exp_write.writerow(["ID", "Name", "Dep", "Course", "Year", "Sem", "Div", "Gender", "DOB", "Mob-No", "Address", "Roll-No", "Email", "Teacher", "Photo"])
                
                # Fetch data from the student_table
                for child in self.attendanceReport_left.get_children():
                    row_data = self.attendanceReport_left.item(child)["values"]
                    exp_write.writerow(row_data)  # Write each row to the CSV
                
                messagebox.showinfo("Success", "Data exported successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()