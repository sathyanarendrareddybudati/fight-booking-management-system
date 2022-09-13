from fpdf import FPDF
import qrcode
from tkinter import *
from tkinter import ttk
from time import strftime
import datetime
import time
import random
import os
import mysql.connector
flights = Tk()
flights.title('Flight bookings')
flights.geometry('500x600')
flights.configure(bg='yellow')
flights.resizable(False, False)
top = Frame(flights, bg="yellow")
top.pack(side=TOP, anchor=E)
flight = Frame(flights, bg='yellow')
flight.pack(pady=10, padx=10)
mydb = mysql.connector.connect(host="localhost", user="root", passwd="satya199", database="flight")
mycursor = mydb.cursor()
price_data = mysql.connector.connect(host="localhost", user="root", passwd="satya199", database="flight")
data_cursor = price_data.cursor()


def ttt():
    st = strftime('%H:%M:%S %p')
    la.config(text=st)
    la.after(1, ttt)


def btd():
    try:
        pfd.destroy()
    except:
        pass


def chk():
    usid = u.get()
    uspw = p.get()
    global pfd
    #create database flight
    #create table data ( userid varchar(20), password varchar(20))
    mycursor.execute("select * from data")
    myres=mycursor.fetchall()
    if usid == "" or uspw == "":
        btd()
        pfd = Label(flight, text="Please fill the details", bg="red")
        pfd.grid(row=4, columnspan=2, pady=10)
    elif (usid, uspw) in myres:
        btd()
        lgn()
        mnp()
    else:
        btd()
        pfd = Label(flight, text="Password is wrong", bg="red")
        pfd.grid(row=4, columnspan=2, pady=10)
        p.set("")


def bdp():
    try:
        ped.destroy()
    except:
        pass


def inst():
    reid = ru.get()
    repw = rp.get()
    reps = rep.get()
    global ped
    mycursor.execute("select userid from data")
    myres=mycursor.fetchall()
    if reid == "" or repw == "" or reps == "":
        bdp()
        ped = Label(flight, text="Please Fill Details", bg='red')
        ped.grid(row=3, column=0)
    elif repw != reps:
        bdp()
        ped = Label(flight, text="Please Check credentials", bg='red')
        ped.grid(row=3, column=0)
    elif (reid, ) in myres:
        bdp()
        ped = Label(flight, text="User id is already taken", bg='red')
        ped.grid(row=3, column=0)
    else:
        bdp()
        form = "insert into data (userid, password) values(%s, %s)"
        mems = [(reid, repw)]
        mycursor.executemany(form, mems)
        mydb.commit()
        fff()
        lgp()


def maximize():
    global clm
    flights.attributes("-fullscreen", True)
    clm = Button(top, text="❏", command=minimize)
    clm.grid(row=0, column=1)
    try:
        cln.destroy()
    except:
        pass


def minimize():
    global cln
    flights.attributes("-fullscreen", False)
    cln = Button(top, text="❏", command=maximize)
    cln.grid(row=0, column=1)
    try:
        clm.destroy()
    except:
        pass


def ext():
    try:
        os.remove(f_name)
    except:
        pass
    finally:
        flights.destroy()


maximize()
clt = Button(top, text="-", command=lambda: flights.iconify()) #.iconify()   .wm_state('iconic')
clt.grid(row=0, column=0)
clb = Button(top, text="X", command=ext)
clb.grid(row=0, column=2)
btm = Frame(flights, bg="yellow")
btm.pack(side=BOTTOM)
la = Label(btm, font=("Times New Roman", 15), bg="black", fg='cyan')
la.grid(row=0, column=2)
ttt()
ct = datetime.datetime.now()
ls = Label(btm, text="    ", bg="yellow")
ls.grid(row=0, column=1, padx=400)
lb = Label(btm, text=(str(ct.day)+":"+str(ct.month)+":"+str(ct.year)), font=("Times New Roman", 15), bg='black',
           fg="cyan")
lb.grid(row=0, column=0)
a = StringVar()
b = StringVar()
u = StringVar()
p = StringVar()
ru = StringVar()
rp = StringVar()
rep = StringVar()


def dest():
    wel.destroy()
    co.destroy()
    clk.destroy()
    cpback.destroy()


def lgarg():
    global wel, clk, co, cpback
    cpback = Button(flight, text='Back', command=lambda: [main_page(), dest()])
    cpback.grid(row=0, column=0, pady=20)
    wel = Label(flight, text="Welcome To Reyaz Flight Bookings", font=('Arial', 20, 'bold'))
    wel.grid(row=1, column=0, pady=10)
    clk = Button(flight, text="Login", font=10, height=2, width=20, command=lambda: [lgp(), dest()])
    clk.grid(row=2, column=0, pady=40)
    co = Button(flight, text="Register", font=10, height=2, width=20, command=lambda: [regt(), dest()])
    co.grid(row=3, column=0, pady=10)


def fff():
    rr.destroy()
    ff.destroy()
    rrr.destroy()


def regt():
    global rr, ff, rrr
    rr = Button(flight, text="Back", command=lambda: [bdp(), fff(), lgarg()])
    rr.grid(row=0, column=0)
    rrr = Label(flight, text='Registration', font=20)
    rrr.grid(row=1, column=0, pady=20)
    ff = Frame(flight, bg='yellow')
    ff.grid(row=2, column=0)
    Label(ff, text='First Name').grid(row=0, column=0, padx=20)
    Entry(ff).grid(row=0, column=1)
    Label(ff, text='Last Name').grid(row=1, column=0, padx=20, pady=20)
    Entry(ff).grid(row=1, column=1)
    Label(ff, text='User id:').grid(row=2, column=0, padx=20)
    Entry(ff, textvariable=ru).grid(row=2, column=1)
    Label(ff, text='Password').grid(row=3, column=0, padx=20, pady=20)
    Entry(ff, textvariable=rp, show='*').grid(row=3, column=1)
    Label(ff, text='Retype pwd:').grid(row=4, column=0, padx=20)
    Entry(ff, textvariable=rep).grid(row=4, column=1)
    Label(ff, text='Ph no:').grid(row=5, column=0, padx=20, pady=20)
    Entry(ff).grid(row=5, column=1)
    Label(ff, text='Email id:').grid(row=6, column=0, padx=20)
    Entry(ff).grid(row=6, column=1)
    Label(ff, text='Address:').grid(row=7, column=0, padx=20, pady=20)
    Entry(ff).grid(row=7, column=1)
    Button(ff, text='Register', command=inst).grid(row=8, columnspan=2)


