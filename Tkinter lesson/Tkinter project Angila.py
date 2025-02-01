project in Tkinter all of it from Angila


Log in:
#This log in will take the name of website,email,password and add those information in File only

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from random import choice,randint,shuffle
root=Tk()
root.title("Password manager")
root.config(padx=0,pady=0)
root.geometry("1000x650")
my_image=ImageTk.PhotoImage(Image.open("C:\\Users\\MRC\\PycharmProjects\\Password Manager\\p.jpg"))
my_labell=Label(image=my_image)
my_labell.pack()

my_image2=ImageTk.PhotoImage(Image.open("C:\\Users\\MRC\\PycharmProjects\\Password Manager\\logo.png"))
my_labell2=Label(image=my_image2,bg="lightcyan")
my_labell2.place(x=400,y=10)
#---------------------------------------------add--------------------------------------------------------

def generate():
    entry_password.insert(0,password)

def add():
    w=entry_website.get()
    e=entry_email_user.get()
    p=entry_password.get()
    my_file = open("file.txt", 'a')


    if len(w)==0 or len(p)==0:
        messagebox.showinfo(title="Oop",message="Please do not put the entries empty or do not add something ok")
    else:
        is_ok=messagebox.askokcancel(title=w,message=f"It is all right to save it as your information\nWedsite: {w}\nEmail|user_name: {e}\nPassword: {p}")
        if is_ok:

            my_file.write(f" {w}  |  {e}  |  Password: {p}\n")
            entry_website.delete(0,END)
            entry_password.delete(0,END)

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password_letters =[choice(letters) for char in range(randint(8, 10))]
password_symbols=[choice(symbols) for char in range(randint(2, 4))]
password_numbers=[choice(numbers) for char in range(randint(2, 4))]

password_list=password_letters+password_symbols+password_numbers

password="".join(password_list)


label_webside=Label(text="Webside: ",bg="white",fg="black")
label_webside.place(x=300,y=280)

label_email_user=Label(text="Email/user_name: ")
label_email_user.place(x=300,y=320)

label_password=Label(text="Password: ")
label_password.place(x=300,y=360)

entry_website=Entry(width=50,borderwidth=2)
entry_website.place(x=370,y=280)
entry_website.focus()

entry_email_user=Entry(width=50,borderwidth=2)
entry_email_user.place(x=420,y=320)
entry_email_user.insert(0,"anilprogs123456@gmail.com")

entry_password=Entry(width=40,borderwidth=2)
entry_password.place(x=380,y=360)

button_genirate=Button(text="Generate Password",width=21,borderwidth=4,command=generate)
button_genirate.place(x=650,y=354)

button_add=Button(text="Add",width=60,borderwidth=4,command=add)
button_add.place(x=380,y=390)

root.mainloop()
-------------------------------------------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#it is log in Appliction which take the name of website,email,password and add it in Json file
#it also have Search button you should put the name of website search button will take out it from the json file

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from random import choice,randint,shuffle
import json
root=Tk()
root.title("Password manager")
root.config(padx=0,pady=0)
root.geometry("1000x650")
my_image=ImageTk.PhotoImage(Image.open("C:\\Users\\MRC\\PycharmProjects\\Password Manager\\p.jpg"))
my_labell=Label(image=my_image)
my_labell.pack()

my_image2=ImageTk.PhotoImage(Image.open("C:\\Users\\MRC\\PycharmProjects\\Password Manager\\logo.png"))
my_labell2=Label(image=my_image2,bg="lightcyan")
my_labell2.place(x=400,y=10)
#---------------------------------------------add--------------------------------------------------------

def generate():
    entry_password.insert(0,password)

def add():
    w=entry_website.get()
    e=entry_email_user.get()
    p=entry_password.get()
    new_data={
        w:{
            "email":e,
            "password":p
        }
    }


    if len(w)==0 or len(p)==0:
        messagebox.showinfo(title="Oop",message="Please do not put the entries empty or do not add something ok")
    else:
        is_ok=messagebox.askokcancel(title=w,message=f"It is all right to save it as your information\nWedsite: {w}\nEmail|user_name: {e}\nPassword: {p}")
        if is_ok:
            try:
                with open("data.json","r") as show:
                    #read the old data
                    data=json.load(show)
            except FileNotFoundError:
                with open("data.json","w") as show:
                    json.dump(new_data,show,indent=4)
            else:
                #update the old data to new data
                data.update(new_data)

                with open("data.json","w") as show:
                    #saving the new data
                    json.dump(data,show,indent=4)
            finally:
                entry_website.delete(0,END)
                entry_password.delete(0,END)


