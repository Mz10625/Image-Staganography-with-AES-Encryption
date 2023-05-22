import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
from tkinter.ttk import *
from threading import Thread
import time
import Encrypt
import Decode

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.width = self.master.winfo_screenwidth()
        self.height =self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (self.width,self.height))
        self.frame = customtkinter.CTkFrame(master=None,width=self.width-200,height=self.height-200,fg_color="gray35")
        self.frame.place(relx=0.1,rely=0.1)
        self.header1=customtkinter.CTkLabel(master=None,text="Image Steganography with AES Encryption",text_color="Deep sky blue",height=60,width=700,font=('Castellar',25))
        self.header1.place(relx=0.17,rely=0.1)
        self.info1=customtkinter.CTkLabel(master=None,text="Secure Encoding of data within Image file.",height=20,width=200,fg_color="gray35",text_color="white",font=('Aparajita',25))
        self.info1.place(relx=0.2,rely=0.2)
        self.info2=customtkinter.CTkLabel(master=None,text="1. Image file format required for Encoding - .jpeg",height=20,width=200,fg_color="gray35",text_color="white",font=('Aparajita',25))
        self.info2.place(relx=0.2,rely=0.25)
        self.info3=customtkinter.CTkLabel(master=None,text="2. The amount of data that can be encoded is based on image resolution.\n    Refer below given values for Encoding :",height=20,width=200,justify="left",fg_color="gray35",text_color="white",font=('Aparajita',25))
        self.info3.place(relx=0.2,rely=0.3)
        self.info4=customtkinter.CTkLabel(master=None,text="RESOLUTION\tDATA",fg_color="gray35",text_color="red",font=('Aparajita',25))
        self.info4.place(relx=0.38,rely=0.4)
        self.info5=customtkinter.CTkLabel(master=None,text="640 x 480\t   110 KB\n800 x 600\t   175 KB\n1024 x 768\t   288 KB\n1280 x 720\t   337 KB\n1280 x 960\t   450 KB\n1280 x 1024\t   480 KB\n1600 x 1200\t   703 KB\n1920 x 1080\t   760 KB\n2048 x 1536\t   1152 KB\n2560 x 1440\t   1349 KB",justify="left",fg_color="gray35",text_color="light blue",font=('Aparajita',20))
        self.info5.place(relx=0.4,rely=0.45)
        self.encodeb=customtkinter.CTkButton(master=None,text="Encode",height=40,width=80,command=self.Encode)
        self.encodeb.place(relx=0.3,rely=0.8)        
        self.decodeb=customtkinter.CTkButton(master=None,text="Decode",height=40,width=80,command=self.Decode)
        self.decodeb.place(relx=0.6,rely=0.8)

    def Encode_to_home(self):
        self.buttonselect1.place_forget()
        self.buttonselect2.place_forget()
        self.encode_backbutton.place_forget()
        self.buttonencode.place_forget()
        self.label3.place_forget()
        self.img_entry.place_forget()
        self.output_destination_button.place_forget()
        if(msgflag == 1):
            self.label1.place_forget()
        if(imgflag == 1):
            self.label2.place_forget()
        if(outputdestinationflag == 1):
            self.label5.place_forget()
        self.frame = customtkinter.CTkFrame(master=None,width=self.width-200,height=self.height-200,fg_color="gray35")
        self.frame.place(relx=0.1,rely=0.1)
        self.header1=customtkinter.CTkLabel(master=None,text="Image Steganography with AES Encryption",text_color="Deep sky blue",height=60,width=700,font=('Castellar',25))
        self.header1.place(relx=0.17,rely=0.1)
        self.info1=customtkinter.CTkLabel(master=None,text="Secure Encoding of data within Image file.",height=20,width=200,fg_color="gray35",text_color="white",font=('Centaur',20))
        self.info1.place(relx=0.2,rely=0.2)
        self.info2=customtkinter.CTkLabel(master=None,text="1. Image file format required for Encoding - .jpeg",height=20,width=200,fg_color="gray35",text_color="white",font=('Centaur',20))
        self.info2.place(relx=0.2,rely=0.25)
        self.info3=customtkinter.CTkLabel(master=None,text="2. The amount of data that can be encoded is based on image resolution.\n    Refer below given values for Encoding :",height=20,width=200,justify="left",fg_color="gray35",text_color="white",font=('Centaur',20))
        self.info3.place(relx=0.2,rely=0.3)
        self.info4=customtkinter.CTkLabel(master=None,text="RESOLUTION\tDATA",fg_color="gray35",text_color="red",font=('Aparajita',25))
        self.info4.place(relx=0.38,rely=0.4)
        self.info5=customtkinter.CTkLabel(master=None,text="640 x 480\t   110 KB\n800 x 600\t   175 KB\n1024 x 768\t   288 KB\n1280 x 720\t   337 KB\n1280 x 960\t   450 KB\n1280 x 1024\t   480 KB\n1600 x 1200\t   703 KB\n1920 x 1080\t   760 KB\n2048 x 1536\t   1152 KB\n2560 x 1440\t   1349 KB",justify="left",fg_color="gray35",text_color="light blue",font=('Aparajita',20))
        self.info5.place(relx=0.4,rely=0.45)
        self.encodeb=customtkinter.CTkButton(master=None,text="Encode",height=40,width=80,command=self.Encode)
        self.encodeb.place(relx=0.3,rely=0.8)        
        self.decodeb=customtkinter.CTkButton(master=None,text="Decode",height=40,width=80,command=self.Decode)
        self.decodeb.place(relx=0.6,rely=0.8)

    def Decode_to_home(self):
        self.decode_backbutton.place_forget()
        self.buttonselect3.place_forget()
        self.output_destination_button.place_forget()  
        if(imgflag == 1):
            self.label2.place_forget()  
        if(outputdestinationflag == 1):
            self.label5.place_forget()   
        self.buttondecode.place_forget() 
        self.label4.place_forget()     
        self.msg_entry.place_forget()     
        self.frame = customtkinter.CTkFrame(master=None,width=self.width-200,height=self.height-200,fg_color="gray35")
        self.frame.place(relx=0.1,rely=0.1)
        self.header1=customtkinter.CTkLabel(master=None,text="Image Steganography with AES Encryption",text_color="Deep sky blue",height=60,width=700,font=('Castellar',25))
        self.header1.place(relx=0.17,rely=0.1)
        self.info1=customtkinter.CTkLabel(master=None,text="Secure Encoding of data within Image file.",height=20,width=200,fg_color="gray35",text_color="white",font=('Centaur',20))
        self.info1.place(relx=0.2,rely=0.2)
        self.info2=customtkinter.CTkLabel(master=None,text="1. Image file format required for Encoding - .jpeg",height=20,width=200,fg_color="gray35",text_color="white",font=('Centaur',20))
        self.info2.place(relx=0.2,rely=0.25)
        self.info3=customtkinter.CTkLabel(master=None,text="2. The amount of data that can be encoded is based on image resolution.\n    Refer below given values for Encoding :",height=20,width=200,justify="left",fg_color="gray35",text_color="white",font=('Centaur',20))
        self.info3.place(relx=0.2,rely=0.3)
        self.info4=customtkinter.CTkLabel(master=None,text="RESOLUTION\tDATA",fg_color="gray35",text_color="red",font=('Aparajita',25))
        self.info4.place(relx=0.38,rely=0.4)
        self.info5=customtkinter.CTkLabel(master=None,text="640 x 480\t   110 KB\n800 x 600\t   175 KB\n1024 x 768\t   288 KB\n1280 x 720\t   337 KB\n1280 x 960\t   450 KB\n1280 x 1024\t   480 KB\n1600 x 1200\t   703 KB\n1920 x 1080\t   760 KB\n2048 x 1536\t   1152 KB\n2560 x 1440\t   1349 KB",justify="left",fg_color="gray35",text_color="light blue",font=('Aparajita',20))
        self.info5.place(relx=0.4,rely=0.45)
        self.encodeb=customtkinter.CTkButton(master=None,text="Encode",height=40,width=80,command=self.Encode)
        self.encodeb.place(relx=0.3,rely=0.8)        
        self.decodeb=customtkinter.CTkButton(master=None,text="Decode",height=40,width=80,command=self.Decode)
        self.decodeb.place(relx=0.6,rely=0.8)
    
    def openmsgfile(self):
        global msgfilename,msgflag
        if(self.msgcount > 0):
            self.label1.place_forget()
        self.msgcount=self.msgcount+1
        msgfilename=StringVar()
        msgfilename=fd.askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("text files","txt"),("all files","*.*"))) 
        self.label1=customtkinter.CTkLabel(master=None,text=msgfilename)
        self.label1.place(relx=0.35,rely=0.3) 
        if(msgfilename != ""):
            msgflag = 1

    def openimgfile(self):
        global imgfilename,imgflag
        if(self.imgcount > 0):
            self.label2.place_forget()
        self.imgcount=self.imgcount+1
        imgfilename=StringVar()
        imgfilename=fd.askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg,png files","*jpg *png"),("all files","*.*")))     
        self.label2=customtkinter.CTkLabel(master=None,text=imgfilename)
        self.label2.place(relx=0.35,rely=0.1)
        if(imgfilename != ""):
            imgflag = 1

    def output_directory(self):
        global outputdestinationflag,output_directory_name
        if(self.outputdestinationcount>0):
            self.label5.place_forget()
        output_directory_name=StringVar()
        self.outputdestinationcount=self.outputdestinationcount+1
        output_directory_name=fd.askdirectory(initialdir="/Desktop",title="Select Directory")
        self.label5 = customtkinter.CTkLabel(master=None,text=output_directory_name)
        self.label5.place(relx=0.35,rely=0.5)
        if(output_directory_name != ""):
            outputdestinationflag = 1

    def Encrypt_PopUpThread(self,Encrypt_thread):
        while(Encrypt_thread.is_alive()):
            time.sleep(1)
        messagebox.showinfo("","Encoding Complete")
        
    def Decode_PopUpThread(self,Decode_thread):
        while(Decode_thread.is_alive()):
            time.sleep(1)
        messagebox.showinfo("","Decoding Complete")
        
    def begin_encode(self):  
        global outputimgfilename
        outputimgfilename = self.img_entry.get()
        if(outputimgfilename=="" or imgfilename=="" or msgfilename==""):
            messagebox.showinfo("","Please select all the required files")
        else:
            E = Encrypt.Encrypt_class(msgfilename,imgfilename,output_directory_name,outputimgfilename) 
            Encrypt_thread = Thread(target = E.encrypt)
            Encrypt_thread.start()
            messagebox.showinfo("","Encoding Please Wait")
            PopUp_thread = Thread(target = self.Encrypt_PopUpThread,args=(Encrypt_thread, )) 
            PopUp_thread.start()                            
    
    def Encode(self):   
        self.header1.place_forget()  
        self.frame.place_forget()  
        self.info1.place_forget()  
        self.info2.place_forget()  
        self.info3.place_forget()  
        self.info4.place_forget()  
        self.info5.place_forget()  
        self.imgcount = 0   
        self.msgcount = 0   
        self.outputdestinationcount = 0   
        self.encodeb.place_forget()
        self.decodeb.place_forget()
        self.buttonselect2=customtkinter.CTkButton(master=None,text='Select image file',height=35,width=160,font=('Aparajita',22),command=self.openimgfile)
        self.buttonselect2.place(relx=0.1,rely=0.1)
        self.buttonselect1=customtkinter.CTkButton(master=None,text='Select text file',height=35,width=160,font=('Aparajita',22),command=self.openmsgfile)
        self.buttonselect1.place(relx=0.1,rely=0.3)  
        self.output_destination_button=customtkinter.CTkButton(master=None,text='Output Destination',height=35,width=160,font=('Aparajita',22),command=self.output_directory)
        self.output_destination_button.place(relx=0.1,rely=0.5)
        self.label3=customtkinter.CTkLabel(master=None,text="Enter output image file name",height=20,width=200,font=('Aparajita',23))
        self.label3.place(relx=0.1,rely=0.7)
        self.img_entry=customtkinter.CTkEntry(master=None,placeholder_text="E.g. MyText")
        self.img_entry.place(relx=0.45,rely=0.7)
        self.encode_backbutton=customtkinter.CTkButton(master=None,text="Back",height=40,width=80,command=self.Encode_to_home)
        self.encode_backbutton.place(relx=0.8,rely=0.1)
        self.buttonencode=customtkinter.CTkButton(master=None,text="Encode",height=40,width=80,hover_color="green4",command=self.begin_encode)
        self.buttonencode.place(relx=0.4,rely=0.9)
    
    def begin_decode(self):
        global outputmsgfilename
        outputmsgfilename =  self.msg_entry.get() 
        if(outputmsgfilename == "" or imgfilename=="" or output_directory_name==""):
            messagebox.showinfo("","Please enter all the required files")
        else:
            D = Decode.Decode_class(imgfilename,output_directory_name,outputmsgfilename)
            Decode_thread = Thread(target=D.decode_program)
            Decode_thread.start()
            messagebox.showinfo("","Decoding Please Wait")
            PopUp_thread = Thread(target = self.Decode_PopUpThread,args=(Decode_thread, )) 
            PopUp_thread.start()   

    def Decode(self):
        self.header1.place_forget()  
        self.frame.place_forget()  
        self.info1.place_forget()  
        self.info2.place_forget()  
        self.info3.place_forget()  
        self.info4.place_forget() 
        self.info5.place_forget() 
        self.imgcount = 0
        self.outputdestinationcount = 0 
        self.encodeb.place_forget()
        self.decodeb.place_forget()
        self.decode_backbutton=customtkinter.CTkButton(master=None,text="Back",height=40,width=80,command=self.Decode_to_home)
        self.decode_backbutton.place(relx=0.8,rely=0.1)
        self.buttonselect3=customtkinter.CTkButton(master=None,text='Select image file',height=35,width=160,font=('Aparajita',22),command=self.openimgfile)
        self.buttonselect3.place(relx=0.1,rely=0.1)
        self.label4=customtkinter.CTkLabel(master=None,text="Enter output text file name",height=30,width=200,font=('Aparajita',23))
        self.label4.place(relx=0.1,rely=0.3)
        self.output_destination_button=customtkinter.CTkButton(master=None,text='Output Destination',height=35,width=160,font=('Aparajita',22),command=self.output_directory)
        self.output_destination_button.place(relx=0.1,rely=0.5)
        self.msg_entry=customtkinter.CTkEntry(master=None,placeholder_text="E.g. MyText")
        self.msg_entry.place(relx=0.45,rely=0.3)
        self.buttondecode=customtkinter.CTkButton(master=None,text="Decode",height=40,width=80,hover_color="green4",command=self.begin_decode)
        self.buttondecode.place(relx=0.4,rely=0.7)


imgfilename = ""
outputimgfilename = ""
msgfilename = ""
outputmsgfilename = ""
output_directory_name = ""
imgflag = 0
msgflag = 0
outputdestinationflag = 0

customtkinter.set_appearance_mode("dark")
root = tk.Tk()
root.configure(bg='grey20')
root.title("Image Steganography")
icon=PhotoImage(file='icon.png')
root.iconphoto(False,icon)
app = MainWindow(root)
root.mainloop()