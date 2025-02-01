Multithreading Artitectures
1:How user-Level thread mapped to karnal-level threads
--------------------------------------------------------------------------------------------------------------------
There are three main type of Threading Modules
1: One to one (OS creates a karnal threads for each user thread)
    #Both _thread and threading modules if from one to one model
    #Better concurrency
    #True Parallelism

    #Alarge number of threads
    #Limited by the number of karnal threads supported by OS

import threading
import time
done=False
def print_text(text,dalay):
    global done
    while not False:
        time.sleep(dalay)
        print(f"Example of {text}")

threading.Thread(target=print_text,args=("Mathimatic",1),daemon=True).start()

input("Enter to stop: ")
done=True
--------------------------------------------------------------------------------------------------------------------

2:Many to one(Multi user thread mapped to a single karnal thread)  
    #The management of thread will handle by user-level library
    #only one thread of them can access the karnal

    #limit concurrency
    #can not fully utilize multi-core processess
    #some simpler thread libraries implement this model

import asyncio
async def print_number(name):
    for i in range(1,6):
        print(f"Task {name}-number {i}")
        await asyncio.sleep(1)
async def main():
    task1=asyncio.create_task(print_number("Task-1"))
    task2=asyncio.create_task(print_number("Task-2"))
    task3=asyncio.create_task(print_number("Task-3"))
    await task1
    await task2
    await task3
asyncio.run(main())
-------------------------------------------------------------------------------------------------------------------

3:Many to many(multi user thread are mapped to an equal or smaller number of karnal threads)
    #combine the advantage of bit one to one and many to one
    #great concurrency and flexibility 
    #butter resoursce utiliization

    #more complex implementation than other modules
    #contex switching between user thread may still incure somE overhead


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
with ThreadPoolExecutor(max_workers=3) as execute:     #if max_workers=1(done all the threads in one time)
    execute.submit(f,n,1)                               #if max_workers=2(done first one thread after the second thread)
    execute.submit(f, n,1)
    execute.submit(f, n, 1)

print("The process done")





