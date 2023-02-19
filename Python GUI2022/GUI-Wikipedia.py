from tkinter import *
from tkinter import ttk,messagebox
import csv
import wikipedia
from datetime import datetime
import webbrowser

def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #  fw = file writer
        fw.writerow(data)

GUI = Tk()
GUI.title('โปรแกรมจัดการ layout')
GUI.geometry('1200x600')

####### TAB Setting 
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

############ TAB 1 กุ้ง ###############

FONT1 = ('Angsana New',25)
FONT2 = ('impact',25)

# set Photo
icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')
icon_tab3 = PhotoImage(file='tab3.png')

latte = PhotoImage(file='latte.png')

Tab.add(T1,text='กุ้ง',image=icon_tab1,compound='left')
Tab.add(T2,text='Wiki',image=icon_tab2,compound='left')
Tab.add(T3,text='CAFE',image=icon_tab3,compound='left')

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
v_link = StringVar() # สร้างตัวแปรเพื่อเอาไปใช้งานในฟังก์ชั่นอื่นต่อ

def Search():

    try:
        search = v_search.get() # ดึงข้อความจากช่องกรอก 
        # text = wikipedia.summary(search)
        text = wikipedia.page(search)
        # print(text)
        v_result.set(text.content[:800]) # กำหนดข้อความให้น้อยกว่า 1500 ตัวอักษร
        print('Link',text.url)
        v_link.set(text.url)
        B3 = ttk.Button(T2,text='อ่านต่อ',command=readmore).pack()
    except:
        v_result.set('ไม่มีข้อมูล กรุณาค้นหาใหม่')

    # เพิ่ม Function สำหรับเว็บ Browser


B2 = ttk.Button(T2,text='search',image=icon_tab2,compound='left',command=Search).pack(ipadx=40)

def readmore():
    webbrowser.open(v_link.get())

v_result = StringVar()
v_result.set('-------Result--------')
result = Label(T2,textvariable=v_result,wraplength=550).pack() # wraplength=550 ตัดคำขึ้นบรรทัดใหม่

############ TAB 3 Ca'fe ###############

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsna New',11))

CF1 = Frame(T3)
CF1.place(x=50,y=100)

allmenu = {}

product = {'latte':{'name':'ลาเต้','price':30},
            'cappuccino':{'name':'คาปูชิโน','price':35},
            'espresso':{'name':'เอสเปรสโซ','price':40}}

def UpdateTable():
    table.delete(*table.get_children())
    for i ,m in enumerate(allmenu.values(),start=1):
        table.insert('','end',value=[i,m[0],m[1],m[2],m[3]])


def AddMenu(name = 'latte'):
    #name = 'latte'
    if name not in allmenu:

        allmenu[name] = [product[name]['name'],product[name]['price'],1,product[name]['price']]
        print(allmenu)
    else:
        qaun = allmenu[name][2] + 1
        total = qaun * product[name]['price']
        allmenu[name] = [product[name]['name'],product[name]['price'],qaun,total]
        print(allmenu)

def Menu1():
    AddMenu('latte')
    UpdateTable()

def Menu2():
    AddMenu('cappuccino')
    UpdateTable()

def Menu3():
    AddMenu('espresso')
    UpdateTable()





# ROW0
B = ttk.Button(CF1,text='ลาเต้',image=latte,compound='top',command=Menu1).grid(row=0,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='คาปูชิโน',image=icon_tab3,compound='top',command=Menu2).grid(row=0,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='เอสเปรสโซ่่',image=icon_tab3,compound='top',command=Menu3).grid(row=0,column=2,ipadx=20,ipady=10)

# ROW1

B = ttk.Button(CF1,text='ชาเขียว',image=icon_tab3,compound='top').grid(row=1,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาเย็น',image=icon_tab3,compound='top').grid(row=1,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาร้อน',image=icon_tab3,compound='top').grid(row=1,column=2,ipadx=20,ipady=10)

CF2 = Frame(T3)
CF2.place(x=500,y=100)

header = ['No.','title','price','quantity','total']
hwidth = [50,200,100,100,100]


table = ttk.Treeview(CF2,columns=header, show='headings',height=15)
table.pack()

for hd,hw in zip(header,hwidth):


    table.column(hd,width=hw)
    table.heading(hd,text=hd)




GUI.mainloop()