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

# region auto alt classes
if class1alt == ['']:
    class1alt = class1
if class2alt == ['']:
    class2alt = class2
if class3alt == ['']:
    class3alt = class3
if class4alt == ['']:
    class4alt = class4
if class5alt == ['']:
    class5alt = class5
if class6alt == ['']:
    class6alt = class6
# endregion

def weblink(urls):
    for i in range(len(urls)):
        web.open(urls[i])

def week():
    today = date.today()
    return today.weekday() - today.day >= -1
    
if week():
    schedule.every().monday.at("07:29").do(weblink, class1)
    schedule.every().wednesday.at("07:29").do(weblink, class1)

if week():
    schedule.every().monday.at("07:29").do(weblink, class1)
    schedule.every().wednesday.at("07:29").do(weblink, class1)

    schedule.every().monday.at("08:23").do(weblink, class2)
    schedule.every().wednesday.at("08:23").do(weblink, class2)

    schedule.every().monday.at("09:18").do(weblink, foundations)
    schedule.every().tuesday.at("09:18").do(weblink, foundations)
    schedule.every().wednesday.at("09:18").do(weblink, foundations)
    schedule.every().thursday.at("09:18").do(weblink, foundations)

    schedule.every().monday.at("09:47").do(weblink, class3)
    schedule.every().wednesday.at("09:47").do(weblink, class3)

    schedule.every().monday.at("10:41").do(weblink, class4)
    schedule.every().wednesday.at("10:41").do(weblink, class4)

    schedule.every().monday.at("12:16").do(weblink, class5)
    schedule.every().wednesday.at("12:16").do(weblink, class5)

    schedule.every().monday.at("13:10").do(weblink, class6)
    schedule.every().wednesday.at("13:10").do(weblink, class6)

    schedule.every().tuesday.at("07:29").do(weblink, class1alt)
    schedule.every().thursday.at("07:29").do(weblink, class1alt)

    schedule.every().tuesday.at("08:23").do(weblink, class2alt)
    schedule.every().thursday.at("08:23").do(weblink, class2alt)

    schedule.every().tuesday.at("09:47").do(weblink, class3alt)
    schedule.every().thursday.at("09:47").do(weblink, class3alt)

    schedule.every().tuesday.at("10:41").do(weblink, class4alt)
    schedule.every().thursday.at("10:41").do(weblink, class4alt)

    schedule.every().tuesday.at("12:16").do(weblink, class5alt)
    schedule.every().thursday.at("12:16").do(weblink, class5alt)

    schedule.every().tuesday.at("13:10").do(weblink, class6alt)
    schedule.every().thursday.at("13:10").do(weblink, class6alt)

else:
    schedule.every().monday.at("07:29").do(weblink, class1)
    schedule.every().wednesday.at("07:29").do(weblink, class1)

    schedule.every().monday.at("08:29").do(weblink, class2)
    schedule.every().wednesday.at("08:29").do(weblink, class2)

    schedule.every().monday.at("09:29").do(weblink, class3)
    schedule.every().wednesday.at("09:29").do(weblink, class3)

    schedule.every().monday.at("10:29").do(weblink, class4)
    schedule.every().wednesday.at("10:29").do(weblink, class4)

    schedule.every().monday.at("12:04").do(weblink, class5)
    schedule.every().wednesday.at("12:04").do(weblink, class5)

    schedule.every().monday.at("13:04").do(weblink, class6)
    schedule.every().wednesday.at("13:04").do(weblink, class6)

    schedule.every().tuesday.at("07:29").do(weblink, class1alt)
    schedule.every().thursday.at("07:29").do(weblink, class1alt)

    schedule.every().tuesday.at("08:29").do(weblink, class2alt)
    schedule.every().thursday.at("08:29").do(weblink, class2alt)

    schedule.every().tuesday.at("09:29").do(weblink, class3alt)
    schedule.every().thursday.at("09:29").do(weblink, class3alt)

    schedule.every().tuesday.at("10:29").do(weblink, class4alt)
    schedule.every().thursday.at("10:29").do(weblink, class4alt)

    schedule.every().tuesday.at("12:04").do(weblink, class5alt)
    schedule.every().thursday.at("12:04").do(weblink, class5alt)

    schedule.every().tuesday.at("13:04").do(weblink, class6alt)
    schedule.every().thursday.at("13:04").do(weblink, class6alt)

while True:
    schedule.run_pending()
    time.sleep(1)