Modules in python

    Amain.py             #if Amain be name of a file or module
        dict={
                "names":["Anil","Ahmad","Ali","Mohammad"],
                "Workers":["Petter","kiiler"]
            }
        
        def circle(r):
            return 3*r**2

    Access.py         #if Access be name of a file or module
        import Amain
        a=Amain.dict["names"]
        print(a)
        >>>['Anil', 'Ahmad', 'Ali', 'Mohammad']

        b=Amain.circle(5)
        print(f"The area of circle is {b}")
        >>>The area of circle is 75

    note:if we do not clear the veriables,dictionary,list,function...... in class can we access it from anther madula
    yes we can by import the name of it in anther madula
-----------------------------------------------------------------------------------
#if you want to find all the modules that you have 
    print(help("Modules"))

>>>Please wait a moment while I gather a list of all available modules...

test_sqlite3: testing with SQLite version 3.43.1
Amain               _xxinterpchannels   idlelib             reprlib
Coffie Machine      _xxsubinterpreters  idna                requests
Detabase            _zoneinfo           imaplib             rf
Ex                  abc                 imghdr              rgm
G                   agae                importlib           rlcompleter
MySQLdb             aifc                importlib_metadata  rt
__future__          antigravity         importlib_resources runpy
__hello__           argparse            inflect             sched
__phello__          array               inspect             secrets  # it is continues we copy less of it
--------------------------------------------------------------------
#if you want to find the all modules methods with example 
    print(help("Pandas"))
 
 >>> |      Series
     |          A Series that must have the same length as self.
     |
     |      Examples
     |      --------
     |      >>> df = pd.DataFrame({'A': range(3), 'B': range(1, 4)})
     |      >>> df
     |         A  B
     |      0  0  1
     |      1  1  2
     |      2  2  3
     |      >>> df.transform(lambda x: x + 1)
     |         A  B
     |      0  1  2
     |      1  2  3
     |      2  3  4
     |#it is continues we copy less of it
--------------------------------------
print(help("tkinter"))
print(help("turtle"))
print(help("calendar"))
print(help("math"))
print(help("os"))
print(help("time"))  ....   #like that you can find lots of modules and its methods explinition of it and practical usage of it
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import os

