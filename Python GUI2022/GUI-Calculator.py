from tkinter import *
from tkinter import ttk,messagebox
import csv

def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #  fw = file writer
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมแรกของฉัน')
GUI.geometry('500x300')

FONT1 = ('Angsana New',25)
FONT2 = ('impact',25)

L1 = Label(GUI,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=FONT1).pack()

v_kilo  = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_kilo,width=10,justify='right',font=FONT2)
E1.pack()

def Calc(event=None):
    print('กำลังคำนวน...รอสักครู่')
    kilo = float(v_kilo.get())
    print(kilo * 10)
    calc_result = kilo * 299
    data = ['กุ้ง','{:.2f}'.format(calc_result)]
    writetocsv(data)

    messagebox.showinfo('รวมราคาทั้งหมด','ลูกค้าต้องจ่ายตังทั้งหมด {:.2f} บาท (กิโลกรัมละ 299 บาท)'.format(calc_result))

B1 = ttk.Button(GUI,text='กรุณาคลิกปุ่มนี้',command=Calc)
B1.pack(ipadx=50,ipady=30,pady=50)

E1.bind('<Return>',Calc)

GUI.mainloop()