from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        title_label = Label(self.root, text="HELP DESK", font=("Times New Roman", 35, "bold"), bg="white", fg="blue")
        title_label.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images\HELP2.jpeg")
        img_top = img_top.resize((1535, 740), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1535, height=740)


        dev_label=Label(first_label,text="Email:parveensaziya34@gamil.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=550,y=220)




if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()