#This is show all the attributes and methods of os module
dir()
    example:
    print(dir(os))
    >>>['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping',....

#this method show the cwd (currently working directory) location
os.getcwd()
    example:
    print(os.getcwd())
    >>>C:\Users\MRC\PycharmProjects\Anil class project 123456

#this method use for change the location of directory
os.chdir()
    example:
    os.chdir('C:\\Users\\MRC\\PycharmProjects\\')  #you need to maintion the location where the directory should be
    print(os.getcwd())
    >>>C:\Users\MRC\PycharmProjects

#this method will list all the files and items in this directory
os.listdir()
    example:
    print(os.listdir())
    >>>['20496.jpg', 'Anil class project 123456', 'anil.jpg', 'c.jpg', 'Cities_Kuala_Lumpur_Malaysia.jpg',
     'p.jpg', 'Password Manager', 'wallpaperflare.com_wallpaper (10).jpg']

#this is for create our own files 
os.makedirs("PttPs")
    example:
    print(os.makedirs("PttPs"))
    >>> None       #the file is in a object
    print(os.makedirs())    #this is show the files that create
    >>>['20496.jpg', 'Anil class project 123456', 'anil.jpg', 'Bbb', 'c.jpg', 'Cities_Kuala_Lumpur_Malaysia.jpg', 'p.jpg',
        'Password Manager', 'PttP', 'PttPs', 'tty', 'wallpaperflare.com_wallpaper (10).jpg']
        
#this is use for create file 
os.mkdir()
    example:
    print(os.mkdir("Bbbttt34ttt"))
    >>> None     # file is create in a object
    print(os.listdir())   #it show the files list
    >>>['20496.jpg', 'Anil class project 123456', 'anil.jpg', 'Bbb', 'Bbbttt34ttt', 'Bbbtttttt', 'Bbbtttttts3s', 'Bbbttttttss', 'c.jpg',
     'Cities_Kuala_Lumpur_Malaysia.jpg', 'jjjpps', 'p.jpg', 'Password Manager', 'PttP', 'PttPs', 'tty', 'wallpaperflare.com_wallpaper (10).jpg']

#this is use to delete the file
os.remove()
    example:
    print(os.remove("Cities_Kuala_Lumpur_Malaysia.jpg"))
    print(os.listdir())
    >>>['20496.jpg', 'Anil class project 123456', 'anil.jpg', 'c.jpg', 'kkp', 'OS-demo-2', 'p.jpg', 'Password Manager',
     'ssp', 'wallpaperflare.com_wallpaper (10).jpg']

os.rmdir()
os.removedirs()

#this is use for rename a file 
os.rename()
    example:
    print(os.rename("exersise.py","play.py"))  # th exersise.py change to play.py
    print(os.listdir())
    >>>['.idea', '.venv', 'Amain.py', 'blank_states_img.gif', 'c.jpg', 'colculate.py', 'Detabase.py', 'Ex.py', 'file',
     'forturtle.gif', 'hack.jpg', 'hh.txt', 'n.text', 'play.py', 'setup.py', 'state_to_learn.csv', '__pycache__']

#this is use to get out all information about the file
os.stat()
    example:
    print(os.listdir())
    print(os.stat("Detabase.py"))
    >>>['.idea', '.venv', 'Amain.py', 'blank_states_img.gif', 'c.jpg', 'colculate.py', 'Detabase.py', 'Ex.py', 'file',
     'forturtle.gif', 'hack.jpg', 'hh.txt', 'n.text', 'play.py', 'setup.py', 'state_to_learn.csv', '__pycache__']

     os.stat_result(st_mode=33206, st_ino=3377699720666002, st_dev=16445132599960587046, st_nlink=1, st_uid=0, st_gid=0,
      st_size=16437, st_atime=1725591947, st_mtime=1724845176, st_ctime=1719378202)   # this the all information about the file Database.py
       # show the size of file
      print(os.stat("Detabase.py").st_size)
    
      import os
      from datetime import datetime
``    obj=os.stat("Detabase.py").st_atime
      print(datetime.fromtimestamp(obj))
      >>>2024-09-05 20:05:47.537696

#it will find the directory of each file on that path,dirpath,dirnames,filnames
#it is use for find some files specially the time of create the web application
os.walk()
    example:
    for dirpath,dirnames,filenames in os.walk("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456"):
        print("current path:",dirpath)
        print("directories:",dirnames)
        print("files:",filenames)
        print("  ")
    >>>current path: C:\Users\MRC\PycharmProjects\Anil class project 123456
    directories: ['.idea', '.venv', '__pycache__']
    files: ['Amain.py', 'blank_states_img.gif', 'c.jpg', 'colculate.py', 'Detabase.py', 'Ex.py', 'file', 'forturtle.gif', 'hack.jpg',
     'hh.txt', 'n.text', 'play.py', 'setup.py', 'state_to_learn.csv']
                                                                            #look it inter inidea
    current path: C:\Users\MRC\PycharmProjects\Anil class project 123456\.idea 
    directories: ['inspectionProfiles']
    files: ['.gitignore', 'Anil class project 123456.iml', 'misc.xml', 'modules.xml', 'workspace.xml']
                                                                                        #after inter in inspectionProfiles
    current path: C:\Users\MRC\PycharmProjects\Anil class project 123456\.idea\inspectionProfiles
    directories: []
    files: ['profiles_settings.xml', 'Project_Default.xml'].....

os.environ=#investicate about it

os.path   #it will use with its methods

    #show all the file of os
    print(dir(os.path))
    >>>['_LCMAP_LOWERCASE', '_LCMapStringEx', '_LOCALE_NAME_INVARIANT', '__all__'.......

    #it show basename of this path
    print(os.path.basename("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456"))
    >>>Anil class project 123456
    #it show the directory name
    print(os.path.dirname("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456"))
    >>>C:\Users\MRC\PycharmProjects
    #it show both directory name and basename
    print(os.path.split("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456"))
    >>>('C:\\Users\\MRC\\PycharmProjects', 'Anil class project 123456')
    #if you want to find this path is exit in windows or not
    print(os.path.exists("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456"))
    >>>True
    print(os.path.exists(("c\\users\\thisprogs")))
    >>>False
    #find it file or directory
    print(os.path.isdir("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456"))
    >>>True
    #find it is file or directory
    print(os.path.isfile("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456"))
    >>>False
    #use for split the extantion
    print(os.path.splitext("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456"))
    >>>('C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456', '')

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
CSV Modules

#csv(comma sperate values)
#when we carry or open exceel files in pycharm for read,write,open,close or append it will open in csv files mode

import csv

#it will read the file line by line if we use for loop
csv.reader(file_name)
    example:
    with open("hh.txt") as csv_files:
        csv_reader=csv.reader(csv_files)
        print(csv_reader)
        #it save in a object
        >>><_csv.reader object at 0x00000212B965D4E0>
        
        #if we use for loop it will read line by line
        for line in csv_reader:
            print(line)
        >>>['name', 'last_name', 'email']
            ['Ali', 'Ahmady', 'ali@gmail.com']
            ['Anil', 'Amiri', 'Anil@gmail.com']
            ['Mohammad', 'Mohammady', 'mohammad@gmail.com']
            ['Ahmad', 'khan', 'khan@gmail.com']
        
        #using index
        for line in csv_reader:
            print(line[2])   #index is int
        >>>email
            ali@gmail.com
            Anil@gmail.com
            mohammad@gmail.com
            khan@gmail.com

#use for delete rows 
next(file_name or name_obj_which_file_exit)
    example:
    import csv
    with open("hh.txt") as csv_files:
        csv_reader=csv.reader(csv_files)
        print(csv_reader)
        
        #we use two time next() it delete two rows
        next(csv_reader)
        next(csv_reader)

        for line in csv_reader:
            print(line)
        >>>['Anil', 'Amiri', 'Anil@gmail.com']
            ['Mohammad', 'Mohammady', 'mohammad@gmail.com']
            ['Ahmad', 'khan', 'khan@gmail.com']

csv.writer()
    example:
    import csv
    with open("hh.txt") as csv_files:
        csv_reader=csv.reader(csv_files)

        with open("new_file_name","w") as file_new:
                                                #delimiter change the , to tap and sperate the values
            file_maker=csv.writer(file_new,delimiter="\t")

            for line in csv_reader:
                file_maker.writerow(line)
    >>>name	last_name	email

        Ali	Ahmady	ali@gmail.com

        Anil	Amiri	Anil@gmail.com

        Mohammad	Mohammady	mohammad@gmail.com

        Ahmad	khan	khan@gmail.com

    example:
    with open("new_file_name") as csv_files:
    csv_reader=csv.reader(csv_files,delimiter="/")
    for line in csv_reader:
        print(line)
    >>>['name\tlast_name\temail']
        ['name\tlast_name\temail']
        ['name\tlast_name\temail']
        ['Mohammad\tMohammady\tmohammad@gmail.com']
        ['Ahmad\tkhan\tkhan@gmail.com']

#open file in dictionary mode
csv.DictReader
    example:
    import csv
    with open("hh.txt") as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for line in csv_reader:
            print(line)
    >>>{'name': 'Ali', 'last_name': 'Ahmady', 'email': 'ali@gmail.com'}
        {'name': 'Anil', 'last_name': 'Amiri', 'email': 'Anil@gmail.com'}
        {'name': 'Mohammad', 'last_name': 'Mohammady', 'email': 'mohammad@gmail.com'}
        {'name': 'Ahmad', 'last_name': 'khan', 'email': 'khan@gmail.com'}
    #if we use index 
        for line in csv_reader:
            print(line["email"])  #index is string


csv.DictWriter
    example:
    import csv
    with open("hh.txt") as csv_files:
        csv_reader=csv.DictReader(csv_files)
        with open("new_file_name","w") as new_file:
            file_names=["name","last_name","email"]
            obj=csv.DictWriter(new_file,file_names)
            for line in csv_reader:
                obj.writerow(line)
        #new_file_name file in here open
        >>>Ali,Ahmady,ali@gmail.com

            Anil,Amiri,Anil@gmail.com

            Mohammad,Mohammady,mohammad@gmail.com

            Ahmad,khan,khan@gmail.com
    #here we bring the header of it and delete the email
    import csv
    with open("hh.txt") as csv_files:
        csv_reader=csv.DictReader(csv_files)
        with open("new_file_name","w") as new_file:
            file_names=["name","last_name"]
            obj=csv.DictWriter(new_file,file_names)
            #header
            obj.writeheader()
            for line in csv_reader:
                #delete the header
                del line["email"]
                obj.writerow(line)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Random Module

#take two number int 
randint(a,b)  #a is start number and b is end number   a<=x<=b
    example:
    import random
    a=random.randint(1,90)
    print(a)
    >>>17

                #different between randint and randrange is randint(a<=x<=b) both have aqual but randrange(a<=x<b) bot do not have aqual
#it will take two int number
randrange(a,b)  #a is start number and b is end number    a<=x<b
    example:
    import random
    a=random.randrange(1,3)
    print(a)
    >>>1
    >>>2     #it will not take out 3

#it is also a function with containt floating numbers
random()      #0.0<=x<1.0  which containt 0.0 but not containt 1.0 beacuse it will take lesser than it (0.999999) 
    example:
    import random
    a=random.random()
    print(a)
    >>>0.02256284558594157      #it will take out number between 0.0 and 1.0 but it will not contain 1.0 
    >>>0.02256284558594157

#it will take both int and float number but resuilt is allways float
uniform(a,b)
    example:
    import random
    a=random.uniform(1,5)  #int
    print(a)
    >>>3.0449453481913045
    >>>4.236704759474689

    import random
    a=random.uniform(1.4,5.4)  #float
    print(a
    >>>1.463051959273634
    >>>1.9269746013599023

#it choice from list one thing for from a bandle of somthing it will chioce
choice(list_name or something_else)
    example:
    import random
    a=[1,2,3,4,5,6,7,7,8]
    print(random.choice(a))
    >>>3
    >>>7

#it will change the place of list items randomly
shuffle(name_list or something_else)
    example:
        import random
        a=[1,2,3,4,5,6,7,7,8]
        random.shuffle(a)
        print(a)
        >>>[5, 6, 1, 7, 8, 4, 7, 3, 2]
        >>>[6, 7, 8, 3, 7, 2, 5, 1, 4]


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Math modula

x=3.14
y=-5
z=8
result=round(x)
print(result)
>>>3

x=3.14
y=-5
z=8
result=abs(y)     #abs  |-5|=5
print(result)
>>>5

x=3.14
y=-5
z=8
result=pow(z,2)    #first number (z) is base and second number is power
print(result)

x=3.14
y=-5
z=8
list=[1,2,3,4,5]
result=max(x,y,z)
result2=max((list))
print(result)
print(result2)
>>>8
>>>5

x=3.14
y=-5
z=8
list=[1,2,3,4,5]
result=min(x,y,z)
result2=min((list))
print(result)
print(result2)
>>>-5
>>>1

import math
print(math.pi)
>>>3.141592653589793
print(math.e)
>>>2.718281828459045

import math
x=math.sqrt(5)
print(x)
>>>2.23606797749979

import math
t=9.9
r=6.2
x=math.ceil(t)  #ceil is take out the big number of it
y=math.ceil(r)
print(x)
>>>10
print(y)
>>>7

import math
t=9.9
r=6.2
x=math.floor(t)
y=math.floor(r)
print(x)
>>>9
print(y)
>>>6

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

json modula
#it is use for converting the json string or file  to python and unlike of that
# json(JavaScript Object Notation)
#it is the same like dictionary which has key and value
#it is for data storing 
#perfrom the following translation in decoding by default(1:json=2:python):
    (1:object=2:dict,1:array=2:list,1:string=2:str,1:number(int)=2:int,1:number(real)=2:float,1:true=2:True,1:false=2:False,1:null=2:None)

use for read
    #loads:it will change the json string to python 
    #load: it will change json file to python 
use for write 
    #dumps : it will change the python string to json 
    #dump: it will change the python files to json 
use for update
    #.update()
    

import json
people_string='''
{
    "people":[
        {
            "name":"Anil Amiri",
            "phone":"234-5657-242",
            "email":null,
            "has_license":false
        },
        {
            "name":"Ahmad Khan",
            "phone":"6546-4747-3463",
            "email":["anil7878amiri@gmail.com"],
            "has_license":true
        }
    ]
}
'''
#loads : convert or change the json string to python
#load:  convert or change the json files to python

data=json.loads(people_string)
print(data)
>>>{'people': [{'name': 'Anil Amiri', 'phone': '3456-356-5464', 'email': None, 'has_license': False}, {'name': 'Ahmad Khan',
 'phone': '335-232-554', 'email': ['anilamiri2005@gmail.com'], 'has_license': True}]}

print(type(data))
>>><class 'dict'>

print(type(data["people"]))
>>><class 'list'>

for i in data["people"]:
    print(i)
>>>{'name': 'Anil Amiri', 'phone': '3456-356-5464', 'email': None, 'has_license': False}
{'name': 'Ahmad Khan', 'phone': '335-232-554', 'email': ['anilamiri2005@gmail.com'], 'has_license': True}

    print(i["name"])
>>>Anil Amiri
    Ahmad Khan
-----------------------------------------------------
#data=json.loads(people_string)

#dumps:  it will change the python string to json string
#dump:   it will change the python files to json files

#convert or change python to json
convert_to_json=json.dumps(data)
print(convert_to_json)  #                                 #it is change from python to json
>>>{"people": [{"name": "Anil Amiri", "phone": "3456-356-5464", "email": null, "has_license": false}, 
{"name": "Ahmad Khan", "phone": "335-232-554", "email": ["anilamiri2005@gmail.com"], "has_license": true}]}


convert_to_json=json.dumps(data,indent=2)  #we can change the indent to 1,2,3,4.....
print(convert_to_json)
>>>{
  "people": [
    {
      "name": "Anil Amiri",
      "phone": "3456-356-5464",
      "email": null,
      "has_license": false
    },
    {
      "name": "Ahmad Khan",
      "phone": "335-232-554",
      "email": [
        "anilamiri2005@gmail.com"
      ],
      "has_license": true
    }
  ]
}

convert_to_json=json.dumps(data,indent=2,sort_keys=True)
print(convert_to_json)
>>>{
  "people": [
    {
      "email": [
        "aniri2005@gmail.com"   #it will bring the important things at the beginning 
      ],                        #like email that is important it come at the beginning 
      "has_license": false,
      "name": "Anil Amiri",
      "phone": "3456-356-5464"
    },
    {
      "email": [
        "anilamiri2005@gmail.com"
      ],
      "has_license": true,
      "name": "Ahmad Khan",
      "phone": "335-232-554"
    }
  ]
}

-----------------------------------------------------------

data=json.loads(people_string)
for person in data["people"]:
    del person["phone"]
    del person["email"]       #it will delete the phone and email
>>>{'name': 'Anil Amiri', 'has_license': False}
   {'name': 'Ahmad Khan', 'has_license': True}


convert_to_json=json.dumps(data)
print(convert_to_json)    
>>>{"people": [{"name": "Anil Amiri", "has_license": false}, {"name": "Ahmad Khan", "has_license": true}]}
-------------------------------------------------------------------------------------

#if we change the json file in python we will use load()
file_name_json       #this information if internal of file of json because of example
        {
        "states":[
                {
                    "name":"Alabama",
                    "abbreviation":"AL",
                    "area_codes":["205","251","356"]
                },
                {
                    "name":"Alaska",
                    "abbreviation":"Al",
                    "area_codes":["907"]
                }
            ]
        }
--------------

import json
with open("file_name_json") as data:
    show=json.load(data)
for json_file in show["states"]:
    print(json_file)

>>>{'name': 'Alabama', 'abbreviation': 'AL', 'area_codes': ['205', '251', '356']}
   {'name': 'Alaska', 'abbreviation': 'Al', 'area_codes': ['907']}

for json_file in show["states"]:
    print(json_file["name"],json_file["abbreviation"])
>>>Alabama AL
   Alaska Al


import json
with open("new_file_name") as data:
    show=json.load(data)
for i in show["states"]:
    del i["name"]
    print(i)
>>>{'abbreviation': 'AL', 'area_codes': ['205', '251', '356']}
   {'abbreviation': 'Al', 'area_codes': ['907']}



import json
with open("new_file_name") as data:
    show=json.load(data)
for i in show["states"]:
    del i["name"]
                        #it will change the json file to python file 
with open("file_man","w") as sh:
    json.dump(show,sh,indent=2)

>>>in internal of file_man  #this file create new
{
"states":[
        {
            "name":"Alabama",
            "abbreviation":"AL",
            "area_codes":["205","251","356"]
        },
        {
            "name":"Alaska",
            "abbreviation":"Al",
            "area_codes":["907"]
        }
    ]
}


.update()

    



\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
time modules
#it will take out the sec since the epoch
#return the number of seconds
time.time()

    example:
    import time
    a=time.time()
    print(a)
    >>>1726484027.5616076

#change the the sec since from epoch to now time
#return the current date and time
time.ctime(optioanl[float])

    b=time.ctime(1726483937.595566)
    print(b)
    >>>Mon Sep 16 03:52:17 2024

#it will show the local time
#return the date and time in time.struct_time format
time.localtime()
    import time
    a=time.localtime()
    print(a)
    >>>time.struct_time(tm_year=2024, tm_mon=9, tm_mday=16, tm_hour=4, tm_min=12, tm_sec=1, tm_wday=0, tm_yday=260, tm_isdst=1)

#you put the local time it take out the sec of it
#return the second passed since epoch pas output
time.mktime(t)
    import time
    a=time.localtime()
    b=time.mktime(a)
    print(b)
    >>>1726485301.0
#return a string representing the same
time.asctime()
    print(time.asctime())
    >>>Mon Sep 16 04:22:25 2024

    import time
    a=time.localtime()
    print(time.asctime(a))
    >>>Mon Sep 16 04:22:25 2024

time.strftime()
    import time
    a=time.strftime("%d/%m/%y")
    print(a)
    >>>16/09/24

    import time
    a=time.strftime("/%m/%y")
    print(a)
    >>>/09/24

#it will change the string to time.struct_time
time.strptime()
    import time
    a="12 August 2024"
    print(time.strptime(a,"%d %B %Y"))
    >>>time.struct_time(tm_year=2024, tm_mon=8, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=225, tm_isdst=-1)

datetime.datetime()
    import datetime
    a=datetime.datetime(2024,7,12,4,53,59)
    print(a)
    >>>2024-07-12 04:53:59

datetime.datetime.today()
    import datetime
    a=datetime.datetime.today()
    print(a)
    >>>2024-09-16 06:17:38.582832

datetime.datetime.now()
    import datetime
    a=datetime.datetime.now()
    print(a)
    >>>2024-09-16 06:19:33.885504
    print(a.year)
    >>>2024
    print(a.month)
    >>>9

datetime.time()
    import datetime
    a=datetime.time(3,6,45)
    print(a)
    >>>03:06:45

datetime.timedelta()
    import datetime
    a=datetime.timedelta(days=60)
    b=datetime.timedelta(days=40)
    c=a-b
    print(c)
    >>>20 days, 0:00:00
    print(type(c))
    >>>  <class 'datetime.timedelta'>
#it wil show the week as will as
    import datetime
    a=datetime.datetime.now()
    print(a.weekday())

















