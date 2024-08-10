from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        title_label = Label(self.root, text="DEVELOPER", font=("Times New Roman", 35, "bold"), bg="white", fg="blue")
        title_label.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1535, 740), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=46, width=1535, height=740)

        main_frame=Frame(first_label,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)


        img_top1= Image.open(r"college_images\tony.jpg")
        img_top1 = img_top1.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        first_label = Label(main_frame, image=self.photoimg_top1)
        first_label.place(x=300, y=0, width=200, height=200)



        dev_label=Label(main_frame,text="Hello my name is saziya parveen",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am full stack developer",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=40)


        img2=Image.open(r"college_images\dev2.jpg")
        img2=img2.resize((500,410),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(main_frame,image=self.photoimg2)
        first_label.place(x=-7,y=200,width=510,height=410)











if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()