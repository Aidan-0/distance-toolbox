import schedule, time
from datetime import date
import webbrowser as web

# put any links here that you would like to launch with each hour
class1 = ['']
class2 = ['']
class3 = ['']
class4 = ['']
class5 = ['']
class6 = ['']

foundations = ['']

# for different tuesday/thursday links. leave blank if n/a
class1alt = ['']
class2alt = ['']
class3alt = ['']
class4alt = ['']
class5alt = ['']
class6alt = ['']

def week():
    today = date.today()
    return today.weekday() - today.day >= -1

if week():
    for item in class1:
        schedule.every().monday.at('7:29').do(web.open(class1[item]))
        schedule.every().wednesday.at('7:29').do(web.open(class1[item]))
    for item in class2:
        schedule.every().monday.at('8:23').do(web.open(class2[item]))
        schedule.every().wednesday.at('8:23').do(web.open(class2[item]))
    for item in foundations:
        schedule.every().monday.at('9:18').do(web.open(foundations[item]))
        schedule.every().tuesday.at('9:18').do(web.open(foundations[item]))
        schedule.every().wednesday.at('9:18').do(web.open(foundations[item]))
        schedule.every().thursday.at('9:18').do(web.open(foundations[item]))
    for item in class3:
        schedule.every().monday.at('9:47').do(web.open(class3[item]))
        schedule.every().wednesday.at('9:47').do(web.open(class3[item]))
    for item in class4:
        schedule.every().monday.at('10:41').do(web.open(class4[item]))
        schedule.every().wednesday.at('10:41').do(web.open(class4[item]))
    for item in class5:
        schedule.every().monday.at('12:16').do(web.open(class5[item]))
        schedule.every().wednesday.at('12:16').do(web.open(class5[item]))
    for item in class6:
        schedule.every().monday.at('1:10').do(web.open(class6[item]))
        schedule.every().wednesday.at('1:10').do(web.open(class6[item]))

    for item in class1alt:
        schedule.every().tuesday.at('7:29').do(web.open(class1alt[item]))
        schedule.every().thursday.at('7:29').do(web.open(class1alt[item]))
    for item in class2alt:
        schedule.every().tuesday.at('8:23').do(web.open(class2alt[item]))
        schedule.every().thursday.at('8:23').do(web.open(class2alt[item]))
    for item in class3alt:
        schedule.every().tuesday.at('9:47').do(web.open(class3alt[item]))
        schedule.every().thursday.at('9:47').do(web.open(class3alt[item]))
    for item in class4alt:
        schedule.every().tuesday.at('10:41').do(web.open(class4alt[item]))
        schedule.every().thursday.at('10:41').do(web.open(class4alt[item]))
    for item in class5alt:
        schedule.every().tuesday.at('12:16').do(web.open(class5alt[item]))
        schedule.every().thursday.at('12:16').do(web.open(class5alt[item]))
    for item in class6alt:
        schedule.every().tuesday.at('1:10').do(web.open(class6alt[item]))
        schedule.every().thursday.at('1:10').do(web.open(class6alt[item]))

else:
    for item in class1:
        schedule.every().monday.at('7:29').do(web.open(class1[item]))
        schedule.every().wednesday.at('7:29').do(web.open(class1[item]))
    for item in class2:
        schedule.every().monday.at('8:29').do(web.open(class2[item]))
        schedule.every().wednesday.at('8:29').do(web.open(class2[item]))
    for item in class3:
        schedule.every().monday.at('9:29').do(web.open(class3[item]))
        schedule.every().wednesday.at('9:29').do(web.open(class3[item]))
    for item in class4:
        schedule.every().monday.at('10:29').do(web.open(class4[item]))
        schedule.every().wednesday.at('10:29').do(web.open(class4[item]))
    for item in class5:
        schedule.every().monday.at('12:04').do(web.open(class5[item]))
        schedule.every().wednesday.at('12:04').do(web.open(class5[item]))
    for item in class6:
        schedule.every().monday.at('1:04').do(web.open(class6[item]))
        schedule.every().wednesday.at('1:04').do(web.open(class6[item]))

    for item in class1alt:
        schedule.every().tuesday.at('7:29').do(web.open(class1alt[item]))
        schedule.every().thursday.at('7:29').do(web.open(class1alt[item]))
    for item in class2alt:
        schedule.every().tuesday.at('8:29').do(web.open(class2alt[item]))
        schedule.every().thursday.at('8:29').do(web.open(class2alt[item]))
    for item in class3alt:
        schedule.every().tuesday.at('9:29').do(web.open(class3alt[item]))
        schedule.every().thursday.at('9:29').do(web.open(class3alt[item]))
    for item in class4alt:
        schedule.every().tuesday.at('10:29').do(web.open(class4alt[item]))
        schedule.every().thursday.at('10:29').do(web.open(class4alt[item]))
    for item in class5alt:
        schedule.every().tuesday.at('12:04').do(web.open(class5alt[item]))
        schedule.every().thursday.at('12:04').do(web.open(class5alt[item]))
    for item in class6alt:
        schedule.every().tuesday.at('1:04').do(web.open(class6alt[item]))
        schedule.every().thursday.at('1:04').do(web.open(class6alt[item]))

# checks every second if anything needs to be run
while True:
    schedule.run_pending()
    time.sleep(1)