def lgn():
    l1.destroy()
    e1.destroy()
    l2.destroy()
    e2.destroy()
    bt.destroy()


def detmn():
    backb.destroy()
    l1.destroy()
    l2.destroy()
    e1.destroy()
    e2.destroy()
    bt.destroy()


def lgp():
    global l1, l2, e1, e2, bt, backb
    backb = Button(flight, text='Back', command=lambda: [lgarg(), detmn(), btd()])
    backb.grid(row=0, columnspan=2)
    l1 = Label(flight, text="Userid:", font=5)
    l1.grid(row=1, column=0, pady=40)
    e1 = Entry(flight, textvariable=u)
    e1.grid(row=1, column=1, padx=10)
    l2 = Label(flight, text="Password:", font=5)
    l2.grid(row=2, column=0)
    e2 = Entry(flight, textvariable=p, show="*")
    e2.grid(row=2, column=1, padx=10)
    bt = Button(flight, text="Login", command=chk)
    bt.grid(row=3, columnspan=2, pady=40)


def srch():
    global wr
    dlt()
    x = a.get()
    y = b.get()
    data_cursor.execute("select * from prices")
    prices = data_cursor.fetchall()
    if x == 'Hyderabad' and y == 'Chennai':
        sr('Hyderabad', 'Chennai', prices[0][1], prices[0][2], prices[0][3], prices[0][4], prices[0][5])
    elif x == 'Hyderabad' and y == 'Delhi':
        sr('Hyderabad', 'Delhi', prices[1][1], prices[1][2], prices[1][3], prices[1][4], prices[1][5])
    elif x == 'Hyderabad' and y == 'Banglore':
        sr('Hyderabad', 'Banglore', prices[2][1], prices[2][2], prices[2][3], prices[2][4], prices[2][5])
    elif x == 'Banglore' and y == 'Chennai':
        sr('Banglore', 'Chennai', prices[3][1], prices[3][2], prices[3][3], prices[3][4], prices[3][5])
    elif x == 'Banglore' and y == 'Delhi':
        sr('Banglore', 'Delhi', prices[4][1], prices[4][2], prices[4][3], prices[4][4], prices[4][5])
    elif x == 'Banglore' and y == 'Hyderabad':
        sr('Banglore', 'Hyderabad', prices[5][1], prices[5][2], prices[5][3], prices[5][4], prices[5][5])
    elif x == 'Delhi' and y == 'Chennai':
        sr('Delhi', 'Chennai', prices[6][1], prices[6][2], prices[6][3], prices[6][4], prices[6][5])
    elif x == 'Delhi' and y == 'Banglore':
        sr('Delhi', 'Banglore', prices[7][1], prices[7][2], prices[7][3], prices[7][4], prices[7][5])
    elif x == 'Delhi' and y == 'Hyderabad':
        sr('Delhi', 'Hyderabad', prices[8][1], prices[8][2], prices[8][3], prices[8][4], prices[8][5])
    elif x == 'Chennai' and y == 'Delhi':
        sr('Chennai', 'Delhi', prices[9][1], prices[9][2], prices[9][3], prices[9][4], prices[9][5])
    elif x == 'Chennai' and y == 'Banglore':
        sr('Chennai', 'Banglore', prices[10][1], prices[10][2], prices[10][3], prices[10][4], prices[10][5])
    elif x == 'Chennai' and y == 'Hyderabad':
        sr('Chennai', 'Hyderabad', prices[11][1], prices[11][2], prices[11][3], prices[11][4], prices[11][5])
    elif x == y:
        wr = Label(flight, text="Arrival And Deparature are Same", bg='red')
        wr.grid(row=2, columnspan=3, pady=10)
    else:
        wr = Label(flight, text="Couldn't Find", bg='red')
        wr.grid(row=2, columnspan=3, pady=10)


def mdf():
    f3.destroy()
    f4.destroy()
    a0['state'] = NORMAL
    a2['state'] = NORMAL
    a4['state'] = NORMAL
    f2 = Button(flight, bg='green', text='Search', width=7, command=srch)
    f2.grid(row=1, column=0, pady=20)
    try:
        lg.destroy()
    except:
        return
    try:
        wr.destroy()
    except:
        return


def dlt():
    global f3, f4
    f2.destroy()
    a0['state'] = DISABLED
    a2['state'] = DISABLED
    a4['state'] = DISABLED
    f3 = Canvas(flight, bg='pink', height=10)
    f3.grid(row=2, column=0, ipady=10)
    f4 = Button(flight, bg='orange', text='Modify', width=7, command=mdf)
    f4.grid(row=1, column=0, pady=20)
    try:
        wr.destroy()
    except:
        return


def bd():
    bc.destroy()
    py.destroy()
    fr.destroy()
    mp.destroy()


def pp():
    global bc, py, fr, mp, price
    price = 0
    if i.get() == 0:
        price = p1
    elif i.get() == 1:
        price = p2
    elif i.get() == 2:
        price = p3
    elif i.get() == 3:
        price = p4
    else:
        price = p5
    bc = Button(flight, text='Back', command=lambda:[fd(), bd()])
    bc.grid(row=0, column=0)
    py = Label(flight, text="Preview", font=20)
    py.grid(row=1, column=0, pady=20)
    fr = Frame(flight, bg='yellow')
    fr.grid(row=2, column=0)
    Label(fr, text='Ticket cost:').grid(row=0, column=0, pady=20, padx=20)
    Label(fr, text=price).grid(row=0, column=1, padx=20)
    Label(fr, text='Service Tax:').grid(row=1, column=0, padx=20)
    Label(fr, text='203').grid(row=1, column=1, padx=20)
    Label(fr, text='GST:').grid(row=2, column=0, pady=20, padx=20)
    Label(fr, text='78').grid(row=2, column=1, padx=20)
    Label(fr, text='Total').grid(row=3, column=0, padx=20)
    Label(fr, text=str(int(price)+203+78)).grid(row=3, column=1, padx=20)
    mp = Button(flight, text='Make Payment', command=lambda:[bd(),pymt()])
    mp.grid(row=3, column=0, pady=20)


def det():
    bk.destroy()
    pf.destroy()
    sb.destroy()


