import os
import time
from typing import Dict
from terminal_setup import console


def readMem():
    with open("/proc/meminfo", "r") as f:
        data = f.readlines()
        full_data = dict()
        for each in data:
            result = each.split(" ")
            name = result[0][:-1]
            value = 0
            for i in result:
                if i.isnumeric():
                    value = int(i)
            full_data[name] = value
    return full_data


def kb2gb(KB: int) -> float:
    """Code to convert KB int GB.

    ARGS:
        KB (int): size in KB.

    RETURNS:
        GB (int): size in GB.
    """
    return round(KB / (1024 * 1024), 2)


def show(full_data: Dict[str, int]):
    total = kb2gb(full_data["MemTotal"])
    used = kb2gb(full_data["MemTotal"] - full_data["MemAvailable"])
    console.print("[bright_cyan][bold]Memory:[/bold][/bright_cyan]")
    console.print("  Total:", total, "GB")
    console.print("  Used:", used, "GB")
    console.print("  Free:", kb2gb(full_data["MemAvailable"]), "GB")
    console.print("  Used %:", round((used / total) * 100, 2), "%")
    console.print("  Buffers:", kb2gb(full_data["Buffers"]), "GB")
    console.print("  Cached:", kb2gb(full_data["Cached"]), "GB")
    console.print("  SwapCached:", kb2gb(full_data["SwapCached"]), "GB")


if __name__ == "__main__":
    while True:
        os.system("clear")
        full_data = readMem()
        show(full_data)
        time.sleep(1)
