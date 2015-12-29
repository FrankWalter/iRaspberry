#coding=utf8
import urllib

def speak(sentence):
    url = "http://tsn.baidu.com/text2audio?tex="\
          +sentence\
          +"&lan=zh&cuid=98-90-96-D6-E5-BD&ctp=1&" \
           "tok=24.61d03e885985b8e8e72d15def900a4c0.2592000.1453982165.282335-7299565"
    urllib.urlretrieve(url, "Resources/voice/alarm.mp3")


# speak("吃饭喽")