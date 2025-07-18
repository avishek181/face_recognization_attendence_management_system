from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendence:
    def __init__(self, root):
            self.root = root
            #self.root.geometry("1530*790+0+0")
            self.root.title("Face Recognization System")
            
            
            #========= variables ==========
            self.var_atten_id=StringVar()
            self.var_atten_roll=StringVar()
            self.var_atten_name=StringVar()
            self.var_atten_dep=StringVar()
            self.var_atten_time=StringVar()
            self.var_atten_date=StringVar()
            self.var_atten_attendence=StringVar()
            
            
            
            # first image
            img_top = r"college_images\smart-attendance.jpg"
            img = Image.open(img_top)
            img = img.resize((800, 200))
            self.photoimg_top = ImageTk.PhotoImage(img)

        
            f_lbl = Label(self.root, image=self.photoimg_top)
            f_lbl.place(x=0, y=0, width=800, height=200)
            # second image
            img_bottom = r"college_images\iStock-182059956_18390_t12.jpg"
            img = Image.open(img_bottom)
            img = img.resize((800, 200))
            self.photoimg_bottom = ImageTk.PhotoImage(img)

            # Display image in label
            f_lbl = Label(self.root, image=self.photoimg_bottom)
            f_lbl.place(x=800, y=0, width=800, height=200)
            
            img4_path = r"C:\face_recognization_attendence_system\college_images\bgimage.jpg"
            img4 = Image.open(img4_path)
            img4 = img4.resize((1530, 710))
            self.photoimg4 = ImageTk.PhotoImage(img4)

            # Display image in label
            bg_img = Label(self.root, image=self.photoimg4)
            bg_img.place(x=0, y=200, width=1530, height=710)
            
            
            title_lbl= Label(bg_img,text="ATTENDENCE MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
            
            title_lbl.place(x=0,y=0,width=1530,height=45)
            
             # create main frame
            main_frame=Frame(bg_img,bd=2,bg="white")
            main_frame.place(x=20,y=50,width=1480,height=600)
            
            
               # left lable frame
            Left_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
            
            Left_frame.place(x=10,y=10,width=730,height=580)
            
            imgright_path = r"college_images\student.jpg"
            imgright = Image.open(imgright_path)
            imgright= imgright.resize((720, 130))
            self.photoimgright = ImageTk.PhotoImage(imgright)

            
            f_lbl4 = Label(Left_frame, image=self.photoimgright)
            f_lbl4.place(x=5, y=0, width=720, height=130)
            
            left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
            left_inside_frame.place(x=0,y=135,width=720,height=300)
            # attendence id 
            attendenceId_lable=Label(left_inside_frame,text="AttendenceID:",font=("times new roman",13,"bold"),bg="white")
            attendenceId_lable.grid(row=0,column=0,padx=5,sticky=W)
            
            attendenceID_entry= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("time new roman",13,"bold"))
            
            attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
            
            #Roll number 
            rollLable=Label(left_inside_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
            rollLable.grid(row=0,column=2,padx=5,pady=8,sticky=W)
            
            attend_roll= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("time new roman",13,"bold"))
            
            attend_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)
            
            # Name
            nameLable=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
            nameLable.grid(row=1,column=0,padx=5,sticky=W)
            
            attend_name= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("time new roman",13,"bold"))
            
            attend_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)
            
            
            
            # date 
            depLable=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
            depLable.grid(row=1,column=2,padx=5,sticky=W)
            
            dep_name= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("time new roman",13,"bold"))
            
            dep_name.grid(row=1,column=3,padx=10,pady=5,sticky=W)
            
            # time
            
            timeLable=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
            timeLable.grid(row=2,column=0,padx=5,sticky=W)
            
            time_name= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("time new roman",13,"bold"))
            
            time_name.grid(row=2,column=1,padx=10,pady=5,sticky=W)
            
            # Date
            dateLable=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
            dateLable.grid(row=2,column=2,padx=5,sticky=W)
            
            date_name= ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("time new roman",13,"bold"))
            
            date_name.grid(row=2,column=3,padx=10,pady=5,sticky=W)
            
            # Attendence
            
            attendenceLable=Label(left_inside_frame,text="Attendence Status",bg="white",font="comicsansns 11 bold")
            attendenceLable.grid(row=3,column=0)
            
            self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendence,font="comicsansns 11 bold",state="readonly")
            self.atten_status["values"]=("Status","Present","Absent")
            self.atten_status.grid(row=3,column=1,pady=8)
            self.atten_status.current(0)
            
            
            #buttons frame
            btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame.place(x=0,y=260,width=715,height=35)
            
            save_btn=Button(btn_frame,text="Importcsv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
            save_btn.grid(row=0,column=0)
            
             
            update_btn=Button(btn_frame,text="Exportcsv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
            update_btn.grid(row=0,column=1)
            
             
            delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
            delete_btn.grid(row=0,column=2)
            
             
            reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
            reset_btn.grid(row=0,column=3)
            
            
            
            
            
            
            
            
            
            
            
            
            
             # right lable frame
            Right_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
            Right_frame.place(x=750,y=10,width=720,height=580)
            
            table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
            table_frame.place(x=5,y=5,width=700,height=455)
            
              # ============scroll bar table ==========
              
            scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
            self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            
            scroll_x.config(command=self.AttendenceReportTable.xview)
            scroll_y.config(command=self.AttendenceReportTable.yview)
            
            self.AttendenceReportTable.heading("id",text="Attendence ID")
            self.AttendenceReportTable.heading("roll",text="Roll")
            self.AttendenceReportTable.heading("name",text="Name")
            self.AttendenceReportTable.heading("department",text="Department")
            self.AttendenceReportTable.heading("time",text="Time")
            self.AttendenceReportTable.heading("date",text="Date")
            self.AttendenceReportTable.heading("attendence",text="Attendence ")
            self.AttendenceReportTable["show"]="headings"
            self.AttendenceReportTable.column("id",width=100)
            self.AttendenceReportTable.column("roll",width=100)
            self.AttendenceReportTable.column("name",width=100) 
            self.AttendenceReportTable.column("department",width=100)
            self.AttendenceReportTable.column("time",width=100)
            self.AttendenceReportTable.column("date",width=100)
            self.AttendenceReportTable.column("attendence",width=100)
            
            self.AttendenceReportTable.pack(fill=BOTH,expand=1)
            self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
            
            
    # =========   fetch data ============
    def fetchData(self,rows):
      self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
      for i in rows:
        self.AttendenceReportTable.insert("",END,values=i)
      
      # import csv
    def importCsv(self):
      global mydata
      mydata.clear()
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
      
      with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        
        self.fetchData(mydata)
        
        
        # export csv
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data","No Data found to export",parent=self.root)
          return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write=csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export"," Your data exported to "+ os.path.basename(fln)+"successfully")
      
      except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
             
          
        
    def get_cursor(self,event=""):
      cursor_row=self.AttendenceReportTable.focus()   
      content=self.AttendenceReportTable.item(cursor_row)
      rows=content['values']
      self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendence.set(rows[6])
    
    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendence.set("")
      
            
            
            
            


if __name__ == "__main__":
    root = Tk()
    app =Attendence(root)
    root.mainloop()