#if it be empty try it to solve it
"""def find_password():
    try:
        with open("data.json","r") as find:
            f=json.load(find)
    except:
        messagebox.showinfo(title="Database",message="Database is empty,no founded such as a file")
    else:
        website = entry_website.get()
        if website in f:
            is_ok=messagebox.showinfo(title=f"{website}",message=f"{f[website]}")
            if is_ok:
                pass
            else:
                pass
    finally:
        pass"""

def search_data():
    website=entry_website.get()
    try:
        with open("data.json","r") as find:
            f=json.load(find)
    except FileNotFoundError:
        messagebox.showinfo("Error",message="No data file found it")
    except:
        messagebox.showinfo(title="Error",message="Database is empty,no founded such as a file")
    else:
        if website in f:
            email=f[website]["email"]
            password=f[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email} and password: {password}")
        else:
            messagebox.showinfo(title=website,message=f" No details for {website} exits.")


#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password_letters =[choice(letters) for char in range(randint(8, 10))]
password_symbols=[choice(symbols) for char in range(randint(2, 4))]
password_numbers=[choice(numbers) for char in range(randint(2, 4))]

password_list=password_letters+password_symbols+password_numbers

password="".join(password_list)


label_webside=Label(text="Webside: ",bg="white",fg="black")
label_webside.place(x=300,y=280)

label_email_user=Label(text="Email/user_name: ")
label_email_user.place(x=300,y=320)

label_password=Label(text="Password: ")
label_password.place(x=300,y=360)

entry_website=Entry(width=50,borderwidth=2)
entry_website.place(x=370,y=280)
entry_website.focus()

entry_email_user=Entry(width=50,borderwidth=2)
entry_email_user.place(x=420,y=320)
entry_email_user.insert(0,"anilprogs123456@gmail.com")

entry_password=Entry(width=40,borderwidth=2)
entry_password.place(x=380,y=360)

button_genirate=Button(text="Generate Password",width=21,borderwidth=4,command=generate)
button_genirate.place(x=650,y=354)

button_add=Button(text="Add",width=60,borderwidth=4,command=add)
button_add.place(x=380,y=390)

button_search=Button(text="Search",command=search_data)
button_search.place(x=710,y=280)

button=Button(root,text="enter")
root.mainloop()
--------------------------------------------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#this log in when you put your email and password correct it will destory the window 
# and your interdection also  exit in it
#it has hacking photo in bg and photo of you

from tkinter import *
from PIL import ImageTk,Image
import math
root=Tk()
root.title("Anil Application")
root.geometry("1600x1000")
root["background"]="lightcyan"
my_image=ImageTk.PhotoImage(Image.open("C:\\Users\\MRC\\PycharmProjects\\wallpaperflare.com_wallpaper (10).jpg"))

my_labell=Label(image=my_image)
my_labell.pack(side="right")

labell1=Label(root,text="Email")
labell1.place(x=540,y=190)

e=Entry(root,width=34,borderwidth=2)
e.place(x=540,y=210)
e.insert(90,"")


def show_hide():

    if show_hide_button["text"]=="Show":

        e1.config(show="")

        show_hide_button.config(text="Hide")


    else:

        e1.config(show="*")

        show_hide_button.config(text="Show")


labell2=Label(root,text="Password")
labell2.place(x=540,y=240)

lab=Label(root,text="secret information Of IBM,Please Inter the code")
lab.place(x=540,y=160)

e1=Entry(root,width=34,borderwidth=2,show="*")

e1.place(x=540,y=260)

e1.insert(90,"")

def Exit():

    if e1.get()=="anil786.com" and e.get()=="anilamiri2005@gmail.com":
        return root.quit()

    elif e1.get()=="anil786.com" and e.get()!="anilamiri2005@gmail.com":

        return my_labell1.place(x=540,y=190)

    elif e1.get()!= "anil786.com"  and e.get() == "anilamiri2005@gmail.com":

        return my_labell2.place(x=540,y=240)

    else:

        return my_labell3.place(x=540,y=160)