def dot():
    ob.destroy()
    fo.destroy()
    pot.set("")


def delf():
    dwls.clear()
    os.remove(f_name)


def ddt():
    bb.destroy()
    ll.destroy()
    br.destroy()
    lr.destroy()


def header():
    pdf.set_font('helvetica', 'B', 15)
    title = "Reyaz Flight Bookings (RFB) "
    w = pdf.get_string_width(title) + 6
    pdf.set_x((210 - w) / 2)
    pdf.set_draw_color(0, 80, 180)
    pdf.set_fill_color(235, 230, 0)
    pdf.set_text_color(220, 50, 50)
    pdf.set_line_width(0.7)
    pdf.cell(w, 9, title, 1, 1, 'C', True)


def tite():
    pdf.set_font('helvetica', "B", size=12)
    pdf.set_text_color(0)
    pdf.ln()
    pdf.set_fill_color(250, 220, 255)
    pdf.cell(0, 10, "Flight Ticket", 0, 1, 'C', True)
    pdf.ln()


def qrg():
    global pwd, f_name
    nums = '0000000'
    pwd = "RFB"
    pwd = pwd + nums
    if j.get() == 0:
        Gen = "Gender: Male"
    else:
        Gen = "Gender: Female"
    qrcd = pwd + "\nName: " + f.get() + "." + l.get() + "\nAge:" + g.get() + "\n" + Gen + "\nAddress: " + add.get() + "\nPhone No: " + ph.get() + "\nEmail id: " + ead.get()
    qr = qrcode.make(qrcd)
    f_name = pwd + ".png"
    qr.save(f_name)


def body():
    pdf.set_font('helvetica', "B", size=12)
    pdf.set_text_color(50)
    pdf.set_fill_color(0, 220, 255)
    pdf.cell(45, 15, txt="PNR No: "+pwd, ln=3, align="L", fill=True)
    pdf.set_font('helvetica', "I", size=10)
    pdf.set_text_color(0)
    pdf.set_fill_color(200, 220, 255)
    if i.get() == 0:
        flt = "Indigo"
    elif i.get() == 1:
        flt = "Vistara"
    elif i.get() == 2:
        flt = "Spicejet"
    elif i.get() == 3:
        flt = "Airindia"
    else:
        flt = "Goair"
    Name = "Name: " + f.get() + "." + l.get()
    Age = "Age: " + g.get()
    if j.get() == 0:
        Gen = "Gender: Male"
    else:
        Gen = "Gender: Female"
    Add = "Address: " + add.get()
    Phn = "Phone No: " + "*" * 6 + ph.get()[-4:]
    Emd = "Email id: " + ead.get()[:4]+"*"*6+"@gmail.com"
    pdf.cell(0, 10, txt=Name, ln=3, align="L", fill=True)
    pdf.cell(0, 10, txt=Age, ln=4, align="L", fill=True)
    pdf.cell(0, 10, txt=Gen, ln=5, align="L", fill=True)
    pdf.cell(0, 10, txt=Add, ln=6, align="L", fill=True)
    pdf.cell(0, 10, txt=Phn, ln=7, align="L", fill=True)
    pdf.cell(0, 10, txt=Emd, align="L", fill=True)
    pdf.ln()
    pdf.ln()
    pdf.set_font('helvetica', "B", size=12)
    pdf.set_text_color(0)
    pdf.set_fill_color(150, 220, 255)
    pdf.cell(0, 10, txt="Booking Company: "+flt, ln=9, align="C", fill=True)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 10, txt="Ticket Cost: "+str(int(price)+203+78), ln=10, align="C", fill=True)
    pdf.set_font('helvetica', size=12)
    pdf.set_fill_color(130, 220, 255)
    pdf.cell(0, 10, txt="   ", ln=10, align="L", fill=True)
    pdf.text(30, 160, txt="From : "+arr)
    pdf.text(150, 160, txt="To : "+des)
    pdf.ln()
    pdf.cell(0, 10, txt="Terms and Conditions", ln=10, align="C")
    pdf.set_font('helvetica', size=8)
    pdf.cell(0, 6, txt="1. These Terms of Use along with Terms of Service (collectively, the 'User Agreement') constitute a legally binding agreement made between you, ", ln=10, align="L")
    pdf.cell(0, 6, txt="    whether personally or on behalf of an entity ('You/User') and Le Travenues Technology Private Limited ('Travenues'), a travel technology company", ln=10, align="L")
    pdf.cell(0, 6, txt="    incorporated and existing in India in accordance with the Companies Act, 1956, concerning your access to and use of the rfb.com website", ln=10, align="L")
    pdf.cell(0, 6, txt="    as well as mobile application related, linked, or otherwise connected thereto (collectively, the 'Site').", ln=10, align="L")
    pdf.cell(0, 6, txt="2. You agree that by accessing the site, you have read, understood, and agree to be bound by all of these Terms of Use.If you do not agree", ln=10, align="L")
    pdf.cell(0, 6, txt="    with all of these Terms of Use, then you are expressly prohibited from using the Site and you must discontinue use immediately.", ln=10, align="L")
    pdf.cell(0, 6, txt="3. Supplemental terms and conditions or documents that may be posted on the site from time to time are hereby expressly incorporated herein by", ln=10, align="L")
    pdf.cell(0, 6, txt=" reference. We reserve the right, in our sole discretion, to make changes or modifications to this User Agreement at any time and for any reason.", ln=10, align="L")
    pdf.cell(0, 6, txt="4. The information provided on the Site is not intended for distribution to or use by any person or entity in any jurisdiction or country where", ln=10, align="L")
    pdf.cell(0, 6, txt="    such distribution or use would be contrary to law or regulation or which would subject us to any registration requirement within such", ln=10, align="L")
    pdf.cell(0, 6, txt="    jurisdiction or country.", ln=10, align="L")
    pdf.cell(0, 6, txt="5. The site is intended for users who are at least 18 years old. Persons under the age of 18 are not permitted to register for the site.", ln=10, align="L")
    pdf.cell(0, 6, txt="    If you are a minor, You must have your parent or guardian read and agree to these Terms of Use prior to you using the site. ", ln=10, align="L")
    pdf.set_draw_color(0)
    pdf.dashed_line(0, 170, 300, 170)
    pdf.image(f_name, 120, 63, 60, 60)
    pdf.set_font('helvetica', size=8)
    pdf.text(123, 149, txt="(Inclusive of all taxes)")


