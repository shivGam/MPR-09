from tkinter import *
import time
import os
import tkinter as tk
from tkinter import ttk 
from PIL import Image , ImageTk
import threading

app=Tk()#app is an object of class Tk() and Tk() is a class in tkinTer library

app.title('Sidevideo')
app.geometry('780x600')
app.configure(bg="#f7e7ce")

vidFrame=[]
frameDelay = 0
frameCount =-1
start=False
label = tk.Label(app)

def typeWrite(string):
        listString = list(string)
        for char in listString:
            print(char, end="", flush=True)
            time.sleep(0.075)
        return ""


class tutorial(ttk.Frame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master = parent)

        style = ttk.Style()
        style.configure("Custom.TFrame", background="grey", )
        
        # Apply the custom style to the frame
        self.configure(style="Custom.TFrame")
        self.start_pos = start_pos 
        self.end_pos = end_pos - 0.01
        self.width = abs(start_pos-end_pos)

        self.pos=self.start_pos
        self.inStartPos = True

        self.place(relx=self.start_pos,rely=0.02,relwidth=self.width,relheight=0.95)

        # Create a Label widget for the GIF
        # self.gifLabel = Label(self)
        # self.gifLabel.pack(expand=True,fill='both',padx=2,pady=2) 

        self.video_label = ttk.Label(self)
        self.video_label.pack(expand=True, fill='both', padx=2, pady=2)

        self.text_label = ttk.Label(self)
        self.text_label.pack(expand=True, fill='both', padx=2, pady=2)
        
        
        self.after(50, self.typeWriter,
        '''
        Job 1 cannot fit into block 1 with only 10k size so we will move to block 2.

        job1 also cannot fit in block 2 with only 5k size in block 3 we have 30k size
        so we can fit our job to this block in first fit we don't have to check
        remaining block after we find block that can be allocate

        after we allocate a job 1 into block we will have 1 0k internal fragmentation
        next we will quick go through remaining

        job first job 2.
        next we move to job3
        and the last one we move to job 4.
        
        so we already finished all of our four Jobs''')

    def typeWriter(self, text):
        if text:
            # Update the label text with the next character
            self.text_label.config(text=self.text_label["text"] + text[0])
            # Call the function again after a delay
            self.after(100, self.typeWriter, text[1:])

    def animate(self):
        if self.inStartPos:
            self.animateFor()
        else:
            self.animateBack()
    
    def animateFor(self):
        if self.pos > self.end_pos:
            self.pos -= 0.010
            self.place(relx=self.pos,rely=0.02,relwidth=self.width,relheight=0.95)
            self.after(10,self.animateFor)
        else:
            self.inStartPos=False
    
    def animateBack(self):
        if self.pos < self.start_pos:
            self.pos += 0.010
            self.place(relx=self.pos,rely=0.02,relwidth=self.width,relheight=0.95)
            self.after(10,self.animateBack)
        else:
            self.inStartPos = True

    

    def startVideo(self):
        global frameCount,currFrame
        if frameCount >=len(vidFrame)-1:
            frameCount=-1
        else:
            frameCount+=1
            currFrame=ImageTk.PhotoImage(vidFrame[frameCount])
            self.video_label.config(image=currFrame)
            app.after(frameDelay,self.startVideo)
        
        # Set the image of the gifLabel to the current frame
        # self.gifLabel.config(image=currFrame)
        # app.after(frameDelay, self.startVideo)
    
    def playVideo(self):
        global frameDelay
        print('started')
        vidFile=Image.open('ffmfinal.gif')
            
        for r in range(0,vidFile.n_frames):
            vidFile.seek(r)
            vidFrame.append(vidFile.copy())
        
        frameDelay=vidFile.info['duration']
        print('Complete')
        #self.startVideo()
    
    
panel=tutorial(app,1,0.3)

#panel.playVideo
Lsidebutton = Button(app, text ="Tutorial" ,font=('bold',10),width=14,height=2,border=0,fg='#f86263',bg='#f7e7ce',command=lambda:[panel.startVideo(),panel.animate()])
Lsidebutton.place(x=5,y=540)


videoLb=ttk.Label(app)
videoLb.pack(fill='both',padx=2,pady=2)

threading.Thread(target=panel.playVideo).start()

app.mainloop()

