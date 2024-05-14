from tkinter import *
from datetime import date
import time
root=Tk()
def send():
    send="You:"+a.get()
    text.insert('end',"\n"+send)
    if(a.get().lower()=='hi'):
        text.insert('end','\n'+"Robot:hello")
    elif(a.get().lower()=='hey'):
        text.insert('end','\n'+"Robot:How may I help you?")
    elif(a.get().lower()=='how are you?'):
        text.insert('end','\n'+"Robot:I am Fine.How are you?")
    elif(a.get().lower()=='I am fine'):
        text.insert('end','\n'+"Robot:Nice to hear that")
    elif(a.get().lower()=='how is your day?'):
        text.insert('end','\n'+"Robot:Good")
    elif(a.get().lower()=='how can you help me?'):
        text.insert('end','\n'+"Robot:What help you need")
    elif(a.get().lower()=='what is your name?'):
        text.insert('end','\n'+"Robot:My name is Ana De Armas")
    elif(a.get().lower()=='are you a human?'):
        text.insert('end','\n'+"Robot:No, I am a Robot")
    elif(a.get().lower()=='what is todays date'):
        text.insert('end','\n'+"Robot:"+str(date.today()))
    elif(a.get().lower()=='what is the time now'):
        text.insert('end','\n'+"Robot:"+str(time.strftime("%I:%m:%S:%p")))
    else:
        text.insert('end','\n'+"Robot:I didn't get you")
root.title("Ana De Armas_GPT")
text=Text(bg="cyan")
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
send=Button(root,bg='blue',text="send",width=20,command=send)
send.grid(row=1,column=1)
a.grid(row=1,column=0)
root.mainloop()