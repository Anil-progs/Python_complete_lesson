#tkinter is simple libriry of graficle python that is like turtle but turtle is for make some lines  or graf
#tkinter use for createing some Application
from tkinter import *
root=Tk()
root.title("lesson of Angila")
root.geometry("500x600")
-----------------------------------------------------------------------------------------------------------
#Labell
my_labell=Label(root,text="This is the place of label",bg="white",fg="black",font=("Brush Script MT",10))
my_labell.place(x=180,y=1)                                                  #font : you can find font from wordpad 
                                                                            #there are lots of fond on there
----------------------------------------------------------------------------------------------------------------
#custom tkinter it is too much graphical
from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("200x300")
#using from custom tkinter it is too much graphical
labell=ttk.Label(root,text="This is the place that you can play football")
labell.pack()
entry=ttk.Entry(root)
entry.pack()
button2=ttk.Button(root,text="click here")
button2.pack()

#this the simple graphice
entry3=Entry(root)
entry3.pack()
button3=Button(root,text="click here")
button3.pack()

root.mainloop()
--------------------------------------------------------------------------
def click():
    #get the Entry
    a=e.get()
    #change label
    my_labell.config(text=a)
#Entry
e=Entry(root,width=30)
e.place(x=190,y=54)

#insert in entry
e.insert(END,string="email:  ")
e.place(x=190,y=54)
---------------------------------------------------------------------------------------------------------------------------------------
#Button
button=Button(root,text="Click Me",bg="white",fg="black",command=click)
button.place(x=200,y=25)

#Button that image is internal of it
from PIL import ImageTk,Image
image_button=ImageTk.PhotoImage(Image.open("right.png"))

button=Button(image=image_button)
button.pack()

#Beautiful Button using Canvas and it also have image internal of it
canvas=Canvas(width=400,height=200)
canvas.pack()

images=PhotoImage(file="right.png")
canvas.create_window((200,200),window=ttk.Button(root,image=images))

#beautifull button using canvas without image
canvas=Canvas(width=400,height=200)
canvas.pack()

images=PhotoImage(file="right.png")
canvas.create_window((200,200),window=ttk.Button(root,text="Select Here",width=20))

#highlightthickness
------------------------------------------------------------------------------------------------------------------------------------
Text
#Text is the same like notepad
text=Text(root,width=30,height=5)
#put curser in the  textbax
text.focus()
#add some text at the beginning
text.insert(END,"Your comment:")
#Get 's current value in text at line 1,charater 0
print(text.get("1.0",END))
text.place(x=170,y=80)
---------------------------------------------------------------------------------------------------------------------------------
Frame        #in frame does not matter to use both grid() and pack()
#it is the same like board of advertisement
#it is the same like window
#we can create our button,lebal.... in frame as will as and create our application on it
frame=Frame(root,bg="white")
frame.pack_propagate(False)
frame.configure(width=100,height=100)
frame.pack()
                                  #padx,pady= it will make the internal size of it
frame=LabelFrame(root,bg="white",padx=200,pady=200)
fram.pack(padx=20,pady=30)  #in pack the padx,pady= it will show the place of your frame in window

button=Button(frame,text="click here",padx=10,pady=7)
buttom.grid(row=0,column=0)#we can use both grid and pack in frame

button=Button(frame,text="Do not click here",padx=10,pady=7)
buttom.grid(row=1,column=0)

frame=LabelFrame(root,text="Here I can use text in my labelframe",padx=200,pady=200)
fram.pack(padx=20,pady=30)
----------------------
LabelFrame:

from tkinter import *
root=Tk()
labelframe=LabelFrame(root,bg="white")
labelframe.configure(width=300,height=300)
labelframe.pack()
#it is the same like frame 
#anything that frame can labelframe also can do it 
#it is beautifull than the frame


root.mainloop()
------------------------------------------------------------------------------------------------------------------------------------

#Spinbox
def spinbox_used():
    #gets the current value in spinbax
    return spinbox.get()
#Spinbox
spinbox=Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.place(x=200,y=200)

example:
    def get():
        a=spinbox.get()
        label=(Label(root,text=f" {a}"))
        label.place(x=1,y=60)
        
    spinbox=Spinbox(root,from_=0,to=10,width=5,command=get)
    spinbox.place(x=1,y=2)
