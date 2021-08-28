# coding:utf-8
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import slackweb #←追加

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin=14) #←配線したGPIOピンの番号を指定

#取得した情報をslackwebに通知する
result = instance.read()
temp = result.temperature
humidity = result.humidity
nowtime = "{0:%Y/%m/%d %H:%M:%S}".format(datetime.datetime.now())
if humidity is not None and temp is not None:
    msg = u"{0}現在の温度は{1:0.1f}度、湿度は{2:0.1f}% です".format(nowtime,temp, humidity)
else:
    msg = u"温湿度を測定できませんでした"

slack = slackweb.Slack(url="https://hooks.slack.com/services/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") #手順4-2のURLを記載する
slack.notify(text=msg)
print msg
