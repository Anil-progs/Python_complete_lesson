from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Anil Application")
root.iconbitmap("logo.png")  #icon
#put image
my_image=ImageTk.PhotoImage(Image.open("logo.png"))
my_lebell=Label(image=my_image)
my_lebell.pack()
#in tkinter we need to do three things
#1:we need to defind
#2:we need to put it in something else
#3:we need to put it or show it in project

Exit_button=Button(root,text="Exit",command=root.destroy)
Exit_button.pack()

Exit_button=Button(root,text="Exit",command=root.quit)
Exit_button.pack()

text=Text(root,width=50,height=10)
text.focus()
text.pack()
text.insert(END,"this is the play game")
print(text.get("1.0",END))

frame=Frame(root,bg="white")
frame.pack_propagate(False)
frame.configure(width=100,height=100)
frame.pack()

root.mainloop()

----------------------------------------------------------------------------------------------------------------------------------------
Build a image viewer Application

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("400x400")
root.iconbitmap("logo.png")  # iconpic1 = ImageTk.PhotoImage(Image.open("anil.JPG"))
pic1 = ImageTk.PhotoImage(Image.open("pic1.png"))
pic2 = ImageTk.PhotoImage(Image.open("pic2.png"))
pic3 = ImageTk.PhotoImage(Image.open("pic3.png"))
pic4 = ImageTk.PhotoImage(Image.open("pic4.png"))
pic5 = ImageTk.PhotoImage(Image.open("pic5.png"))
pic6 = ImageTk.PhotoImage(Image.open("pic6.png"))

list_pic=[pic1,pic2,pic3,pic4,pic5,pic6]
                          #0
labell_image=Label(image=pic1)
labell_image.grid(row=0,column=0,columnspan=3)
                 #2
                 #3
def forward(image_number):
    #we make all of it global beacuse of this that put relation between local scope and global scope to a chieve the buttons and labels
    global button_forword
    global button_back
    global labell_image
    #grid_forget in here use for this reason to delete the provius photo because photo can not come on photo
    labell_image.grid_forget()           #2-1=1
                                         #3-1=2
    labell_image=Label(image=list_pic[image_number-1])
    labell_image.grid(row=0, column=0, columnspan=3)
#here we update the argument to show the next label of photo
                                                                 #2+1=3
                                                                 #3+1=4
    button_forword=Button(root,text=">>",command=lambda : forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda : back(image_number-1))

    #here you can update the number of pictures
    statues=Label(root,text="This is Anil pic from "+ str(image_number)+" to" + str(len(list_pic)),bd=1,releif=SUNKEY,anchor=E )
    statues.grid(row=2,column=0,columnspan=3,sticky=W+E)

    if image_number==5:
        button_forword=Button(root,text=">>",state=DISABLED)

    button_forword.grid(row=1, column=0)
    button_back.grid(row=1, column=2)

            #5
            #4
            #3
def back(image_number):
    global button_forword
    global button_back
    global labell_image
    labell_image.grid_forget()          #5-1=4
                                        #4-1=3
                                        #3-1=2
    labell_image=Label(image=list_pic[image_number-1])
    labell_image.grid(row=0, column=0, columnspan=3)
    button_forword=Button(root,text=">>",command=lambda : forward(image_number+1))
                                                              #5-1=4
                                                              #4-1=3
                                                              #3-1=2
    button_back=Button(root,text="<<",command=lambda : back(image_number-1))

    
    #here you can update the number of pictures
    statues=Label(root,text="This is Anil pic from "+ str(image_number)+" to" + str(len(list_pic)),bd=1,releif=SUNKEY,anchor=E )
    statues.grid(row=2,column=0,columnspan=3,sticky=W+E)

    if image_number==0:                  #here the button will not work
        button_back=Button(root,text="<<",state=DISABLED)

    button_forword.grid(row=1, column=0)
    button_back.grid(row=1, column=2)

#when function of command need argument to put the argument in parameter of def we will use lambda function
button_forword = Button(text=">>",command=lambda:forward(2))
button_forword.grid(row=1, column=0)

button_back = Button(text="<<",command=back)
button_back.grid(row=1, column=2)

button_exit = Button(text="Exit",command=root.quit)
button_exit.grid(row=1, column=1,pady=10)

#relief=SUNKEY    :  it will put these text in SUNKEY and get four side of it boarder
#sticky=N or sticky=W  or sticky=E,S   or sticky=W+E   pr  sticky=S+N
#anchor=E,W,N,S    it will show the postion of its text by anchor=E,W,N,S

statues=Label(root,text="This is Anil pic from 1 to" + str(len(list_pic)),bd=1,releif=SUNKEY,anchor=E )
statues.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
----------------------------------------------------------------------------------------------------------------------------------------------

Add frame to your programe

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
---------------------------------------------------------------------------------------------------------------------------------------------
Radiobutton with tkinter

from tkinter import *
root=Tk()
p=IntVar()