------------------------------------------------------------------------------------------------------------------------------------------
#Scale

Sliders_With_TKinter_-_Python_Tkinter_GUI_Tutorial_#16(360p)

#Called with current scale value.
def scale_used(value):
    return value
#scale
scale=Scale(from_=0,to=100,command=scale_used)
scale.place(x=210,y=250)

example:
    def get(value):
        labell=Label(root,text=f"{value}")
        labell.place(x=5,y=100)

    scale=Scale(root,from_=0,to=10,command=get)
    scale.place(x=2,y=5)

example:
    harizantal=Scale(root,from_=0,to=100)
    harizantal.pack()

    def show():
        label=Label(root,text=harizantal.get())
        label.pack()

    button=Button(root,text="get it",command=show)
    button.pack()


example:
    harizantal=Scale(root,from_=0,to=500,orient=HORIZONTAL)
    harizantal.pack()

    vertical=Scale(root,from_=0,to=500,orient=VERTICAL)
    vertical.pack()

    def play():
        root.geometry(f"{harizantal.get()}x{vertical.get()}")

    button=(root,text="Size manage",command=play)
    button.pack()
------------------------------------------------------------------------------------------------------------------------------------------

relief=SUNKEY    :  it will put these text in SUNKEY and get four side of it boarder

sticky=N or sticky=W  or sticky=E,S   or sticky=W+E   pr  sticky=S+N

anchor=E,W,N,S    it will show the postion of its text by anchor=E,W,N,S

    list_pic=5
    statues=Label(root,text="This is my pic form 1 to "+ str(len(list_pic)),bd=1,releif=SUNKEY,anchor=E)
    statues.grid(row=2,column=0,columnspan=3,sticky=W+E)

--------------------------------------------------------------------------------------------------------------------------------------------
checkbutton with tkinter

from tkinter import *
root=Tk()
def show():
    Label(root,text=var.get()).pack()
               #when button cliked if checkbox check already label will get out 1,otherwise it will get out 0
var=IntVar()  #int
check_button=Checkbutton(root,text="please click here",variable=var).pack()

button=Button(root,text="click here",command=show)
root.mainloop()

example real:
    from tkinter import *
    root=Tk()
    def show():
        Label(root,text=var.get()).pack()
         #str
    var=StringVar()    #beacuse it is Stringvar we need to use onvalue and offvalue
    check_button=Checkbutton(root,text="check here",variable=var,onvalue="on",offvalue="off").pack()

    check_button.deselect()  #it is important otherwise before to check the checkbutton it will be check

    button=Button(root,text="click",command=show)
    root.mainloop()



def checkbutton_used():
    #prints 1 if on button checkd,
    #otherwise 0
    print(check_state.get())
#variable to hold on to checked state,
# 0 is off, 1 is on.
check_state=IntVar()
#check button
check_button=Checkbutton(root,text="is on",
variable=check_state,command=checkbutton_used)
check_state.get()
check_button.place(x=100,y=240)
-------------------------------------------------------------------------------------------------------------------------------------------

#Radiobutton
def radio_used():
    print(radio_state.get())
#variable to hold on to which radio 
#button value is checked.
radio_state=IntVar()                          #anything that value is we should take the variable the same datatype
radiobutton1=Radiobutton(root,text="Option1",value=1,
variable=radio_state,command=radio_used)

radiobutton2=Radiobutton(root,text="option2",value=2,
variable=radio_state,command=radio_used)
radiobutton1.place(x=140,y=280)
radiobutton2.place(x=140,y=300)

Example:
    list_food=[
        ("pizza","pizza"),
        ("bolani","bolani"),
        ("been","been")
    ]

    p=StringVar()
    p.set("None")
    def show(value):
        labell=Label(root,text=value)
        labell.pack()

    for text,mode in list_food:
        radiobutton=Radiobutton(root,text=text,variable=p,value=mode)
        radiobutton.pack()

    labell=Label(root,text=p.get())
    labell.pack()

    button=Button(root,text="Choose",command=lambda:show(p.get()))
    button.pack()




---------------------------------------------------------------------------------------------------------------------------------------------
listbox in tkinter

