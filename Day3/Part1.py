import sys

with open(f"{sys.path[0]}/input.txt") as file:
    file = file.readlines()
    gammaBits, epsilonBits = "", ""
    for j in range(0, len(file[0])-1):
        zeroCount, oneCount = 0, 0
        for i in file:
            i = i.strip()
            if i[j] == '0':
                zeroCount += 1
            elif i[j] == '1':
                oneCount += 1
            else:
                break
        if zeroCount > oneCount:
            gammaBits = gammaBits + '0'
        else:
            gammaBits = gammaBits + '1'
        if zeroCount < oneCount:
            epsilonBits = epsilonBits + '0'
        else:
            epsilonBits = epsilonBits + '1'         
    gammaRate = int(gammaBits, 2)
    epsilonRate = int(epsilonBits, 2)
    power = gammaRate * epsilonRate
    print(f"{power}") 
            
            

    