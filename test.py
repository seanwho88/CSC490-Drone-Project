import tkinter
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("850x510")
app.resizable(False, False)


def projectLabel():
    labelName = tkinter.StringVar(value="CSC490 Drone Project")
    label = customtkinter.CTkLabel(master=app,
                                   textvariable=labelName,
                                   width=250,
                                   height=35,
                                   font=("bold", 20),
                                   fg_color=("white", "grey23"),
                                   corner_radius=8)
    label.pack(padx=20, pady=10)

def commandButton():
    infoButton = customtkinter.CTkButton(master=app,
                                         text="Show available commands",
                                         command=commandButtonEvent)
    infoButton.pack(side=tkinter.BOTTOM, pady=10)

def commandButtonEvent():
    dialog = customtkinter.CTkTextbox(master=app,
                                      width=200,
                                      corner_radius=20)
    dialog.pack(padx=20, pady=10)
    dialog.insert("0.0", "Placeholder\n"
                         "Placeholder\n"
                         "Placeholder\n"
                         "Placeholder\n"
                         "Placeholder\n"
                         "Placeholder\n"
                         "Placeholder\n"
                         "Placeholder\n"
                         "Placeholder\n")
    dialog.configure(state="disabled")


def userInput():
    global entry
    entry = customtkinter.CTkEntry(master=app,
                                   placeholder_text="Enter a command: ")
    entry.pack(padx=20, pady=10)

def enterFunction():
    global testing
    testing = entry.get()
    entry.delete(0, tkinter.END)
    print(testing)


def clearFunction():
    entry.delete(0, tkinter.END)

def entryAndClear():
    entrybutton = customtkinter.CTkButton(master=app,
                                          text="Enter",
                                          command=enterFunction)
    entrybutton.pack(padx=2, pady=5)
    clearbutton = customtkinter.CTkButton(master=app,
                                          text="Clear",
                                          command=clearFunction)
    clearbutton.pack(padx=2, pady=10)


def dronePicture():
    image1 = Image.open("airbuzzone_drone_fp11.jpg")
    img = image1.resize((200, 100), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(img)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.pack(side=tkinter.BOTTOM)


dronePicture()
projectLabel()
userInput()
entryAndClear()
commandButton()

app.mainloop()