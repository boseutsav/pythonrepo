import subprocess
from os import popen

#subprocess.call([r"D:\Documents\LEARNING\Professional_Testing\Tutorial videos\python\practice\testbat.bat"])
p = subprocess.run(['dir'])
print(p.stdout)
# with popen("dir") as x:
#     f = x.readlines()
#     for each in f:
#         print(each,end="")