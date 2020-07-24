from flask import Flask, request, send_file, jsonify, send_from_directory
from flask_restful import Resource, Api
from flask_apscheduler import APScheduler
import os
import sys
import time
sys.path.append(os.getcwd()+'\\controller')

# print(os.getcwd())

import username
from GMM1 import *

app = Flask(__name__)
api = Api(app)
scheduler = APScheduler()


class Recognition(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        file = request.files.getlist("file[]")

        name_file = str(time.time()*100000)[0:15]
        path = "training_data/"+name_file+".wav"


        file[0].save(path)


        person = {'id': username.test1(path), 'rate': 80, 'name_file' : name_file}
        return jsonify(person)




class TrainSpeaker(Resource):
    def post(self):
        file = request.files.getlist("file[]")
        nameSpeaker = request.form['id']

        for i in range(5):
            tmp = "_"+ str(time.time()*100000)[0:15]
            path_store = 'training_data/'+nameSpeaker + tmp + '.wav'
            file[i].save(path_store)


        traine(nameSpeaker)

        f = open('controller/info_recognize.txt', 'a')
        f.write(nameSpeaker +" 0\n")
        f.close()

        return nameSpeaker

class NoiseReduce(Resource):
    def post(self):
        return send_file('../controller/testfile.wav', attachment_filename='testfile.wav')

class Download(Resource):
    def get(self):
        file_name = request.args.get('file_name')
        return send_file('../training_data/' + file_name)

class ListFile(Resource):
    def get(self):
        list = []
        id_user = request.args.get('id')
        for root, dirs, files in os.walk(os.getcwd() +"\\training_data"):
            for filename in files:
                if(filename.startswith(id_user)):
                    list.append(filename)
        return jsonify(list)

class Confirm(Resource):
    def get(self):
        id_user = request.args.get('id')
        name_file = request.args.get('name_file')

        src = 'training_data/'+ name_file +'.wav'
        dst = 'training_data/' + id_user + '_' + name_file + '.wav'
        os.rename(src, dst)

        f = open('controller/info_recognize.txt', 'r')
        lines = f.readlines()
        f.close()

        for i in range(len(lines)):
            arr = lines[i].split(' ')

            if arr[0] == id_user:
                arr[1] = str(int(arr[1]) + 1) + '\n'
                lines[i] = arr[0] + ' ' + arr[1]
                break

        f = open('controller/info_recognize.txt', 'w')
        f.writelines(lines)
        f.close()

        return "success!!!"



api.add_resource(Recognition, '/recognize')
api.add_resource(TrainSpeaker, '/train')
api.add_resource(NoiseReduce, '/noise_reduce')
api.add_resource(Download, '/download')
api.add_resource(ListFile, '/listFile')
api.add_resource(Confirm, '/confirm')


def re_train():
    f = open('controller/info_recognize.txt', 'r')
    lines = f.readlines()
    f.close()

    for i in range(len(lines)):
        if len(lines[i]) == 0:
            break

        arr = lines[i].split(' ')

        if int(arr[1]) == 1:
            print(arr[0])
            traine(arr[0])
            lines[i] = arr[0] + ' 0\n'

            f = open('controller/info_recognize.txt', 'w')
            f.writelines(lines)
            f.close()

def dothing():
    print(time.time())

if __name__ == '__main__':

    scheduler.add_job(id= 'scheduler task', func = re_train, trigger = 'interval', seconds = 15)
    scheduler.start()
    app.run(debug=True, use_reloader=False)
    scheduler.shutdown()
    print('shut down')





