import datetime
#input month of birth and year of birth
MOB=input("Enter your Month of Birth:")
YOB=input("Enter your Year of Birth:")
#define what month and year today is
CurrentMonth=datetime.datetime.now().month
CurrentYear=datetime.datetime.now().year
#if clause
if int(MOB)>CurrentMonth:
    year=CurrentYear-int(YOB)-1
    month=12-(int(MOB)-CurrentMonth)
else:
    year=CurrentYear-int(YOB)
    month=CurrentMonth-int(MOB)
print("Your age is {}".format(year))
print("{} month".format(month))
