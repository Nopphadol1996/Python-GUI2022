from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.title('โปรแกรมแรกของฉัน')
GUI.geometry('500x300')

def show():
    messagebox.showinfo('Show Box','สวสัดีจ้าได้แล้ว')

B1 = ttk.Button(GUI,text='กรุณาคลิกปุ่มนี้',command=show)
B1.pack(ipadx=50,ipady=30,pady=50)

GUI.mainloop()