example:
    def listbox_used(event):
        #Gets current selection from listbox
        print(listbox.get(listbox.curselection()))

    listbox=Listbox(root,height=4,width=20)
    fruits=["Apple","Banana","orange","pear"]
    for item in fruits:
        listbox.insert(fruits.index(item),item)
    listbox.bind("<<ListboxSelect>>",listbox_used)
    listbox.place(x=180,y=370)

    root.mainloop()

example:
    from tkinter import *
    root=Tk()

    listbox=Listbox(root,height=4,width=20)
    listbox.pack()

    #to insert something in listbox
    #we can insert at the END,0,2,1,3....
    listbox.insert(END,"English")

    #to insert many items 
    list=["English","Mathmatic","Python","Database"]
    for main in list:
        listbox.insert(END,main)

    root.mainloop()

example:

    from tkinter import *
    root=Tk()
    root.geometry("600x600")

    listbox=Listbox(root,height=10,width=20)
    listbox.place(x=10,y=10)

    list = ["1:English", "2:Mathmatice", "3:Phesice", "4:Paython","TC book"]
    for main in list:
        listbox.insert(END,main)
    def delete():
        #ANCHOR : put selection to each line you want it will deleted
        #0: if you put zero each time that you press delete button it will delete the first line
        #1
        #END:if you put END each time that you press delete button it will delete the END line
        listbox.delete(ANCHOR)

    button=Button(root,text="delete",command=delete)
    button.place(x=9,y=190)

    global labell
    labell=Label(root,text="are you select")
    labell.place(x=100,y=200)
    def select():
        #ANCHOR: means that one that you select
        labell.config(text=listbox.get(ANCHOR))

    button2=Button(root,text="select",command=select)
    button2.place(x=9,y=230)

    def down():
        global listbox_anther
        listbox_anther=Listbox(root)
        listbox_anther.place(x=400,y=70)
        list = ["1:English", "2:Mathmatice", "3:Phesice", "4:Paython"]
        for main in list:
            listbox_anther.insert(END,main)


    spanbox=Spinbox(root,from_=0,to=5,command=down)
    spanbox.place(x=400,y=50)
    root.mainloop()
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Tkinter layout manager
    #if a item deos not have layout it will not show it self
    #layouts are pack(),place(),grid()
    pack()
        #it will get the items under each other
        #like interperter
        .pack(side="right")
        .pack((side="left" or "center"  or "button"))
    grid()
        #it has row and column 
        #it will show your item on grid that you mantion
        .grid(row=0,column=0,columnspan=3)
        .grid(column=1,row=2,columnspan=2)
    place()                     columnspan: it is use the time that your button or entry is more than it postion to go from up of it 
                                                we will use this
        #it also a layout 
        #it will put item on specifice place that you mantion
        # you need to obviuse the place of it by x and y
         .place(x=33,y=23) 

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#according x how much posh it and according y how much posh it
root.config(padx=100,pady=100) 

#it will bring some icon in your program
root.iconbitmap("C:\\Users\\MRC\\PycharmProjects\\Password Manager\\p.jpg")

#it is use for quit the program
root.quit()
Exit_button=Button(root,text="Exit",command=root.quit)
Exit_button.pack()

#it will also destroy the program
root.destroy()
Exit_button=Button(root,text="Exit",command=root.destroy)
Exit_button.pack()

#config  it will change the lebal text
config()
labell=(Label(root,text="This the old progect",fg="black"))
labell.pack()
labell.config(text="This is the nowest version of python")

--------------------------------------------------------------------------------------------------------------------------------------------

Open_Files_Dialog_Box_-_Python_Tkinter_GUI_Tutorial_#15(360p)

#it is not use only for photes it also for other files that we can upload it like pdf files........

syntax:     #filetypes it is really import to curefully put all the things in it
    name_obj=filedialog.askopenfilename(initialdir="[you can put directory]",title="select title",filetypes=(("png files","*.png"),("all files","*.*"))))


