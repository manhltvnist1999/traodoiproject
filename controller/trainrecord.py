
import pyaudio
import wave
import os


test =  os.getcwd() + "\\test_data\\"
train = os.getcwd() + "\\training_data\\"


def testr(x, type ,RECORD_SECONDS = 10):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        i=1
        while("TRUE"):
            fname=type+x+str(i)+".wav"
            if os.path.isfile(fname):
                i+=1
            else:
                break
        fname =type+x+str(i)+".wav"
        INPUT_DEVICE_INDEX=0
        
        p = pyaudio.PyAudio()
        
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,input_device_index=INPUT_DEVICE_INDEX)
        
        print("* recording")
        
        frames = []
        
        for i in range(0, int(RATE / CHUNK * int(RECORD_SECONDS))):
            data = stream.read(CHUNK)
            frames.append(data)
        
        print("* done recording")
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        wf = wave.open(fname, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        i+=1
        return fname

def recordTrain(name):
    print("start record 5 files training!!!")
    for i in range(5):
        print("file " + str(i+1))
        testr(name, train)
    print("Done!!!")

def recordTest(name):
    print("start record 3 files training!!!")
    for i in range(3):
        print("file " + str(i + 1))
        testr(name, test)
    print("Done!!!")


recordTrain("le_quoc_phong");
recordTest("le_quoc_phong");