def show(value):
    labell=Label(root,text=value)
    labell.pack()

radiobutton1=Radiobutton(root,text="class 1",variable=p,value=1,command=lambda:show(p.get()))
radiobutton2=Radiobutton(root,text="class 2",variable=p,value=2,command=lambda:show(p.get()))
radiobutton3=Radiobutton(root,text="class 3",variable=p,value=3,command=lambda:show(p.get()))
radiobutton4=Radiobutton(root,text="class 4",variable=p,value=4,comand=lambda:show(p.get()))

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

labell=Label(root,text=p.get())
labell.pack()
#if we use pack to them all the number will get out to the back of each other 
#if we use place or grid first will delete and the second will come 

button=Button(root,text="Choose",command=lambda:show(p.get()))

1:button and radiobuttons will take the value of p after this the value will go as value of show(Value)
2:if button click the button will do up work and if radiobutton check that radiobutton will do up work deos not matter which button or radiobutton

root.mainloop()
--------------

from tkinter import *
root=Tk()
list_food=[
    ("pizza","pizza"),
    ("bolani","bolani"),
    ("been","benn")
]

def show(value):
    labell=Label(root,text=value)
    labell.pack()

p=StringVar()
p.set("none")
for text,mode in list_food:
    radiobutton=Radiobutton(root,text=text,variable=p,value=mode)
    radiobutton.pack(anchor=W)

labell=Label(root,text=p.get())
labell.pack()

button=Button(root,text="Choose",command=lambda:show(p.get()))
button.pack()

root.mainloop()
--------------------------------------------------------------------------------------------------------------------------------------------
Messagebox with tkinter
example:
    from tkinter import *
    from tkinter import messagebox
    root=Tk()
    def popup():
        is_ok=messagebox.askokcancel(title="oop",message="Are you sure to save this information in here")

        if is_ok:      #it will take out 1 if yes press
            Label(root,text=is_ok).pack()
        else:          #it will take out 0 if no press
            Label(root,text=is_ok).pack()

    button=Button(root,text="enter",command=popup).pack()

    if __name__ == '__main__':
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

----------------------------------------------------------------------------------------------------------------------------------------------

Create new window using Toplevel()

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
        labell_image.pack()     #if we use top.quit it will quit both the main window and Toplevel window
                                #if we use top.destroy it will only destroy the Toplevel window not main window
        button_exit=Button(top,text="Close",command=top.destroy)

    button=Button(root,text="open new window",command=my_function)
    
    root.mainloop()

-------------------------------------------------------------------------------------------------------------------------------------------
Checkbutton using tkinter


from tkinter import *
root=Tk()
def show():
    Label(root,text=var.ge()).pack()
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

-------------------------------------------------------------------------------------------------------------------------------------------

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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
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

--------------------------------------------------------------------------------------------------------------------------------------------

Building_Out_The_GUI_for_our_Database_App_-_Python_Tkinter_GUI_Tutorial_#20(360p)

Delete_A_Record_From_Our_Database_-_Python_Tkinter_GUI_Tutorial_#21(360p)

from tkinter import *
from typing import List, Tuple

