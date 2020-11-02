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
            #it prints the capital of country
            print(country.currencies())
            #it prints currency of country
        i=i+1 
def bot():
    greeting()
    name = input("enter your name please:  ")
    welcome(name)
    capital()
bot() 








    

    