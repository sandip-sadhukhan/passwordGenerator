import tkinter as tk
import random
#Default Vars
HEIGHT = 400
WIDTH = 420
root = tk.Tk()
root.title("Password Generator")
#define generatePassword function
def generatePassword():
    length=passwordLength.get()
    passwordList = ['a','b','c','d','e','f','5','6','7','g','h','i','j','k','l','m','n','o','p','q','W','X','r','s','t','1','2','3','M','#','$','%','N','O','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','8','9','P','Q','R','S','T','U','V','Y','Z','4','!','@',]
    newPassword = ""
    for i in range(length):
        randomIndex = random.randint(0,len(passwordList)-1)
        newPassword+=passwordList[randomIndex]
    entryBar.set(newPassword)

def savePassword():
    mainPassword = str(entryBar.get())
    if mainPassword=='':
        return
    with open('passwords.txt','a') as fh:
        fh.write(mainPassword+'\n')
#Your code is here
canvas = tk.Canvas(root, height = HEIGHT,width=WIDTH)
canvas.pack()

frame = tk.Frame(root,bg="tomato",bd=5)
frame.place(relwidth=.8,relheight=.8,relx=.1,rely=.1)

generateButton = tk.Button(frame,text="Generate",bg="teal",fg="white",command=generatePassword)
generateButton.place(relx=.12,rely=.48,relwidth=.3,relheight=.1)

saveButton = tk.Button(frame,text="Save",bg="orange",fg="black",command=savePassword)
saveButton.place(relx=.5,rely=.48,relwidth=.3,relheight=.1)

Heading = tk.Label(frame,text="Password Generator",fg="#fff",bg="blueviolet")
Heading.place(relx=.3,rely=.02,relwidth=.45,relheight=.1)

entryBar=tk.StringVar()
entry = tk.Label(frame,textvariable=entryBar,font=25,bd=12)
entry.place(relx=.1,rely=.32,relwidth=.8,relheight=.1)


lengthText=tk.Label(frame,text="Password Length : ",bg="tomato",fg="#fff",font=55)
lengthText.place(relx=.09,rely=.2)
passwordLength=tk.IntVar()
passwordLenghtDropdown=tk.OptionMenu(frame,passwordLength,8,9,10,11,12,13,14,15,16,17,18,19,20)
passwordLenghtDropdown.place(relx=.6,rely=.19)
passwordLength.set(12)
generatePassword()

#copyright
copyrightText = tk.Label(frame,text="Developed By Sandip Sadhukhan.",fg="white",font = 60,bg="tomato")
copyrightText.place(relx=.1,rely=.7)

root.mainloop()
