#when our program should be big we will make for each part of it Micro service
#Modula : Modules means file in a folder
#Package: It is a collection of Folders in a Folder that each of it has its own files or modules

#__init__.py : file by the name of __init__.py -->>it will run directly the time that you import one of 
# the file or modules of that folder in your main.py even without maintioning of it all the items of it will appear

#Ctr + Space   it will show all the class that you have and other futures
#we can collect all the modules of a folder in file __init__.py after take out it from its folder
example:

First_project    #that is the main Folder
    Top   #it is a Folder (it is internal of main folder)
        go.py  #it is a file in Top folder
            class son:
                def __init__(self,name):
                    self.name=name
                def display(self):
                    print(f" is {self.name}")

        cat.py  #it is a file in Top folder
            class fat:
                def __init__(self,name):
                    self.name=name
                def play(self):
                    print(f"The father name is {self.name}")

        __init__.py    #it is a file in Top folder
            from .go import *
            from .cat import *

main.py    #it is a file in main folder
    from Top import cat,go
    obj1=cat.fat("petter")
    print(obj1.play())
    print(obj1.name)

    obj2=go.son("khan")
    print(obj2.name)
    print(obj2.display())

------------------------------------------------------------------------------------------------------------------
what is means 
if __name__=="__main__":
    pass

cat.py   #it is file

    class father:
        def __init__(self,name):
            self.name=name
        def play(self):
            print(f"The father name is {self.name}")

        
    print("it will appear in your second file") #it will appear in your second file

    def my_function(name):
        print(f"{name} is my name.")

    my_function("Ali") #if  you import file1 in file2 my_function also get appear
    #but
    #when you put your function and anther things internal of if__name__=="__main__": 
    #when you import this file1 into file2 these function and thing will not appear 
    #beacuse it is internal of if __name__=="__main__":
    if __name__=="__main__":
        print("it will appear in your second file")  #it will not appear in file2 beacuse it is internal if if __name__=="__main__":

        def my_function(name):
        print(f"{name} is my name.")
        my_function("Ali")            #it will not appear in file2 beacuse it is internal if if __name__=="__main__":
                                        #but when you run file1 in its file it will get appear

file2   #it is a file
    from cat import father
    object=father("khan")
    print(object.play())
    print(object.name)
>>>the father name is khan
>>>khan          #we only want to appear these two but beacuse we do not take the that print and function internal of __name__=="__main__":
                  #these are also appear 
>>>it will appear in your second file
>>>khan is my name

    from cat import father
    object=father("khan")
    print(object.play())
    print(object.name)
>>>the father name is khan
>>>khan