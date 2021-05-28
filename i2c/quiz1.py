from picamera import *
from time import *
from schedule import *

i = 0
camera = PiCamera()

def job():    
    sleep(2)
    global i
    i += 1
    fileName = str(i).rjust(3,"0")+".jpg"
    camera.capture(fileName)

#every().day.at("06:00").do(job)
every(2).seconds.do(job)

while True:
    run_pending()
    sleep(1)

