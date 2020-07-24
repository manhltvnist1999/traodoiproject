# from controller.record_module import *
# from controller.username import *
import os
import sys
sys.path.append(os.getcwd()+'\\controller')
from username import *
import json
import wave
# print("Press enter to record")
# record_audio()
# print("done!!!")

# print("recognizing.........")

import soundfile

# data, samplerate = soundfile.read('../test_data/hung1.wav')
# print(samplerate)
# file = wave.open('F:client1/out.wav', 'r')
#
# print(file.getparams())
# soundfile.write('new.wav', data, samplerate, subtype='PCM_16')
# print("Hello: " + test1("F:client1/out.wav"))

for root, dirs, files in os.walk("C:/Users/Van_Hung/PycharmProjects/SpeakerRecognition/controller"):
    numberFile = 0
    trueFile = 0
    list = []
    for filename in files:
        # print(test1("../test_data/" + filename))
        numberFile += 1
        list.append(filename)
        # test1("..\\test_data\\" + filename)
        # print(filename)
        # if(filename.startswith(test1("..\\test_data\\" + filename))):
        #     trueFile += 1
        # else:
        #     print(filename + "   :   "+ test1("..\\test_data\\" + filename))
    print(json.dumps(list))

# print("Rate: " + str(100*trueFile/numberFile) +"%")

# print(test1("C:\\Users\\Van_Hung\\Desktop\Project2\\testfile.wav"));


