from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import font
import random
from paras import paragraphs


# highlightFont = font.Font(family='Roboto Mono', name='appHighlightFont', size=12, weight='bold')
# Cascadia Code Semibold = font.Font(family="Bitstream Vera Sans Mono", size=9)

root =Tk()

def change_paragraph():
    new_paragraph = random.choice(paragraphs)
    text_area.config(text=new_paragraph)

def create_window():
    global root  # To access the main window
    if window_exists.get():
        # If the new window exists, destroy it and show the main window
        window.destroy()
        window_exists.set(False)
        root.deiconify()
    else:
        # If the new window doesn't exist, hide the main window and create the new window
        root.withdraw()
        window_exists.set(True)
        create_window_instance()

def create_window_instance():
    global window  # To access the new window
    window = Toplevel(root)
    window.title("Results")
    window.configure(bg="black")
    window.iconbitmap("icon2.ico")

    window.maxsize(900,600)
    window.minsize(900,600)

    label = Label(window,text="Finger",font=("Cascadia Code Semibold", 20),fg="#8A2BE2",bg="black")
    label.place(x=100,y=50)

    label2 = Label(window,text="Bolt",font=("Cascadia Code Semibold", 20),fg="white",bg="black")
    label2.place(x=200,y=50)

    heading = Label(window,text="Results",font=("Cascadia Code Semibold", 20),fg="#8A2BE2",bg="black")
    heading.place(x=400, y=100)

    info = Label(window,text='''Wpm: 93
    Accuracy:95%
    Character Length: 256
    Correct words: 20
    Highest Score: 95wpm''',bg="black",fg="white",font=("Cascadia Code Semibold",20))
    info.place(x=200,y=200)

    credits = Label(window,text="Made by: Vivek Gupta,Vedansh Sharma,Parth Wadhwa",font = ("Cascadia Code Semibold",20),bg="black",fg="white") 
    credits.place(x=70,y=500)


    change_paragraph()
    # create_window()

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()


# Todo for black screen
root.configure(bg="black")
root.iconbitmap("icon2.ico")
window = None
window_exists = BooleanVar()
window_exists.set(False)

# print(screen_width, screen_height)
root.maxsize(1300,715)
root.minsize(1300,715)

label = Label(root,text="Finger",font=("Cascadia Code Semibold", 20),fg="#8A2BE2",bg="black")
label.place(x=100,y=50)

label2 = Label(root,text="Bolt",font=("Cascadia Code Semibold", 20),fg="white",bg="black")
label2.place(x=200,y=50)



text_area = Label(root,text=f"{random.choice(paragraphs)}",font=("Cascadia Code Semibold", 21), fg ="#A800AB",bg="black", wraplength=1000)
text_area.place(x=150,y=250)



image = Image.open("./Untitled.png")
icon = ImageTk.PhotoImage(image)
Label(root,image=icon,bg="black").place(x=520,y=150)

# instruction = Label(root,text="Type the Text below",fg="white",bg="#854091",font=("Helvetica",20))
# instruction.place(x=550,y=150)

input_area = Text(root,bg="#D9D9D9",width=75,height=5 ,font=("Cascadia Code Semibold",20))

input_area.place(x=50,y=420)

image2 = Image.open("./Restart_icon.png")
icon2 = ImageTk.PhotoImage(image2)

result = Button(root,image = icon2,bg="black",fg="white",width=150,height=80,font=('Cascadia Code Semibold',10),borderwidth=0, command=create_window)
result.place(x=600,y=600)



credits = Label(root,text="Project Submitted by-",font = ("Cascadia Code Semibold",15),bg="black",fg="white") 
credits.place(x=350,y=680)
credits2 = Label(root,text="Vivek Gupta, Vedansh Sharma, Parth Wadhwa", font = ("Cascadia Code Semibold",15),bg="black",fg="#854091") 
credits2.place(x=600,y=680)




root.mainloop()