example:
    from tkinter import *
    from PIL import ImageTk,Image
    from tkinter import filedialog
    root=Tk()
    root.geometry("500x500")
    root.title("Application")
    root.iconbitmap("DSC_0466.JPG")
    frame=LabelFrame(root,bg="white")
    frame.configure(width=200,height=200)
    frame.place(x=5,y=5)

    def show():
        #be curefile that make my_image global
        global my_image
        root.filedialog=filedialog.askopenfilename(initialdir="Pictures",title="select a file"
                                                ,filetypes=(("png files","*.png"),("all files","*.*")))
        my_image=ImageTk.PhotoImage(Image.open(root.filedialog))
        my_labell=Label(frame,image=my_image)
        my_labell.pack()

    button=Button(frame,text="Upload",command=show)
    button.pack()
    root.mainloop()

example:
    def show():
        #the my_image should become global
        global my_image
        filedialogs=filedialog.askopenfilename(initialdir="Picture",title="select file",
                                            filetypes=(("png file","*.png"),("all files","*.*")))
        my_image=ImageTk.PhotoImage(Image.open(filedialogs))
        labell=Label(root,image=my_image)
        labell.pack()

    button=Button(root,text="Upload",command=show)
    button.pack()
    root.mainloop()


-------------------------------------------------------------------------------------------------------------------------------------------
Convas lesson in tkinteer


# A canvas is a widget that allow you to draw shapes
#like drawing square,circle,lines,text etc
#if you want to create paint you would need a canvas
import tkinter
from tkinter import ttk
from tkinter import *
root=Tk()
canvas=Canvas(root,bg="white")
canvas.pack()
#width: in canvas for borderwidth we will use width
#fill: use for the color of that shape
#desh: it is like dash
#outline: it will clear the border line color
#-------------------------------------------------------
#canvas.create_oval(left,top,right,bottom)
canvas.create_rectangle(10,10,100,200,fill="#BFEFFF",width=0)
#--------------------------------------------------------
#canvas.create_oval(left,top,right,bottom)
#we can put the position and shape size on tuple
canvas.create_oval((100,20,10,100),width=4,fill="blue",dash=10,outline="green")
#canvas.create_oval((200,200,45,45),width=4,fill="blue",dash=(4,2))
#canvas.create_oval((200,200,45,45),width=4,fill="blue",dash=(4,2,1,1))
#------------------------------------------------------
#canvas.create_line(start_x,start_y,end_x,end_y)
canvas.create_line((0,0,100,150))
#-----------------------------------------------------
#canvas.create_polygon((x1,y1,x2,y2,x3,y3))
canvas.create_polygon(0,0,100,200,300,50,fill="black")

#---------------------------------------------
#tkinter.ARC
#tkinter.PIESLICE
#tkinter.CHORD
canvas.create_arc((0,0,100,200),
                  fill="brown",
                  start=45,
                  style=tkinter.CHORD,
                  width=1,
                  outline="green",
                  dash=(1,1,4,3))
#----------------------------------------------------------------------------------
# width=it will make it slice slice
canvas.create_text((200,100),text="This is my application",fill="green")
#canvas.create_text((200,100),text="This is my application",fill="green",width=10)
#-------------------------------------------------------------------------------
#vary beautifull button you can create by with convas
canvas.create_window((200,200),window=ttk.Label(root,text="This is my label on canvas"))
canvas.create_window((200,240),window=ttk.Button(root,text="This is my label on canvas"))

#----------------------------------------------------------------------------
def draw_on_canvas(event):
    x=event.x
    y=event.y
    canvas.create_oval((x- brush_size / 2,y- brush_size / 2,x+ brush_size / 2,y+brush_size/2),fill="black")
def brush_size_adjust(event):
    global brush_size
    if event.delta >0:
        brush_size +=4
    else:
        brush_size -=4
    brush_size=max(0,min(brush_size,50))
brush_size=4
canvas.bind('<Motion>',draw_on_canvas)
canvas.bind('<MouseWheel>',brush_size_adjust)

root.mainloop()

-----------------------------------------------------------------------------------------------------------------------------------------
Image in tkinter

my_image=PhotoImage(file="DSC_0466.JPG")
labell=Label(image=my_image)
labell.pack()


from PIL import ImageTk,Image

