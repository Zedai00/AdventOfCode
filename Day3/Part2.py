import sys
import operator

oGS, cO2 = "", ""


def main(bits, r, v):
    if len(bits) > 1:
        zeroBits, oneBits = 0, 0
        for j in bits:
            if j[r] == "0":
                zeroBits += 1
            else:
                oneBits += 1
        newBIts = []
        if v(zeroBits, oneBits):
            for j in bits:
                if j[r] == "0":
                    newBIts.append(j)
            return main(newBIts, r+1, v)
        elif v(oneBits, zeroBits):
            for j in bits:
                if j[r] == "1":
                    newBIts.append(j)
            return main(newBIts, r+1, v)
        elif oneBits == zeroBits:
            if v == operator.gt:
                for j in bits:
                    if j[r] == "1":
                        newBIts.append(j)
            else:
                for j in bits:
                    if j[r] == "0":
                        newBIts.append(j)
            return main(newBIts, r+1, v)
        else:
            return main(newBIts, r+1, v)
    else:
        return int(bits[0], 2)


if __name__ == "__main__":
    with open(f"{sys.path[0]}/input.txt") as file:
        file = file.readlines()
        oGS = main(file, 0, operator.gt)
        cO2 = main(file, 0, operator.lt)
        print(oGS * cO2)