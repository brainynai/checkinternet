import subprocess
import ctypes
from time import sleep

foundIt = False

while(foundIt == False):
    p = subprocess.Popen('ping www.google.com -n 1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    #Ping yourself - for testing
    #p = subprocess.Popen('ping localhost -n 1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    output = "".join([line.decode('UTF-8').strip() for line in p.stdout.readlines()])

    if "Received = 1" in output and "unreachable" not in output:
        ctypes.windll.user32.MessageBoxW(0, "Interwebs found", "Internet Alert", 8192)
        foundIt = True
        break

    retval = p.wait()
    sleep(10)
