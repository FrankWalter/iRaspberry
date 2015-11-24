import urllib
def speak(sentence):
    url = "http://tsn.baidu.com/text2audio?tex="\
          +sentence\
          +"&lan=zh&cuid=98-90-96-D6-E5-BD&ctp=1&" \
           "tok=%2224.4d6e1ff797005ad2d5ede0be5de0b131.2592000.1450878473.282335-7299565%22"
    print url
    urllib.urlretrieve(url, "../resources/voice/hello.mp3")