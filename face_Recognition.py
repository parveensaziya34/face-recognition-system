from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import cv2.data
import numpy as np
import csv
from datetime import datetime


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="FACE RECOGNITION", font=("Times New Roman", 35, "bold"), bg="white", fg="green")
        title_label.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"college_images/face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=5, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        second_label = Label(self.root, image=self.photoimg_bottom)
        second_label.place(x=650, y=55, width=950, height=700)

        # Button
        btn1_1 = Button(self.root, text="FACE RECOGNITION", cursor="hand2", command=self.face_recog, font=("Times New Roman", 14, "bold"), bg="darkgreen", fg="white")
        btn1_1.place(x=1020, y=680, width=200, height=40)

    # ***********************attendance***************
    def mark_attendance(self, studentid, name, roll, dep):
        today = datetime.now().date()
        now = datetime.now().time()

        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Saziya@123",
                database="saziya"
            )
            my_cursor = conn.cursor()

            # Check if attendance is already marked for today
            my_cursor.execute("""
                SELECT * FROM attendance 
                WHERE studentid = %s AND date = %s
            """, (studentid, today))
            result = my_cursor.fetchone()

            if result:
                print(f"Attendance already marked for student {studentid} today.")
            else:
                # Insert attendance record into MySQL database
                my_cursor.execute("""
                    INSERT INTO attendance (studentid, date, time, name, roll, status) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (studentid, today, now, name, roll, 'present'))
                conn.commit()
                print(f"Attendance marked as 'present' for student {studentid}.")

                # Also write to CSV file
                with open("saziya.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([studentid, name, roll, dep, now.strftime("%H:%M:%S"), today.strftime("%d/%m/%y"), "present"])

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            my_cursor.close()
            conn.close()

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(30, 30))

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Saziya@123", database="saziya")
                    my_cursor = conn.cursor()

                    query = "SELECT Name, Roll, Dep FROM student WHERE student_id=%s"
                    my_cursor.execute(query, (id,))
                    result = my_cursor.fetchone()
                    name = result[0] if result else "Unknown"
                    roll = result[1] if result else "Unknown"
                    dep = result[2] if result else "Unknown"
                    student_id = id

                    conn.close()

                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    name, roll, dep = "Unknown", "Unknown", "Unknown"

                # Display results on the image
                if confidence > 77:
                    cv2.putText(img, f"StudentId: {student_id}", (x, y - 100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
                    cv2.putText(img, f"Name: {name}", (x, y - 70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
                    cv2.putText(img, f"Roll: {roll}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
                    cv2.putText(img, f"Department: {dep}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
                    self.mark_attendance(student_id, name, roll, dep)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                coord = [x, y, w, h]
            return img

        def recognize(img, clf, faceCascade):
            if not faceCascade or not clf:
                raise ValueError("faceCascade and clf must be valid objects.")

            try:
                img = draw_boundary(img, faceCascade, 1.1, 5, (255, 25, 255), "Face", clf)
            except Exception as e:
                # print(f"Error in draw_boundary: {e}")
                pass

            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            print("Error: Could not open video capture.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade)

            # Check if img is a valid NumPy array
            if isinstance(img, np.ndarray):
                cv2.imshow("Welcome To Face Recognition", img)
            else:
                print("Error: The image is not a valid NumPy array.")
                break

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()


# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import cv2.data
# import mysql.connector
# from datetime import datetime
# import cv2
# import numpy as np
# import csv

# class FaceRecognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         title_label = Label(self.root, text="FACE RECOGNITION", font=("Times New Roman", 35, "bold"), bg="white", fg="green")
#         title_label.place(x=0, y=0, width=1530, height=45)

#         img_top = Image.open(r"college_images\face_detector1.jpg")
#         img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
#         self.photoimg_top = ImageTk.PhotoImage(img_top)

#         first_label = Label(self.root, image=self.photoimg_top)
#         first_label.place(x=0, y=55, width=650, height=700)

#         img_bottom = Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
#         img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
#         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

#         second_label = Label(self.root, image=self.photoimg_bottom)
#         second_label.place(x=650, y=55, width=950, height=700)

#         # Button
#         btn1_1 = Button(second_label, text="FACE RECOGNITION", command=self.face_recog,cursor="hand2", font=("Times New Roman", 18, "bold"), bg="darkgreen", fg="white")
#         btn1_1.place(x=350, y=620, width=250, height=40)



#     def mark_attendance(self, student_id, name, roll, dep):
#             today = datetime.now().date()
#             now = datetime.now().time()

#             try:
#                 # Connect to the MySQL database
#                 conn = mysql.connector.connect(host="localhost", username="root", password="Saziya@123", database="saziya")
#                 my_cursor = conn.cursor()

#                 # Check if attendance is already marked for today
#                 my_cursor.execute("""
#                     SELECT * FROM attendance 
#                     WHERE studentid = %s AND date = %s
#                 """, (student_id, today))
#                 result = my_cursor.fetchone()

#                 if result:
#                     print(f"Attendance already marked for student {student_id} today.")
#                 else:
#                     # Insert attendance record into MySQL database
#                     my_cursor.execute("""
#                         INSERT INTO attendance (student_id, date, time,name,roll, status) 
#                         VALUES (%s, %s, %s, %s,%s,%s)
#                     """, (student_id, today, now, name,roll, 'present'))
#                     conn.commit()
#                     print(f"Attendance marked as 'present' for student {student_id}.")

#                     # Also write to CSV file
#                     with open("saziya.csv", "a", newline="") as f:
#                         writer = csv.writer(f)
#                         writer.writerow([student_id, name, roll, dep, now.strftime("%H:%M:%S"), today.strftime("%d/%m/%y"), "present"])

#             except mysql.connector.Error as err:
#                 print(f"Error: {err}")

#             finally:
#                 my_cursor.close()
#                 conn.close()


#     def face_recog(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(30, 30))

#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
#                 id, predict = clf.predict(gray_image[y:y + h, x:x + w])
#                 confidence = int(100 * (1 - predict / 300))

#                 try:
#                     # Fetch student details from database
#                     query = "SELECT Name, Roll, Dep FROM student WHERE student_id=%s"
#                     my_cursor.execute(query, (id,))
#                     result = my_cursor.fetchone()
#                     name = result[0] if result else "Unknown"
#                     roll = result[1] if result else "Unknown"
#                     dep = result[2] if result else "Unknown"

#                     # Mark attendance
#                     if confidence > 77:
#                         cv2.putText(img, f"student_id: {id}", (x, y - 100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
#                         cv2.putText(img, f"Name: {name}", (x, y - 70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
#                         cv2.putText(img, f"Roll: {roll}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
#                         cv2.putText(img, f"Department: {dep}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)
#                         self.mark_attendance(id, name, roll, dep)
#                     else:
#                         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                         cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

#                 except mysql.connector.Error as err:
#                     print(f"Error: {err}")
#                     cv2.putText(img, "Database Error", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

#             return img

#         def recognize(img, clf, faceCascade):
#             faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")
#             if not faceCascade or not clf:
#                 raise ValueError("faceCascade and clf must be valid objects.")
#             try:
#                 img = draw_boundary(img, faceCascade, 1.1, 5, (255, 25, 255), "Face", clf)
#             except Exception as e:
#                 print(f"Error in draw_boundary: {e}")
#             return img

#         faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer.create()
#         clf.read("classifier.xml")

#         try:
#             video_cap = cv2.VideoCapture(0)
#             if not video_cap.isOpened():
#                 print("Error: Could not open video capture.")
#                 return

#             # Connect to the database once
#             conn = mysql.connector.connect(host="localhost", username="root", password="Saziya@123", database="saziya")
#             my_cursor = conn.cursor()

#             while True:
#                 ret, img = video_cap.read()
#                 if not ret:
#                     print("Failed to grab frame")
#                     break

#                 img = recognize(img, clf, faceCascade)

#                 if isinstance(img, np.ndarray):
#                     cv2.imshow("Welcome To Face Recognition", img)
#                 else:
#                     print("Error: The image is not a valid NumPy array.")
#                     break

#                 if cv2.waitKey(1) == 13:  # Press Enter to exit
#                     break

#         except Exception as e:
#             print(f"Error: {e}")

#         finally:
#             video_cap.release()
#             cv2.destroyAllWindows()
#             my_cursor.close()
#             conn.close()


# if __name__ == "__main__":
#     root = Tk()
#     obj = FaceRecognition(root)
#     root.mainloop()