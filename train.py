from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np 


class Train:
    def __init__(self, root):
            self.root = root
            #self.root.geometry("1530*790+0+0")
            self.root.title("Face Recognition System")
            title_lbl= Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
            
            title_lbl.place(x=0,y=0,width=1530,height=45)
            
            
            img_top = r"college_images\facialrecognition1.png"
            img = Image.open(img_top)
            img = img.resize((1530, 325))
            self.photoimg_top = ImageTk.PhotoImage(img)

            # Display image in label
            f_lbl = Label(self.root, image=self.photoimg_top)
            f_lbl.place(x=0, y=55, width=1530, height=325)
            
            b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white" )  # ✅ Use self.photoimg5 (lowercase "p")
            b1_1.place(x=0, y=380, width =1530,height=60)
            
            img_bottom = r"college_images\face.jpg"
            img = Image.open(img_bottom)
            img = img.resize((1530, 325))
            self.photoimg_bottom = ImageTk.PhotoImage(img)

            # Display image in label
            f_lbl = Label(self.root, image=self.photoimg_bottom)
            f_lbl.place(x=0, y=440, width=1530, height=325)
            
        
        
    
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        
        for image in path:
            img=Image.open(image).convert('L')# convert to gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training ",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        #=============== train the classifier and save ========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
        
            
            
        
            
           
            
            
            




if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()