def dwn():
    global pdf, p_name
    pdf = FPDF()
    pdf.add_page()
    qrg()
    header()
    pdf.set_font("helvetica")
    pdf.set_title("Booking")
    tite()
    body()
    p_name = l.get()+".pdf"
    pdf.output(p_name)


dwls = []


def dwp():
    global pdf, p_name
    dwls.append("1")
    pdf = FPDF()
    pdf.add_page()
    header()
    pdf.set_font("helvetica")
    pdf.set_title("Booking")
    tite()
    body()
    dwt = len(dwls)
    p_name = l.get()+str(dwt)+".pdf"
    pdf.output(p_name)
    opdf()


def cat():
    f.set("")
    l.set("")
    g.set("")
    add.set("")
    ead.set("")
    ph.set("")
    j.set(0)
    cno.set("")
    chn.set("")
    cvv.set("")
    em.set("")
    ey.set("")
    pot.set("")
    i.set(0)


def vrf():
    global bb, ll, lr, br
    ll = Label(flight, text="Succesful", bg='green', fg='white', font=30)
    ll.grid(row=0, column=0)
    lr = Label(flight, text='You can download the ticket\n By clicking on the Download button', bg='skyblue', font=10)
    lr.grid(row=1, column=0, pady=30)
    br = Button(flight, text='Download', command=dwp)
    br.grid(row=2, column=0, pady=30)
    bb = Button(flight, text="Go to main menu", command=lambda:[delf(), cat(), mnp(), ddt()])
    bb.grid(row=3, column=0, pady=10)


def chod():
    try:
        faf.destroy()
    except:
        pass


def chotp():
    global faf
    chod()
    ktp = pot.get()
    if ktp == opt:
        pot.set("")
        dwn()
        opdf()
        vrf()
        dot()
    elif ktp == "":
        faf = Label(flight, text="Enter OTP", bg='red')
        faf.grid(row=2, column=0, pady=5)
    else:
        faf = Label(flight, text="wrong otp", bg='red')
        faf.grid(row=2, column=0, pady=5)


def opdf():
    os.startfile(p_name)


pot = StringVar()

def otp():
    global ob, fo, opt
    opt = str(random.randrange(1000, 9999))
    print(opt)
    ob = Button(flight, text='Back', command=lambda:[chod(), pymt(), dot()])
    ob.grid(row=0, column=0)
    fo = Frame(flight, bg='yellow')
    fo.grid(row=1, column=0, pady=20)
    Label(fo, text="OTP Verification", font=20).grid(row=0, columnspan=2)
    Label(fo, text="Enter otp:").grid(row=1, column=0, pady=20)
    Entry(fo, textvariable=pot).grid(row=1, column=1, padx=5)
    Button(fo, text='Verify', command=chotp).grid(row=2, columnspan=2)
    Label(fo, text="OTP is generating \nPlease donot press the back button", bg="blue", fg="white").grid(row=3, columnspan=2, pady=10)


def cdvd():
    try:
        ccp.destroy()
    except:
        pass


def cdv():
    global ccp
    cdvd()
    if cno.get() == "" or chn.get() == "" or cvv.get() == "" or em.get() == "" or ey.get() == "":
        ccp = Label(flight, text="Please enter the details", bg="red")
        ccp.grid(row=3, column=0, pady=10)
    else:
        det()
        otp()


cno = StringVar()
chn = StringVar()
cvv = StringVar()
em = StringVar()
ey = StringVar()


def pymt():
    global bk, pf, sb
    bk = Button(flight, text='Back', command=lambda:[cdvd(), pp(), det()])
    bk.grid(row=0, column=0)
    pf = Frame(flight, bg='yellow')
    pf.grid(row=1, column=0, pady=20)
    Label(pf, text='Enter Card Details', font=20).grid(row=0, columnspan=5)
    Label(pf, text="Card Number").grid(row=1, column=0, pady=20)
    Entry(pf, textvariable=cno, width=4).grid(row=1, column=1)
    Entry(pf, width=4).grid(row=1, column=2)
    Entry(pf, width=4).grid(row=1, column=3)
    Entry(pf, width=4).grid(row=1, column=4)
    Label(pf, text="Card Holder Name").grid(row=2, column=0)
    Entry(pf, textvariable=chn).grid(row=2, column=1, columnspan=4, padx=5)
    Label(pf, text="Expiry Date").grid(row=3, column=0, pady=20)
    ttk.Combobox(pf, values=('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'), textvariable=em, width=2).grid(row=3, column=1, columnspan=2)
    ttk.Combobox(pf, values=('2020', '2021', '2022', '2023', '2024', '2025'), textvariable=ey, width=4).grid(row=3, column=3, padx=5, columnspan=2)
    Label(pf, text="CVV:").grid(row=4, column=0)
    Entry(pf, textvariable=cvv).grid(row=4, column=1, columnspan=4)
    sb = Button(flight, text="Confirm Payment", command=cdv)
    sb.grid(row=2, column=0)


def fp():
    lb.destroy()
    fm.destroy()
    cb.destroy()
    bm.destroy()


def contd():
    try:
        conb.destroy()
    except:
        pass


def cont():
    global conb
    contd()
    if f.get() == "" or l.get() == "" or g.get() == "" or add.get() == "" or ph.get() == "" or ead.get() == "":
        conb = Label(flight, text="Please fill all the details", bg="red")
        conb.grid(row=5, column=0, pady=20)
    else:
        pp()
        fp()


f = StringVar()
l = StringVar()
g = StringVar()
add = StringVar()
ead = StringVar()
ph = StringVar()
j = IntVar()


