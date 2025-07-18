from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
            self.root = root
            #self.root.geometry("1530*790+0+0")
            self.root.title("Face Recognition System")
            
            title_lbl= Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
            
            title_lbl.place(x=0,y=0,width=1530,height=45)
            
            
            img_top = r"college_images\dev.jpg"
            img = Image.open(img_top)
            img = img.resize((1530, 720))
            self.photoimg_top = ImageTk.PhotoImage(img)

            # Display image in label
            f_lbl = Label(self.root, image=self.photoimg_top)
            f_lbl.place(x=0, y=55, width=1530, height=720)
            
            #=== frame ======
            main_frame=Frame(f_lbl,bd=2)
            main_frame.place(x=1000,y=0,width=500,height=600)
            
            
            img_top1 = r"college_images\avi.jpg"
            img1 = Image.open(img_top1)
            img1 = img1.resize((200, 200))
            self.photoimg_top1 = ImageTk.PhotoImage(img1)

            # Display image in label
            f_lbl = Label(main_frame, image=self.photoimg_top1)
            f_lbl.place(x=300, y=0, width=200, height=200)
            
            # developer info 
            dev_lable=Label(main_frame,text="Avi and its team mates",font=("times new roman",20,"bold"),bg="white")
            dev_lable.place(x=0,y=5)
            
            dev_lable=Label(main_frame,text="i am a full stack developer",font=("times new roman",20,"bold"),bg="white")
            dev_lable.place(x=0,y=5)
            
            
            img_top11 = r"college_images\p.jpg"
            img11 = Image.open(img_top11)
            img1 = img11.resize((500, 390))
            self.photoimg_top11 = ImageTk.PhotoImage(img11)

            # Display image in label
            f_lbl = Label(main_frame, image=self.photoimg_top11)
            f_lbl.place(x=0, y=210, width=500, height=390)
            
            
            
            
            
            
    
    
            


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()