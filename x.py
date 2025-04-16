import cv2
import pymysql
import pickle
import csv
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import numpy as np


import cv2
import pymysql
import pickle
import csv
import numpy as np  # Import numpy
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")

        # Load the ID map during initialization
        self.id_map = self.load_id_map()  # Store it as a class attribute

        # This part is image labels setting start
        # first header image
        img = Image.open(r"Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(r"Images_GUI\bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("Verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # Training button 1
        std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

    # =====================Attendance===================

    def load_id_map(self):
        try:
            with open("id_map.pkl", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("ID map file not found. Please ensure id_map.pkl exists.")
            return {}  # Return an empty dictionary if the file isn't found
        except Exception as e:
            print(f"Error loading ID map: {e}")
            return {}

    def mark_attendance(self, regd_no, roll, name):
        today = datetime.now().strftime("%d/%m/%Y")
        found = False
        with open("attendance.csv", "r+", newline="") as f:
            reader = csv.reader(f)
            data = list(reader)
            for row in data:
                if row[0] == regd_no and row[4] == today:
                    found = True
                    break

            if not found:
                time_now = datetime.now().strftime("%H:%M:%S")
                data.append([regd_no, roll, name, time_now, today, "Present"])

            # Go back to the start of the file to overwrite it
            f.seek(0)
            writer = csv.writer(f)
            writer.writerows(data)

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)  # Detect faces
        coord = []

        if len(features) == 0:
            print("No faces detected.")  # Print message if no faces are found

        for (x, y, w, h) in features:
            id_num, pred = clf.predict(gray[y:y + h, x:x + w])  # Predict face ID
            confidence = int(100 * (1 - pred / 300))

            regd_no = next((k for k, v in self.id_map.items() if v == id_num), "Unknown")

            if regd_no != "Unknown":
                try:
                    conn = pymysql.connect(host="localhost", user="root", password="root", database="face_recognition")
                    cursor = conn.cursor()

                    cursor.execute("SELECT Name, Roll FROM student WHERE Regd_no = %s", (regd_no,))
                    result = cursor.fetchone()
                    conn.close()

                    if result:
                        name, roll = result
                        if confidence > 65:
                            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)  # Draw rectangle around face
                            cv2.putText(img, f"Regd_no: {regd_no}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)
                            cv2.putText(img, f"Name: {name}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)
                            cv2.putText(img, f"Roll: {roll}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)
                            self.mark_attendance(regd_no, roll, name)
                        else:
                            cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                except Exception as e:
                    print(f"DB error: {e}")

        return img  # Return the image after processing

    def recognize(self, img, clf, faceCascade):
        img = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), clf)
        return img  # Ensure the processed image is returned correctly

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)
        while True:
            ret, img = videoCap.read()
            if not ret:
                print("Error: Unable to access camera or capture image.")
                break

            # Process the image
            img = self.recognize(img, clf, faceCascade)

            # Ensure the image is a valid numpy array
            if img is not None and isinstance(img, np.ndarray):
                cv2.imshow("Face Detector", img)  # Show the image only if it's valid
            else:
                print("Error: Invalid image format received for display.")

            if cv2.waitKey(1) == 13:  # Press Enter key to exit the loop
                break

        videoCap.release()
        cv2.destroyAllWindows()



# Main loop for Tkinter
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
