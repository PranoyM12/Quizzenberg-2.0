import os
import tkinter
import pygame
import random
from tkinter import *
import cv2
import win32com.client as win32
import mysql.connector
pygame.mixer.init()
score = 0

mydb = mysql.connector.connect(host= "localhost", user = "root",password=os.getenv("DB_PASS"), database = 'india')

cur = mydb.cursor()
cur.execute('Select * from questions')
result = cur.fetchall()
#print(result)


xyz = mydb.cursor()
xyz.execute('Select * from options')
total = xyz.fetchall()
#print(total)


list_names = []

answers = [2,1,3,1,0,3,2,1,0,1]

user_answer = []

indexes = []

def win():
    pygame.mixer.music.load("winner.mp3")
    pygame.mixer.music.play(loops = 0)

def good():
    pygame.mixer.music.load("good.mp3")
    pygame.mixer.music.play(loops = 0)

def lose():
    pygame.mixer.music.load("lost.mp3")
    pygame.mixer.music.play(loops = 0)

def start_music():
    pygame.mixer.music.load("correct(1).wav")
    pygame.mixer.music.play(loops = 0)

def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue 
        else:
            indexes.append(x)
   # print(indexes)


def certify():
    global score
    scr = str(score)
    for index, name in enumerate(list_names):
        template = cv2.imread('Certificate of Excellence.png')
        #template = cv2.imread(r'C:\Users\prano\OneDrive\Desktop\NEIL\Quizzenberg Project file\Certificate of Excellence.png')
        cv2.putText(template, name, (814,1189), cv2.FONT_HERSHEY_TRIPLEX, 2, (51, 65, 102), 2, cv2.LINE_AA)
        cv2.putText(template, scr, (631,1245), cv2.FONT_HERSHEY_TRIPLEX, 2, (51, 65, 102), 2, cv2.LINE_AA)
        #cv2.imwrite(f'C:\\Users\\prano\\OneDrive\\Desktop\\Quizzenberg Project file\\Generated certificates\\{name}.png', template)
        cv2.imwrite(f'C:\\Users\\prano\\OneDrive\\Desktop\\NEIL\\Quizzenberg Project file\\Generated certificates\\{name}.png',template)
        print('Processing Certificate...')
        print('Certificate sent to entered email successfully')

        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')
        mail_item = olApp.CreateItem(0)
        mail_item.Subject = "Certificate of Excellence"

        mail_item.Body = f"Hi {name}, thankyou for playing the game.\nHere is you certificate of excellence with your score in it."
        mail_item.To = email1

        image_path = f"C:\\Users\\prano\\OneDrive\\Desktop\\NEIL\\Quizzenberg Project file\\Generated certificates\\{name}.png"

        mail_item.Attachments.Add(image_path)

        mail_item.Display()
        mail_item.save()
        mail_item.Send()


def submitispressed():
    global list_names
    global email1
    name1 = name_var.get()
    email1 = email_var.get()
    list_names.append(name1)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ddedc8",
        border = 0
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",22),
        background="#ddedc8",
    )
    labelresulttext.pack()

    labelscore = Label(
        root,
        font=("Consolas", 22),
        background="#ddedc8",
    )
    labelscore.pack()

    if score >= 20:
        win()
        img = PhotoImage(file="great.png")
        labelimage.config(image=img)
        labelimage.image = img
        labelimage.pack(pady=(50, 30))
        labelresulttext.config(text="You Are Excellent!")
        labelscore.config(text=f"Your score is: {score}")
    elif (score >= 10 and score < 20):
        good()
        img = PhotoImage(file="ok.png")
        labelimage.config(image=img)
        labelimage.image = img
        labelimage.pack(pady=(10, 10))
        labelresulttext.config(text="You Can Be Better!")
        labelresulttext.pack()
        labelscore.config(text=f"Your score is: {score}")
    else:
        lose()
        img = PhotoImage(file="bad.png")
        labelimage.config(image=img)
        labelimage.image = img
        labelimage.pack(pady=(15, 50))
        labelresulttext.config(text="You Should Work Hard!")
        labelscore.config(text=f"Your score is: {score}")

    lblcertify = Label(
        root,
        text = "To get your certificate enter the following:",
        font = ("Bell MT", 18, "bold"),
        background="#ddedc8",
    )
    lblcertify.place(relx=0.185, rely=0.64)

    lblname = Label(
        root,
        text="Enter Your Name:",
        font=("Comic sans MS", 16, "bold"),
        background="#ddedc8",
    )
    lblname.place(relx=0.17, rely=0.7)
    name_window = Entry(
        root,
        width=20,
        background="#ddedc8",
        textvariable=name_var,
        foreground="#000000",
        font=("Arial Rounded MT", 15, "bold"),
        borderwidth=5
    )
    name_window.place(relx=0.5, rely=0.7)

    lblemail = Label(
        root,
        text="Enter Your Email:",
        font=("Comic sans MS", 16, "bold"),
        background="#ddedc8",
    )
    lblemail.place(relx=0.17, rely=0.8)

    email_window = Entry(
        root,
        width=20,
        background="#ddedc8",
        foreground="#000000",
        textvariable=email_var,
        font=("Arial Rounded MT", 15, "bold"),
        borderwidth=5
    )
    email_window.place(relx=0.5, rely=0.8)

    btnSubmit = Button(
        root,
        text="SUBMIT",
        font=("Cambria", 20, "bold"),
        anchor="center",
        background='#ff9700',
        command=lambda: [submitispressed(), certify(), root.quit()],
    )
    btnSubmit.pack(pady=(10, 40))
    btnSubmit.pack(side=BOTTOM)


