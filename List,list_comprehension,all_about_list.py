list
    X=3
    del X
    print(x)           >>>name 'x' is not define
    ex: a=['anil', 'amiri', 'is', 'coming', 'to', 'US']
        print(a[::-1])
        >>>['US', 'to', 'coming', 'is', 'amiri', 'anil']
        list is changable but tuple is not changable     and for get put its method>>>  [].
        a[1]="nit"
        a[0]="slhdfh"
        print(a)
        >>>['slhdfh', 'nit', 'is', 'coming', 'to', 'US']

    x=[1,2,3,4,5]
    x.clear()
    print(x)     >>>[]

    x=[1,2,3,4,"pip",5,"hi"]
    x.remove("hi")
    print(x)      >>>[1, 2, 3, 4, 'pip', 5]
    
    x=[1,2,3,4,"pip",5,"hi"]
    x2=x.copy()
    print(x2)         >>>[1, 2, 3, 4, 'pip', 5, 'hi']
    x3=x
    print(x3)           >>>[1, 2, 3, 4, 'pip', 5, 'hi']

    x=[1,2,3,4,"pip",5,"hi"]
    n=x.count("8")
    print(n)     >>>0
    m=x.count(4)
    print(m)       >>>1
    print(x.count("pip"))      >>>1

    x=[1,2,3,4,"pip",5,"hi"]
    x1=["sdhf",3,5,"jlsdf"]
    x.extend(x1)               #jain x with x1 we will use extend() to jain lists
    print(x)        >>>[1, 2, 3, 4, 'pip', 5, 'hi', 'sdhf', 3, 5, 'jlsdf']
    x.extend(x)
    print(x)        >>>[1, 2, 3, 4, 'pip', 5, 'hi', 'sdhf', 3, 5, 'jlsdf', 1, 2, 3, 4, 'pip', 5, 'hi', 'sdhf', 3, 5,'jlsdf']

    x=[1,2,3,4,"pip",5,"hi"]
    print(x.index("pip"))     >>>4

    x=[1,2,3,4,"pip",5,"hi"]
    x.insert(0,"flsdhfshgsh")
    print(x)            >>>['flsdhfshgsh', 1, 2, 3, 4, 'pip', 5, 'hi']
    x.insert(3,"lshdfklsdh")
    print(x)           >>>['flsdhfshgsh', 1, 2, 'lshdfklsdh', 3, 4, 'pip', 5, 'hi']

    x=[1,2,3,4,"pip",5,"hi"] # pop will delete from back one one
    x.pop()
    print(x) >>>[1, 2, 3, 4, 'pip', 5]
    x.pop()
    print(x)    >>>[1, 2, 3, 4, 'pip']

    x=[1,2,3,4,"pip",5,"hi"] 
    x.reverse()
    print(x)    >>>['hi', 5, 'pip', 4, 3, 2, 1]

    x=[1,5,7,9,34,88,90,234,1,2,0,8,235,232,456367,1234]
    x.sort()
    print(x)       >>>[0, 1, 1, 2, 5, 7, 8, 9, 34, 88, 90, 232, 234, 235, 1234, 456367]
    x.sort(reverse=True)
    print(x)       >>>[456367, 1234, 235, 234, 232, 90, 88, 34, 9, 8, 7, 5, 2, 1, 1, 0]

