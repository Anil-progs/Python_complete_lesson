#Panda is a library of python for data analyzing
#CSV : comma sperate values

"""with open("C:\\Users\\MRC\\Desktop\\weather_info.txt","r") as show:
    a=show.readlines()
    for i in a:
        print(i)"""
"""import csv
with open("C:\\Users\\MRC\\Desktop\\weather_info.txt","r") as show:
    a=csv.reader(show)
    print(a)
    list=[]
    for row in a:
        if row[1] !="temp":
            list.append(row[1])
    print(list)
    
import csv
import random
with open("french_words.csv","r") as show:
    a=csv.reader(show)
    list=[]
    for row in a:
        list.append(row[0])
    word=random.choice(list)
    print(word)"""
# manage the data with csv it is a little bite wast our time but instead of it we can use from pandas
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
day,temp,condition
Monday,12,Sunny
Tuesday,14,Sunny
Wedneday,15,Run
Thursday,21,Sunny
Friday,21,Sunny
Saturday,21,Sunny
Sunday,24,Sunny

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
pritn(data)
>>>        day  temp condition
0    Monday    12     Sunny
1   Tuesday    14     Sunny
2  Wedneday    15       Run
3  Thursday    21     Sunny
4    Friday    21     Sunny
5  Saturday    21     Sunny
6    Sunday    24     Sunny
PS C:\Users\MRC>

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
print(f"{data["temp"]},{data["condition"]}")
>>>0    12
1    14
2    15
3    21
4    21
5    21
6    24
Name: temp, dtype: int64,0    Sunny
1    Sunny
2      Run
3    Sunny
4    Sunny
5    Sunny
6    Sunny
Name: condition, dtype: object     
PS C:\Users\MRC> 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
print(type(data["temp"]))
>>><class 'pandas.core.series.Series'> # each column is called series
PS C:\Users\MRC> 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#to_dict(): it will create data in dictionary
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
b=data.to_dict()
print(b)
>>>{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wedneday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
 'temp': {0: 12, 1: 14, 2: 15, 3: 21, 4: 21, 5: 21, 6: 24},
 'condition': {0: 'Sunny', 1: 'Sunny', 2: 'Run', 3: 'Sunny', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
PS C:\Users\MRC>
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# to_list() :
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
b=data["temp"].to_list()
print(b)
>>>[12, 14, 15, 21, 21, 21, 24]
PS C:\Users\MRC> 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
b=data["temp"].to_list()
v=sum(b)/len(b)           #averge
print(v)
>>>18.285714285714285
b=data["temp"].mean()   #here we use the .mean() it will find the avarage 
print(b)
>>>18.285714285714285
b=data["temp"].max()
>>>24
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
print(data.condition)
>>>0    Sunny
1    Sunny
2      Run
3    Sunny
4    Sunny
5    Sunny
6    Sunny
Name: condition, dtype: object
PS C:\Users\MRC>
print(data.day)
print(data.temp)
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # to get data in row
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
print(data[data.day =="Monday"])
>>>   day  temp condition
0  Monday    12     Sunny
PS C:\Users\MRC> 
print(data[data.temp ==max(data["temp"])])
>>>   day  temp condition
6  Sunday    24       Sunny
PS C:\Users\MRC> 
datas=data[data.temp==max(data["temp"])]
print(datas)
>>>  day  temp condition
6  Sunday    24     Sunny
PS C:\Users\MRC> 
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info.txt")
for i in data["temp"]:
    datas=int(i)*(9/5)+32    #change to faranhaide 
    print(datas)
>>>75.2
53.6
57.2
59.0
69.80000000000001
69.80000000000001
69.80000000000001
75.2
PS C:\Users\MRC>
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#implementation of pandas in dictionary
import pandas
dict={
    "goods":["rice","been","flour"],
    "things":["car","bike","bicycle"]
}
data=pandas.DataFrame(dict)
print(data)
>>> goods   things
0   rice      car
1   been     bike
2  flour  bicycle
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import pandas
dict={
    "goods":["rice","been","flour"],
    "things":["car","bike","bicycle"]
}
data=pandas.DataFrame(dict)
print(data.to_csv("hh.txt"))  # it will create a new file,with these items in dict,and open the item of 
                             #dict in file
#example of it 
import pandas
dict={
    "goods":["rice","been","flour"],
    "things":["car","bike","bicycle"]
}
data=pandas.DataFrame(dict)
print(data.to_csv("hh.txt"))
datas=pandas.read_csv("hh.txt")
print(datas)
>>>   Unnamed: 0  goods   things
0           0   rice      car
1           1   been     bike
2           2  flour  bicycle
PS C:\Users\MRC> 
#example of it
import pandas
data=pandas.read_csv("C:\\Users\\MRC\\Desktop\\weather_info - Copy.txt")
print(data[data.temp>14])
>>>   day  temp condition
2  Wedneday    15       Run
4    Friday    21     Sunny
5  Saturday    21     Sunny
PS C:\Users\MRC> 
------------------------------------------------
state,x,y
alabama,139,-77
california,-204,-170
arizona,-203,-40
california,-297,96
california,-112,20
florida,370,25

import pandas
data=pandas.read_csv("C:\\Users\\MRC\\PycharmProjects\\Anil class project 123456\\file")
count=len(data[data.state=="california"])
dict={
    "name":["colforinia"],
    "counts":[count]
}
print(pandas.DataFrame(dict))
>>>     name  counts
0  colforinia       3
-------------------------------------------------------------------
dict={
    "name":["Ahmad","mohmmad","Ali"],
    "score":[344,675,353]
}
#loop throw a dictionary
for (key,value) in dict.items():
    print(key,value)
>>>name ['Ahmad', 'mohmmad', 'Ali']
score [344, 675, 353]


dict={
    "name":["Ahmad","mohmmad","Ali"],
    "score":[344,675,353]
}
import pandas
data=pandas.DataFrame(dict)
print(data)
>>>name  score
0    Ahmad    344
1  mohmmad    675
2      Ali    353

#loop through a DataFrame
dict={
    "name":["Ahmad","mohmmad","Ali"],
    "score":[344,675,353]
}
import pandas
data=pandas.DataFrame(dict)

for (key,value) in data.items():

    print(key,value)
>>>name 0      Ahmad
1    mohmmad
2        Ali
Name: name, dtype: object
score 0    344
1    675
2    353
Name: score, dtype: int64

    print(value)
>>>0      Ahmad
1    mohmmad
2        Ali
Name: name, dtype: object
0    344
1    675
2    353
Name: score, dtype: int64

#loop through rows of data frame
dict={
    "name":["Ahmad","mohmmad","Ali"],
    "score":[344,675,353]
}
import pandas
data=pandas.DataFrame(dict)
for (index,row) in data.iterrows():
    print(row)
>>>name     Ahmad
score      344
Name: 0, dtype: object
name     mohmmad
score        675
Name: 1, dtype: object
name     Ali
score    353
Name: 2, dtype: object

    print(row["name"])
>>>Ahmad
mohmmad
Ali
    print(row.score)
>>>344
675
353

dict={
    "name":["Ahmad","mohmmad","Ali"],
    "score":[344,675,353]
}
import pandas
data=pandas.DataFrame(dict)
for (index,row) in data.iterrows():
    if row["name"]=="Ahmad":
        print(row.score)
>>>344






