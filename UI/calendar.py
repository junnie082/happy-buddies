from tkinter import *
from tkcalendar import DateEntry

root = Tk()

f1=Frame(root,width=1500,height=100,relief=SUNKEN,bd=4,bg='light steel blue')
f1.pack(side=TOP)
f2=Frame(root,width=1500,height=550,relief=SUNKEN,bd=4,bg='white')
f2.pack()
f3=Frame(root,width=1600,height=100,relief=SUNKEN,bd=4,bg='white')
f3.pack(side=BOTTOM)


#Creating the date column
l4=Label(f2,text='DATE',font=('tahoma',20,'bold'),fg='black',anchor='w')
l4.grid(row=0,column=3)

cal=DateEntry(f2,dateformat=3,width=12, background='darkblue',
                    foreground='white', borderwidth=4,Calendar =2018)
cal.grid(row=1,column=3,sticky='nsew')

root.mainloop()
# [출처] [tkinter] calendar 사용하기|작성자 초초

