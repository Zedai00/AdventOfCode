import sys

def main():
    with open(f"{sys.path[0]}/input.txt", "r") as file:
        count = 0
        f = file.readlines()
        for i in range(0, len(f)-3):
            a = int(f[i]) + int(f[i+1]) + int(f[i+2])
            b = int(f[i+1]) + int(f[i+2]) + int(f[i+3])
            if b > a:
                count += 1
        return print(count)

if __name__ == "__main__":
    main()