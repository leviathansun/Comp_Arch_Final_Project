import sys
import os

opcodes = {
    0: "rtyp",
    2: "J",
    5: "BNE",
    6: "BLEZ",
    8: "ADDI",
    28: "MUL",
    35: "LW",
    43: "SW"
}

functionCodes = {}
functionCodes[0] = {'name': "SLL", 'subType': 0}
functionCodes[2] = {'name': "SLR", 'subType': 0}
functionCodes[8] = {'name': "JR", 'subType': 1}
functionCodes[10] = {'name': "MOVZ", 'subType': 2}
functionCodes[13] = {'name': "BREAK", 'subType': 3}
functionCodes[32] = {'name': "ADD", 'subType': 2}
functionCodes[34] = {'name': "SUB", 'subType': 2}
functionCodes[36] = {'name': "AND", 'subType': 2}
functionCodes[37] = {'name': "OR", 'subType': 2}
functionCodes[38] = {'name': "XOR", 'subType': 2}

registers = {
    0: "R0",
    1: "R1",
    2: "R2",
    3: "R3",
    4: "R4",
    5: "R5",
    6: "R6",
    7: "R7",
    8: "R8",
    9: "R9",
    10: "R10",
    11: "R11",
    12: "R12",
    13: "R13",
    14: "R14",
    15: "R15",
    16: "R16",
    17: "R17",
    18: "R18",
    19: "R19",
    20: "R20",
    21: "R21",
    22: "R22",
    23: "R23",
    24: "R24",
    25: "R25",
    26: "R26",
    27: "R27",
    28: "R28",
    29: "R29",
    30: "R30",
    31: "R31"
}

inputFile = open("test1_bin.txt", "r")
print("Welcome to this Bullshit")

memoryLocation = 96
breakFound = False
for line in inputFile:
    if breakFound is False:
        validbit = line[0]
        opcode = line[1:6]
        group1 = line[7:11]
        group2 = line[11:16]
        group3 = line[16:21]
        group4 = line[21:25]
        group5 = line[25:32]
        sys.stdout.write(validbit + ' ' + opcode + ' ' + group1 + ' ' + group2 + ' ' + group3 + ' ' + group4 \
                         + ' ' + group5 + ' ' + str(memoryLocation))
        if int(validbit) is 0:
            sys.stdout.write(" Invalid Instruction")
        else:
            if int(opcode, 2) is 0:
                rs = registers[int(group1, 2)]
                rt = registers[int(group2, 2)]
                rd = registers[int(group3, 2)]
                sa = int(group4, 2)
                function = int(group5, 2)
                functionname = functionCodes[function]['name']
                subtype = functionCodes[function]['subType']
                if subtype is 0:
                    if rd is 0 and rt is 0:
                        sys.stdout.write(' ' + "NOP")
                    else:
                        sys.stdout.write(' ' + functionname + ' ' + rd + ', ' + rt + ', #' + str(sa))
                if subtype is 1:
                    sys.stdout.write(' ' + functionname + ' ' + rs)
                if subtype is 2:
                    sys.stdout.write(' ' + functionname + ' ' + rd + ', ' + rs + ', ' + rt)
                if subtype is 3:
                    sys.stdout.write(' ' + functionname)
                if functionname is "BREAK":
                    breakFound = True

        sys.stdout.write("\n")
    else:
        sys.stdout.write(line)
    memoryLocation += 4

inputFile.close()
