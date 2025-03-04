import cv2
import mysql.connector
import csv  # Import the csv module
from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x700+0+0")
        self.root.title("Face Recognition Based Security System")

        # Load and display images
        self.load_images()

        # Button for face recognition
        self.create_recognition_button()

    def load_images(self):
        # Load header image
        img = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\banner.jpg")
        img = img.resize((1250, 120), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1250, height=120)

        # Load background image
        bg1 = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\bg3.jpg")
        bg1 = bg1.resize((1250, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1250, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="Welcome to the facial recognition system", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1250, height=40)

    def create_recognition_button(self):
        # Button for face recognition
        std_img_btn = Image.open(r"C:\Users\Admin\Desktop\Face_Recognition_Based_Security_System\Images_GUI\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(self.root, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=500, y=300, width=180, height=180)

        std_b1_1 = Button(self.root, command=self.face_recog, text="Recognition", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=500, y=450, width=180, height=45)

    def mark_attendance(self, student_id, roll_no, name, department, gender):
        attendance_file = "attendance.csv"
        last_recorded_times = {}

        # Read existing attendance records
        try:
            with open(attendance_file, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 4:
                        last_recorded_times[row[0]] = datetime.strptime(row[3].strip(), "%H:%M:%S")
        except FileNotFoundError:
            pass  # File does not exist yet

        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        date_string = now.strftime("%d/%m/%Y")

        # Check if the student has been recorded in the last hour
        if student_id in last_recorded_times:
            last_time = last_recorded_times[student_id]
            if now - last_time < timedelta(hours=1):
                print(f"Skipping attendance for {student_id} (Already recorded within the last hour)")
                return

        # Log attendance
        with open(attendance_file, "a+", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([student_id, roll_no, name, dt_string, date_string, department, "Face Detected"])
            print(f"Attendance recorded for ID: {student_id}, Roll No: {roll_no}, Name: {name}, Category: {department}, Gender: {gender}")

    def face_recog(self):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, face_cascade)
            cv2.imshow("Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def recognize(self, img, clf, face_cascade):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = face_cascade.detectMultiScale(gray_image, 1.1, 10)

        for (x, y, w, h) in features:
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            # Connect to the database
            conn = mysql.connector.connect(username="root", password="admin", host="127.0.0.1", database="face_recognizer", port=3306)
            cursor = conn.cursor()

            cursor.execute("SELECT ID, Name, Department, Gender, Roll_No FROM student WHERE ID=%s", (id,))
            result = cursor.fetchone()
            conn.close()

            if result:
                student_id, name, department, gender, roll_no = result
            else:
                student_id, name, department, gender, roll_no = "Unknown", "Unknown", "Unknown", "Unknown", "Unknown"

            if confidence > 77:
                cv2.putText(img, f"ID: {student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                cv2.putText(img, f"Roll-No: {roll_no}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                self.mark_attendance(student_id, roll_no, name, department, gender)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

        return img

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
