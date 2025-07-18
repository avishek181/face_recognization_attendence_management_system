from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from time import strftime
from datetime import datetime

from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help
#from login import Login




class FaceRecognitionSystem:
      def __init__(self, root):
            self.root = root
            self.root.geometry("1530x790+0+0")
            self.root.title("Face Recognition System")

       
            # 1 first image
            img_path = r"C:\face_recognization_attendence_system\college_images\Stanford.jpg"
            img = Image.open(img_path)
            img = img.resize((500, 130))
            self.photoimg = ImageTk.PhotoImage(img)

            # Display image in label
            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=500, height=130)
            
            
            
            #2 nd image
            img2_path = r"C:\face_recognization_attendence_system\college_images\facialrecognition1.png"
            img2 = Image.open(img2_path)
            img2 = img2.resize((500, 130))
            self.photoimg2 = ImageTk.PhotoImage(img2)

            # Display image in label
            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=500, y=0, width=500, height=130)
            
            # 3 rd image
            
            img3_path = r"C:\face_recognization_attendence_system\college_images\u.jpg"
            img3 = Image.open(img3_path)
            img3 = img3.resize((500, 130))
            self.photoimg3 = ImageTk.PhotoImage(img3)

            # Display image in label
            f_lbl3 = Label(self.root, image=self.photoimg3)
            f_lbl3.place(x=1000, y=0, width=550, height=130)
            
            #background image
            
            img4_path = r"C:\face_recognization_attendence_system\college_images\bgimage.jpg"
            img4 = Image.open(img4_path)
            img4 = img4.resize((1530, 710))
            self.photoimg4 = ImageTk.PhotoImage(img4)

            # Display image in label
            bg_img = Label(self.root, image=self.photoimg4)
            bg_img.place(x=0, y=130, width=1530, height=710)
            
            
            
            
            #title
            
            
            title_lbl= Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
            title_lbl.place(x=0,y=0,width=1530,height=45)
            # time ======= current time shows 
            def time():
                   string =strftime('%H:%M:%S %p')
                   lbl.config(text=string)
                   lbl.after(1000,time)
            lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
            lbl.place(x=0,y=0,width=110,height=50)
            time()
            
            
            
            
            
            
          # Student button
            img5_path = r"C:\face_recognization_attendence_system\college_images\student.jpg"
            img5 = Image.open(img5_path)
            img5 = img5.resize((220, 220))
            self.photoimg5 = ImageTk.PhotoImage(img5)  # ✅ Corrected

            b1 = Button(bg_img, image=self.photoimg5,command=self.student_details , cursor="hand2")  #self.student_table.column("dep",width=100)
            b1.place(x=200, y=100, width =220,height=220)
            
            b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white" )  # ✅ Use self.photoimg5 (lowercase "p")
            b1_1.place(x=200, y=300, width =220,height=40)

           
           
           # detect face  button
            img6_path = r"C:\face_recognization_attendence_system\college_images\face_detector1.jpg"
            img6 = Image.open(img6_path)
            img6 = img6.resize((220, 220))
            self.photoimg6 = ImageTk.PhotoImage(img6)  # ✅ Corrected

            b1 = Button(bg_img, image=self.photoimg6,command=self.face_data, cursor="hand2")  # ✅ Use self.photoimg5 (lowercase "p")
            b1.place(x=500, y=100, width =220,height=220)
            
            b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white" )  # ✅ Use self.photoimg5 (lowercase "p")
            b1_1.place(x=500, y=300, width =220,height=40)
            
            
           #Attendence
            img7_path = r"C:\face_recognization_attendence_system\college_images\attendence.jpg"
            img7 = Image.open(img7_path)
            img7 = img7.resize((220, 220))
            self.photoimg7 = ImageTk.PhotoImage(img7)  

            b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.attendence_data)  
            b1.place(x=800, y=100, width =220,height=220)
            
            b1_1 = Button(bg_img, text="Attendence", cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white" ) 
            b1_1.place(x=800, y=300, width =220,height=40)


           #HELP DESK
            img8_path = r"C:\face_recognization_attendence_system\college_images\helpdesk.jpg"
            img8 = Image.open(img8_path)
            img8 = img8.resize((220, 220))
            self.photoimg8 = ImageTk.PhotoImage(img8)  

            b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.help_data)  
            b1.place(x=1100, y=100, width =220,height=220)
            
            b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white" ) 
            b1_1.place(x=1100, y=300, width =220,height=40)

           
             #TRAIN FACE BUTTON
            img9_path = r"C:\face_recognization_attendence_system\college_images\Train.jpg"
            img9 = Image.open(img9_path)
            img9 = img9.resize((220, 220))
            self.photoimg9 = ImageTk.PhotoImage(img9)  

            b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.train_data)  
            b1.place(x=200, y=380, width =220,height=220)
            
            b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white" ) 
            b1_1.place(x=200, y=580, width =220,height=40)

           
           
             #photos face button
            img10_path = r"college_images\face.jpg"
            img10 = Image.open(img10_path)
            img10 = img10.resize((220, 220))
            self.photoimg10 = ImageTk.PhotoImage(img10)  

            b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)  
            b1.place(x=500, y=380, width =220,height=220)
            
            b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white" ) 
            b1_1.place(x=500, y=580, width =220,height=40)

             #developer 
            img11_path = r"college_images\Team-Management-Software-Development.jpg"
            img11 = Image.open(img11_path)
            img11 = img11.resize((220, 220))
            self.photoimg11 = ImageTk.PhotoImage(img11)  

            b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.developer_data)  
            b1.place(x=800, y=380, width =220,height=220)
            
            b1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white" ) 
            b1_1.place(x=800, y=580, width =220,height=40)
            
            
              #EXITS face button
            img12_path = (r"college_images\exit.jpg")
            img12 = Image.open(img12_path)
            img12 = img12.resize((220, 220))
            self.photoimg12 = ImageTk.PhotoImage(img12)  

            b1 = Button(bg_img, image=self.photoimg12, cursor="hand2",command=self.iExit)  
            b1.place(x=1100, y=380, width =220,height=220)
            
            b1_1 = Button(bg_img, text="Exits", cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white" ) 
            b1_1.place(x=1100, y=580, width =220,height=40)
            
            
            
            
             
  

            
      def open_img(self):
        os.startfile("data")
        
        
      def iExit(self):
              exit_comfirmation=messagebox.askyesno("Face Recognition ","Are you sure exit this project?",parent=self.root)
              if exit_comfirmation> 0:
                     self.root.destroy()
              
              else :
                     return
             
            
            

       
      def student_details(self):
             self.new_window=Toplevel(self.root)
             self.app=Student(self.new_window)
             
      
      def train_data(self):
             self.new_window=Toplevel(self.root)
             self.app=Train(self.new_window)
             
      
      def face_data(self):
             self.new_window=Toplevel(self.root)
             self.app=Face_Recognition(self.new_window)
             
      def attendence_data(self):
             self.new_window=Toplevel(self.root)
             self.app=Attendence(self.new_window)
       
      def developer_data(self):
             self.new_window=Toplevel(self.root)
             self.app=Developer(self.new_window)
       
      def help_data(self):
             self.new_window=Toplevel(self.root)
             self.app=Help(self.new_window)
         
            

if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()
    
   

