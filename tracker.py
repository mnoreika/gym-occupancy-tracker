import requests
import time
import sched

from lxml import html

def getPeopleInGymNumber():
    response = requests.get("https://www.st-andrews.ac.uk/sport/");

    doc = html.fromstring(response.text)
    link = doc.cssselect("h3")[8]

    people_in_gym = link.text_content().split()[1]
    
    return (people_in_gym[:-1])

def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def record_gym_activity():
    with open("data.csv", "a") as datafile:
        datafile.write(getTime() + " " + getPeopleInGymNumber() + "\n")
        print ("Data has been recorded.")

print ("Running gym occupancy tracker job...")

job = sched.scheduler(time.time, time.sleep)
job.enter(300, 1, record_gym_activity(), (job,))
job.run()

