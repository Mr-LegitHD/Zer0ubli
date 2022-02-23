from tkinter import *
import sys
import json
import os

root = Tk()
root.title("Zer0ubli Interface")
root.resizable(0, 0)


#NameInputField
NameInputField = Entry(root, width=28)
NameInputField.grid(row=1, column=0)
NameInputField.insert(0, "")

#Create Textbox
T = Text(root, height = 5, width = 35)
T.grid(row=100, column=1)

f = NameInputField.get()
#button funktion
def ClickMonday():
    T.delete(1.0, END)
    r = open(str(NameInputField.get().lower() + ".montag.json"))
    daten = json.load(r)
    Content = (str(str("     Schulstunden am Montag:"+ "\nFächer:" + str(daten["lessions"]).title()+"\nBücher: "+str(daten["books"]))).replace("'"," ").replace( "[", "").replace("]", ""))
    T.insert(1.0,Content)

def ClickTuesday():
    T.delete(1.0, END)
    r = open(str(NameInputField.get().lower() + ".dienstag.json"))
    daten = json.load(r)
    Content = (str(str("     Schulstunden am Dienstag:" + "\nFächer:" + str(daten["lessions"]).title() + "\nBücher: " + str(daten["books"]))).replace("'", " ").replace("[", "").replace("]", ""))
    T.insert(1.0,Content)

def ClickWednesday():
    T.delete(1.0, END)
    r = open(str(NameInputField.get().lower() + ".mittwoch.json"))
    daten = json.load(r)
    Content = (str(str("     Schulstunden am Mittwoch:"+ "\nFächer:" + str(daten["lessions"]).title()+"\nBücher: "+str(daten["books"]))).replace("'"," ").replace( "[", "").replace("]", ""))
    T.insert(1.0,Content)

def ClickThursday():
    T.delete(1.0, END)
    r = open(str(NameInputField.get().lower() + ".donnerstag.json"))
    daten = json.load(r)
    Content = (str(str("     Schulstunden am Donnerstag:" + "\nFächer:" + str(daten["lessions"]).title() + "\nBücher: " + str(daten["books"]))).replace("'", " ").replace("[", "").replace("]", ""))
    T.insert(1.0,Content)

def ClickFriday():
    T.delete(1.0, END)
    r = open(str(NameInputField.get().lower() + ".freitag.json"))
    daten = json.load(r)
    Content = (str(str("     Schulstunden am Freitag:" + "\nFächer:" + str(daten["lessions"]).title() + "\nBücher: " + str(daten["books"]))).replace("'", " ").replace("[", "").replace("]", ""))
    T.insert(1.0,Content)

def ClickSaturday():
    T.delete(1.0, END)
    r = open(str(NameInputField.get().lower() + ".samstag.json"))
    daten = json.load(r)
    Content = (str(str("     Schulstunden am Samstag:"+ "\nFächer:" + str(daten["lessions"]).title()+"\nBücher: "+str(daten["books"]))).replace("'"," ").replace( "[", "").replace("]", ""))
    T.insert(1.0,Content)

def ClickExit():
    ExitLabel = Label(root, text="Exit")
    ExitLabel.grid()
    sys.exit()

def ClickSettings():
    Settingslabel = Label(root, text=" ")
    Settingslabel.grid()
    #os.system('setup.py')
    exec(open("setup.py").read())

#Buttons creation
MondayButton = Button(root, text="Montag", padx=71, pady=20, command=ClickMonday, fg="#000000", bg="#65B1B2")
MondayButton.grid(row=2, column=0)

TuesdayButton = Button(root, text="Dienstag", padx=80, pady=20, command=ClickTuesday, fg="#000000", bg="#65B1B2")
TuesdayButton.grid(row=2, column=1)

WednesdayButton = Button(root, text="Mittwoch", padx=54, pady=10, command=ClickWednesday, fg="#000000", bg="#65B1B2")
WednesdayButton.grid(row=2, column=2)

ThursdayButton = Button(root, text="Donnerstag", padx=71, pady=20, command=ClickThursday, fg="#000000", bg="#65B1B2")
ThursdayButton.grid(row=3, column=0)

FridayButton = Button(root, text="Freitag", padx=85, pady=20, command=ClickFriday, fg="#000000", bg="#65B1B2")
FridayButton.grid(row=3, column=1)

SaturdayButton = Button(root, text="Samstag", padx=57, pady=20, command=ClickSaturday, fg="#000000", bg="#65B1B2")
SaturdayButton.grid(row=3, column=2)

ExitButton = Button(root, text="Exit", padx=80, pady=20, command=ClickExit)
ExitButton.grid(row=4, column=0)

SettingsButton = Button(root, text="Einstellungen", padx=44, pady=20, command=ClickSettings)
SettingsButton.grid(row=4, column=2)
EnteryournameLabel = Label(root, text="Enter your name", padx=10, pady=10)
EnteryournameLabel.grid(row=0, column=0)

#Enter name Label

#Bücher Label
Bücherlabel = Label(root, text="Bücher:", padx=10, pady=10)
Bücherlabel.grid(row=4, column=1)


#root.iconbitmap('hnet.com-image.ico')
root.mainloop()