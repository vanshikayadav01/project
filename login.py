from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk



def register_window():
    window.destroy()
    import register


def signin():
    try:
        if mailentry.get()== '' or passwordentry.get()== '':
            messagebox.showerror("Error","All Fields are required")
        else :
            con=pymysql.connect(host='localhost',user='root',password='12345',database='register')
            cur =con.cursor()
            cur.execute('select* from members where email =%s and password =%s',(mailentry.get(),passwordentry.get()))
            row= cur.fetchone()
            if row ==None:
                messagebox.showerror("Error","Invalid Email or Password")
            else :
                import dictcheck
                window.destroy()    
            con.close()    
    except Exception as e:
        messagebox.showerror("Error","Error doe to {e}")

def resetpass():
    if mailentry.get()=='':
        messagebox.showerror("Error","Please Enter Email id to reset Password")
    else:
        con = pymysql.connect(host='localhost',user='root',password='12345',database='register') 
        cur = con.cursor()
        cur.execute('select * from members where email = %s',mailentry.get())
        row = cur.fetchone()
        if row == None:
            messagebox.showerror('Error',"No Registration with this ID")
        else:
        
            con.close()
            def newpass():
                if securityquestioncombo.get()=='select' or answerentry.get()==''or newpassentry.get()=='':
                    messagebox.showerror("Error","All Fields are Required")
                else:
                    con = pymysql.connect(host='localhost',user='root',password='12345',database='register')  
                    cur = con.cursor()
                    cur.execute('select * from members where email=%s and questions = %s and answer = %s',(mailentry.get(),securityquestioncombo.get(),answerentry.get()))
                    row=cur.fetchone()
                    if row== None:
                        messagebox.showerror("Error","You have given wrong input",parent=root2)
                    else:
                        cur.execute('update members set password=%s where email=%s',(newpassentry.get(),mailentry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","You can login with new Password now",parent=root2)    
                        securityquestioncombo.current(0)
                        answerentry.delete(0,END)
                        newpassentry.delete(0,END)
                        root2.destroy()





            root2 = Toplevel()
            root2.title("Forgot Password")
            root2.geometry('470x500+400+100')
            root2.config(bg='white')
            forgotlabel = Label(root2,text ="Forgot Password",font = ("times new roman",22,'bold'),bg='white',fg='red')
            forgotlabel.place(x=128,y=10)

            securityquestionlabel = Label(root2,text ="security Questions",font =("times new roman",22,'bold'),bg='white',fg='green')
            securityquestionlabel.place(x=128,y=80)

            securityquestioncombo = ttk.Combobox(root2,font =("times new roman",20),state='readonly',values = ("select","Your pet Name","Your Birth Place","Your Best Friend Name","Your Favorite Teacher",
                            "your Hobby"))
            securityquestioncombo.place(x=100,y=125)   
            securityquestioncombo.current(0)             

            answerlabel=Label(root2,text='Answer',font = ("times new roman",22,'bold'),bg='white',fg='green')
            answerlabel.place(x=180,y=175)
            answerentry=Entry(root2,font=('times new roman',20),bg='white')
            answerentry.place(x=100.,y=220)

            newpasslabel=Label(root2,text='New Password',font = ("times new roman",22,'bold'),bg='white',fg='green')
            newpasslabel.place(x=138,y=270)
            newpassentry=Entry(root2,font=('times new roman',20),bg='white')
            newpassentry.place(x=100.,y=315)

            changebutton = Button(root2,text='Change Password',font=('arial',17,'bold'),bg='green',fg='white',cursor='hand2',bd=10,command=newpass)
            changebutton.place(x=130,y=400)
            



            root2.mainloop()     
        
            




window = Tk()


window.geometry('900x600+100+100')
window.title("Login Page")

window.configure(bg='lightblue')


frame =Frame(window,width=560,height =320,bg ='white')
frame.place(x=165,y=140)

maillabel = Label (frame,text ="Email",font = ("arial",22,'bold'),bg= "white",fg = "darkblue")
maillabel.place(x=225,y=35)
mailentry = Entry(frame,font= ("arial",22,),bg= "white",width = 27)
mailentry.place(x=65,y=75)

passwordlabel =Label(frame,text ="Password",font = ("arial",22,'bold'),bg= "white",fg = "darkblue")
passwordlabel.place(x =200,y= 130)
passwordentry = Entry(frame,font= ("arial",22,),bg= "white",width = 27,show = "*")
passwordentry.place(x=65,y=170)

regbutton = Button(frame,text="Register New Account",font = ("arial",12),bd = 0,bg ='white',cursor='hand2',activebackground='white',command = register_window)
regbutton.place(x=75,y=250)

forgetbutton = Button(frame,text="Forgot Password",font = ("arial",12),bd = 0,bg ='white',cursor='hand2',activebackground='white',fg="red",command=resetpass)
forgetbutton.place(x=335,y=250)
loginbutton = Button(window,text="Login",font = ("arial",20),bd = 10,bg ='white',cursor='hand2',activebackground='lightblue',command = signin)
loginbutton.place(x=375,y=475)


window.mainloop()