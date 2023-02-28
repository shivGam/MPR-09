from tkinter import *
from tkinter import messagebox
app=Tk()
app.title('First Fit Management scheme')
app.geometry('800x400')
#app.configure(bg="#141414")

def submitValue():

    if blockSize.get()=='' or numBlock.get()=='' or processSize.get()=='':
         messagebox.showerror('Required field','Please Fill Fields')
         return 

    numBlockDE=int(numBlock.get())
    item1=str(blockSize.get())
    item2=str(processSize.get())
    blockSizeDE = [int(item) for item in item1.split()]
    processSizeDE= [int(item) for item in item2.split()]

    clear()

def allot():
    print('alot')

def clear():
    blockEntry.delete(0,END)
    numBlockEntry.delete(0,END)
    processEntry.delete(0,END)

numBlock=StringVar()
numBlockLabel=Label(app,text='Number of blocks: ',font=('bold',12),pady=20,padx=10)
numBlockLabel.grid(row=0,column=0,sticky=W)
numBlockEntry=Entry(app,width=60,textvariable=numBlock)
numBlockEntry.grid(row=0,column=1)

blockSize=StringVar()
blockLabel=Label(app,text='Declare Blocks: ',font=('bold',12),pady=20,padx=10)
blockLabel.grid(row=1,column=0,sticky=W)
blockEntry=Entry(app,width=60,textvariable=blockSize)
blockEntry.grid(row=1,column=1)

processSize=StringVar()
processLabel=Label(app,text='Process size: ',font=('bold',12),pady=20,padx=10)
processLabel.grid(row=2,column=0,sticky=W)
processEntry=Entry(app,width=60,textvariable=processSize)
processEntry.grid(row=2,column=1)

submitButton=Button(app,text="Submit",width=12,command=submitValue)
submitButton.grid(row=4,column=0)
clearButton=Button(app,text="Clear",width=12,command=clear)
clearButton.grid(row=4,column=1)
goButton=Button(app,text='GO',width=12,command=allot)
goButton.grid(row=4,column=2)

app.mainloop()