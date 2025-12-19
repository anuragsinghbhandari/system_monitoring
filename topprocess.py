import os
from terminal_setup import console

def kb2mb(KB):
    return round((KB/1024),2)

def get_top5():
    dirs = os.listdir("/proc")
    pids = []
    for each in dirs:
        if each.isnumeric():
            pids.append(each)

    # console.print(pids)
    result = {}
    for eachpid in pids:
        with open(f"/proc/{eachpid}/status") as f:
            data = f.readlines()
            global each_data
            each_data = {}
            for j in data:
                pdata = j.split()
                try:
                    each_data[pdata[0][:-1]] = pdata[1]
                except:
                    continue
            if 'RssAnon' in each_data.keys():
                result[eachpid] = {"Name": each_data["Name"], "RssAnon": kb2mb(int(each_data['RssAnon']))}

    top5 = sorted(
        result.items(),
        key = lambda item: item[1]['RssAnon'],
        reverse=True
        )[:5]
    console.print(f"[bright_cyan][bold]Top 5 Process by Memory[/bold][/bright_cyan]")
    console.print(f"PID \t Name \t Mem (Anon)")
    for each in top5:
        console.print(each[0],'\t',each[1]["Name"],'\t\t\t\t\t',each[1]["RssAnon"])