def calc():
    global indexes,user_answer,answers, score
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score += 5
        x += 1


    #print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=result[indexes[ques]])
        r1['text'] = total[indexes[ques]][0]
        r2['text'] = total[indexes[ques]][1]
        r3['text'] = total[indexes[ques]][2]
        r4['text'] = total[indexes[ques]][3]
        ques += 1
    else:
        calc()


def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text=result[indexes[0]],
        font = ("Consolas",26),
        width = 500,
        justify = "center",
        wraplength = 600,
        background = "#ddedc8",
    )
    lblQuestion.pack(pady=(110,40))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=total[indexes[0]][0],
        font = ("Times", 20),
        value = 0,
        variable = radiovar,
        command = selected,
        background="#ddedc8",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=total[indexes[0]][1],
        font = ("Times", 20),
        value = 1,
        variable = radiovar,
        command = selected,
        background="#ddedc8",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=total[indexes[0]][2],
        font = ("Times", 20),
        value = 2,
        variable = radiovar,
        command = selected,
        background="#ddedc8",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=total[indexes[0]][3],
        font = ("Times", 20),
        value = 3,
        variable = radiovar,
        command = selected,
        background="#ddedc8",
    )
    r4.pack(pady=5)

def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblinstructions.destroy()
    lblrules.destroy()
    btnStart.destroy()
    lbltag.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("Quizzenberg")
root.geometry("750x700")
root.config(background='#ddedc8')
#root.resizable(0,0)

name_var = tkinter.StringVar()
email_var = tkinter.StringVar()

img1 = PhotoImage(file="QUIZ(2).png")

labelimage = Label(
    root,
    image = img1,
    background = "#ddedc8"
)

labelimage.pack(pady=(20,20))

labeltext = Label(
    root,
    text = "Quizzenberg",
    font = ("Algerian",26, "bold"),
    background = "#ddedc8",
)
labeltext.place(relx = 0.5, rely = 0.5, anchor = CENTER)

lbltag = Label(
    root,
    text = "You are a click away from fun learning experince !",
    font = ("Comic sans MS", 18),
    background = "#ddedc8",
    foreground= "#434838",
)
lbltag.place(relx = 0.5, rely = 0.57, anchor = CENTER)

img2 = PhotoImage(file="Start.png")
btnStart = Button(
        root,
        image=img2,
        border=0,
        background="#ddedc8",
        command=lambda: [startIspressed(), start_music()],
)
btnStart.place(relx = 0.5, rely = 0.7, anchor = CENTER)

lblinstructions = Label(
        root,
        text = "Read The  Rules And\nClick Start Once You Are Ready",
        background = "#ddedc8",
        foreground= "#434838",
        font = ("Consolas" ,14,"bold"),
        justify = "center",
)
lblinstructions.place(relx = 0.5, rely = 0.84, anchor = CENTER)

lblrules = Label(
        root,
        text = "This quiz contains 10 questions\nOnce you a select a radio button that will be a final choice\nHence think before you select!",
        width = "100",
        font = ("Times",18,"bold"),
        background = "#ff9700",
        foreground = "#000000",
)
lblrules.place(relx = 0.5, rely = 0.94, anchor = CENTER)


root.mainloop()