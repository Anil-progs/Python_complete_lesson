Thread:
#we wana use threads for speed and excute our program concurrently
#Thread: part of a process

start(): begin th execution of new thread or process
join(): wait for a thread or process to complete

_thread

#is a module of python for thread but it is low level(means it hard to work with it, it has weak methods)
#it has less error handling
#it is deffecult for synchronization

import _thread
def function_of_thread(paramiter):
    real code
_thread.start_new_thread(function_of_thread,(arguments)).start()
while 1:
    pass


example:
    _thread

    import _thread
    import time

    def print_thread(text,dalay):
        count=0
        while count<3:
            time.sleep(dalay)
            count+=1
            print(f"you done thread   :  {count}: {text}")

    try:
        #in here you spawn the thread                #this will write after 1 sec 
        _thread.start_new_thread(print_thread,("yes",1)).start()
                                    #instance,function     #arguments                    
        _thread.start_new_thread(print_thread,("No",2)).start() #this will write after 2 sec 
    except:
        print("please check your code some place is range")

    while 1: #we need to take this beacuse if it is not exit it will not work
        pass
------------------------------------------------------------------------

import time

done=False
def work():
    count=0
    while not done:
        time.sleep(2)
        count+=1
        print("you get it",count)

work()
#it will not ask from input beacuse only it will run the program
#what is solution using thread

input("inter it will stop")
done=True
-------------------------
 threading
#it is module of python for threading and it has more methods for use
#error handling is easy with this
#synchronization is easy with it like method of it (locks,semaphore,event)
#it is use for multithreading in larger application 

import threading
def function_of_thread(paramiter):
    real code
threading.Thread(target=function_of_thread,args=(arguments)).start()

or 

t1=threading.Thread(target=function_of_thread,args=(arguments))
t2=threading.Thread(target=function_of_thread,args=(arguments))

t1.start()
t2.start()

t1.join()
t2.join()


example:
import threading
import time

def task(name,lock):
    print(f"Thread {name} starting")

    with lock:
        for i in range(3):
            print(f"Thread {name} working...")
            time.sleep(1)
        print(f"Thread {name} finished")
lock=threading.Lock()
t1=threading.Thread(target=task,args=("A",lock))
t2=threading.Thread(target=task,args=("B",lock))

t2.daemon=True

t1.start()
t2.start()

t1.join()
print("Thread A has complete")
---------------------------------------------------------------------------------
using ThreadPoolExecutor from concurrent.futures
#it will make the thread easy and have more methods for it,it is super poorfull for Thread in our program
#let you specify the number of thread in pool 

#structures:
from concurrent.futures import ThreadPoolExecutor
def function_of_thread(paramiter):
    real code

with concurrent.futures.ThreadPoolExecutor() as execute:
    execute.submit(function_of_thread,arguments)

with concurrent.futures.ThreadPoolExecutor(max_workers=1,2,3...) as execute:
     execute.submit(function_of_thread,arguments)


#mthod:
submit()   #it is for execute Thread

from concurrent.futures import ThreadPoolExecutor
def task(n):
    return n*n

with ThreadPoolExecutor(max_workers=5) as ex:
    futures=[ex.submit(task,i) for i in range(10)]
            #if you don't take .result() the address of it in object will get out
    result=[f.result() for f in futures]
print(result)

#method:
map()         #map will apply function in all items of list speratly
               #if you have list of items that you want to apply thread function on all of it use map()
               #generally if you have list of items you want to Thread on them use from map()
from concurrent.futures import ThreadPoolExecutor
def square(n):
    return n*n

numbers=[23,12,9,6]

with ThreadPoolExecutor() as ex:
    result=list(ex.map(square,number))
    print(result)

import time
import threading
from concurrent.futures import ThreadPoolExecutor
class counter:
    def __init__(self):
        self.value=0
        self.lock=threading.Lock()
    def update(self,name,dalay):
        print(f"you update {name}")
        self.lock.acquire()   #when one of it inter,it will lock the door
        val=self.value
        val+=1
        self.value=val
        time.sleep(dalay)
        self.lock.release()   #here it will open the door that anther thread inter
        print(f"download the matter{name}")