import mysql.connector as data
class database(Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("500x500")
        self.list=["name","last_name","address","city","state","Zipcode","id"]
        self.postion=[10,30,60,80,100,130,160]
        for item in range(len(self.list)):
            labell=Label(self,text=self.list[item],bg="black",fg="white")
            labell.place(x=100,y=self.postion[item])

        self.entry_n=Entry(self)
        self.entry_n.place(x=200,y=10)

        self.entry_l=Entry(self)
        self.entry_l.place(x=200,y=30)

        self.entry_a=Entry(self)
        self.entry_a.place(x=200,y=60)

        self.entry_c=Entry(self)
        self.entry_c.place(x=200,y=80)

        
        self.entry_s=Entry(self)
        self.entry_s.place(x=200,y=100)

        self.entry_z=Entry(self)
        self.entry_z.place(x=200,y=130)

        self.entry_id=Entry(self)
        self.entry_id.place(x=200,y=150)

        self.button=Button(self,text="Upload to database",command=self.select)
        self.button.place(x=200,y=170)

        self.button_get = Button(self, text="Get from database",command=self.show)
        self.button_get.place(x=200,y=200)

    # noinspection PyTypeChecker
    def select(self):
        m=self.entry_id.get()
        n=self.entry_n.get()
        l=self.entry_l.get()
        a=self.entry_a.get()
        c=self.entry_c.get()
        s=self.entry_s.get()
        z=self.entry_z.get()
        db_insert = "insert into moon(moonID,name,last,address,city,state,zipcode) values (%s,%s,%s,%s,%s,%s,%s)"
        db_l=[(m,n,l,a,c,s,z)]
        mydb=data.connect(
            host="Localhost",
            user="root",
            password="1998",
            database="code"
        )
        db_cursor = mydb.cursor()
        db_cursor.executemany(db_insert,db_l)
        mydb.commit()
        mydb.close()

        self.entry_n.delete(0,END)
        self.entry_l.delete(0,END)
        self.entry_a.delete(0,END)
        self.entry_c.delete(0,END)
        self.entry_s.delete(0,END)
        self.entry_z.delete(0,END)
        self.entry_id.delete(0,END)

    def show(self):
        mydb=data.connect(
            host="Localhost",
            user="root",
            password="1998",
            database="code"
        )
        db_cursor = mydb.cursor()
        db_cursor.execute("select * from moon")
        a=db_cursor.fetchall()
        print_record=""
        #it will take out all information each person in new line
        for i in a:
            print(i)
            print_record += str(i) + "\n"
        labell_show = Label(self, text=(print_record))
        labell_show.place(x=200, y=240)
        # this is will take out the first person all information
        for i in a[0]:
            print_record += str(i) + "\n"
        labell_show = Label(self, text=(print_record))
        labell_show.place(x=200, y=260)

        #it will only take out the primary key of them means ID
        for i in a:
        print_record+=str(i[0]) +"  " + str(i[1])+"\n"
        labell_show=Label(self,text=(print_record))
        labell_show.place(x=1,y=240)

#Delete_A_Record_From_Our_Database_-_Python_Tkinter_GUI_Tutorial_#21(360p)

    #here when you put the id it will delete it for you
    def delete_person(self):
        mydb = data.connect(
            host="Localhost",
            user="root",
            password="1998",
            database="code"
        )
        db_cursor = mydb.cursor()
        db_cursor.execute("delete from moon where moonID="+self.entry_delete.get())
        mydb.commit()
        mydb.close()

if __name__=="__main__":
    obj=database()
    obj.mainloop()
--------------------------------------------------------------------------------------------------------------------------------------------
Loading program

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

---------------------------------------------------------------------------------------------------------------------------------------------

Dropdown_Menus_With_TKinter_-_Python_Tkinter_GUI_Tutorial_#18(360p)

from tkinter import *
root=Tk()
list=["class1","class2","class3","class4"]
var=StringVar()
var.set(list[0])
#if we put list instead of values we need to take * before the value
option_menu=OptionMenu(root,var,*list)
option_menu.pack()

def show():
    labell=Label(root,text=var.get())
    labell.pack()

button=Button(root,text="Get values",command=show)
root.mainloop()


from tkinter import *
from tkinter import *
class Menue_bar():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.list=["english","math","pashto","france"]
        self.p=StringVar()
        self.p.set(self.list[0])
        self.menue_bar=OptionMenu(self.root,self.p,*self.list)
        self.menue_bar.pack()
        self.label=(Label(self.root,text=""))
        self.label.pack()
        self.button=Button(self.root,text="Get it",command=self.show)
        self.button.place(x=2,y=10)
        self.root.mainloop()
    def show(self):
        self.label.config(text=self.p.get())
if __name__=="__main__":
    Menue_bar()
----------------------------------------------------------------------------------------------------------------------------------------------

Delete, Enter and show the datas from Database
accurding of object orainted

from tkinter import *
import mysql.connector as myconn
class Menue_bar():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.entry=Entry(self.root)
        self.entry.pack()

        self.button=Button(self.root,text="Select",command=self.insert)
        self.button.pack()
        self.button1=Button(self.root,text="show",command=self.show_info)
        self.button1.pack()
        self.button2=Button(self.root,text="delete",command=self.delete)
        self.button2.pack()
        self.root.mainloop()
    def insert(self):
        id=self.entry.get()
        b="insert into n(nID,name) values (%s,%s)"
        v=(id,"Ahmad")
        mydb = myconn.connect(
            host="Localhost",
            user="root",
            password="1998",
            database="h"  # clear the database
        )
        db_cursor = mydb.cursor()
        db_cursor.execute(b,v)
        mydb.commit()
        self.entry.delete(0,END)

    def delete(self):
        s=self.entry.get()
        mydb = myconn.connect(
            host="Localhost",
            user="root",
            password="1998",
            database="h"  # clear the database
        )
        db_cursor = mydb.cursor()
        db_cursor.execute(f"delete from n where nID="+s)
        mydb.commit()
        self.entry.delete(0, END)

    def show_info(self):
        mydb = myconn.connect(
            host="Localhost",
            user="root",
            password="1998",
            database="h"  # clear the database
        )
        db_cursor = mydb.cursor()
        db_cursor.execute("select * from n")
        y=db_cursor.fetchall()
        print_all=""
        for i in y:
            print_all+=str(i[0])+"  "+str(i[1])+"\n"
        labell=Label(self.root,text=print_all)
        labell.place(x=50,y=200)

    def edit(self):
        top=Toplevel(self.root)
        top.title("Update name")
        top.geometry("200x200")
        entry_update=Entry(top)
        entry_update.pack()
        entry_update_name=Entry(top)
        entry_update_name.pack()
if __name__=="__main__":
    Menue_bar()
----------------------------------------------------------------------------------------------------------------------------------------------
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