img=ImageTk.PhotoImage(Image.open('C:\\Users\\RC\\Desktop\\Anil.py\\the Besic Angila exersise and solution'))
labell=Label(Image=img)
labell.pack()
---------------------------------------------------------------------------------------------------------------------------------------------
Dropdown_Menus_With_TKinter_-_Python_Tkinter_GUI_Tutorial_#18(360p)
OptionMenu

var=StringVar()
var.set("English")
option_menu=OptionMenu(root,var,"English","franch","spanish")
option_menu.pack()


from tkinter import *
root=Tk()
list=["English","spanish","french","chinessess"]
var=StringVar()
var.set(list[0])
#if we put list instead of values we need to take * before the value
option_menu=OptionMenu(root,var,*list) #*list : it is beacuse of many thing are in list
option_menu.pack()

def show():
    Label(root,text=var.get()).pack()

button=Button(root,text="Get the Value",commend=show)
root.mainloop()


-----------------------------------------------------------------------------------------------------------------------------------------------
#this will remove the toolbar of window
root.overrideredirect(True)

#it is the same like loading program
example:
from tkinter import *
from PIL import ImageTk,Image
class loading(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("521x333+400+200")
        self.loading_image=ImageTk.PhotoImage(Image.open("pil.png"))
        self.labell_image=Label(image=self.loading_image)
        self.labell_image.pack()
        self.labell_text=Label(text="  TC.com  ",font=("@SimSun",50),bg="black",fg="white")
        self.labell_text.place(x=30,y=230)
        self.labell_text2=Label(text=" Loading.......",font=("@SimSun",15))
        self.labell_text2.place(x=60,y=305)
        self.after(3000,func=self.coming_at_first)
        self.overrideredirect(True)
        self.configure(bg="lightblue")
    def coming_at_first(self):
        self.destroy()

if __name__ =="__main__":
    main=loading()
    main.mainloop()

-----------------------------------------------------------------------------------------------------------------------------------------------
#event 

#'<method-1>'    :method means(Button,Double...)  if it 1 show that action happen by click the left click
                                                #if it is 2 show action happen by click the meddle click
                                                #if it is 3 show action happen by click the right click
from tkinter import *
class mygui():
    #here is the function of it 
    def first_click(self,event):
        Label(self.root,text='If you click here two time it will destroy').pack()

    def double_click(self,event):
        self.root.destroy()

    def __init__(self):
        self.root=Tk()
        self.root.title("The GuI new method")
        self.root.geometry("300x300")
        self.button=Button(self.root,text="Click here")
        self.button.place(x=200,y=250)
        #'<Button-1>'  : if it is 1 it show that action happen by click the left click
        self.button.bind('<Button-1>',self.first_click)
        #'<Double>'  : action will happen by click twice 
        self.button.bind('<Double-1>',self.double_click)

        #'<Button-2>'  : if it is 2 it show that action happen by click the middle click
        self.button.bind('<Button-2>',self.first_click)

        #'<Button-3>'  : if it is 3 it show that action happen by click the right click
        self.button.bind('<Button-3>',self.first_click)

        self.root.mainloop()
if __name__=="__main__":
    mygui()

anther example :
    from tkinter import *
    class mygui():
        #here is the function of it 
        def first_click(self,event):
            self.labell.config(text="My jap is Development of Softwares",fg="red")
            
        def double_click(self,event):
            self.labell.config(text="I am a hocker of AIT and CIA",fg="green")

        def key_typeing(self,event):
            self.labell.config(text="Alt+Shift+Enter  : it will also do something special")

        def __init__(self):
            self.root=Tk()
            self.root.title("The GuI new method")
            self.root.geometry("300x300")
            self.labell=Label(self.root,text="What is your work?")
            self.labell.pack()

            self.button=Button(self.root,text="click to swich")
            self.button.place(x=100,y=200)

            self.button.bind('<Button-1>',self.first_click)

            self.button.bind('<Double-1>',self.double_click)

            self.button.bind('<Button-3>',self.key_typeing)

            #we can also make it like this                KeyPress here means Shift
            self.root.bind('<Alt-KeyPress-Z>',self.first_click)

            self.root.bind('<Alt-KeyPress-X>',self.double_click)

            self.root.mainloop()
    if __name__=="__main__":
        mygui()

example:

from tkinter import *
class mygui():
    #here is the function of it 
    def first_click(self,event):
        self.labell.config(text="My jap is Development of Softwares",fg="red")

    def double_click(self,event):
        self.labell.config(text="I am a hocker of AIT and CIA",fg="green")

    def key_typeing(self,event):
        self.labell.config(text="Alt+Shift+Enter  : it will also do something special")

    def __init__(self):
        self.root=Tk()
        self.root.title("The GuI new method")
        self.root.geometry("300x300")
        self.labell=Label(self.root,text="What is your work?")
        self.labell.pack()
        
        self.root.bind('<Alt-KeyPress-A>',self.key_typeing)
        #Enter means when kercer come on window it will react 
        self.root.bind('<Enter>',self.first_click)
        #Leave means when kercer leave the window it will react
        self.root.bind('<Leave>',self.double_click)

        self.root.mainloop()
if __name__=="__main__":
    mygui()
---------------------------------------------------------------------------------------------------------------------------------------------
#Update the datas from mysql 
Update_A_Record_With_SQLite_-_Python_Tkinter_GUI_Tutorial_#22(360p)

from tkinter import *
import mysql.connector as myconn
class Menue_bar():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")
        self.list=["name","last_name","address","city","state","zipcode"]
        self.postion=[35,60,80,100,130,160]
        for item in range(len(self.list)):
            labell=Label(self.root,text=self.list[item],bg="black",fg="white")
            labell.place(x=100,y=self.postion[item])
        self.button=Button(self.root,text="Update_info",command=self.add_new_information)
        self.button.place(x=100,y=200)

        self.entry_n = Entry(self.root)
        self.entry_n.place(x=200, y=35)

        self.entry_l = Entry(self.root)
        self.entry_l.place(x=200, y=60)

        self.entry_a = Entry(self.root)
        self.entry_a.place(x=200, y=80)

        self.entry_c = Entry(self.root)
        self.entry_c.place(x=200, y=100)

        self.entry_s = Entry(self.root)
        self.entry_s.place(x=200, y=125)

        self.entry_z=Entry(self.root)
        self.entry_z.place(x=200,y=160)

        self.entry_id = Entry(self.root)
        self.entry_id.place(x=350, y=200)
        self.button_is=Button(self.root,text="select",command=self.update_informaion,)
        self.button_is.place(x=350,y=240)
        self.root.mainloop()

    def update_informaion(self):
        m=self.entry_id.get()
        n=self.entry_id.delete(0,END)
        b=self.entry_n.delete(0,END)
        l=self.entry_l.delete(0,END)
        a=self.entry_a.delete(0,END)
        c=self.entry_c.delete(0,END)
        s=self.entry_s.delete(0,END)
        z=self.entry_z.delete(0,END)
        mydb=myconn.connect(
            host="Localhost",
            user="root",
            password="1998",
            database="code"
        )
        db_cursor = mydb.cursor()
        try:
            db_cursor.execute("select * from moon where moonID="+m)
        except:
            pass
        else:
            c=db_cursor.fetchall()
            for record in c:
                self.entry_id.insert(0,record[0])
                self.entry_n.insert(0,record[1])
                self.entry_l.insert(0,record[2])
                self.entry_a.insert(0,record[3])
                self.entry_c.insert(0,record[4])
                self.entry_s.insert(0,record[5])
                self.entry_z.insert(0,record[6])
    def add_new_information(self):
        m=self.entry_id.get()
        n=self.entry_n.get()
        l=self.entry_l.get()
        a=self.entry_a.get()
        c=self.entry_c.get()
        s=self.entry_s.get()
        z=int(self.entry_z.get())
        mydb=myconn.connect(
            host="Localhost",
            user="root",
            password="1998",
            database="code"
        )
        db_cursor = mydb.cursor()
        #al=db_cursor.fetchall()
        #self.list = ["name", "last_name", "address", "city", "state", "Zipcode"]
        sql="update moon set name=%s,last=%s,address=%s,city=%s,state=%s,zipcode=%s where moonID=%s"
        values=(n,l,a,c,s,z,m)
        db_cursor.execute(sql,values)
        mydb.commit()
if __name__=="__main__":
    Menue_bar()
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\ \\ \\\ \\\ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\ \\\\\\\\\\ \ \\\ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
windows.geometry("244x535")
windows.colormapwindows()
windows.title(" ")

#Write a text by the tkinter       .pack() is important
labell=Labell(windows,text="anything you can write",fg="blue",bg="yellow",font=("get it from notepad",10))
font=15,).place=(x=1,y=1)

