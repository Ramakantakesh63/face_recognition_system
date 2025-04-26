# Import necessary libraries
import cv2
import numpy as np
import os
import pymysql
import threading
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")

        self.stop_recognition = False
        self.recognition_thread = None

        # Header image
        img = Image.open(r"Images_GUI/banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(r"Images_GUI/bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"), bg="white",
                          fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Buttons for face recognition
        std_img_btn = Image.open(r"Images_GUI/f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.start_recognition_thread, image=self.std_img1, cursor="hand2")
        std_b1.place(x=500, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.start_recognition_thread, text="Start Detector", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=500, y=350, width=180, height=45)

        # Stop and Exit buttons
        stop_btn = Button(bg_img, command=self.stop_recognition_fn, text="Stop", font=("tahoma", 15, "bold"), bg="red", fg="white", cursor="hand2")
        stop_btn.place(x=700, y=170, width=180, height=45)


    def start_recognition_thread(self):
        if self.recognition_thread is None or not self.recognition_thread.is_alive():
            self.recognition_thread = threading.Thread(target=self.face_recog)
            self.recognition_thread.daemon = True
            self.recognition_thread.start()

    def stop_recognition_fn(self):
        self.stop_recognition = True

    def mark_attendance(self, Student_ID, Roll_No, Name):
        with open("attendance.csv", "r+", newline="\n") as f:
            existing_data = f.readlines()
            recorded_names = [line.split(",")[0] for line in existing_data]

            if Student_ID not in recorded_names:
                now = datetime.now()
                date_str = now.strftime("%Y-%m-%d")
                time_str = now.strftime("%H:%M:%S")
                f.writelines(f"\n{Student_ID}, {Roll_No}, {Name}, {time_str}, {date_str}, Present")

    def face_recog(self):
        self.stop_recognition = False

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            coordinates = []

            for (x, y, w, h) in features:
                face_roi = gray_img[y:y + h, x:x + w]
                if face_roi.size == 0:
                    continue

                try:
                    internal_id, prediction = clf.predict(face_roi)
                    confidence = int((100 * (1 - prediction / 300)))
                except Exception as e:
                    print("Prediction error:", e)
                    continue


                if confidence > 75:
                    try:
                        conn = pymysql.connect(user='root', password='root', host='localhost', database='face_recognition', port=3306)
                        cursor = conn.cursor()
                        cursor.execute("SELECT Student_ID, Name, Roll_No FROM student WHERE ID = %s", (internal_id,))
                        result = cursor.fetchone()
                        conn.close()


                        if result:
                            Student_ID, Name, Roll_no = result
                            self.mark_attendance(Student_ID, Roll_no, Name)
                            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                            cv2.putText(img, f"Student_ID: {Student_ID}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                            cv2.putText(img, f"Name: {Name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                            cv2.putText(img, f"Roll No: {Roll_no}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)

                        else:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                            cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                    except Exception as e:
                        print("Database error:", e)
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coordinates = [x, y, w, h]

            return coordinates

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("Images_GUI/haarcascade_frontalface_default.xml")
        if faceCascade.empty():
            messagebox.showerror("Error", "Cannot load haarcascade_frontalface_default.xml. Make sure the file exists.")
            return

        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            messagebox.showerror("Error", "cv2.face.LBPHFaceRecognizer_create() is missing. Please install OpenCV contrib version.")
            return

        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        while not self.stop_recognition:
            ret, img = videoCap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break

        videoCap.release()
        cv2.destroyAllWindows()


# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
