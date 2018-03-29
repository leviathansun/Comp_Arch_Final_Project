import sys
import os

#dictionary of opcodes that relate their name,binary code, and a subtype used to identify their output
opcodes = {}
opcodes[0] = {'name': "R", 'subType': 0}
opcodes[2] = {'name': "J", 'subType': 4}
opcodes[5] = {'name': "BNE", 'subType': 5}
opcodes[6] = {'name': "BLEZ", 'subType': 6}
opcodes[8] = {'name': "ADDI", 'subType': 8}
opcodes[28] = {'name': "MUL", 'subType': 7}
opcodes[3] = {'name': "LW", 'subType': 5}
opcodes[11] = {'name': "SW", 'subType': 5}

#dictionary of Function codes that relate their name,binary code, and a subtype used to identify their output
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

#list of all registers
registers = {}
registers[0] = {'name': "RO", 'data': 0}
registers[1] = {'name': "R1", 'data': 0}
registers[2] = {'name': "R2", 'data': 0}
registers[3] = {'name': "R3", 'data': 0}
registers[4] = {'name': "R4", 'data': 0}
registers[5] = {'name': "R5", 'data': 0}
registers[6] = {'name': "R6", 'data': 0}
registers[7] = {'name': "R7", 'data': 0}
registers[8] = {'name': "R8", 'data': 0}
registers[9] = {'name': "R9", 'data': 0}
registers[10] = {'name': "R1O", 'data': 0}
registers[11] = {'name': "R11", 'data': 0}
registers[12] = {'name': "R12", 'data': 0}
registers[13] = {'name': "R13", 'data': 0}
registers[14] = {'name': "R14", 'data': 0}
registers[15] = {'name': "R15", 'data': 0}
registers[16] = {'name': "R16", 'data': 0}
registers[17] = {'name': "R17", 'data': 0}
registers[18] = {'name': "R18", 'data': 0}
registers[19] = {'name': "R19", 'data': 0}
registers[20] = {'name': "R2O", 'data': 0}
registers[21] = {'name': "R21", 'data': 0}
registers[22] = {'name': "R22", 'data': 0}
registers[23] = {'name': "R23", 'data': 0}
registers[24] = {'name': "R24", 'data': 0}
registers[25] = {'name': "R25", 'data': 0}
registers[26] = {'name': "R26", 'data': 0}
registers[27] = {'name': "R27", 'data': 0}
registers[28] = {'name': "R28", 'data': 0}
registers[29] = {'name': "R29", 'data': 0}
registers[30] = {'name': "R3O", 'data': 0}
registers[31] = {'name': "R31", 'data': 0}

assembledlist = []

class simulator(object):

    #initializer / instance attributes
    def _init_(self):
        pass

    #method that runs the Simulator
    def tycoon(self, opcode, subtype, function_name):
        memspace1 = memspace()
        output_file2 = open ("team2_out_sim.txt", "w")


    def SWsim(self):
        pass

    def LWsim(self):
        pass

    def SLLsim(self):
        pass

    def SRLsim(self):
        pass

    def MULsim(self):
        pass

    def ANDsim(self):
        pass

    def ORsim(self):
        pass

    def XORsim(self):
        pass

    def MOVsim(self):
        pass

    def NOPsim(self):
        pass

    def BNEsim(self):
        pass

    def BLEZsim(self):
        pass

    def Jsim(self):
        pass

    def JRsim(self):
        pass

    def SUBsim(self):
        pass

    def BREAKsim(self):
        pass

    def ADDsim(self):
        pass

    def Rsim(self):
        pass


class memspace(object):
    def _init_(self):
        pass

    def SWmem(self):
        pass

    def LWmem(self):
        pass

    def SLLmem(self):
        pass

    def SRLmem(self):
        pass

    def MULmem(self):
        pass

    def ANDmem(self):
        pass

    def ORmem(self):
        pass

    def XORmem(self):
        pass

    def MOVmem(self):
        pass

    def NOPmem(self):
        pass

    def BNEmem(self):
        pass

    def BLEZmem(self):
        pass

    def Jmem(self):
        pass

    def JRmem(self):
        pass

    def SUBmem(self):
        pass

    def BREAKmem(self):
        pass

    def ADDmem(self):
        pass

    def Rmem(self):
        pass


