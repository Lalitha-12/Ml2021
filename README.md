# Ml2021
OBJECTIVE:
      Chatbot which give information about capitals of countrys
Description:
        my chatbot helps to find capitals of countries which ere enterd by the user.first it greets user and asks users name and welcomes user based upon the time they used it
        after it asks user to enter the country which they want to know the capital then it gives the capital of the country and the currency of the country as output.
Block diagram:
              

 
CODE:
import random
from datetime import datetime
from countryinfo import CountryInfo
def greeting():
    greet = ["Hii,i am bot your name please i will help you to find capitals to countries","It's wonderful to see you your name please i will tell capitals to countries"]
    print(random.choice(greet))
def curr_datetime():
    curtime = datetime.now()
    timeday_greeting = "Good Morning"
    if curtime.hour > 11 and curtime.hour < 17:
        timeday_greeting = "Good Afternoon"
    elif curtime.hour >16 and curtime.hour <22:
        timeday_greeting = "Good Evening"
    elif curtime.hour > 22:
        timeday_greeting = "It's to late"
    return timeday_greeting
def welcome(name):
    response = ['Hello,have a nice day','Nice to meet you','lets have a fun to meet you']
    print(f"{curr_datetime()},{random.choice(response)}")  
def capital():
    i=1
    while i>0:
        a = input("Enter country name: ")
        if(a=="bye"):
            break
        else:
            s=a
            country = CountryInfo(s)
            print(country.capital())
            print(country.currencies())
        i=i+1 
def bot():
    greeting()
    name = input("enter your name please:  ")
    welcome(name)
    capital()
bot() 
youtube link:
           


online reference link:
https://pypi.org/project/countryinfo/ 
