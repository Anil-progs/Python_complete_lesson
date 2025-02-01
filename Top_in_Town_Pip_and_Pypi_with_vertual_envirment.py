pip is a saftware, when you install the pyton in your computer it will also install it that we can install other packages from it

Definition: pip is a package manager for Python that allows you to install and
manage software packages (libraries) from the Python Package Index (PyPI) and other sources.

Usage: You can use pip to install packages by running commands in the terminal, such as pip install package_name

PyPI is the repository where those packages are hosted  and pypi is a side that we can install packages from it
	
The Python Package Index (PyPI) is a repository of software for the Python programming language.

#pip install colorama
    from colorama import Fore
    print(Fore.BLUE+"This is my jap")
    print(Fore.MAGENTA+"Hi, How are you")

#pip install seaborn
-----------------------------------------------------------------------

pip      #show all the methods that you have

vertual envitment

venv: Vertual Enviroment: it is  a vertual enviroment that we can create for our program Cmd can install our own packages on it
#How to create a vertual enviroment
1:create a foldet
2:open the folder with cmd or terminal of VC or pycharm
cmd
    cd Desktop
    cd first_venv_p
    python -m venv env
    cd env
    cd scripts
    .\activate
    pip install flask

    new open the folder in VS code
    open the terminal of VS code  and see that the env should none by terminal   PS C:\Users\MRC\Desktop\first_venv_project>
    python 
    python main. --->>>>that  is main you should run your code
    new run the VC code  to achieve the code and search it in google
    >>> * Running on http://127.0.0.1:5000
            Press CTRL+C to quit   
            * Restarting with stat
            * Debugger is active!
            * Debugger PIN: 708-924-071
            #This is use specially for web development

    pip freeze     #show all the labriries that you installed
    >>>blinker==1.8.2
    click==8.1.7       
    colorama==0.4.6    
    Flask==3.0.3       
    itsdangerous==2.2.0
    Jinja2==3.1.4      
    MarkupSafe==3.0.2  
    Werkzeug==3.1.2 

    pip freeze > requirment.txt    #it will make a file that all your labriries is exits in it
-------------------------
#never push the env of your project in gethun beacuse it will take more internet to install it 
vs code 
    exit
cmd
    exit
    deactivate
vs code
    #delete your env
    python -m venv new_env
    cd new_env/scripts
    cd ..  #go one step back
        PS C:\Users\MRC\Desktop\first_ennnew_env\scripts> cd ..
        PS C:\Users\MRC\Desktop\first_env_p\new_env> cd ..
        PS C:\Users\MRC\Desktop\first_env_p> pip install -r requirment.txt

    again go to cmd and do thid
    cd Desktop
    cd first_env  #that is the folder of it
    cd env
    cd scripts
    pip install flask

    go to VS code and  again run it 
    >>> * Running on http://127.0.0.1:5000
        Press CTRL+C to quit
        * Restarting with stat
        * Debugger is active!
        * Debugger PIN: 708-924-071
        127.0.0.1 - - [06/Nov/2024 12:41:39] "GET / HTTP/1.1" 200 -
        127.0.0.1 - - [06/Nov/2024 13:41:13] "GET / HTTP/1.1" 200 -

cd Desktop
git clone https://github.com/

usage of env:
    when we install python 3.10.1 which pyqt5 is for it and you also install pyqt5 but in anther project you need
    for pyqt5.4 after you can not install on top of pyqt5 the pyqt5.4  that is why we will use env
3:open the folder in VS code open the terminal of it
>>>PS C:\Users\MRC\Desktop\first_venv_project>

4: python -m venv package_name    #it will make vertual envirment internal of our folder
                                   #package_name you should choose name for it
5:befor to intall any package for your project active the vertual envirment
cd env       #it will inter in your env
cd scripts      #it will inter in your scripts
pip install flask

6:cmd
cd scripts
.\activate
=======================================================================================================================================
------------------------------------------------------------------------------------------------------------------------------------------
env(envitrment varible)

Using environment variables allows for easy configuration changes without modifying the source code.
Developers can define different settings for development, testing, 
and production environments simply by changing the environment variable values.
This flexibility makes it easier to deploy applications across various environments that may require different configurations

#simply:  it is like a box that you will put your import information that you use in your program like if you put your program in 
# github,pythonanywhere.....

>>>export OWM_API_KEY= 960ebe87d9483953dd8e630b2930da62
#your information will hide in OWM_API_KEY





