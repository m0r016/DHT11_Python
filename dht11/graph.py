import RPi.GPIO as GPIO
import dht11
import time
import sys
import csv
import datetime
import slackweb

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=14)

result = instance.read()
temp = result.temperature
humidity = result.humidity

while True:
    try:
        val = [0, 0, 0]
        val[0] = datetime.datetime.now()
        val[1] = temp
        val[2] = humidity
        print('now time ' + str(val[0]) + ',' + ' now temp ' +
              str(val[1]) + ',' + 'now humidity' + str(val[2]))

        with open('./log.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(val)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
