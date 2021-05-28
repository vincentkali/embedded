import time
import picamera
import datetime
with picamera.PiCamera() as camera:
    camera.start_preview()
    try:
        i = 0
        while True:
            now = datetime.datetime.now()
            fileName = "image{"+str(now.year)+str(now.month)+str(now.day)+"_" \
                +str(now.hour)+str(now.minute)+"}.png"
            camera.capture_continuous(fileName)
            print(fileName)
            time.sleep(1)
            i += 1
            if i == 5:
                break
    finally:
        camera.stop_preview()
        pass