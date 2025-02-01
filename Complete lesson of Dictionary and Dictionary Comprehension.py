
Dictionary
    item
        key  >>> int,float,string
        value  >>> everthing

    ex:

    dect={
    "name":"anil",
    "jap":"saftware engineer",
    "tasr":"conguretheworld"
    }
    print(dect["name"])    >>>anil

    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    for i in dict:
        print(i)    # it only get out keys of it
        >>>name
        last
        jap

    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    dict["last"]="khan"
    print(dict)
    >>>{'name': 'anil', 'last': 'khan', 'jap': 'Software Engineer'}
    

    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    for key,value in dict.items():
        print(f"{key}:{value}")
    >>> name:anil
        last:amiri
        jap:Software Engineer

    
    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    dict.pop("jap")   #it will delete the item of dictionary when you put in pop key or key,value
    print(dict)
    >>>{'name': 'anil', 'last': 'amiri'}
    dict.pop("last","amiri)
    >>>{'name': 'anil', 'jap':'Software Engineer}

    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    x=dict
    x3=x.copy()
    print(x3)
    >>>{'name': 'anil', 'last': 'amiri', 'jap': 'Software Engineer'}


    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    print(dict.values())
    >>>dict_values(['anil', 'amiri', 'Software Engineer'])
    print(dict.keys())
    >>>dict_keys(['name', 'last', 'jap'])

    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    print(dict.get("name"))
    >>>anil

    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    dict.clear()   # it will clean all the keys and values of dict
    print(dict)
    >>>{}


    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    dict2={                             #update: it will new the dict by dict2
        "name":"ahmad",
        "last":"khan",
        "jap":"teacher"
    }
    dict.clear()
    dict.update(dict2)
    print(dict)
    >>>{'name': 'ahmad', 'last': 'khan', 'jap': 'teacher'}


    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    dict.fromkeys("name","anil")
    print(dict)
    >>>{'name': 'anil', 'last': 'amiri', 'jap': 'Software Engineer'}


    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    dict.setdefault("picture")     #it will put key in dict and value for it
    dict["picture"]="flower"
    print(dict)
    >>>{'name': 'anil', 'last': 'amiri', 'jap': 'Software Engineer', 'picture': 'flower'}


    dict={
        "name":"anil",
        "last":"amiri",
        "jap":"Software Engineer"
    }
    dict.popitem()   # it will clean from end one one
    print(dict)
    >>>{'name': 'anil', 'last': 'amiri'}


    
    list=[
        [1,2,3,4,5],
        [6,7,8,9,43]
    ]
    print(list[0])  >>>[1, 2, 3, 4, 5]
    print(list[1][3])    >>>9


    list=[
        [1,2,3,4,5],
        [
            [34,45,57,634,444]
        ],
        "string"
    ]

    print(list[1][0][4])     >>>444
    print(list[2][2])   >>>r


    d={
        "item1":[
            {"sub item 1":{
                "sub item 2":[
                    [1,2,3],["pyton","c++",("hi","hello","nice")]
                ]
            }
            }
        ]
    }
    print(d["item1"][0]["sub item1"]["sub item2"][1][2][1])


    list={"anil":98,"ahmad":87}
    print(list.get("anil"))   >>>98

    list={"anil":98,"ahmad":87}
    print(list.keys())      >>>dict_keys(['anil', 'ahmad'])


    list={"anil":98,"ahmad":87}
    list.pop("anil")
    print(list)        >>>{'ahmad': 87}
    print(list.pop("ahmad"))   >>>87


    list={"anil":98,"ahmad":87}
    list2={"anil":100,"ahmad":78}
    list.update(list2)
    print(list)              >>>{'anil': 100, 'ahmad': 78}


    list={"anil":98,"ahmad":87}
    list2={"anil":100,"ahmad":78,"name":64}
    list.update(list2)
    print(list)                         >>>{'anil': 100, 'ahmad': 78, 'name': 64}


    list2={"anil":100,"ahmad":78,"name":64}
    list2.setdefault("picture")
    print(list2)                       >>>{'anil': 100, 'ahmad': 78, 'name': 64, 'picture': None}
    list2["picture"]="lksdjf;lasdjf"
    print(list2)              >>>{'anil': 100, 'ahmad': 78, 'name': 64, 'picture': 'lksdjf;lasdjf'}
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Dictionary comprehension
    #create new dictionary from previus dictionary

Syntax:
    #this is use when you put the items of list in dictionary
    new_dict={new_key:new_value for item in list}

    example:
        list=["hhp","mysql","python","c++"]
        dictionary={ item for item in list}
        print(dictionary)
        >>>{'mysql', 'hhp', 'python', 'c++'}

Syntax:
    #this is use we get the items from dictionary
    new_dict={new_key:new_value for (key,value) in dict}
    example:

        dict={
            "name":"Anil",
            "f_name":"Essmatullah",
            "jap":"software Engineer"
        }
        dictionary={key for key in dict}
        print(dictionary)    #it only show the key of it
        >>>{'jap', 'name', 'f_name'}

        dict={
            "name":"Anil",
            "f_name":"Essmatullah",
            "jap":"software Engineer"
        }
        dict={key:value for (key,value) in dict.items()}  #it get out keys and values
        print(dict)
        >>>{'name': 'Anil', 'f_name': 'Essmatullah', 'jap': 'software Engineer'}
        name=["anil","mohammad","ali","khan"]
        import random
        new_dict={key:random.randint(60,90) for key in name}
        print(new_dict)
        >>>{'anil': 86, 'mohammad': 88, 'ali': 77, 'khan': 71}

Syntax:
    new_dict={new_key:new_value for (key,value) in dict.items() if test}

    example:
        name=["anil","mohammad","ali","khan"]
        import random
        show=random.randint(60,90)
        new_dict={key:show for key in name if show>70}
        print(new_dict)
        >>>{'anil': 71, 'mohammad': 71, 'ali': 71, 'khan': 71}

        name={
            "ali":676,
            "ahmad":355,
            "ahmady":876,
            "teacher":456
        }
        dict={key:value for (key,value) in name.items() if value>500}
        print(dict)
        >>>{'ali': 676, 'ahmady': 876}

        sentence="what is your name"
        dict={words:len(words) for words in sentence.split()}
        print(dict)
        >>>{'what': 4, 'is': 2, 'your': 4, 'name': 4}


        weather_c={
            "Monday":12,
            "Thuosday":14,
            "Wensday":21,
            "Friday":22,
            "Saturday":24,
            "Sunday":43
        }
        weather={day:(temp*(9/5))+32 for (day,temp) in weather_c.items()}
        print(weather)
        >>>{'Monday': 53.6, 'Thuosday': 57.2, 'Wensday': 69.80000000000001, 'Friday': 71.6, 'Saturday': 75.2, 'Sunday': 109.4}


        import pandas
        data=pandas.read_csv("state_to_learn.csv")
        dict={row.letter:row.code for (index,row) in data.iterrows()}
        name=input("Enter the name:").upper()
        for letter in name:
            a=dict[letter]
            print(a)

        dictionary={dict[letter] for letter in name}
        print(dictionary)
        >>>Enter the name:anil
            Alfa
            November
            India
            Lima
            {'Lima', 'November', 'India', 'Alfa'}















