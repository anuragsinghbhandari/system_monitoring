import time, os
from pynput.keyboard import Listener
from cpu import read_cpu, calc
from memory import readMem, show
from topprocess import get_top5
from terminal_setup import console
stop_flag = False
def on_press(key):
    global stop_flag
    try:
        if key.char == 'q':
            stop_flag = True
            return False
    except AttributeError:
        pass

listener = Listener(on_press=on_press)
listener.start()

a = read_cpu()
time.sleep(1)
while not stop_flag:
    b = read_cpu()
    full_data = readMem()
    show(full_data)
    get_top5()
    print("\n")
    calc(b,a)
    print("\n")

    console.print("[bright_red][bold]Press:[/bold][/bright_red]\n [red]q (quit)[/red]")
    a = b
    time.sleep(1)
    os.system("clear")


listener.join()
