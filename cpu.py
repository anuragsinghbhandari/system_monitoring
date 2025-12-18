import re
from typing import List
from terminal_setup import console
"""
proc/stat contains data like this
for cpuN:--> user: int(user-space)
             nice: int(user-process with modified priority)
             system: int(kernal-code)
             idle: int(eating 5 star)
             iowait: int(waiting for io completion)
             irq: int(servicing hardware interrupts)
             softirq: int(servicing software interrupts)
             steal: int(time stolen by vms or clouds happens inside vms)
             guest: int(running vms)
             guest_nice: int(guest with nice priority)

each of these numbers are in integer form representing jiffy time unit. 1 jiffy = 1/HZ seconds  (here HZ is kernal constant). my kernals HZ is 100 hence 1 jiffy = 10 ms. you can check yours by typing "getconf CLK_TCK" in bash.
***NOTE :- /proc/stat contains more data, but i only showed the useful ones.
"""

user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice = range(10)

def read_cpu()-> List[List[int]]:
    """
    Function to read cpu data from proc file.
    
    Returns:
       List[List]: detail of each core at that time. 
    """
    result = []
    with open("/proc/stat", "r") as f:
            while True:
                data = f.readline()
                if data[0:3]=="cpu":
                    if re.match(r"cpu", data[0:3]):
                        result.append(list(map(int, data.split()[1:])))
                else:
                    break
    return result

def calc(b: List[List[int]], a: List[List[int]]):
    """
    Function to calculate and display the usage which is difference in data at particular  time intervals.

    Args:
        b (List[List]): current data of proc file.
        a (List[List]): previous data of proc file.

    Returns:
        None
    """
    console.print(f"[bright_cyan][bold]cpu(busy) \tuser  nice  system   idle    iowait    irq  softirq  steal  guest  guest_nice[/bold][/bright_cyan] ") 
    for i in range(len(b)):
        diff = [c - p for c , p in zip(b[i],a[i])]
        total = sum(diff)
        if total == 0:
            continue
        perc = [(each/total)*100 for each in diff]
        busy = perc[user]+perc[nice]+perc[system]+perc[irq]+perc[softirq]+perc[steal]
        if i == 0:
            console.print(f"[bright_yellow]CPU({busy:.1f}): -> [/bright_yellow] ", end = '\t')
            for j in perc:
                console.print (f"[bright_yellow]{j:.1f}[/bright_yellow]", end= '\t')
        else:
            console.print(f"CPU{i-1}",'(',end='')
            console.print(round(busy,1),end='')
            console.print("): -> ", end = '\t')
            for j in perc:
                console.print(round(j,1), end= '\t')
        console.print()


if __name__== "__main__":
    print("ok")
