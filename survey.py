import tkinter
from tkinter import *
#import Question
import time
#import Image
import random
#create the questions


#bcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

#ssssssssssssssssssssssssssssssssss'

question_prompts = [
    "1.	What is your position within the company?",
    "2.	Does your company have a security team?",
    "3.	Do you know who to contact in case you are hacked or if your computer is infected? ",
    "4.	Have you ever found  a virus or Trojan on your computer at work?",
    "5.	Do you know how to tell if your computer is hacked or infected? ",
    "6.	Have you ever given your password from work to someone else? ",
    "7.	If you format a hard drive or erase the files on it all the information on it is permanently lost.",
    "8.	How secure do you feel your computer is? ",
    "9.	Is the firewall on your computer enabled? ",
    "10. Is your computer configured to be automatically updated? ",
    "11. How careful are you when you open an attachment in email? ",
    "12. Do you know what a phishing attack is? ",
    "13. Do you know what an email scam is and how to identify one? ",
    "14. Is anti-virus currently installed, updated and enabled on your computer?",
    "15. My computer has no value to hackers, they do not target me.",
    "16. Does your company have policies on which websites you can visit?   ",
    "17. Does your company have policies on which websites you can visit?   ",
    "18. Is instant messaging allowed in our organization? ",
    "19. Can you use your own personal devices, such as your mobile phone, to store or transfer confidential company"
    " information? ",
    "20. Have you downloaded and installed software on your computer at work?",
    "21. Has your boss or anyone else you know at work asked you for your password? ",
    "22. Do you use the same passwords for your work accounts as you do for your personal accounts "
    "at home, such as Facebook, Twitter or your personal email accounts? ",
    "23. How often do you take information from the office and use your computer at home to work on it?",
    "24. Have you logged into work accounts using public computers, such as from a library, "
    "cyber café or hotel lobby? ",
    "25. If you delete a file from your computer or USB stick, that information can no longer be recovered. ",
]





#create the multiple choices
answers_choice = [
    ["a. Full/Part time employee ","b. Contractor/Vendor ","c. Other "],
    ["a. Yes, we have a company security team. ","b. No, we do not have a company security team. ","c. I do not know."],
    ["a. Yes, I know who to contact. ","b. No, I do not know who to contact. ", "c. I am not sure "],
    ["a. Yes, my computers has been infected before","b. No, my computer has never been infected. ",
     "c. I do not know what a virus or Trojan is. "],
    ["a. Yes, I know what to look for to see if my computer is hacked or infected. ",
     "b. No, I do not know what to look for to see if my computer is hacked or infected. ", "c. I am not sure"],
    ["a. Yes ","b. No "," c. Not sure"],
    ["a. True ","b. False ", "c. Dont Know"],
    ["a. Very secure ","b. Secure ","c. Not secure "],
    ["a. Yes, it is enabled. ", "b. No, it is not enabled. ","c. I do not know what a firewall is. "],
    ["a. Yes, it is. ","b. No, it is not. ","c. I do not know. "],
    ["a. I always make sure it is from a person I know and I am expecting the email. ",
     "b. As long as I know the person or company that sent me the attachment I open it. ",
     "c. There is nothing wrong with opening attachments. "],
    ["a. Yes, I do. ","b. No, I do not. ","c. Not sure"],
    ["a. Yes I do. ","b. No, I do not. ","c. Not sure."],
    ["a. Yes it is. ","b. No it is not. ","c. I do not know how to tell / I do not know what anti-virus is. "],
    ["a. True ","b. False","c. I cant say."],
    ["a. No, there are no policies, I can visit whatever websites I want while at work",
     "b. Yes, there are policies limiting what websites I can and cannot visit while at work, but I do not "
     "know the policies.", "c. Yes, there are policies and I know and understand them. "],
    ["a. No, there are no policies, I can send whatever emails I want to whomever I want while at work. ",
     "b. Yes, there are policies limiting what emails I can and cannot send while at work, "
     "but I do not know the policies. ","c.	Yes, there are policies and I know and understand them. "],
    ["a. Yes, instant messaging is allowed in our organization. ","b. No, instant messaging "
     "is not allowed in our organization. ","c.	I do not know. "],
    ["a. Yes I can","b. No I cannot. ","c. I do not know"],
    ["a. Yes I have. ","b. No I have not. ","c. Not sure"],
    ["a. Yes, they have ","b. No, they have not. ","c. I can not remember"],
    ["a. Yes I do. ", "b. No I do not. ", "c. Not sure"],
    ["a. Almost every day. ", "b. At least once a week/ monthly ", "c. Never"],
    ["a. Yes, I have ", "b. No, I have not ", "c. I can not remember"],
    ["a. True ", "b. False", "c. I do not know"],

]