#show the text or buttom be in which row and column
labell.grid(row=0,column=0)

#To make a entary by tkinter
e=Entry(windows,width=24,borderwidt=35)
e.place(x=34,y=5)

#make the text of entary 
e.insert(90,"Enter something that you want to put it in entry")

#To create a buttom by tkinter
# padx: according x how much should be the big ness of it
# pady : according y how uch should be the big ness of it
button=Button(windows,text="select",fg=" ",bg=" ",padx=numbet,pady=number)

#Button that after click something happen
def myClick():
    get="Hello world" +e.get()
    my_labell=Label(windows,text=get)
    my_labell.place(x=234,y=346)
    my_labell.pack()
my_button=Button(windows,text="select",command=myClick
wid.).place(x=342,y=264)

#use to continue the screen 
windows.mainloop()

#To make a entery after clean it write your own entry after click the  button the text that you write should get clear
e=Entry(windows,width=34,borderwidth=6)
e.place(x=any place you to put,y= )
e.insert(windows,text="Enter your email address")
def buttonClick():
    get="Email address: " + e.get()#both will jain with each other
    my_labell=Label(windows,text=get)
    my_labell.place(x=,y=)
    my_labell.pack()# pack() is use to get it
my_button=Button(windows,text="Enter your name",command=buttonClick)

