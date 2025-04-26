from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np

class Train:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Panel")

        img = Image.open(r"Images_GUI/banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        bg1 = Image.open(r"Images_GUI/t_bg1.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        title_lb1 = Label(bg_img, text="Welcome to Training Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        std_img_btn = Image.open(r"Images_GUI/t_btn1.png")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.train_classifier, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.train_classifier, text="Train Dataset", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

    # ================== Create Function for Training ===================
    def train_classifier(self):
        data_dir = "data_img"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
            cursor = conn.cursor()

            for image_path in path:
                img = Image.open(image_path).convert('L')  # convert to grayscale
                imageNp = np.array(img, 'uint8')

                try:
                    student_uid = os.path.split(image_path)[1].split('.')[1]  # keep string ID

                    # Get internal numeric ID for training based on student_uid
                    cursor.execute("SELECT ID FROM student WHERE Student_ID = %s", (student_uid,))
                    result = cursor.fetchone()
                    if result:
                        internal_id = result[0]
                        faces.append(imageNp)
                        ids.append(internal_id)
                        cv2.imshow("Training", imageNp)
                        cv2.waitKey(1) == 13
                except Exception as e:
                    print(f"Skipping image due to error: {e}")

            conn.close()
        except Exception as db_err:
            messagebox.showerror("Database Error", str(db_err), parent=self.root)
            return

        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()