# repeat and more information about list

          example:
            list=["anil","ahmad","mohammad",9879,987]
            list[2]="anil"
            print(list)    
            >>>['anil', 'ahmad', 'anil', 9879, 987]
            print(list.count("anil))
            >>>2

            append : we will add data at the end of list

            list=["anil","ahmad","mohammad",9879,987,"ggg","ggg"]
            list.clear()  #clear will clean all the data of list
            print(list)
            >>>[]

            list=["anil","ahmad","mohammad",9879,987,"ggg","ggg"]
            list.remove("anil")    #remove: it will clean the data that we will take
            print(list)
            >>>['ahmad', 'mohammad', 9879, 987, 'ggg', 'ggg']


            list=["anil","ahmad","mohammad",9879,987]
            list.insert(3,"jjj")    #first show the postion and second put the data
            print(list)        # in 3 postion put jjj
            >>>['anil', 'ahmad', 'mohammad', 'jjj', 9879, 987]

            list=["anil","ahmad","mohammad",9879,987,"ggg","ggg"]
            list.copy()
            print(list)
            >>>["anil","ahmad","mohammad",9879,987,"ggg","ggg"]

            list=["anil","ahmad","mohammad",9879,987,"ggg","ggg"]
            list.extend("it is car photo")   #extend : splite the characterstic of them and put them in list,even space of it
            print(list)
            >>>['anil', 'ahmad', 'mohammad', 9879, 987, 'ggg', 'ggg', 'i', 't', ' ', 'i', 's', ' ', 'c', 'a', 'r', ' ', 'p', 'h', 'o', 't', 'o']

            list.index()

            list=["anil","ahmad","mohammad",9879,987,"ggg","ggg"]
            list.pop()
            list.pop()    #it will clean from end one one
            list.pop()     # three pop used and three item from list deleted
            print(list)
            >>>['anil', 'ahmad', 'mohammad', 9879]

            list=["anil","ahmad","mohammad",9879,987,"ggg","ggg"]
            list.pop(1)   #we cal also show for pop to delete which item of list
            print(list)
            >>>['anil', 'mohammad', 9879, 987, 'ggg', 'ggg']

            list=["anil","ahmad","mohammad",9879,987,"ggg","ggg"]
            list.reverse()   #it will reverse the list
            print(list)
            >>>['ggg', 'ggg', 987, 9879, 'mohammad', 'ahmad', 'anil']

            list=[34,56,12,2,6,9,35,15,14,17,10]
            list.sort()    #it will manage from down to up 
            print(list)
            >>> [2, 6, 9, 10, 12, 14, 15, 17, 34, 35, 56]

            list=["naw","sow","ani","kle","bo","do","eo"]
            list.sort()     #it also manage according the alphabite of english
            print(list)
            >>>['ani', 'bo', 'do', 'eo', 'kle', 'naw', 'sow']

            list=["naw","sow","ani","klelsdfjlsd","bo","do","eo"]
            del list[3]    #it will delete the item that you take position of it
            print(list)     #look it delete the third item "klelsdfjlsd
            >>>['naw', 'sow', 'ani', 'bo', 'do', 'eo']

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#List comprehension:
    #create list using list comprehension
    #use to create new short list from proveuse list

Syntax:
    new_list=[new_item for item in list]

example:
    list=[1,2,3,4,5]
    list_new=[]
    for new in list:
        add=new+3
        list_new.append(add)
    print(list_new)
    >>>[4, 5, 6, 7, 8]

    #Using from list comprehension
    list_new=[new+3 for new in list]
    print(list_new)
    >>>[4, 5, 6, 7, 8]
    -----------------------------
    a="anil"
    for i in a:
        print(i)
    >>>a
        n
        i
        l
    #using form list comprehesion
    new_list=[i for i in a]
    print(new_list)
    >>>['a', 'n', 'i', 'l']
    ----------------------------
    list=[]
    for i in range(1,10):
        list.append(i*2)
    print(list)
    >>>[2, 4, 6, 8, 10, 12, 14, 16, 18]

    #use form list comprehension
    list=[i*2 for i in range(1,10)]
    print(list)
    >>>[2, 4, 6, 8, 10, 12, 14, 16, 18]

    number=[1,2,3,4,5,6,7,8]
    square_number=[num*num for num in number]
    print(square_number)
    >>>[1, 4, 9, 16, 25, 36, 49, 64]

    data=open("file")
    data.readline()
    new=[datas for datas in data]
    print(new)
    >>>['Alabama,139,-77\n', 'Alaska,-204,-170\n', 'Arizona,-203,-40\n', 'Arkansas,57,-53\n', 'California,-297,13]

    -------------------------------------
    tuple=("anil","ahmad","mohammad")
    list_new=[name+"TC" for name in tuple]
    print(list_new)
    >>>['anilTC', 'ahmadTC', 'mohammadTC']

Conditional list comprehension
    Syntax:
        new_list=[new_item for item in list if test]

    example:
        name=["Anil","Ali khan","Mohammad","Ahmad Ahmady","Ali"]
        new=[names for names in name if len(names)>5] #inter in new list those names which len nems is >5
        print(new)
        >>>['Ali khan', 'Mohammad', 'Ahmad Ahmady']

        name=["Anil","Ali khan","Mohammad","Ahmad Ahmady","Ali"]
        new=[names.upper() for names in name if len(names)<5] #inter in new list those names which len nems is >5
        print(new)
        >>>['ANIL', 'ALI']

        number=[1,2,3,4,5,6,7,8,9,10]
        square_number=[num for num in number if num%2==0]
        print(square_number)
        >>>[2, 4, 6, 8, 10]

        number=[1,2,3,4,5,6,7,8,9,10]
        square_number=[num**2 for num in number if num%2==0]  #first it will multiply with the power of 2 after % will do its work
        print(square_number)
        >>>[4, 16, 36, 64, 100]

        show_x=it is a file that contian some numbet
        show_y= it is also a file that contian some number

        with open("file_y") as show_y:
            show_y=show_y.readlines()

        with open("file_x") as show_x:
            show_x=show_x.readlines()
        p=[int(num) for num in show_x if num in show_y]
        print(p)
        >>>[1,2,4]  #these number is exit in show_x and show_y

