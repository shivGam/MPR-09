from tkinter import *
import os
from tkinter import messagebox #messeage box is a widget which displays a message on certain condition is revoked i.e. validation
from tkinter import ttk #treeview is widget which can display data in hierachical structure 
from mpr09 import Main
app=Tk()#app is an object of class Tk() and Tk() is a class in tkinTer library

app.title('First Fit Management scheme')
app.geometry('780x600')

table=ttk.Treeview(app)
app.configure(bg="#f7e7ce")

def submitValue():

    if blockSize.get()=='' or numBlock.get()=='' or processSize.get()=='':
         messagebox.showerror('Required field','Please Fill Fields')
         return 
    for record in table.get_children():
        table.delete(record)
        
    numBlockDE=int(numBlock.get())
    item1=str(blockSize.get())
    item2=str(processSize.get())
    blockSizeDE = [int(item) for item in item1.split()]
    processSizeDE= [int(item) for item in item2.split()]
    Main.defineValue(blockSizeDE,processSizeDE)

    treeview_for_only_blocks(blockSizeDE,numBlockDE,processSizeDE)
    #return numBlockDE,blockSizeDE,processSizeDE

def treeview_for_only_blocks(blockSizedDE,numberBlockDE,processSizeDE):
    
    table['columns']=('Process Allocated','Blocks Declared')
    table.place(x=200,y=300)

    table.column("#0",width=0,stretch=NO)
    table.column("Process Allocated",anchor=CENTER,width=120)
    table.column("Blocks Declared",anchor=CENTER,width=120)

    table.heading("#0",text='',anchor=W)
    table.heading("Process Allocated",text="Process Allocated",anchor=CENTER)
    table.heading("Blocks Declared",text="Blocks Declared",anchor=CENTER)
    
    result=Main.allocation()
    for record in result:
        table.insert(parent='',index='end',text='',values=(0,record[1]))
    
def treeview_for_only_allocation(blockSizedDE,processSizeDE):
    #edit kar
    table['columns']=('Process Allocated','Blocks Declared')
    table.place(x=200,y=300)

    table.column("#0",width=0,stretch=NO)
    table.column("Process Allocated",anchor=CENTER,width=120)
    table.column("Blocks Declared",anchor=CENTER,width=120)

    table.heading("#0",text='',anchor=W)
    table.heading("Process Allocated",text="Process Allocated",anchor=CENTER)
    table.heading("Blocks Declared",text="Blocks Declared",anchor=CENTER)
    result=Main.allocation()
    print(result)
      
def allot():
    if blockSize.get()=='' or numBlock.get()=='' or processSize.get()=='':
         messagebox.showerror('Required field','Please Fill Fields')
         return 
    treeview_for_only_allocation(Main.block_sizes,Main.process)
    for record in table.get_children():
        table.delete(record)
    result=Main.allocation()
    for record in result:
        table.insert(parent='',index='end',text='',values=(record[0],record[1]))

def demons():
    os.system('python demonstration.py')

def tut():
    os.system('python tutorial.py')

def clear():
    blockEntry.delete(0,END)
    numBlockEntry.delete(0,END)
    processEntry.delete(0,END)
    for record in table.get_children():
        table.delete(record)

def on_enter(e):
    submitButton['background']='#f86263'
    submitButton['foreground']='#f7e7ce'
    clearButton['background']='#f86263'
    clearButton['foreground']='#f7e7ce'
    goButton['background']='#f86263'
    goButton['foreground']='#f7e7ce'

def on_leave(e):
    submitButton['background']='#f7e7ce'
    submitButton['foreground']='#f86263'
    clearButton['background']='#f7e7ce'
    clearButton['foreground']='#f86263'
    goButton['background']='#f7e7ce'
    goButton['foreground']='#f86263'

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
    


panel=tutorial(app,1,0.3)


numBlock=StringVar()#stringVar() string data where we can set text value and can retrive it
numBlockLabel=Label(app,text='Number of blocks: ',bg='#f7e7ce',fg='#141414',font=('bold',12),pady=20,padx=10)#Label is used to specify container box where we display text as well as images
numBlockLabel.grid(row=0,column=0,sticky=W)
numBlockEntry=Entry(app,width=80,textvariable=numBlock)#Entry box is widget which is used to enter or display a single line text
numBlockEntry.grid(row=0,column=1)

blockSize=StringVar()
blockLabel=Label(app,text='Declare Blocks: ',bg='#f7e7ce',fg='#141414',font=('bold',12),pady=20,padx=10)
blockLabel.grid(row=1,column=0,sticky=W)
blockEntry=Entry(app,width=80,textvariable=blockSize)
blockEntry.grid(row=1,column=1)

processSize=StringVar()
processLabel=Label(app,text='Process size: ',bg='#f7e7ce',fg='#141414',font=('bold',12),pady=20,padx=10)
processLabel.grid(row=2,column=0,sticky=W)
processEntry=Entry(app,width=80,textvariable=processSize)
processEntry.grid(row=2,column=1)

submitButton=Button(app,text="Submit",font=('bold',10),width=14,height=2,border=0,fg='#f86263',bg='#f7e7ce',activeforeground='#f7e7ce',activebackground='#f86263',command=submitValue)
submitButton.grid(row=4,column=0)#button is widget which is used to interact with user
submitButton.bind("<Enter>",on_enter)
submitButton.bind("<Leave>",on_leave)

clearButton=Button(app,text="Clear",font=('bold',10),width=14,height=2,border=0,fg='#f86263',bg='#f7e7ce',activeforeground='#f7e7ce',activebackground='#f86263',command=clear)
clearButton.grid(row=4,column=1)
clearButton.bind("<Enter>",on_enter)
clearButton.bind("<Leave>",on_leave)

goButton=Button(app,text='GO',font=('bold',10),width=14,height=2,border=0,fg='#f86263',bg='#f7e7ce',activeforeground='#f7e7ce',activebackground='#f86263',command=allot)
goButton.grid(row=4,column=2)
goButton.bind("<Enter>",on_enter)
goButton.bind("<Leave>",on_leave)

Lsidebutton = Button(app, text ="Tutorial" ,font=('bold',10),width=14,height=2,border=0,fg='#f86263',bg='#f7e7ce',command = panel.animate)
Lsidebutton.place(x=5,y=540)

Rsidebutton = Button(app, text ="Demonstrate" ,font=('bold',10),width=14,height=2,border=0,fg='#f86263',bg='#f7e7ce',command = demons)
Rsidebutton.place(x=650,y=540)

app.mainloop()