object=counter()
list=["Ali","Ahmad","Mohammad"]
list_num=[1,1,1]
with ThreadPoolExecutor(max_workers=3) as ex:
    ex.map(object.update,list,list_num)
    ex.shutdown(wait=True)
print(object.value)




#method:
shutdown()    #shutdown(wait=True) wait for all the submitted tasks to complete before shutting down       
               #with wait=True it ensures all running tasks finish before clean up
from concurrent.futures import ThreadPoolExecutor 
import time
def sleep_task(seconds):
    print(f"sleep for {second} seconds")
    time.sleep(second)
    print(f"{seconds}")

with ThreadPoolExecutor() as ex:
    futures=[ex.submit(sleep_task,sec) for sec in [1,2,3]]
     #using of shutdown()
    ex.shutdown(wait=True)
print("All the process finish we will shutdown the application")



example: 

from concurrent.futures import ThreadPoolExecutor
import time

def f(n,times):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        num=1
        for i in range(1,n+1):
            num*=i
            time.sleep(times)
            print(num)
n=int(input("Enter to find fibonance of number: "))

                      #max_workers=it will show the number of your threads
                      #max_workers: The maximum number of threads that can be used to execute the given calls
with ThreadPoolExecutor(max_workers=3) as execute:     #if max_workers=1( it means that only one worker thread or
                                                                          # process will be allowed to run at any given time)
    execute.submit(f,n,1)                               #if max_workers=2(it means that two worker thread or
    execute.submit(f, n,1)                                                  #process will be allowed to run at any given time)
    execute.submit(f, n, 1)

print("The process done")
--------------------------------------------------------------------------------------------------------------------------

GIL:(global interpreter lock)
#python beacuse of GIL can not use from more threading and excute more threads in one time
#it will let only one Thread to excute in one time
#in python instade of multithreading , we will use from multi processing
#Resource Sharing: As we know that threads can share the memory of global variable. So,
# operation perform by a thread can cause problems to other threads.

import threading
import time

done=False
def work(text,dalay):
    count=0
    while not done:
        time.sleep(dalay)
        count+=1
        print(f"{text}:{count}")

t1=threading.Thread(target=work,args=("this is right",1),daemon=True)
t2=threading.Thread(target=work,args=("tell me ",2),daemon=True)

t1.start()
t2.start()

t1.join()
t2.join()

input("inter to end the program: ")
done=True
------------------------------------------------------------------------------------------------------------------------------------------
different between multi threading and multi processess

>>>Thread will get less memory than process
>>>To many thread will take one part os memory internal of process but each process will take it own memory and thwy will not share 
their memory for each other
>>>multi threading is limites due to GIL(global interperter lock) but multi process achieves true parallelisem

----------------------------------------------------------------------------------------------------------
Thread Synchronizition Using Lock

import time
import threading
from concurrent.futures import ThreadPoolExecutor
class counter:
    def __init__(self):
        self.value=0
        self.lock=threading.Lock()
    def update(self,name,dalay):
        print(f"you update {name}")
        self.lock.acquire()   #when one of it inter,it will lock the door
        val=self.value
        val+=1
        self.value=val
        time.sleep(dalay)
        self.lock.release()   #here it will open the door that anther thread inter
        print(f"download the matter{name}")
object=counter()

with ThreadPoolExecutor(max_workers=3) as ex:
    ex.submit(object.update,"Ali",1)
    ex.submit(object.update,"Mohammad khan",1)
    ex.submit(object.update, "khan", 1)
print(object.value)





Multi processess

from multiprocessing import Process,current_process

def square(number):
    process_name=current_process().name
    print(f"{process_name} calculate the square of {number}")
    result=number*number
    print(f"{process_name} result={result}")
if __name__=="__main__":
    list_number=[1,2,3,4,5]
    list_process=[]
    for num in list_number:
        process_of=Process(target=square,args=(num,)) #beacuse the tuple get one item use ,
        list_process.append(process_of)

    for process_in in list_process:
        process_in.start()

    for process_in in list_process:
        process_in.join()

    print("The process is done")