def fd():
    global lb, fm, cb, bm
    bm = Button(flight, text='Back', command=lambda:[contd(), mnp(), fp(), srch()])
    bm.grid(row=0, column=0)
    lb = Label(flight, text="Fill Details", font=20)
    lb.grid(row=1, column=0, pady=20)
    fm = Frame(flight, bg='yellow')
    fm.grid(row=2, column=0)
    Label(fm, text='First Name').grid(row=0, column=0, padx=20)
    Entry(fm, textvariable=f).grid(row=0, column=1)
    Label(fm, text='Last Name').grid(row=1, column=0, padx=20, pady=20)
    Entry(fm, textvariable=l).grid(row=1, column=1)
    Label(fm, text='Age').grid(row=2, column=0, padx=20)
    Entry(fm, textvariable=g).grid(row=2, column=1)
    Label(fm, text='Gender').grid(row=3, column=0, padx=20, pady=20)
    rf = Frame(fm, bg='yellow')
    rf.grid(row=3, column=1)
    rf1 = Radiobutton(rf, text="Male", variable=j, value=0)
    rf1.grid(row=0, column=0)
    rf2 = Radiobutton(rf, text="Female", variable=j, value=1)
    rf2.grid(row=0, column=1, padx=5)
    Label(fm, text='Address').grid(row=4, column=0, padx=20)
    Entry(fm, textvariable=add).grid(row=4, column=1)
    Label(fm, text='Ph No:').grid(row=5, column=0, padx=20)
    Entry(fm, textvariable=ph).grid(row=5, column=1, pady=20)
    Label(fm, text='Email id:').grid(row=6, column=0, padx=20)
    Entry(fm, textvariable=ead).grid(row=6, column=1)
    cb = Button(flight, text="Continue", command=cont)
    cb.grid(row=4, column=0, pady=20)


i = IntVar()


def gt():
    try:
        f4.destroy()
    except:
        pass
    f3.destroy()
    lg.destroy()
    f1.destroy()
    f2.destroy()
    fd()


def sr(x, y, r1, r2, r3, r4, r5):
    global lg, arr, des, p1, p2, p3, p4, p5
    arr = x
    des = y
    p1 = r1
    p2 = r2
    p3 = r3
    p4 = r4
    p5 = r5
    time.sleep(0.8)
    Label(f3, text='Available Flights', width=40).grid(row=0, columnspan=3, pady=10, padx=10)
    Label(f3, text=x, width=15).grid(row=1, column=0)
    Label(f3, text='->', bg='yellow').grid(row=1, column=1, padx=10)
    Label(f3, text=y, width=15).grid(row=1, column=2)
    Label(f3, text='Name', bg='red').grid(row=2,column=0,pady=10)
    Label(f3, text='Price', bg='red').grid(row=2, column=2)
    s1 = Radiobutton(f3, text='Indigo', variable=i, value=0)
    s1.grid(row=3, column=0)
    Label(f3, text=p1).grid(row=3, column=2)
    s2 = Radiobutton(f3, text='Vistara', variable=i, value=1)
    s2.grid(row=4, column=0,pady=10)
    Label(f3, text=p2).grid(row=4, column=2)
    s3 = Radiobutton(f3, text='Spicejet', variable=i, value=2)
    s3.grid(row=5, column=0)
    Label(f3, text=p3).grid(row=5, column=2)
    s4 = Radiobutton(f3, text='AirIndia', variable=i, value=3)
    s4.grid(row=6, column=0,pady=10)
    Label(f3, text=p4).grid(row=6, column=2)
    s5 = Radiobutton(f3, text='GoAir', variable=i, value=4)
    s5.grid(row=7, column=0)
    Label(f3, text=p5).grid(row=7, column=2)
    lg = Button(flight, text="Let's Go", command=gt)
    lg.grid(row=3, column=0, pady=10)


def swp():
    x = a.get()
    y = b.get()
    time.sleep(0.5)
    a.set(y)
    b.set(x)


def ddd():
    f1.destroy()
    f2.destroy()
    u.set("")
    p.set("")
    ru.set("")
    rp.set("")
    rep.set("")
    try:
        f3.destroy()
        lg.destroy()
    except:
        return


def mnp():
    global f1, f2, a0, a2, a4
    f1 = Frame(flight, bg='yellow')
    f1.grid(row=0, column=0)
    a1 = Label(f1, text='From')
    a1.grid(row=0, column=0)
    a2 = ttk.Combobox(f1, values=('Hyderabad', 'Banglore', 'Delhi', 'Chennai'), textvariable=a)
    a2.current(0)
    a2.grid(row=0, column=1)
    a0 = Button(f1, text="Swap", command=swp)
    a0.grid(row=0, column=2, padx=10)
    a3 = Label(f1, text='To')
    a3.grid(row=0, column=3)
    a4 = ttk.Combobox(f1, values=('Chennai', 'Delhi', 'Banglore', 'Hyderabad'), textvariable=b)
    a4.grid(row=0, column=4)
    a4.current(0)
    Button(f1, text="Logout", bg='darkred', fg='white', command=lambda:[ddd(), lgarg()]).grid(row=0, column=5, padx=10)
    f2 = Button(flight, bg='green', text='Search', width=7, command=srch)
    f2.grid(row=1, column=0, pady=20)


i0 = StringVar()
i1 = StringVar()
i2 = StringVar()
i3 = StringVar()
i4 = StringVar()
j0 = StringVar()
j1 = StringVar()
j2 = StringVar()
j3 = StringVar()
j4 = StringVar()
k0 = StringVar()
k1 = StringVar()
k2 = StringVar()
k3 = StringVar()
k4 = StringVar()
l0 = StringVar()
l1 = StringVar()
l2 = StringVar()
l3 = StringVar()
l4 = StringVar()
m0 = StringVar()
m1 = StringVar()
m2 = StringVar()
m3 = StringVar()
m4 = StringVar()
n0 = StringVar()
n1 = StringVar()
n2 = StringVar()
n3 = StringVar()
n4 = StringVar()
o0 = StringVar()
o1 = StringVar()
o2 = StringVar()
o3 = StringVar()
o4 = StringVar()
p0 = StringVar()
p1 = StringVar()
p2 = StringVar()
p3 = StringVar()
p4 = StringVar()
q0 = StringVar()
q1 = StringVar()
q2 = StringVar()
q3 = StringVar()
q4 = StringVar()
r0 = StringVar()
r1 = StringVar()
r2 = StringVar()
r3 = StringVar()
r4 = StringVar()
s0 = StringVar()
s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
t0 = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()


def destpop():
    try:
        popup.destroy()
    except:
        pass


