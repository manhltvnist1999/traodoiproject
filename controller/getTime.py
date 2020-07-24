import datetime
import time
import os
import re
import os
import sys
import time
sys.path.append(os.getcwd()+'\\controller')
import username
# print(datetime.datetime.now().timestamp() * 10000)
# print("hung " + str(time.time())[0:10]+ "aa")

# f= open('info_recognize.txt', 'r')

# while True:
#     # print(int(re.split(r' ', f.readline())[1]))
#     s = f.readline()
#     if len(s) == 0:
#         break
#     print(s.split(' '))
# lines = f.readlines()
# f.close()
#
# for i in range(len(lines)):
#     arr = lines[i].split(' ')
#
#     if arr[0] == 'manh':
#         arr[1] = str(int(arr[1]) + 1)+'\n'
#         lines[i] = arr[0] + ' '+ arr[1]
#         break
# f= open('info_recognize.txt', 'w')
# f.writelines(lines)
# f.close()

print(username.test1('training_data/159496798694412.wav'))