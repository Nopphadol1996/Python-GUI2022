from tkinter import *
from tkinter import ttk,messagebox
import csv
import wikipedia
from datetime import datetime

def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #  fw = file writer
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมจัดการ layout')
GUI.geometry('800x600')

####### TAB Setting 
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)

############ TAB 1 กุ้ง ###############

FONT1 = ('Angsana New',25)
FONT2 = ('impact',25)

icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')

Tab.add(T1,text='กุ้ง',image=icon_tab1,compound='left')
Tab.add(T2,text='Wiki',image=icon_tab2,compound='left')

L1 = Label(T1,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=FONT1).pack()

v_kilo  = StringVar()
E1 = ttk.Entry(T1,textvariable=v_kilo,width=10,justify='right',font=FONT2)
E1.pack()

def Calc(event=None):
    print('กำลังคำนวน...รอสักครู่')
    kilo = float(v_kilo.get())
    print(kilo * 10)
    calc_result = kilo * 299
    date = datetime.now()
    year = date.year + 543
    stamp = date.strftime('{}-%m-%d %H:%M:%S'.format(year)) # Thai year
    data = [stamp,'กุ้ง','{:.2f}'.format(calc_result)]
    writetocsv(data)

    messagebox.showinfo('รวมราคาทั้งหมด','ลูกค้าต้องจ่ายตังทั้งหมด {:.2f} บาท (กิโลกรัมละ 299 บาท)'.format(calc_result))

B1 = ttk.Button(T1,text='กรุณาคลิกปุ่มนี้',command=Calc)
B1.pack(ipadx=50,ipady=30,pady=50)

E1.bind('<Return>',Calc)

############ TAB 2 Wiki ###############
L2 = Label(T2,text='ค้นหาข้อมูล wikipedia',font=('Angsna New',25))
L2.pack()

v_search = StringVar()
E2 = ttk.Entry(T2,textvariable=v_search,font=FONT1).pack(pady=10)

wikipedia.set_lang("th") # ตั้งเป็นภาษาไทย
def Search():

    try:

        search = v_search.get() # ดึงข้อความจากช่องกรอก 
        text = wikipedia.summary(search)
        # print(text)
        # v_result.set(text[:500])
        v_result.set(text[:1500]) # กำหนดข้อความให้น้อยกว่า 1500 ตัวอักษร
    except:
        v_result.set('ไม่มีข้อมูล กรุณาค้นหาใหม่')

    # เพิ่ม Function สำหรับเว็บ Browser


B2 = ttk.Button(T2,text='search',image=icon_tab2,compound='left',command=Search).pack(ipadx=40)

v_result = StringVar()
v_result.set('-------Result--------')
result = Label(T2,textvariable=v_result,wraplength=550).pack() # wraplength=550 ตัดคำขึ้นบรรทัดใหม่

GUI.mainloop()