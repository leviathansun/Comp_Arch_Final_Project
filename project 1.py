print("Welcome to this Bullshit")
inputFile = open("test1_bin.txt", "r")
dataList = inputFile.read().splitlines()
for i in range (0 , len(dataList)):
    print(dataList[i])


inputFile.close()
