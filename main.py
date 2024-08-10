from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_Recognition import FaceRecognition
from attendance import Attendance
import tkinter
from datetime import datetime
from time import strftime
from developer import Developer
from help import Help



class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")
        # first img
        img=Image.open(r"college_images/BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second img
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third img
        img2=Image.open(r"college_images/images.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # bg img
        img3=Image.open(r"college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        def tym():
            string =strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,tym)

        lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("items new roman",12,"bold"),bg="white",fg="red")
        lbl.place(x=0,y=0,width=110,height=45)
        tym()

        # student button
        img4=Image.open(r"college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)


        b2=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkbLUE",fg="white")
        b2.place(x=200,y=300,width=220,height=40)

        # detect face button
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)


        b2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=300,width=220,height=40)

        # Attendance Face button
        img6=Image.open(r"college_images\hi.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)


        b2=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=800,y=300,width=220,height=40)

        
        # Help Desk
        img7=Image.open(r"college_images\help.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help_desk,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)


        b2=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1100,y=300,width=220,height=40)

        
        # Train  button
        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)


        b2=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=580,width=220,height=40)


         # Photos  button
        img9=Image.open(r"college_images\photos.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)


        b2=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=580,width=220,height=40)
 
 
        # Developerface button
        img10=Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)


        b2=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=800,y=580,width=220,height=40)


        # Exit face button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exitohome)
        b1.place(x=1100,y=380,width=220,height=220)


        b2=Button(bg_img,text="Exit",cursor="hand2",command=self.exitohome,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")
    def exitohome(self):
        self.exitohome=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit from this project",parent=self.root)
        if self.exitohome:
            self.root.destroy()
        else:
            return

    
        # **************function button*************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        


        






 
 
        
        
 

 
if __name__ == "__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()


 