class Dissasembler(object):
    # initializer / instance attributes
    def _init_(self):
        pass

    # method that runs the dissasember
    def dirty_work(self, input_name, output_name):
        input_file = open(input_name, "r")
        output_file = open(output_name, "w")
        linecount = 0;

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
                                  + ' ' + group5 + '\t' + str(memory_location) + '\t') #space output
                if int(validbit) is 0:#check for invalid instruction
                    output_file.write("Invalid Instruction")
                else:
                    if int(opcode, 2) is 0:#Check for R type and use function code
                        rs = registers[int(group1, 2)]['name']
                        rt = registers[int(group2, 2)]['name']
                        rd = registers[int(group3, 2)]['name']
                        sa = int(group4, 2)
                        funct = int(group5, 2)
                        function_name = functionCodes[funct]['name']
                        subtype = functionCodes[funct]['subType']
                        if subtype is 0:
                            if (rd == registers[0]['name']) and (rt == registers[0]['name']):
                                output_file.write('%s' % ('NOP'))

                                assembledlist.append(['NOP'])
                            else:
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rd + ' ' + rt + ' ' + str(sa))

                                assembledlist.append([function_name + ' ' + rd + ' ' + rt + ' ' + str(sa)])
                        if subtype is 1:
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rs)

                            assembledlist.append([function_name + ' ' + rs])
                        if subtype is 2:
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rd + ', ' + rs + ', ' + rt)

                            assembledlist.append([function_name + ' ' + rd + ' ' + rs + ' ' + rt])
                        if subtype is 3:
                            output_file.write('%s' % (function_name))

                            assembledlist.append([function_name])
                        if function_name is "BREAK":
                            break_found = True
                    else:#not R type instructions
                        if (int(opcode, 2) in opcodes) == True:
                            funct = int(opcode, 2)
                            function_name = opcodes[funct]['name']
                            subtype = opcodes[funct]['subType']
                            if subtype is 4:
                                jumpCode = int(line[6:32], 2)*4
                                output_file.write('%s' % (function_name))
                                output_file.write('\t#' + str(jumpCode))

                                assembledlist.append([function_name + ' ' + str(jumpCode)])
                            if subtype is 5:
                                rs = registers[int(group1, 2)]['name']
                                rt = registers[int(group2, 2)]['name']
                                offset = int(line[16:32], 2)*4
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rs + ', ' + rt + ', #' + str(offset))

                                assembledlist.append([function_name + ' ' + rs + ' ' + rt + ' ' + str(offset)])
                            if subtype is 6:
                                rs = registers[int(group1, 2)]['name']
                                offset = int(line[16:32], 2)*4
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rs + ', #' + str(offset))

                                assembledlist.append([function_name + ' ' + rs + ' ' + str(offset)])
                            if subtype is 7:
                                rs = registers[int(group1, 2)]['name']
                                rt = registers[int(group2, 2)]['name']
                                rd = registers[int(group3, 2)]['name']
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rd + ', ' + rs + ', ' + rt)

                                assembledlist.append([function_name + ' ' + rd + ' ' + rs + ' ' + rt])
                            if subtype is 8:
                                rs = registers[int(group1, 2)]['name']
                                rt = registers[int(group2, 2)]['name']
                                immediate = str(self.twos_comp(int(line[16:32], 2), len(line[16:32])))
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rt + ', ' + rs + ', #' + str(immediate))

                                assembledlist.append([function_name + ' ' + rt + ' ' + rs + ' ' + str(immediate)])
            else:#Output after Break
                output_file.write('%s' % (line[0:32]))
                output_file.write('\t' + (str(memory_location) + '\t' + str(self.twos_comp(int(line[0:32], 2), len(line[0:32])))))
            output_file.write("\n")
            memory_location += 4 # iterate memory location
        #close out files
        input_file.close()
        output_file.close()

        #debug list
        #for i in range(len(assembledlist)):
        #    for j in range(len(assembledlist[i])):
         #       print(assembledlist[i][j])
          #  print("\n")

    # method used to compute the 2's compliment
    def twos_comp(self, number, bitlength):
        if (number & (1 << (bitlength - 1))) != 0:#check first digit
            number = number - (1 << bitlength)
        return number


# driver for program
def run():
    dissasembler1 = Dissasembler()
    inputfilename = ""
    outputfilename = ""
    for i in range(len(sys.argv)):
        if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):#check for input file name
            inputfilename = sys.argv[i + 1]
        elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):#check for output file name
            outputfilename = sys.argv[i + 1]
            outputfilename = outputfilename + "_dis.txt"
    if not inputfilename:#default file names if not given
        inputfilename = "test1_bin.txt"
    if not outputfilename:
        outputfilename = "team2_out_dis.txt"
    dissasembler1.dirty_work(inputfilename, outputfilename)

    return


run()