def change():
    global popup
    destpop()
    data1 = 'update prices set Indigo=' + i0.get() + ',Vistara=' + i1.get() + ',Spicejet='+i2.get()+',Airindia='+i3.get()+',Goair='+i4.get()+' where Places = "Hyd to Che"'
    data_cursor.execute(data1)
    data2 = 'update prices set Indigo=' + j0.get() + ',Vistara=' + j1.get() + ',Spicejet=' + j2.get() + ',Airindia=' + j3.get() + ',Goair=' + j4.get() + ' where Places = "Hyd to Del"'
    data_cursor.execute(data2)
    data3 = 'update prices set Indigo=' + k0.get() + ',Vistara=' + k1.get() + ',Spicejet=' + k2.get() + ',Airindia=' + k3.get() + ',Goair=' + k4.get() + ' where Places = "Hyd to Bng"'
    data_cursor.execute(data3)
    data4 = 'update prices set Indigo=' + l0.get() + ',Vistara=' + l1.get() + ',Spicejet=' + l2.get() + ',Airindia=' + l3.get() + ',Goair=' + l4.get() + ' where Places = "Bng to Che"'
    data_cursor.execute(data4)
    data5 = 'update prices set Indigo=' + m0.get() + ',Vistara=' + m1.get() + ',Spicejet=' + m2.get() + ',Airindia=' + m3.get() + ',Goair=' + m4.get() + ' where Places = "Bng to Del"'
    data_cursor.execute(data5)
    data6 = 'update prices set Indigo=' + n0.get() + ',Vistara=' + n1.get() + ',Spicejet=' + n2.get() + ',Airindia=' + n3.get() + ',Goair=' + n4.get() + ' where Places = "Bng to Hyd"'
    data_cursor.execute(data6)
    data7 = 'update prices set Indigo=' + o0.get() + ',Vistara=' + o1.get() + ',Spicejet=' + o2.get() + ',Airindia=' + o3.get() + ',Goair=' + o4.get() + ' where Places = "Del to Che"'
    data_cursor.execute(data7)
    data8 = 'update prices set Indigo=' + p0.get() + ',Vistara=' + p1.get() + ',Spicejet=' + p2.get() + ',Airindia=' + p3.get() + ',Goair=' + p4.get() + ' where Places = "Del to Bng"'
    data_cursor.execute(data8)
    data9 = 'update prices set Indigo=' + q0.get() + ',Vistara=' + q1.get() + ',Spicejet=' + q2.get() + ',Airindia=' + q3.get() + ',Goair=' + q4.get() + ' where Places = "Del to Hyd"'
    data_cursor.execute(data9)
    data10 = 'update prices set Indigo=' + r0.get() + ',Vistara=' + r1.get() + ',Spicejet=' + r2.get() + ',Airindia=' + r3.get() + ',Goair=' + r4.get() + ' where Places = "Che to Del"'
    data_cursor.execute(data10)
    data11 = 'update prices set Indigo=' + s0.get() + ',Vistara=' + s1.get() + ',Spicejet=' + s2.get() + ',Airindia=' + s3.get() + ',Goair=' + s4.get() + ' where Places = "Che to Bng"'
    data_cursor.execute(data11)
    data12 = 'update prices set Indigo=' + t0.get() + ',Vistara=' + t1.get() + ',Spicejet=' + t2.get() + ',Airindia=' + t3.get() + ',Goair=' + t4.get() + ' where Places = "Che to Hyd"'
    data_cursor.execute(data12)
    price_data.commit()
    popup = Toplevel()
    popup.title("Successful")
    popup.configure(bg="green")
    popup.geometry("250x150")
    popup.resizable(False, False)
    Label(popup, text="Saved \n Sucessfully", font=("Times New Roman", 15, "bold"), bg="green").pack()
    Label(popup, text="Do you want to exit portal").pack(pady=10)
    ping = Frame(popup, bg="green")
    ping.pack()
    Button(ping, text="Yes", width=10, command=lambda: [page_destroy(), popup.destroy()]).grid(row=2, column=0, padx=5)
    Button(ping, text="No", width=10, command=popup.destroy).grid(row=2, column=1, padx=5)


def page_destroy():
    slu.set("")
    slp.set("")
    page.destroy()
    i0.set("")
    i1.set("")
    i2.set("")
    i3.set("")
    i4.set("")
    j0.set("")
    j1.set("")
    j2.set("")
    j3.set("")
    j4.set("")
    k0.set("")
    k1.set("")
    k2.set("")
    k3.set("")
    k4.set("")
    l0.set("")
    l1.set("")
    l2.set("")
    l3.set("")
    l4.set("")
    m0.set("")
    m1.set("")
    m2.set("")
    m3.set("")
    m4.set("")
    n0.set("")
    n1.set("")
    n2.set("")
    n3.set("")
    n4.set("")
    o0.set("")
    o1.set("")
    o2.set("")
    o3.set("")
    o4.set("")
    p0.set("")
    p1.set("")
    p2.set("")
    p3.set("")
    p4.set("")
    q0.set("")
    q1.set("")
    q2.set("")
    q3.set("")
    q4.set("")
    r0.set("")
    r1.set("")
    r2.set("")
    r3.set("")
    r4.set("")
    s0.set("")
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    t0.set("")
    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    main_page()



