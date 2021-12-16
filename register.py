from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql


def login_window():
        root.destroy()
        import login


def clear():
        entryfirstname.delete(0,END)
        entrylastname.delete(0,END)
        emailname.delete(0,END)
        contactname.delete(0,END)
        comboquestion.current(0)
        passwordname.delete(0,END)
        confirmname.delete(0,END)
        answername.delete(0,END)
        check.set(0)
        tick.set(0)


def register():
        if entryfirstname.get() == '' or entrylastname.get() == '' or emailname.get() == '' \
                or contactname.get() == '' or passwordname.get ()== '' or confirmname.get() == ''\
                         or comboquestion.get() == 'select' or answername.get()== '':
                         messagebox.showerror('Error',"All Fields are Required")
        elif passwordname.get() != confirmname.get():
                messagebox.showerror("Error","Password Mismatch")
        elif check.get()== 0:
                messagebox.showerror("Error","Please agree all terms and conditions")    
        elif tick.get()== 0:
                messagebox.showerror("Error","Please make sure you are above 18")    
        else :
                try:
                                con = pymysql.connect(host = 'localhost', user = 'root', password = '12345',database='register')
                                cur = con.cursor()
                                cur.execute("select * from members where email = %s",emailname.get())
                                row = cur.fetchone()
                                if row != None:
                                        messagebox.showerror("Error","User Already Exist")
                                else :
                                        cur.execute('insert into members(f_name,l_name,contact,email,questions,answer,password) values(%s,%s,%s,%s,%s,%s,%s)',
                                        (entryfirstname.get(),entrylastname.get(),contactname.get(),emailname.get(),comboquestion.get(),answername.get(),passwordname.get())) 
                                        con.commit()
                                        con.close()

                                        messagebox.showinfo("Success","Registered Successfully") 
                                        clear() 
                except Exception as e:
                        messagebox.showerror("Error",f"Error due to{e}")

        

root = Tk()

root.geometry('1200x700')
root.title("Registration Form")
root.configure(bg='pink')
title = Label(root,text = 'Registration',font=('Allura','25','bold'),fg ='pink',bg = 'grey')
title.place(x=500,y=0)

registerFrame = Frame(root, width = 700, height = 600)
registerFrame.place(x=100,y=50)

firstnamelabel = Label(registerFrame, text = "First Name", font=('times new roman',18,'bold'))
firstnamelabel.place(x=20,y=40)
entryfirstname = Entry(registerFrame,font = ('times new roman',18),bg = "Lightgray")
entryfirstname.place(x=20,y=80)

lastnamelabel = Label(registerFrame, text = "Last Name", font=('times new roman',18,'bold'))
lastnamelabel.place(x=400,y=40)
entrylastname = Entry(registerFrame,font = ('times new roman',18),bg = "Lightgray")
entrylastname.place(x=400,y=80)

contactlabel = Label(registerFrame, text = "Contact", font=('times new roman',18,'bold'))
contactlabel.place(x=20,y=150)
contactname = Entry(registerFrame,font = ('times new roman',18),bg = "Lightgray")
contactname.place(x=20,y=190)

emaillabel = Label(registerFrame, text = "email ID", font=('times new roman',18,'bold'))
emaillabel.place(x=400,y=150)
emailname = Entry(registerFrame,font = ('times new roman',18),bg = "Lightgray")
emailname.place(x=400,y=190)

securitylabel = Label(registerFrame, text = "Security Question", font=('times new roman',18,'bold'))
securitylabel.place(x=20,y=260)
comboquestion = Combobox(registerFrame,font=('times new roman', 16),state="readonly",values = ("select","Your pet Name","Your Birth Place","Your Best Friend Name","Your Favorite Teacher",
        "your Hobby"))
comboquestion.place(x=20,y=300)
comboquestion.current(0) 

answerlabel = Label(registerFrame, text = "Answer", font=('times new roman',18,'bold'))
answerlabel.place(x=400,y=260)
answername = Entry(registerFrame,font = ('times new roman',18),bg = "Lightgray")
answername.place(x=400,y=300)

passwordlabel = Label(registerFrame, text = "Password", font=('times new roman',18,'bold'))
passwordlabel.place(x=20,y=370)
passwordname = Entry(registerFrame,show = "*",font = ('times new roman',18),bg = "Lightgray")
passwordname.place(x=20,y=410)

confirmlabel = Label(registerFrame, text = "Confirm Password", font=('times new roman',18,'bold'))
confirmlabel.place(x=400,y=370)
confirmname = Entry(registerFrame,show = "*",font = ('times new roman',18),bg = "Lightgray")
confirmname.place(x=400,y=410)

check = IntVar()

checkbutton = Checkbutton(registerFrame,text="I agree all terms and Conditions",onvalue=1,offvalue=0,font = ("times new roman",14,"bold"),variable = check)
checkbutton.place(x=200,y=480)

tick = IntVar()

checkbutton = Checkbutton(registerFrame,text="I am above 18",onvalue=1,offvalue=0,font = ("times new roman",14,"bold"),variable=tick)
checkbutton.place(x=200,y=520)

registerbutton = Button(root,text = "REGISTER" ,font = ('times new roman',18,'bold'),bd = 18, bg = 'darkgray',activebackground='lightgray',width=15,command = register)
registerbutton.place(x=875,y=180)

loginbutton = Button(root,text = "LOGIN" ,font = ('times new roman',18,'bold'),bd = 18, bg = 'darkgray',activebackground='lightgray',width=15,command = login_window)
loginbutton.place(x=875,y=350)


root.mainloop()