answers = [1,0,0,1,0,0,1,1,0,2,0,1,2,1,2,1,2,2,1,1,1,1,0,1,1]

user_answer = []

indexes = []

gee = []



def gen():
    global indexes
    for i in range(25):
        indexes.append(i) 


def showresult(score):
    labelQ2.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    labelimage2 = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage2.pack()

    labelresulttext = Label(
        root,
        font = ("Comic sans",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="start.png")
        labelimage2.configure(image=img)
        labelimage2.image = img
        labelresulttext.configure(text="You have a high level of Cyber user security awareness!!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="next.png")
        labelimage2.configure(image=img)
        labelimage2.image = img
        labelresulttext.configure(text="You Can Be Better with a Cyber user security awareness revision!!")
    else:
        img = Photoimage(file="next.png")
        labelimage2.configure(image=img)
        labelimage2.image = img
        labelresulttext.configure(text="You Can Be Better with a Cyber user security awareness training!!")

def calc():
#   global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)



def selectedbtn():

    global radiovar,user_answer
    global labelQ2,r1,r2,r3
    x = radiovar.get()
    user_answer.append(x)
    print(user_answer)
    # time.sleep(1)
    d = 1


    if len(gee) == 0:
        gee.append(d)
        labelQ2.config(text=question_prompts[gee[0]])
        r1['text'] = answers_choice[gee[0]][0]
        r2['text'] = answers_choice[gee[0]][1]
        r3['text'] = answers_choice[gee[0]][2]
    else:
        if gee[0] == 24:
            print(indexes)
            print(user_answer)
            calc()

        else:
            y = gee[0] + 1
            gee[0] = y
            labelQ2.config(text=question_prompts[gee[0]])
            r1['text'] = answers_choice[gee[0]][0]
            r2['text'] = answers_choice[gee[0]][1]
            r3['text'] = answers_choice[gee[0]][2]

        


# countquest = 0
#<!---- show first question and move to next question ---->
def Questionshow():
    global labelQ2,r1,r2,r3
    labelQ2 = Label(
           root,
           text=(question_prompts[0]),
           font=("Comic sans MS", 24, "bold"),
           background="#ffffff",
           width=500,
           justify="center",
           wraplength=1000,
    )
    labelQ2.pack()

#create the option buttons
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(
        root,
        text= answers_choice[0][0],
        font = ("Comic sans MS", 20, "bold"),
        value = 0,
        variable = radiovar,
    )
    r1.pack()


    r2 = Radiobutton(
        root,
        text=answers_choice[0][1],
        font=("Comic sans MS", 20, "bold"),
        value=1,
        variable=radiovar,
        background="#ffffff",
    )
    r2.pack()


    r3 = Radiobutton(
        root,
        text=answers_choice[0][2],
        font=("Comic sans MS", 20, "bold"),
        value=2,
        variable=radiovar,
        background="#ffffff",

    )
    r3.pack()


    img4 = PhotoImage(file='nextt.png')
    btnnext = Button(
        image=img4,
        relief=FLAT,
        border=0,
        #command=Sleepsome,
        command=selectedbtn,
    )
    btnnext.pack()
    create_image(image=img4)
#<!----- end of optionbuttons----->

#<!----- move to first question ----->
def StartIspressed():
    labeltext.destroy()
    btnStart.destroy()
    labelimage1.destroy()
    gen()
    Questionshow()


   






#<----- Program start here ----->
root = tkinter.Tk()
root.title("Cyber User Awareness Test")
root.geometry("1500x800")
root.config(background="#ffffff")
# root.iconbitmap('c:/New Folder/halo_shield.ico')
root.resizable(0,0)
labeltext = Label(
      root,
      text = "Welcome!, Thank you for offering to participate in this test. Click start to begin.",
      font = ("Comic sans MS", 24, "bold"),
      background = "#ffffff",
)

labeltext.pack(pady=(0,50))


img2 = PhotoImage(file='user_awareness1.png')
labelimage1 = Label(
    root,
    image = img2,
    background = "#ffffff",
)
labelimage1.pack(pady=(40,0))


img1 = PhotoImage(file='start.png')
btnStart = Button(
    root,
    image = img1,
    relief = FLAT,
    border = 0,
    command = StartIspressed,

)
btnStart.pack()
















root.mainloop()
