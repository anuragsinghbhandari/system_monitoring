from cpu import read_cpu, calc
from memory import readMem, show
import time, os
if __name__=="__main__":
    a = read_cpu()
    time.sleep(1)
    while True:
        b = read_cpu()
        full_data = readMem()
        show(full_data)
        calc(b,a)
        a = b
        time.sleep(1)
        os.system("clear")

