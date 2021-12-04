def main():
    with open("input.txt", "r") as file:
        count = 0
        f = file.readlines()
        for i in range(0 , len(f)-1):
            if f[i+1]:
                a = int(f[i])
                b = int(f[i+1])
                if int(f[i]) < int(f[i+1]):
                    count += 1
        print(count)


if __name__ == "__main__":
    main()