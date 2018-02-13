print("Testing the github update process")
inputFile = open("test1_bin.txt", "r")
print("Hello")
dataList = inputFile.read().splitlines()
for i in range (0 , len(dataList)):
    print(dataList[i])


inputFile.close()
