import sys


with open(f"{sys.path[0]}/input.txt", "r") as file:
    h, d = 0, 0
    file = file.readlines()
    for i in range(0, len(file)):
        steps = file[i].split()
        if "forward" in steps:
            h += int(steps[1])
        elif "up" in steps:
            d -= int(steps[1])
        elif "down" in steps:
            d += int(steps[1])
        else:
            break
    print(h*d)
