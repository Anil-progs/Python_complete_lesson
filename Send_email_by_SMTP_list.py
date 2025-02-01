Send Email By smtplib in python

#Email SMTP: it is use to send email by python
#SMTP    (simple mail transfer protocal)

#Gmail Mail Server: it will receive our email
#Yahoo Mail Server: it will store our email


#sender:the person who send email
#recipient or receiver: the person who receive the email

#sender(anilamiri2005@gmail.com)    SMTP      recipient(timmy@yahoo.com)

#SMTP is like the person who work in post office and carry pur email or bring it to put in mail box
# we have labirary for SMTP smtplib

#smtp.gmail.com:it is the location of smtp server for gmail
    #anilamiri2005@gmail.com
        #anilamiri2005  :it is the identity of your email account
        #gmail.com  : it is the indentity of your email provider

#Gmail(smtp.gmail.com)         Hotmail(smtp.live.com)            Yahoo(smtp,mail.yahoo.com)

#it is really important
    #in this kind of send email we need to make our email security less from management our email

import smtplib

my_email="anilamiri2005@gmail.com"
my_email_password="range123@you"

#in .SMTP(" ") in the middle of this clear that is Gmail or yahoo,....
with smtplib.SMTP("smtp.gmail.com") as connection:  #it is connection
    #tls  (Transport Layer Security)
    connection.starttls()  #it will take security for our email,if some one want to read our email
                            #because of TLS it will increpyt and can not read it someone

    connection.login(user=my_email,password=my_email_password)

    #\n\n: after take this you can write your email body
    connection.sendmail(from_addr=my_email,
                        to_addrs="naweedullahamiri777@gmail.com",
                        msg="Subject:hello world\n\n here I can write my email body")
#above does not need for close it 
-------------------------------------------------------------
#look in here we will write connection.close() at the end
connection.login(user=my_email,password=password)
#\n\n: after take this you can write your email body
connection.sendmail(from_addr=my_email,
                    to_addrs="naweedullahamiri777@gmail.com",
                    msg="Subject:hello world\n\n here I can write my email body")
connection.close()


examlple:

    import pandas
    import datetime
    import random
    import smtplib

    user="anilamri200@gmail.com"
    password="rangeone78"

    data_time=datetime.datetime.now()

    data_pandas=pandas.read_csv("words_I _do't_know.csv")

    tuples=(data_time.month,data_time.day)
    dict_birday={(row_value["month"],row_value["day"]):row_value for (index,row_value) in data_pandas.iterrows()}
    if tuples in dict_birday:
        birday_person=dict_birday[tuples]
        file_path=f"New_project_file\\letter_templates\\letter_{random.randint(1,3)}.txt"
        with open(file_path) as show:
            letter=show.read()
            letter=letter.replace("[NAME]",birday_person["name"])
        with smtplib.SMTP("smtp.gmail.com") as connaction:
            connaction.starttls()
            connaction.login(user=user,password=password)
            connaction.sendmail(from_addr=user,
                                to_addrs=birday_person["email"],
                                msg=f"Subject:happy birday\n\n{letter}")   
-------------------------------------
#internal of this file
file (words_I_do't_know.csv)
name,email,year,month,day,message
Ahmad,ahmad@gmail.com,2008,12,23,[my_friend]
Test,test@email.com,1961,10,21,[Anil your lovely friend!]
Ali,ali@gmail.com,2016,9,14,[happy bird day to you]
