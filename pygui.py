from tkinter import *
from tkinter import messagebox
from tkinter import ttk
app=Tk()
app.title('First Fit Management scheme')
app.geometry('650x600')
table=ttk.Treeview(app)
app.configure(bg="#141414")

def submitValue():

    if blockSize.get()=='' or numBlock.get()=='' or processSize.get()=='':
         messagebox.showerror('Required field','Please Fill Fields')
         return 

    numBlockDE=int(numBlock.get())
    item1=str(blockSize.get())
    item2=str(processSize.get())
    blockSizeDE = [int(item) for item in item1.split()]
    processSizeDE= [int(item) for item in item2.split()]

    treeview(blockSizeDE)

def treeview(blockSizedDE):
    
    table['columns']=('Process Allocated','Blocks Declared')
    table.place(x=200,y=300)

    table.column("#0",width=0,stretch=NO)
    table.column("Process Allocated",anchor=CENTER,width=120)
    table.column("Blocks Declared",anchor=CENTER,width=120)

    table.heading("#0",text='',anchor=W)
    table.heading("Process Allocated",text="Process Allocated",anchor=CENTER)
    table.heading("Blocks Declared",text="Blocks Declared",anchor=CENTER)

    count=0
    for record in blockSizedDE:
        table.insert(parent='',index='end',text='',values=(blockSizedDE[count]))
        count +=1

def allot():
    print('alott')

def clear():
    blockEntry.delete(0,END)
    numBlockEntry.delete(0,END)
    processEntry.delete(0,END)
    for record in table.get_children():
        table.delete(record)
    

numBlock=StringVar()
numBlockLabel=Label(app,text='Number of blocks: ',bg='#141414',fg='#FFFFFF',font=('bold',12),pady=20,padx=10)
numBlockLabel.grid(row=0,column=0,sticky=W)
numBlockEntry=Entry(app,width=60,textvariable=numBlock)
numBlockEntry.grid(row=0,column=1)

blockSize=StringVar()
blockLabel=Label(app,text='Declare Blocks: ',bg='#141414',fg='#FFFFFF',font=('bold',12),pady=20,padx=10)
blockLabel.grid(row=1,column=0,sticky=W)
blockEntry=Entry(app,width=60,textvariable=blockSize)
blockEntry.grid(row=1,column=1)

processSize=StringVar()
processLabel=Label(app,text='Process size: ',bg='#141414',fg='#FFFFFF',font=('bold',12),pady=20,padx=10)
processLabel.grid(row=2,column=0,sticky=W)
processEntry=Entry(app,width=60,textvariable=processSize)
processEntry.grid(row=2,column=1)

submitButton=Button(app,text="Submit",width=14,height=2,command=submitValue)
submitButton.grid(row=4,column=0)
clearButton=Button(app,text="Clear",width=14,height=2,command=clear)
clearButton.grid(row=4,column=1)
goButton=Button(app,text='GO',width=14,height=2,command=allot)
goButton.grid(row=4,column=2)


app.mainloop()