#The Button that have all the thing
button = (Button(windows, text="First homework of python",command=myClick1,borderwidth=4,fg="black", bg="white", font=17,padx=39, pady=5))

#icon picture
#' ' single cotition butween address of picture is important, \\ geting two slish is important
windows.iconbitmap('C:\\Users\\MRC\\Pictures')

# exit button
button_quit=Button(windows,text="Exit button",command=windows.quit)
button_quit.pack()

#delete button of entry
e=Entry(windows,text="Delete the entry ",width=34,borderwidth=6)
def button_clear():
    e.delete(0,END)

button_clean=Button(windows,text="Clear",fg="black",bg="white",command=button_clear)
button_clear.pack()

#Image
#if image not appare in window be curfull to make the obj of image global
#It need for perimasion
from PIL import ImageTk,Image
img=ImageTk.PhotoImage(Image.open('C:\\Users\\RC\\Desktop\\Anil.py\\the Besic Angila exersise and solution'))
ing=Label(Image=img)
ing.pack()

#ccount the number
def count():
    global account
    account+=1
    my_labell.config(text="Count {}".format(account))
my_labell = Label(root, text="Count ")
my_labell.place(x=100, y=100)
    #print(account)
button=Button(root,text="Click",fg="black",bg="white",command=count)
button.pack()

#Farmate usege
def sign_up():
    print("Welcome mr/ms {} {}".format(first_name.get(),last_name.get()))

Label(root,text="first_name").pack()
first_name=Entry(root)
first_name.pack()

Label(root,text="last_name").pack()
last_name=Entry(root)
last_name.pack()

Button(root,text="Sign_up",command=sign_up).pack()

# When you want to click and the entry print internal of GUL
def sign_up():
    labell2.config(text="Welcom mr/mrs  {}".format(First_name.get(),last_name.get()))

Label(root,text="First_name").pack()
First_name=Entry(root)
First_name.pack()

Label(root,text="last_name").pack()
last_name=Entry(root)
last_name.pack()

Button(root,text="Sign_up",command=sign_up).pack()

