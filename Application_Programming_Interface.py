Application Programming Interface

#API(Application Programming Interface)
#we can create with it ISS(international space station)

#An Application Programming Interface(API): is a set of commands,function,
#protocols and objects
#that programmers can use to create software or interact with an external
#system

#like you can go in yahoo!,coinbase,NBA

#we should obay from rules of API to take for our request response
                         #it is a interface between your program and external system
your program                 API(request)                       External system  
your program                 API (respose)                      External system 

you                          (request)API(bank teller)                   bank vault
you                           (response)API(banck teller)                banck vault
#Location of API that we will take is also important  like api.coinbase.com AND http://api.open-notify.org/iss-now.json
#The API it is like Menu that can be as interface between your requests and kitchen
your tommy                        Menu                       Kitchen

----------------------------------------------------------
if you search this ISS address(http://api.open-notify.org/iss-now.json) in google the data will show you like this 
{"timestamp": 1730953262, "iss_position": {"latitude": "13.4095", "longitude": "23.9975"}, "message": "success"}

http://api.open-notify.org/iss-now.json : this is also called end_paint
---------------------------------------------------------------

import requests
response=response.get("http://api.open-notify.org/iss-now.json")  #address of ISS
print(response)
>>><Response [200]>

#after you run the program the response will be this
1xx :  like 101,120,....= #Hold on means wait for a minite
2xx :  like 201,200,....= #Here you go means everything is sucessfull done
3xx :  like 300,301,....= #go away means you shuld not mention this go away
4xx :  like 400,4002,...= #you screwed up meaans that you screwed up something you looking for it is not exit
5xx :  like 500,501,....= #I screwed up means maybe the website is down 

404 it means The page that your looking for it it deos not exit

----------------------------------------------------------------------------------------------------------------
what is url
Sider Fusion
A URL, or Uniform Resource Locator, is a reference or address used to access resources on the internet.
 It specifies the location of a resource and the protocol used to retrieve it. A typical URL consists of several components, including:

Protocol: The method used to access the resource (e.g., http, https, ftp).
Domain Name: The address of the server hosting the resource (e.g., www.example.com).
Path: The location of the specific resource on the server (e.g., /folder/page.html).
Query String (optional): Additional parameters that can be passed to the resource (e.g., ?id=123).
Fragment (optional): A specific section within the resource (e.g., #section1).
An example of a complete URL is:

https://www.example.com/folder/page.html?id=123#section1

This URL specifies that a secure HTTP request should be made to the server at www.example.com,
 accessing the resource located at /folder/page.html,
with the query parameter id=123 and directing the browser to a section with the identifier section1.
---------------------------------------------------------------------------------------------------------------------
get(url=address)

import requests
response=requests.get(url="http://api.open-notify.org/iss-now.json")  #switch in
print(response.json())  #switch out
>>>{'message': 'success', 'iss_position': {'longitude': '104.5198', 'latitude': '-22.4803'}, 'timestamp': 1731026334}

print(response.json()["iss_position"])
>>>{'longitude': '104.5198', 'latitude': '-22.4803'}

print(response.headers)
>>>{'Server': 'nginx/1.10.3', 'Date': 'Fri, 08 Nov 2024 00:58:29 GMT', 'Content-Type': 'application/json', 'Content-Length': '115',
 'Connection': 'keep-alive', 'access-control-allow-origin': '*'}

import requests
response=requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
>>>200

print(response.raise_for_status())#this is mean if 200 do not get out raise exception error

using more methods of get()  use--> .  like response.

--------------------------------------------------------------------------------------------------------

API Parameter:
#some API to response for our request need parameter like this API  https://api.sunrise-sunset.org/json to show the 
# when sun will rise and set need our Parameter(maens longitude,latitude of us or location of us ) 
#you need to take parameter(information) to achieve response from API

An API parameter is a value that can be added to a URL to customize the behavior of the API request.
Parameters are typically used to filter, sort, or customize the results returned by an API.

#like when you go to bank and say what time do you close on {sunday}

#some of parameters in API is requir and some are optional like lat,lng is requir in some API

https://api.sunrise-sunset.org/json?lat=40.7128&lng=-74.0060&date=2024-11-08

in this question (https://api.sunrise-sunset.org/json) #this is end paint or addressess
and  (?) # sparate the address with parameter
and  (lat=40.7128&lng=-74.0060&date=2024-11-08)  #this is paramater
and  (&) #this means and



To achieve this you will take a parameter like this https://api.sunrise-sunset.org/json?lat=40.7128&lng=-74.0060&date=2024-11-08

example:

#end_paint:  https://api.sunrise-sunset.org/json
import requests

response=request.get("https://api.sunrise-sunset.org/json")
print(response)
>>><Response [400]>               #beacuse raise some error this API need paramter

response.raise_for_status()
print(response)
>>>error requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: https://api.sunrise-sunset.org/json

#solution
parameter={
    "lat":33.939110,
    "lng":67.709953,
}

#note : you can find your lat and lng go to google search for Latitude and Longitude Finder 
#write the name of your country it will take out it

response=requests.get("https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
print(response)
>>><Response [200]

print(response.json())
>>>{'results': {'sunrise': '1:53:58 AM', 'sunset': '12:31:52 PM', 'solar_noon': '7:12:55 AM',
 'day_length': '10:37:54', 'civil_twilight_begin': '1:29:10 AM', 'civil_twilight_end': '12:56:40 PM',
  'nautical_twilight_begin': '12:59:19 AM', 'nautical_twilight_end': '1:26:31 PM',
   'astronomical_twilight_begin': '12:29:54 AM', 'astronomical_twilight_end': '1:55:56 PM'}, 'status': 'OK', 'tzid': 'UTC'}

print(show.json()['results']['sunrise'])
>>>1:53:58 AM

#note: if you go and search this in google https://api.sunrise-sunset.org/json?lat=40.7128&lng=-74.0060&date=2024-11-08 it will show this
#? means you want to add paramater,& means and
{
  "results": {
    "sunrise": "11:33:58 AM",
    "sunset": "9:45:39 PM",
    "solar_noon": "4:39:49 PM",
    "day_length": "10:11:41",
    "civil_twilight_begin": "11:06:35 AM",
    "civil_twilight_end": "10:13:02 PM",
    "nautical_twilight_begin": "10:33:52 AM",
    "nautical_twilight_end": "10:45:46 PM",
    "astronomical_twilight_begin": "10:01:45 AM",
    "astronomical_twilight_end": "11:17:53 PM"
  },
  "status": "OK",
  "tzid": "UTC"
}


print(play.split("T"))
>>>['2024-11-08', '01:53:58+00:00']
print(play.split("T")[1])
>>>01:53:58+00:00
print(play.split("T")[1].split(":"))
>>>['01', '53', '58+00', '00']
print(play.split("T")[1].split(":")[0])
>>>01
--------------------------------------------------------------------------------------------------------------
API response some of them have html charactersitice like this 


import requests
import html
paramater={
    "amount":10,
    "type":"boolean",
}
question_datas=requests.get(url="https://opentdb.com/api.php",params=paramater)
question_datas.raise_for_status()
question_data=question_datas.json()["results"]
print(question_data)


[{'type': 'boolean', 'difficulty': 'medium', 'category': 'General Knowledge',
'question': 'Coca-Cola&#039;s original colour was green.', 'correct_answer': 'False',
 'incorrect_answers': ['True']}, {'type': 'boolean', 'difficulty': 'hard',
 'category': 'Entertainment: Japanese Anime &amp; Manga', 'question': 'Throughout the entirety of &quot;Dragon Ball Z&quot;
&quot
&quot  #these are in html 

solution:

question_data=html.unescape(question_datas.json()["results"])
print(question_data)

---------------------------------------------------------------------------------------------------------------------
real example for API

from tkinter import *
import requests
def get_quote():
    show = requests.get(url="https://api.Kanye.rest")
    show.raise_for_status()
    response=show.json()["quote"]
    canvas.create_text(150,207,text=response,width=250,font=("Arial",30,"bold"),fill="white",tags="text")

def clear_text():
    canvas.delete("text")
    get_quote()

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# Draw text and assign it a tag
canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
                   font=("Arial", 30, "bold"), fill="white",tags="text")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=clear_text)
kanye_button.grid(row=1, column=0)

window.mainloop()
---------------------
Parameter in API

import requests
from datetime import datetime
#end_paint:https://api.sunrise-sunset.org/json
my_lat=33.939110
my_lng=67.709953

paramater={
    "lat":my_lat,
    "lng":my_lng,
    "formatted":0,
}

show=requests.get(url="https://api.sunrise-sunset.org/json",params=paramater)
show.raise_for_status()
play=show.json()['results']['sunrise'].split("T")[1].split(":")[0]
play1=show.json()['results']['sunset'].split("T")[1].split(":")[0]
print(play)
print(play1)
a=datetime.now().hour
print(a)
------------------------------------------------------------------------------------------------------------------
#This example is like this that when the ISS accrose from you lat and lng email will come in your gmail
import requests
from datetime import datetime
import smtplib
import time
MY_EMAIL="anihghlsdsthamiri2sgs05@gmailgfgh.com"
MY_PASSWORD="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

my_lat=33.939110
my_lng=67.709953

def iss_over_head():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

    is_lat=float(data["iss_position"]["latitude"])
    is_lng=float(data["iss_position"]["longitude"])
    print(is_lat)
    print(is_lng)
    #your position with in +5 or -5 degree of iss postion
    if my_lat-5 <= is_lat <= my_lat+5 and my_lng-5 <= is_lng <= my_lng+5:
        return True


#end_paint:https://api.sunrise-sunset.org/json

def is_night():
    paramater = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0,
    }
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=paramater)
    response.raise_for_status()
    sunrise=int(response.json()['results']['sunrise'].split("T")[1].split(":")[0])
    sunset=int(response.json()['results']['sunset'].split("T")[1].split(":")[0])
    time_now=datetime.now().hour
    if time_now>= sunset or time_now<=sunrise:
        return True

while True:
    if iss_over_head() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up\n\nThe ISS is above you in the sky"
        )

-----------------------------------------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Athentication: it will clear who you are
API authentication is the process of verifying the identity of a user or
application making a request to an API (Application Programming Interface). 


Athentorization: it will clear what can you do or what you can accuss

API Keys: after you sign in this application will take you API like: 960ebe87d9483953dd8e630b2930da62

API Key Authentication: An API key is issued to a client application to identify and control its access to the API.
While simple to use, compromised API keys can lead to unauthorized access5.

#openweathermap.org
#openweathermap.org/weather-conditions         #show the weather condition in number like 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}
#online json veiwer
#ventusky     #show the weather condition with the best graphic





Common Methods of API Authentication

HTTP Basic Authentication: This is one of the simplest methods, involving the transmission of a username and password encoded in Base64.
It's easy to implement but not secure unless used over HTTPS4.

API Key Authentication: An API key is issued to a client application to identify and control its access to the API.
While simple to use, compromised API keys can lead to unauthorized access5.

OAuth 2.0: This is a widely used authorization framework that 
allows third-party applications to access user data without exposing user credentials.
 OAuth 2.0 provides secure delegated access to APIs through tokens rather than direct access to user password6.

JWT (JSON Web Tokens): JWT is a compact and secure way to represent claims between two parties. 
They are signed tokens that contain user information and are widely used for maintaining session information in a stateless manner7.

Digest Authentication: An improvement over basic authentication, where a hashed representation of the password is sent instead, 
reducing the risk of password interception9.

LDAP (Lightweight Directory Access Protocol): This method authenticates users based on their credentials stored in a centralized directory, 
making it ideal for enterprise scenarios


#import os

import requests
from twilio.rest import Client
#from twilio.http.http_client import TwilioHttpClient

#proxy_clien=TwilioHttpClient()
#proxy_clien.session.proxies={"https":os.environ["https_proxy"]}



account_sid="AC4398ac1f029969643bfbb1aff64a5694"
auth_token="95847792bdfa2f204deca032c0ad7d78"
my_lat=33.939110
my_lng=67.709953

new_paramater={
    "q":"Kabul",
    "appid":"960ebe87d9483953dd8e630b2930da62",
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/weather",params=new_paramater)
response.raise_for_status()
data=response.json()["weather"][0]["id"]
if data < 700:
    print("use ambrilla")
else:
    client=Client(account_sid,auth_token)
    message=client.messages \
        .create(
        body="Hello Anil Ahmad prog\nGood morning\nAnil remember your goals\nToday of you will make tomorrow of you\n"
             "Don't forget Anil you is a hacker,software Engineer and deep coder",
        from_="+16467982558",
        to="+93787062443"
    )
    print(message.status)

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
---------------------------------------------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Advance Authentication and Post/Put/Delete request
    http Request
        get ---> request.get()  #we send request to Application by API and Application will take response or data
        post---> request.post() #we will send or post data to that Application and we don't want to thing about response 
                                    #it is like when we post data in Facebook,Twitter,google sheet
        Put---->  request.put()  #by put we will update data in external system or that application and we can switch the current data to anther data
        delete----> request.delete() #by delete we can delete the data from application like when we delete a pic from facebook

This is for create account in pexila application

    import requests
    from datatime import datatime
    token="slhdfl23kjkjb252kjk"
    username="progs"
    pixel_end_paint="https://pixe.la/v1/users"

    parameters={
        "token":token,
        "username":username,
        "agreeTermsOfService":"yes",
        "notMinor":"yes",
    }

    response=requests.post(url="https://pixe.la/v1/users",json=parameters)
    print(response.text)

This is for create graph in pexila application

    grag_end_paint=f"{pixel_end_paint}/{username}/graphs"

    params_graphs={
        "id":"graph2",
        "name":"cycling graph",
        "unit":"km",
        "type":"float",
        "color":"ajisai"
    }
    headers={
        "X-USER-TOKEN":token
    }

    response_g=requests.post(url=grag_end_paint, json=params_graphs,headers=headers)
    print(response_g.text)


This is for post in your graph your activity

    post_end_paint=f"{pixel_end_paint}/{username}/graphs/graph2"
    post_paramater={
        "data":"20241127",
        "quantity":"19"
    }

    header_post={
        "X-USER-TOKEN":token,
    }

    data=request.post(url=post_end_paint,json=post_paramater,headers=header_post)
    print(data.text)

This is for delete the data from pixel_end_paint

    end_paint_delete=f'{pixel_end_paint}/{username}/graphs/graph2/20241127'
    delete_data=requests.delete(url=end_paint_delete,headers=header_post)
    print(delete_data.text)


slhdfl23kjkjb252kjkjk2b5
slhdfl23kjkjb252kjk

{"message":"Success. Let's visit https://pixe.la/@progs , it is your profile page!","isSuccess":true}