show_hide_button=Button(root,text="Show",font=("SimSum",10),command=show_hide,padx=5,pady=5)

show_hide_button.place(x=755,y=264)


my_labell1=Label(root,text="Email is incorrect Please inter a valid email address")

my_labell2=Label(root,text="Password is incorrect Please inter a valid Password")

my_labell3=Label(root,text="Please inter correct Password and Email address")

button_Exit=Button(root,text="Enter",fg="white",bg="black",width=20,borderwidth=3,command=Exit)

button_Exit.place(x=540,y=290)

button=Button(root,text="2024",fg="white",bg="black",width=20,borderwidth=4)
button.place(x=500,y=400)

button=Button(root,text="2025",fg="white",bg="black",width=20,borderwidth=4)
button.place(x=500,y=434)

button=Button(root,text="2026",fg="white",bg="black",width=20,borderwidth=4)

button.place(x=500,y=467)
button=Button(root,text="2027",fg="white",bg="black",width=20,borderwidth=4)
button.place(x=500,y=500)

frame3 = Frame(root, bg="white")
frame3.place(x=1030, y=480)
frame3.pack_propagate(False)
frame3.configure(width=290, height=150)
label3 = Label(frame3, text="Contact with me")
label3.pack()

label3 = Label(frame3, text="Address: 6 district,kabul,Afghanistan\n"
                            "Email:anilamiri2005@gmail.com\n"
                            "Phone number: +93787062443\n"
                            "Facebook: Anil Amiri\n"
                            "Youtube: @ANILAMIRI-nr2ce\n"
                            "GitHub:https://github.com/Anil-progs/Anil-progs,\n"
               )
label3.pack()

frame1=Frame(root,bg="white")
frame1.place(x=1070,y=1)
frame1.pack_propagate(False)
frame1.configure(width=300,height=380)

photos = ImageTk.PhotoImage(Image.open("C:\\Users\\MRC\\PycharmProjects\\20496.jpg"))
photo_label=Label(frame1,image=photos)
photo_label.pack()

frame=Frame(root,bg="white")
frame.place(x=1,y=1)
frame.pack_propagate(False)
frame.configure(width=495,height=700)
phot = ImageTk.PhotoImage(Image.open("C:\\Users\\MRC\\PycharmProjects\\wallpaperflare.com_wallpaper (10).jpg"))
phot_label=Label(frame,image=phot)
phot_label.pack()

label1=Label(frame,text="My information")
label1.place(x=10,y=5)
label1=Label(frame,text="Name: Anil Amiri\n"
                        "Father Name: Essmatullah\n"
                        "Date of Birth:19/1/2005\n"
                        "Gender: Male\n"
                        "Field: Software Engineer\n"
                        "Birth place: Kabul, Afghanistan,\n"
             )
label1.place(x=2,y=30)


label2=Label(frame,text="Abilities")
label2.place(x=80, y=190)
label2=Label(frame,text="Software coding\n"
                        "Developing webs\n"
                        "Hacking and defending hack attack\n"
                        "Deep coding \n"
                        "Active in AI section\n"
             )
label2.place(x=2,y=220)


label4=Label(frame,text="Language Ability")
label4.place(x=20,y=360)
label4=Label(frame,text="Programing language: python\n"
                        "Literature:English(DEL)>>> graduate from Muslim English Language\n"
                        "Ferdowsee Education Center\n"
                        "Deep self study of English language\n"
             )
label4.place(x=2,y=400)

label5 = Label(frame, text=" Important Photos during work")
label5.place(x=20, y=560)

button=Button(frame,text="Hack AIT",fg="white",bg="black",width=20,borderwidth=4)
button.place(x=1,y=600)

button=Button(frame,text="Broke IP",fg="white",bg="black",width=20,borderwidth=4)
button.place(x=160,y=600)

button=Button(frame,text="Web TC",fg="white",bg="black",width=20,borderwidth=4)
button.place(x=320,y=600)

WORK_MIN=1
SHORT_BREAK_NIM=2
LONG_BREAK_MIN=2
timer=None

def reset_timer():
    root.after_cancel(timer)
    label_time.config(text="00:00")
    label_time.config(text="Timer")
    check_box.config(text="")
    global reps
    reps=0


