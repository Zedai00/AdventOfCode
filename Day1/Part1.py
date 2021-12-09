import sys

with open(f"{sys.path[0]}/input.txt", "r") as file:
    f = file.readlines()
    count = 0
    for i in range(0, len(f)-1):
        if int(f[i]) < int(f[i+1]):
            count += 1
    print(count)
