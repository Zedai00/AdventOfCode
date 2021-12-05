import sys

with open(f"{sys.path[0]}/input.txt", "r") as file:
    h, d, a = 0, 0, 0
    file = file.readlines()
    for i in range(0, len(file)):
        steps = file[i].split()
        if "forward" in steps:
            if a:
                h += int(steps[1])
                d += int(a) * int(steps[1])
            else:
                h += int(steps[1])
        elif "up" in steps:
            a -= int(steps[1])
        elif "down" in steps:
            a += int(steps[1])
        else:
            break
        print(h*d)