reps=0
def door():
    global reps
    reps +=1
    work_sec=WORK_MIN *60
    short_break_sec=SHORT_BREAK_NIM *60
    long_break_sec=LONG_BREAK_MIN * 60
    if reps %8==0:
        count(long_break_sec)
        label_time2.config(text="Break",fg="red")
    elif reps%2==0:
        count(short_break_sec)
        label_time2.config(text="Break",fg="blue")
    else:
        count(work_sec)
        label_time2.config(text="work",fg="black")
label_time=Label(root,text="Timer Anil")
label_time.place(x=200,y=200)

def count(num):
    count_min=math.floor(num/60)
    count_sec=num % 60
    if count_sec == 0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"

    label_time.config(text=f"{count_min}:{count_sec}")


    if num > 0:
        global timer
        timer=label_time.after(1000,count,num-1)
    else:
        door()
        marks=("")
        section=math.floor(reps/2)
        for _ in range(section):
            marks+="</"
        check_box.config(text=marks)

label_time2=Label(root,text="Timer Anil",font=("bold",10))
label_time2.place(x=500,y=4)

label_time=Label(root,text="00:00",fg="black",bg="white",font=("bold",35))
label_time.place(x=600,y=2)

button=Button(root,text="start",bg="white",fg="black",command=door,width=10,highlightthickness=0)
button.place(x=730,y=3)

button_reset=Button(root,text="Reset",fg="black",bg="white",command=reset_timer,width=10,highlightthickness=0)
button_reset.place(x=730,y=35)

check_box=Label(root,text="</")
check_box.place(x=750,y=70)
root.mainloop()
-----------------------------------------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Flash card 
#we use here from canvas some methods of it create_text,create_image......


from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import random
import pandas

root=Tk()
root.title("Flash Card")
root.geometry("1400x730")
root.configure(bg="#BFEFFF")
current_word={}
def change_the_word():
    global current_word,flip_timer
    root.after_cancel(flip_timer)
    current_word=random.choice(obj)
    canvas.itemconfig(canvas_title,text="French",fill="black")
    canvas.itemconfig(canvas_text,text=current_word["French"],fill="black")
    canvas.itemconfig(background,image=image_card_infront)
    flip_timer=root.after(3000, func=flip_flop)

    """word=pandas.read_csv("french_words.csv")
    list=[]
    for i in word["French"]:
        list.append(i)
    b=random.choice(list)
    canvas.itemconfig(canvas_title,text="French")
    canvas.itemconfig(canvas_text,text=b)"""

def is_known():
    obj.remove(current_word)
    print(len(obj))
    data=pandas.DataFrame(obj)
    data.to_csv("words_I_do't_know.csv",index=False)
    change_the_word()
def flip_flop():
    canvas.itemconfig(canvas_title,text="English",fill="white")
    canvas.itemconfig(canvas_text,text=current_word["English"],fill="white")
    canvas.itemconfig(background,image=image_card_background)

flip_timer=root.after(3000,func=flip_flop)

canvas=Canvas(width=800,height=526)
#these pic will changing
image_card_infront=PhotoImage(file="card_front.png")
image_card_background=PhotoImage(file="card_back.png")

background=canvas.create_image(400,263,image=image_card_infront)
canvas.config(bg="#BFEFFF",highlightthickness=0)
canvas.place(x=100,y=30)

obj={}
#word=pandas.read_csv("french_words.csv")
try:
    word=pandas.read_csv("words_I_do't_know.csv")
except FileNotFoundError:
    word = pandas.read_csv("french_words.csv")
    obj=word.to_dict(orient="records")
else:
    obj=word.to_dict(orient="records")
#orient: it will show the first row titles and its item




canvas_title=canvas.create_text(400,150,text="",font=("Bahnschrift SemiCondensed",40))
canvas_text=canvas.create_text(400,263,text="",font=("Bahnschrift SemiCondensed",60,"bold"))

image_right=ImageTk.PhotoImage(Image.open("right.png"))
known_button=Button(image=image_right,highlightthickness=0,command=is_known)
known_button.place(x=1100,y=50)

#PhotoImage : it will use when the picture pixel is less if not use PIL

image_range=PhotoImage(file="wrong.png")
unknown_button=Button(image=image_range,highlightthickness=0,command=change_the_word)
unknown_button.place(x=1100,y=450)
#if we use the change_the _word() in here it show that once our program should run after by button

change_the_word()
root.mainloop()

