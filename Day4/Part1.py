import sys

def main(file):
    numbers = file[0]
    grids = [[]]
    i = 0
    for j in range(2, len(file)-1, 6):
        grids[i] = file[j:j+5]
        grids.append([])
        i += 1
    print(grids)


if __name__ == "__main__":
    with open(f"{sys.path[0]}/input.txt") as input:
        file = []
        for i in input:
            file.append(i.strip())
        main(file)