def change_page():
    global page
    data_cursor.execute("select * from prices")
    prices = data_cursor.fetchall()
    page = Frame(flight, bg="yellow")
    page.pack(side=TOP)
    lb = Label(page, text="Flight Prices Management", font=20)
    lb.pack(pady=20)

    fr = Frame(page, bg="yellow")
    fr.pack()

    Label(fr, text="Places").grid(row=0, column=0, padx=4)
    Label(fr, text="Indigo").grid(row=0, column=1, padx=4)
    Label(fr, text="Vistara").grid(row=0, column=2, padx=4)
    Label(fr, text="Spicejet").grid(row=0, column=3, padx=4)
    Label(fr, text="Airindia").grid(row=0, column=4, padx=4)
    Label(fr, text="Goair").grid(row=0, column=5, padx=4)

    Label(fr, text="Hyderabad To Chennai").grid(row=1, column=0, padx=10, pady=10)
    a1 = Entry(fr, textvariable=i0, width=6)
    a1.grid(row=1, column=1, padx=4)
    a1.insert("end", prices[0][1])
    a2 = Entry(fr, textvariable=i1, width=6)
    a2.grid(row=1, column=2, padx=4)
    a2.insert("end", prices[0][2])
    a3 = Entry(fr, textvariable=i2, width=6)
    a3.grid(row=1, column=3, padx=4)
    a3.insert("end", prices[0][3])
    a4 = Entry(fr, textvariable=i3, width=6)
    a4.grid(row=1, column=4, padx=4)
    a4.insert("end", prices[0][4])
    a5 = Entry(fr, textvariable=i4, width=6)
    a5.grid(row=1, column=5, padx=4)
    a5.insert("end", prices[0][5])

    Label(fr, text="Hyderabad To Delhi").grid(row=2, column=0, padx=10, pady=10)
    b1 = Entry(fr, textvariable=j0, width=6)
    b1.grid(row=2, column=1, padx=4)
    b1.insert("end", prices[1][1])
    b2 = Entry(fr, textvariable=j1, width=6)
    b2.grid(row=2, column=2, padx=4)
    b2.insert("end", prices[1][2])
    b3 = Entry(fr, textvariable=j2, width=6)
    b3.grid(row=2, column=3, padx=4)
    b3.insert("end", prices[1][3])
    b4 = Entry(fr, textvariable=j3, width=6)
    b4.grid(row=2, column=4, padx=4)
    b4.insert("end", prices[1][4])
    b5 = Entry(fr, textvariable=j4, width=6)
    b5.grid(row=2, column=5, padx=4)
    b5.insert("end", prices[1][5])

    Label(fr, text="Hyderabad To Banglore").grid(row=3, column=0, padx=10, pady=10)
    c1 = Entry(fr, textvariable=k0, width=6)
    c1.grid(row=3, column=1, padx=4)
    c1.insert("end", prices[2][1])
    c2 = Entry(fr, textvariable=k1, width=6)
    c2.grid(row=3, column=2, padx=4)
    c2.insert("end", prices[2][2])
    c3 = Entry(fr, textvariable=k2, width=6)
    c3.grid(row=3, column=3, padx=4)
    c3.insert("end", prices[2][3])
    c4 = Entry(fr, textvariable=k3, width=6)
    c4.grid(row=3, column=4, padx=4)
    c4.insert("end", prices[2][4])
    c5 = Entry(fr, textvariable=k4, width=6)
    c5.grid(row=3, column=5, padx=4)
    c5.insert("end", prices[2][5])

    Label(fr, text="Banglore To Chennai").grid(row=4, column=0, padx=10, pady=10)
    d1 = Entry(fr, textvariable=l0, width=6)
    d1.grid(row=4, column=1, padx=4)
    d1.insert("end", prices[3][1])
    d2 = Entry(fr, textvariable=l1, width=6)
    d2.grid(row=4, column=2, padx=4)
    d2.insert("end", prices[3][2])
    d3 = Entry(fr, textvariable=l2, width=6)
    d3.grid(row=4, column=3, padx=4)
    d3.insert("end", prices[3][3])
    d4 = Entry(fr, textvariable=l3, width=6)
    d4.grid(row=4, column=4, padx=4)
    d4.insert("end", prices[3][4])
    d5 = Entry(fr, textvariable=l4, width=6)
    d5.grid(row=4, column=5, padx=4)
    d5.insert("end", prices[3][5])

    Label(fr, text="Banglore To Delhi").grid(row=5, column=0, padx=10, pady=10)
    e1 = Entry(fr, textvariable=m0, width=6)
    e1.grid(row=5, column=1, padx=4)
    e1.insert("end", prices[4][1])
    e2 = Entry(fr, textvariable=m1, width=6)
    e2.grid(row=5, column=2, padx=4)
    e2.insert("end", prices[4][2])
    e3 = Entry(fr, textvariable=m2, width=6)
    e3.grid(row=5, column=3, padx=4)
    e3.insert("end", prices[4][3])
    e4 = Entry(fr, textvariable=m3, width=6)
    e4.grid(row=5, column=4, padx=4)
    e4.insert("end", prices[4][4])
    e5 = Entry(fr, textvariable=m4, width=6)
    e5.grid(row=5, column=5, padx=4)
    e5.insert("end", prices[4][5])

    Label(fr, text="Banglore To Hyderabad").grid(row=6, column=0, padx=10, pady=10)
    f1 = Entry(fr, textvariable=n0, width=6)
    f1.grid(row=6, column=1, padx=4)
    f1.insert("end", prices[5][1])
    f2 = Entry(fr, textvariable=n1, width=6)
    f2.grid(row=6, column=2, padx=4)
    f2.insert("end", prices[5][2])
    f3 = Entry(fr, textvariable=n2, width=6)
    f3.grid(row=6, column=3, padx=4)
    f3.insert("end", prices[5][3])
    f4 = Entry(fr, textvariable=n3, width=6)
    f4.grid(row=6, column=4, padx=4)
    f4.insert("end", prices[5][4])
    f5 = Entry(fr, textvariable=n4, width=6)
    f5.grid(row=6, column=5, padx=4)
    f5.insert("end", prices[5][5])

    Label(fr, text="Delhi To Chennai").grid(row=7, column=0, padx=10, pady=10)
    g1 = Entry(fr, textvariable=o0, width=6)
    g1.grid(row=7, column=1, padx=4)
    g1.insert("end", prices[6][1])
    g2 = Entry(fr, textvariable=o1, width=6)
    g2.grid(row=7, column=2, padx=4)
    g2.insert("end", prices[6][2])
    g3 = Entry(fr, textvariable=o2, width=6)
    g3.grid(row=7, column=3, padx=4)
    g3.insert("end", prices[6][3])
    g4 = Entry(fr, textvariable=o3, width=6)
    g4.grid(row=7, column=4, padx=4)
    g4.insert("end", prices[6][4])
    g5 = Entry(fr, textvariable=o4, width=6)
    g5.grid(row=7, column=5, padx=4)
    g5.insert("end", prices[6][5])

    Label(fr, text="Delhi To Banglore").grid(row=8, column=0, padx=10, pady=10)
    h1 = Entry(fr, textvariable=p0, width=6)
    h1.grid(row=8, column=1, padx=4)
    h1.insert("end", prices[7][1])
    h2 = Entry(fr, textvariable=p1, width=6)
    h2.grid(row=8, column=2, padx=4)
    h2.insert("end", prices[7][2])
    h3 = Entry(fr, textvariable=p2, width=6)
    h3.grid(row=8, column=3, padx=4)
    h3.insert("end", prices[7][3])
    h4 = Entry(fr, textvariable=p3, width=6)
    h4.grid(row=8, column=4, padx=4)
    h4.insert("end", prices[7][4])
    h5 = Entry(fr, textvariable=p4, width=6)
    h5.grid(row=8, column=5, padx=4)
    h5.insert("end", prices[7][5])

    Label(fr, text="Delhi To Hyderabad").grid(row=9, column=0, padx=10, pady=10)
    u1 = Entry(fr, textvariable=q0, width=6)
    u1.grid(row=9, column=1, padx=4)
    u1.insert("end", prices[8][1])
    u2 = Entry(fr, textvariable=q1, width=6)
    u2.grid(row=9, column=2, padx=4)
    u2.insert("end", prices[8][2])
    u3 = Entry(fr, textvariable=q2, width=6)
    u3.grid(row=9, column=3, padx=4)
    u3.insert("end", prices[8][3])
    u4 = Entry(fr, textvariable=q3, width=6)
    u4.grid(row=9, column=4, padx=4)
    u4.insert("end", prices[8][4])
    u5 = Entry(fr, textvariable=q4, width=6)
    u5.grid(row=9, column=5, padx=4)
    u5.insert("end", prices[8][5])

    Label(fr, text="Chennai To Delhi").grid(row=10, column=0, padx=10, pady=10)
    v1 = Entry(fr, textvariable=r0, width=6)
    v1.grid(row=10, column=1, padx=4)
    v1.insert("end", prices[9][1])
    v2 = Entry(fr, textvariable=r1, width=6)
    v2.grid(row=10, column=2, padx=4)
    v2.insert("end", prices[9][2])
    v3 = Entry(fr, textvariable=r2, width=6)
    v3.grid(row=10, column=3, padx=4)
    v3.insert("end", prices[9][3])
    v4 = Entry(fr, textvariable=r3, width=6)
    v4.grid(row=10, column=4, padx=4)
    v4.insert("end", prices[9][4])
    v5 = Entry(fr, textvariable=r4, width=6)
    v5.grid(row=10, column=5, padx=4)
    v5.insert("end", prices[9][5])

    Label(fr, text="Chennai To Banglore").grid(row=11, column=0, padx=10, pady=10)
    w1 = Entry(fr, textvariable=s0, width=6)
    w1.grid(row=11, column=1, padx=4)
    w1.insert("end", prices[10][1])
    w2 = Entry(fr, textvariable=s1, width=6)
    w2.grid(row=11, column=2, padx=4)
    w2.insert("end", prices[10][2])
    w3 = Entry(fr, textvariable=s2, width=6)
    w3.grid(row=11, column=3, padx=4)
    w3.insert("end", prices[10][3])
    w4 = Entry(fr, textvariable=s3, width=6)
    w4.grid(row=11, column=4, padx=4)
    w4.insert("end", prices[10][4])
    w5 = Entry(fr, textvariable=s4, width=6)
    w5.grid(row=11, column=5, padx=4)
    w5.insert("end", prices[10][5])

    Label(fr, text="Chennai To Hyderabad").grid(row=12, column=0, padx=10, pady=10)
    x1 = Entry(fr, textvariable=t0, width=6)
    x1.grid(row=12, column=1, padx=4)
    x1.insert("end", prices[11][1])
    x2 = Entry(fr, textvariable=t1, width=6)
    x2.grid(row=12, column=2, padx=4)
    x2.insert("end", prices[11][2])
    x3 = Entry(fr, textvariable=t2, width=6)
    x3.grid(row=12, column=3, padx=4)
    x3.insert("end", prices[11][3])
    x4 = Entry(fr, textvariable=t3, width=6)
    x4.grid(row=12, column=4, padx=4)
    x4.insert("end", prices[11][4])
    x5 = Entry(fr, textvariable=t4, width=6)
    x5.grid(row=12, column=5, padx=4)
    x5.insert("end", prices[11][5])
    btpa = Frame(page, bg="yellow")
    btpa.pack(pady=10)
    subb = Button(btpa, text="Submit", command=change)
    subb.grid(row=0, column=0, padx=30)
    bckp = Button(btpa, text="Cancel", command=page_destroy)
    bckp.grid(row=0, column=1, padx=30)




