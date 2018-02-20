import sys
import os

opcodes = {}
opcodes[0] = {'name': "R", 'subType': 0}
opcodes[2] = {'name': "J", 'subType': 4}
opcodes[5] = {'name': "BNE", 'subType': 5}
opcodes[6] = {'name': "BLEZ", 'subType': 6}
opcodes[8] = {'name': "ADDI", 'subType': 8}
opcodes[28] = {'name': "MUL", 'subType': 7}
opcodes[3] = {'name': "LW", 'subType': 5}
opcodes[11] = {'name': "SW", 'subType': 5}

functionCodes = {}
functionCodes[0] = {'name': "SLL", 'subType': 0}
functionCodes[2] = {'name': "SRL", 'subType': 0}
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
    31: "R31",
}


class Dissasembler(object):
    # initializer / instance attributes
    def _init_(self):
        pass

    # method that runs the dissasember
    def dirty_work(self, input_name, output_name):
        input_file = open(input_name, "r")
        output_file = open(output_name, "w")

        memory_location = 96
        break_found = False
        for line in input_file:#iterate through every line in file
            if break_found is False:
                validbit = line[0] #parse out the bits
                opcode = line[1:6]
                group1 = line[6:11]
                group2 = line[11:16]
                group3 = line[16:21]
                group4 = line[21:26]
                group5 = line[26:32]
                output_file.write(validbit + ' ' + opcode + ' ' + group1 + ' ' + group2 + ' ' + group3 + ' ' + group4
                                  + ' ' + group5 + ' ' + str(memory_location)) #space output
                if int(validbit) is 0:#check for invalid instruction
                    output_file.write(" Invalid Instruction")
                else:
                    if int(opcode, 2) is 0:#Check for R type and use function code
                        rs = registers[int(group1, 2)]
                        rt = registers[int(group2, 2)]
                        rd = registers[int(group3, 2)]
                        sa = int(group4, 2)
                        funct = int(group5, 2)
                        function_name = functionCodes[funct]['name']
                        subtype = functionCodes[funct]['subType']
                        if subtype is 0:
                            if rd is 0 and rt is 0:
                                output_file.write(' ' + "NOP")
                            else:
                                output_file.write(' ' + function_name + ' ' + rd + ', ' + rt + ', #' + str(sa))
                        if subtype is 1:
                            output_file.write(' ' + function_name + ' ' + rs)
                        if subtype is 2:
                            output_file.write(' ' + function_name + ' ' + rd + ', ' + rs + ', ' + rt)
                        if subtype is 3:
                            output_file.write(' ' + function_name)
                        if function_name is "BREAK":
                            break_found = True
                    else:#not R type instructions
                        funct = int(opcode, 2)
                        function_name = opcodes[funct]['name']
                        subtype = opcodes[funct]['subType']
                        if subtype is 4:
                            jumpCode = int(line[6:32], 2)*4
                            output_file.write(' ' + function_name + ' #' + str(jumpCode))
                        if subtype is 5:
                            rs = registers[int(group1, 2)]
                            rt = registers[int(group2, 2)]
                            offset = int(line[16:32], 2)
                            output_file.write(' ' + function_name + ' ' + rt + ', ' + str(offset) + '(' + rs + ')')
                        if subtype is 6:
                            rs = registers[int(group1, 2)]
                            offset = int(line[16:32], 2)*4
                            output_file.write(' ' + function_name + ' ' + rt + ', #' + str(offset))
                        if subtype is 7:
                            rs = registers[int(group1, 2)]
                            rt = registers[int(group2, 2)]
                            rd = registers[int(group3, 2)]
                            output_file.write(' ' + function_name + ' ' + rd + ', ' + rs + ', ' + rt)
                        if subtype is 8:
                            rs = registers[int(group1, 2)]
                            rt = registers[int(group2, 2)]
                            immediate = str(self.twos_comp(int(line[16:32], 2), len(line[16:32])))
                            output_file.write(' ' + function_name + ' ' + rt + ', ' + rs + ', #' + str(immediate))
            else:#Output after Break
                output_file.write(line[0:32])
                output_file.write(' ' + str(self.twos_comp(int(line[0:32], 2), len(line[0:32]))))
            output_file.write("\n")
            memory_location += 4 # iterate memory location
        #close out files
        input_file.close()
        output_file.close()

    # method used to compute the 2's compliment
    def twos_comp(self, number, bitlength):
        if (number & (1 << (bitlength - 1))) != 0:#check first digit
            number = number - (1 << bitlength)
        return number


# driver for program
def run():
    dissasembler1 = Dissasembler()
    inputFileName = ""
    outputFileName = ""
    for i in range(len(sys.argv)):
        if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):#check for input file name
            inputFileName = sys.argv[i + 1]
        elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):#check for output file name
            outputFileName = sys.argv[i + 1]
            outputFileName = outputFileName + ".txt"
    if not inputFileName:#default file names if not given
        inputFileName = "test1_bin.txt"
    if not outputFileName:
        outputFileName = "team2_out.txt"
    dissasembler1.dirty_work(inputFileName, outputFileName)

    return


run()