labell2=Label(root,text="")
labell2.pack(

#make a entry to hide the password that you write
ask_entry=Entry(root,font=("SimSun",15),show="*")
ask_entry.pack(side=LEFT,anchor=N,padx=5,pady=5)

def show_hide():
    if show_hide_button["text"]=="Show":
        ask_entry.config(show="")
        show_hide_button.config(text="Hide")

    else:
        ask_entry.config(show="*")
        show_hide_button.config(text="Show")

show_hide_button = Button(root, text="Show", , command=show_hide)
show_hide_button.pack(side=LEFT, anchor=N, padx=5, pady=5)

#background color we have two way
#this is the first number
root["background"]="black"
#this the second number
root.configure(bg="red")
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# you can also clear the side of label
label=Label(root,text="It ia my label you can not do ah=nything")
label.pack(side="left")


#when we want to change the label here is two way
my_label=Label(root,text="Text is very good",bg="white",fg="black")
my_label.pack(side="right")

my_label["text"]="las;dfjsdhfadskhfjsdakf"              #first way
my_label.config(text="this is the book")
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#use for dim the light of button,labell.... it also full the four side of itself
highlighttickness

-------------------------------------------------------------------------------------------------------------------------------------------

Toplevel()

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
my_image=ImageTk.PhotoImage(Image.open("logo.png"))
labell=Label(image=my_image)
label.pack()

top=Toplevel()
label1=Label(top,text="Simple top window").pack()
button1=Button(top,text="click").pack()
root.mainloop()


real example:
    #make obj of image global,if you don't make it global image will not come at bg
    #make sure when you global obj of image bring it at up or top side beacuse it is global
    #make sure the spelling is right
    #if you use .quit() >> it will quit both main window and Toplevel window
    #if you use .destroy() >> it will destroy only the Toplevel window
    from tkinter import *
    from PIL import ImageTk,Image
    root=Tk()
    my_image=ImageTk.PhotoImage(Image.open("logo.png"))
    labell=Label(image=my_image)
    label.pack()

    def my_function():
        global images
        top=Toplevel()
        images=ImageTk.PhotoImage(Image.open("DSC_0466.JPG"))
        labell_image=Label(top,image=images)
        labell_image.pack()
        button_exit=Button(top,text="Close",command=top.destroy)

    button=Button(root,text="open new window",command=my_function)
    
    root.mainloop()
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
messagebox

messagebox.askokcancel()
    from tkinter import *
    from tkinter import messagebox
    root=Tk()
    def show():
        messagebox.askokcancel()  #it has ok and cancel
        obj=messagebox.askokcancel(title="?",message="Are you sure to save this in your document?")

        messagebox.showinfo()    #it only have ok
        obj=messagebox.showinfo(title="information",message="are you sure to save all the information in document")

        messagebox.askquestion()    
        obj=messagebox.askquestion(title="?",message="Are you employer here?")

        messagebox.askretrycan()
        obj=messagebox.askretrycan(title="oop",message="are you sure or retry it")

        messagebox.askyesno()
        obj=messagebox.askyesno(title="!",message="this is your name?")

        messagebox.askyesnocancel()
        obj==messagebox.askyesnocancel(title="oop",message="are you sure to go forward")

        messagebox.showerror()
        obj=messagebox.showerror(title="oop",message="you can not go forward")

        messagebox.showwarning()
        obj=messagebox.showwarning(title="oop",message="it will destory your document")

        if obj:
            print("it is save")
        else:
            print("it is cancel")
    button=Button(root,text="save",command=show)
    button.pack()

    root.mainloop()

example:

    from tkinter import *
    from tkinter import messagebox
    root=Tk()
    def popup():
        is_ok=messagebox.askokcancel(title="oop",message="Are you sure to save this information in here")
        if is_ok==1:
            Label(root,text="you click it").pack()
        else:
            Label(root,text="you do not click it").pack()

    button=Button(root,text="enter",command=popup).pack()

    if __name__ == '__main__':
        root.mainloop()
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
grid_forget()    #it is use for forget that thing  with its grid come
#your labell or anythng it should be it need to be with grid after it will work
    labell_image=Label(image=pic1)
    labell_image.grid(row=0,column=0,columnspan=3)
        #use to get out of it from program it is use in def mostly
    labell_image.grid_forget()
-----------------------------------------------------------------------------------------
#it is use for disable of the command it means that it should not work
#use for disable the button
    if image_number==5:
        button_forword=Button(root,text=">>",state=DISABLED)
------------------------------
#when function of command need argument to put the argument in parameter of def we will use lambda function
    button_forword=Button(root,text=">>",command=lambda : forward(2))
    #when we want to get argument for parameter of def of command we should use lambda function
    #when drop something in def of command we will do it with lambda function