slu = StringVar()
slp = StringVar()


def dtdt():
    try:
        pfdt.destroy()
    except:
        pass


def slchk():
    global pfdt
    #create table stafflogin (staffid varchar(20), staffpwd varchar(20))
    #insert into stafflogin values("reyaz", "123")
    mycursor.execute("select * from stafflogin")
    sldta = mycursor.fetchall()
    if slu.get() == "" or slp.get() == "":
        dtdt()
        pfdt = Label(slfr, text="Please fill the details", bg="red")
        pfdt.grid(row=4, columnspan=2, pady=10)
    elif (slu.get(), slp.get()) in sldta:
        slback.destroy()
        slfr.destroy()
        change_page()
    else:
        dtdt()
        pfdt = Label(slfr, text="Please check your credentials", bg="red")
        pfdt.grid(row=4, columnspan=2, pady=10)


def staff_login():
    global slfr, slback
    slback = Button(flight, text='Back', command=lambda: [main_page(), slback.destroy(), slfr.destroy()])
    slback.grid(row=0, column=0)
    slfr = Frame(flight, bg="yellow")
    slfr.grid(row=1, column=0, pady=40)
    l1 = Label(slfr, text="Userid:", font=5)
    l1.grid(row=1, column=0, pady=40)
    e1 = Entry(slfr, textvariable=slu)
    e1.grid(row=1, column=1, padx=10)
    l2 = Label(slfr, text="Password:", font=5)
    l2.grid(row=2, column=0)
    e2 = Entry(slfr, textvariable=slp, show="*")
    e2.grid(row=2, column=1, padx=10)
    bt = Button(slfr, text="Login", command=slchk)
    bt.grid(row=3, columnspan=2, pady=40)

def mp_dest():
    mpwel.destroy()
    mpclk.destroy()
    mpco.destroy()


def main_page():
    global mpwel, mpclk, mpco
    mpwel = Label(flight, text="Welcome To RFB", font=('Arial', 20, 'bold'))
    mpwel.grid(row=0, column=0, pady=10)
    mpclk = Button(flight, text="Book Ticket", font=10, height=2, width=20, command=lambda: [lgarg(), mp_dest()])
    mpclk.grid(row=1, column=0, pady=40)
    mpco = Button(flight, text="Staff Login", font=10, height=2, width=20, command=lambda: [staff_login(), mp_dest()])
    mpco.grid(row=2, column=0, pady=10)


main_page()
flights.protocol("WM_DELETE_WINDOW", ext)
flights.mainloop()
