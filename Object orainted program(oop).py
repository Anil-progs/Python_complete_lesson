Object Oriented Programming(OOP)

#It is a procedural (have complexity in itself) programming
# To solve or create a complex or complicated program we will do it by using object oriened program(oop)
# For solve or create a complex program we need to slice or split or cut the program into small peicesses and tacal or solve each of it one by one
# Example:
#       To create a electronical car we need to slice the program into small peicesses 
            #1 Cammera checker 
            #2 Map checker
            ## Line checker
            #4 Fual checker or charging checker.....

        #after we will code or solve each small peicesses in to modules and each part code should be reusable  
#Example:
       #when you have a restorant only you can not do all the japs by yourself like you can not be a waiters,receiptiones,cleaner.... in one time
       #but we can use from OOP to take each jap for each person to do it(it means that we will splite the japs of restorant into small peicesses
       #each one should do their jap)

#A collection of objects is termed as class in oops concept.every class has its own unique and distinguishable attrubutes and methods

--------------------------------
object
#object: is genaral we can say for everything object
#Anything that has state or variable or attributes and behavior or methods or function can be termed as an object, be it physical or logical
#combination of attributes and methods is called OOP
#attribtes ---> has (what it has)
    _is_holding_plate=True
    _tables_responsible=[12,343,46]
#methods or function ---->(what it deos)
    def take_order(table,order):
        #take order to chef
    def take_payment(amount):
        #add money to restaurant 

#from the object we can access attributes and methods 
    class access():
        def __init__(self):
            self.name="Ahmad"  #attribute
        def function(self):     #method
            print(f"{self.name}")
    object=access()
    object.name
    object.function()
#why we put class in object:
from tkinter import *
root=Tk()
    #Imagen you travel to Japan,your clod get durty, you also don't know the langauge,you don't know that where is the laundry shop for this 
    #reason you will take your clods for waiter to clean it for you the waiter will do all the japs for this reason we will put the TK() class 
    #into object after accurding object we will accuss to methods
---------------------------------------------------------------------------------------------------
different between object and instance
object: is genaral we can say for everything object
instance: is the object of class 
we can say for instance object but we can not say for each object instance

class math:
    def __init__(self,n,m):
        self.n=n
        self.m=m  #instance attributes(beacuse we can accuess them from instance)

    def play(self):  #istance methods(we can access them from instance)
        print(self.n*self.m)
show=math(1,2)   #show in here is instance
#but object we can say for all of it
-------------------------------------------------------------------------------------------------
class 
#class are those codes which is made my anther programmer that we can use them in our program and class has methods and attriutes



instance attributes,class attributes,instance methods,class methods,static methods

#Class attributes are the variables defined directly in the class outside constructor and
# shared by all objects of the class.

#Instance attributes are attributes or properties attached to an instance of a class,
#instance attributes are defined in the constructor using self parameter.

#Class attribute can be accessed using class name or object name with dot notation

#Instance Method: The instance method acts on an object’s attributes.
# It can modify the object state by changing value of instance variables

#Class Method: Class method used to access or modify the class state by changing value of the class
# variable that would apply across all the class objects.

#Static Method: This method don’t have access to instance attributes or class attributes.
# It is a general utility that a perform task in isolation.


class company:
    first_emp="Ahmad khan"  #class attrubites

    #constructor or initiolizer
    def __init__(self,second_emp,third_emp):
        self.second_emp=second_emp
        self.third_emp=third_emp    #instance attributes
        self.defult="This is called defult value"

    #instance methods
    def my_first_company(self,you):
        return f"first emp={self.first_emp},second_emp={self.second_emp},name={you},{company.first_emp}"
    @classmethod
    def my_sencond_company(cls,last): #in class method we can access the class attributes and change it
        a=cls.first_emp=last          # but we can not access instance attributes
        print(a)
    @staticmethod
    def my_third_company(jap,oop):
        #company.first_emp="anil khan"
        return f"{jap,oop}"

show=company("ali",'khan')
print(show.second_emp," ",show.third_emp)
print(show.my_third_company("engineer","hhopssf"))
print(show.my_sencond_company("ghani"))
print(show.my_third_company("teacher","56789"))


what is instance or object


#new infomation about super().
class company:
    def info_company(self):
        return "this is TC company"
class organization(company):
    def info_organization(self):
        take=super().info_company()
        print("this is TC orginization",take)

show=organization()
print(show.info_organization())


#Abstraction is use to hide internal functionality of function
# from the user, user can only interact with the basic implementation 
#of the function, inner working is hidden.
#Abstraction is used to reduce the complexity. It also enhances the application efficiency.
#In python abstraction can be achieved using abstract classes and interfaces
----------------------------------------------------------------------------------------------------------------------------

in my idology what is abstraction

#when in base class we abstract a method of it ,it means we hide its functionality from programmers, beacuse the class is also abstract
# we can not accuess directly to attributes, we can achieve its attributes from anther class when we inherites abstract class 

from abc import ABC, abstractmethod
class Father(ABC):
    def __init__(self,height,weight):
        self.weight=weight
        self.height=height
    
    @abstractmehtod
    def dad(self):  #we abstract it that programmers should not see functionality of it
        pass

class son(Father):
    def __init__(self,height,weight,habit):   #we can acuess to attibutes of it, when we inherited
        super().__init__(height,weight)
        self.habit=habit
    
    def dad(self):     #we make with the saim name a method that create a new functionality for it
        return f" height={self.height},weight={self.weight}"

show=son(170,175,"creativity")
print(show.weight)
print(show.dad())       
------------------------------------------------------------------------------------------------

what is Encapsulation

Encapsulation= Data hiding +  abstraction

data hiding:
    public
    proteted
    privide

class student:
    def __init__(self,name,last,age):
        self.name=name
        self._last=last  #protected
        self.__age=age  #privide
    
    def _first_info(self):  #proteted
        return f" name={self.name},last={self._last},age={self.__age}"

    def __second_info(self):
        return f"name={self.name},last={self.last},age={self.__age}"

    def solution_for_privide(self):
        return f"{self.__second_info()},age={self.age}"

show=student("Ali","Mohammad",12)
print(show.last)
print(show._first_info())

print(show.__second_info()) #take Error

solution for privide
print(show.solution_for_privide())
or
print(show._student__age)
print(show._student__second_info())
