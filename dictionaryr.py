from tkinter import *
from tkinter import messagebox
import pyttsx3

from PyDictionary import PyDictionary

engine = pyttsx3.init()

def clear():
    entry.config(state = NORMAL)
    entry.delete(0,END)
    textarea.delete(1.0, END)
    textarea.config(state = DISABLED)

def exit():
    res = messagebox.askyesno('Confirm','Do you want to EXIT ?')
    if res == True:
        root.destroy()
    else:
        pass   

def  wordtoaudio():
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.setProperty('rate',170)
    engine.say(entry.get())
    engine.runAndWait()

def  texttoaudio():
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
    engine.setProperty('rate',175)
    engine.say(textarea.get(1.0, END))
    engine.runAndWait()   


def search():
    try:
        word = entry.get()
        word = word.lower()
        dictionary = PyDictionary()
        mean = dictionary.meaning(word)
        textarea.insert(END,mean)
    except:
        messagebox.showerror("ERROR","invalid word")    
        

    
    



root = Tk()
root.geometry('800x800+100+50')
root.title("Dictionary")
root.configure(bg ='grey')
title = Label(root,text = 'Dictionary',font=('Allura','50','bold'),fg ='pink',bg = 'grey')
title.place(x=225,y=0)

EnterWord = Label(root,text = 'Enter Word',font=('castellar','30','bold'),fg ='pink',bg = 'grey')
EnterWord.place(x=225,y=90)

entry = Entry(root, font =('castellar','30','bold'),bd = 8, bg ='Whitesmoke',justify=CENTER, relief=GROOVE)
entry.place(x=100,y=160)

entry.focus_set()

searchbutton = Button(root,text = "SEARCH" ,bd=10, bg = 'yellow',activebackground='Whitesmoke', command=search)
searchbutton.place(x=200,y=250)

speakbutton = Button(root,text = "LISTEN" ,bd=10, bg = 'yellow',activebackground='Whitesmoke',command= wordtoaudio)
speakbutton.place(x=500,y=250)

meaning = Label(root,text = 'Meaning',font=('Castellar','25','bold'),fg ='pink',bg = 'grey')
meaning.place(x=285,y=300)

textarea = Text(root, font =('Castellar','18','bold'), width = 34, height = 10, bd = 5, relief=GROOVE, wrap = 'word')
textarea.place(x=100,y=350)

audiobutton = Button(root,text = "AUDIO" ,bd=10, bg = 'yellow',activebackground='Whitesmoke', command= texttoaudio)
audiobutton.place(x=250,y=675)

clearbutton = Button(root,text = "CLEAR" ,bd=10, bg = 'yellow',activebackground='Whitesmoke',command= clear)
clearbutton.place(x=350,y=675)

exitbutton = Button(root,text = "LEAVE" ,bd=10, bg = 'yellow',activebackground='Whitesmoke', command= exit)
exitbutton.place(x=450,y=675)


root.mainloop()
