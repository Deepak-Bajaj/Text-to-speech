from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("350x300")
root.configure(bg = "blue")
root.title("Application to convert Text to Speech")

label = Label(root, text = "Text to speech Coversion for free", font = "arial 15 bold", bg = "ghost white").pack()
label1 = Label(root, text = "END exit to leave the page", font = "arial 15 bold", width = "20", bg = "ghost white").pack(side = "bottom")

txt = StringVar()
label2 = Label(root, text = "Enter your Sentence", font = "arial 15 bold", bg = "white smoke", width = "15").place(x=30, y=60)

enter_text = Entry(root, textvariable=txt, width = "50")
enter_text.place(x=20, y = 100)

def txt_to_speech():
    msg = enter_text.get()
    speech = gTTS(text = msg, slow = False)
    speech.save('Deepak.mp3')
    playsound('Deepak.mp3',)

def Exit():
    root.destroy()

def Reset():
    txt.set("")

Button(root, text = "PLAY", font = "arial 15 bold", command = txt_to_speech, width = "4").place(x=25, y=140)
Button(root, text = "EXIT", font = "arial 15 bold", width = "4", command = Exit, bg = "orangered1").place(x=100,y=140)
Button(root, text = "RESET", font = "arial 15 bold", command = Reset, width = "6").place(x=175, y=140)

root.mainloop()