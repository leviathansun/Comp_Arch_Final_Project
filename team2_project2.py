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
registers[0] = {'name': "R0", 'data': 0}
registers[1] = {'name': "R1", 'data': 0}
registers[2] = {'name': "R2", 'data': 0}
registers[3] = {'name': "R3", 'data': 0}
registers[4] = {'name': "R4", 'data': 0}
registers[5] = {'name': "R5", 'data': 0}
registers[6] = {'name': "R6", 'data': 0}
registers[7] = {'name': "R7", 'data': 0}
registers[8] = {'name': "R8", 'data': 0}
registers[9] = {'name': "R9", 'data': 0}
registers[10] = {'name': "R10", 'data': 0}
registers[11] = {'name': "R11", 'data': 0}
registers[12] = {'name': "R12", 'data': 0}
registers[13] = {'name': "R13", 'data': 0}
registers[14] = {'name': "R14", 'data': 0}
registers[15] = {'name': "R15", 'data': 0}
registers[16] = {'name': "R16", 'data': 0}
registers[17] = {'name': "R17", 'data': 0}
registers[18] = {'name': "R18", 'data': 0}
registers[19] = {'name': "R19", 'data': 0}
registers[20] = {'name': "R20", 'data': 0}
registers[21] = {'name': "R21", 'data': 0}
registers[22] = {'name': "R22", 'data': 0}
registers[23] = {'name': "R23", 'data': 0}
registers[24] = {'name': "R24", 'data': 0}
registers[25] = {'name': "R25", 'data': 0}
registers[26] = {'name': "R26", 'data': 0}
registers[27] = {'name': "R27", 'data': 0}
registers[28] = {'name': "R28", 'data': 0}
registers[29] = {'name': "R29", 'data': 0}
registers[30] = {'name': "R30", 'data': 0}
registers[31] = {'name': "R31", 'data': 0}

assembledlist = []
datalist = []


class simulator(object):
    pc = 0
    break_found = False
    output_file2 = 0

    # initializer / instance attributes
    def _init_(self):
        pass

    # method that runs the Simulator
    def tycoon(self):
        memspace1 = memspace()
        out_file = open ("team2_out_sim.txt", "w")
        self.output_file2 = out_file
        cycle = 0
        self.pc = 0
        self.break_found = False

        if not assembledlist:
            self.output_file2.write("no input")
            return

        while self.break_found is False:
            if(assembledlist[self.pc][0] is not 'NOP' ):
                cycle = cycle + 1
                self.output_file2.write("=====================\n")
                self.output_file2.write("cycle:" + str(cycle) + " " + str((self.pc * 4) + 96) + "\t")

                self.choose(memspace1)
                self.regout()
            self.pc = self.pc + 1

        out_file.close()
        self.output_file2.close()

    # method that creates register output
    def regout(self):
        self.output_file2.write('\nR00:\t' + str(registers[0]['data']) + '\t' + str(registers[1]['data']) + '\t'
                                + str(registers[2]['data']) + '\t' + str(registers[3]['data']) + '\t'
                                + str(registers[4]['data']) + '\t' + str(registers[5]['data']) + '\t'
                                + str(registers[6]['data']) + '\t' + str(registers[7]['data']) + '\n')
        self.output_file2.write('R08:\t' + str(registers[8]['data']) + '\t' + str(registers[9]['data']) + '\t'
                                + str(registers[10]['data']) + '\t' + str(registers[11]['data']) + '\t'
                                + str(registers[12]['data']) + '\t' + str(registers[13]['data']) + '\t'
                                + str(registers[14]['data']) + '\t' + str(registers[15]['data']) + '\n')
        self.output_file2.write('R16:\t' + str(registers[16]['data']) + '\t' + str(registers[17]['data']) + '\t'
                                + str(registers[18]['data']) + '\t' + str(registers[19]['data']) + '\t'
                                + str(registers[20]['data']) + '\t' + str(registers[21]['data']) + '\t'
                                + str(registers[22]['data']) + '\t' + str(registers[23]['data']) + '\n')
        self.output_file2.write('R24:\t' + str(registers[24]['data']) + '\t' + str(registers[25]['data']) + '\t'
                                + str(registers[26]['data']) + '\t' + str(registers[27]['data']) + '\t'
                                + str(registers[28]['data']) + '\t' + str(registers[29]['data']) + '\t'
                                + str(registers[30]['data']) + '\t' + str(registers[31]['data']) + '\n')

        self.output_file2.write('\nData:\n')
        dataindex = 0
        while (dataindex < len(datalist)):
            if (dataindex % 8 == 0):
                self.output_file2.write(str(datalist[dataindex][0]) + ':\t' + str(datalist[dataindex][1]) + '\t')
            if (dataindex % 8 == 7):
                self.output_file2.write(str(datalist[dataindex][1]) + '\n')
            else:
                self.output_file2.write(str(datalist[dataindex][1]) + '\t')
            dataindex += 1
        self.output_file2.write('\n')


    # method that selects which instruction is being called
    def choose(self, memspace1):
        if assembledlist[self.pc][0] is 'SLL':
            memspace1.SLLmem(self.pc)
            self.SLLsim()
        elif assembledlist[self.pc][0] is 'BREAK':
            memspace1.BREAKmem(self.pc)
            self.BREAKsim()
            self.break_found = True
        elif assembledlist[self.pc][0] is 'NOP':
            memspace1.NOPmem(self.pc)
            self.NOPsim()
        elif assembledlist[self.pc][0] is 'J':
            self.Jsim()
        elif assembledlist[self.pc][0] is 'BNE':
            memspace1.BNEmem(self.pc)
            self.BNEsim()
        elif assembledlist[self.pc][0] is 'BLEZ':
            memspace1.BLEZmem(self.pc)
            self.BLEZsim()
        elif assembledlist[self.pc][0] is 'ADDI':
            memspace1.ADDImem(self.pc)
            self.ADDIsim()
        elif assembledlist[self.pc][0] is 'AND':
            memspace1.ANDmem(self.pc)
            self.ANDsim()
        elif assembledlist[self.pc][0] is 'MUL':
            memspace1.MULmem(self.pc)
            self.MULsim()
        elif assembledlist[self.pc][0] is 'LW':
            memspace1.LWmem(self.pc)
            self.LWsim()
        elif assembledlist[self.pc][0] is 'SW':
            memspace1.SWmem(self.pc)
            self.SWsim()
        elif assembledlist[self.pc][0] is 'SRL':
            memspace1.SRLmem(self.pc)
            self.SRLsim()
        elif assembledlist[self.pc][0] is 'JR':
            self.JRsim()
        elif assembledlist[self.pc][0] is 'MOVZ':
            memspace1.MOVZmem(self.pc)
            self.MOVZsim()
        elif assembledlist[self.pc][0] is 'ADD':
            memspace1.ADDmem(self.pc)
            self.ADDsim()
        elif assembledlist[self.pc][0] is 'SUB':
            memspace1.SUBmem(self.pc)
            self.SUBsim()
        elif assembledlist[self.pc][0] is 'OR':
            memspace1.ORmem(self.pc)
            self.ORsim()
        elif assembledlist[self.pc][0] is 'XOR':
            memspace1.XORmem(self.pc)
            self.XORsim()

    def SWsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '(' + str(assembledlist[self.pc][1]) + ')' + '\n')

    def LWsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '(' + str(assembledlist[self.pc][1]) + ')' + '\n')

    def SLLsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', #' +
                                str(assembledlist[self.pc][3]) + '\n')

    def SRLsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', #' +
                                str(assembledlist[self.pc][3]) + '\n')

    def MULsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '\n')

    def ANDsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '\n')

    def ORsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '\n')

    def XORsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '\n')

    def MOVsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '\n')

    def NOPsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))

    def BNEsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', #' +
                                str(assembledlist[self.pc][3]) + '\n')
        if registers[int(filter(str.isdigit,assembledlist[self.pc][1]))]['data'] != registers[int(filter(str.isdigit,assembledlist[self.pc][2]))]['data']:
            self.pc += (int(assembledlist[self.pc][3]) / 4)

    def BLEZsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', #' + str(assembledlist[self.pc][2]) + '\n')
        if registers[int(filter(str.isdigit,assembledlist[self.pc][1]))]['data'] <= 0:
            self.pc += ((int(assembledlist[self.pc][2])) / 4)

    def Jsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t#' + str(assembledlist[self.pc][1]) + '\n')
        self.pc = (int(assembledlist[self.pc][1]) -96) /4 -1

    def JRsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + '\n')
        self.pc = registers[int(filter(str.isdigit,assembledlist[self.pc][1]))]['data'] / 4 - 1

    def SUBsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '\n')

    def BREAKsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))

    def ADDsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '\n')

    def ADDIsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', #' +
                                str(assembledlist[self.pc][3]) + '\n')

    def MOVZsim(self):
        self.output_file2.write('%s' % (str(assembledlist[self.pc][0])))
        self.output_file2.write('\t' + str(assembledlist[self.pc][1]) + ', ' + str(assembledlist[self.pc][2]) + ', ' +
                                str(assembledlist[self.pc][3]) + '\n')


class memspace(object):
    def _init_(self, pc):
        pass

    def SWmem(self, pc):
        regsourcedata = registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data']
        offset = registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data']
        datalistindex = (int(assembledlist[pc][3]) - datalist[0][0] + regsourcedata + offset)/4 -2
        while (datalistindex >= len(datalist)):
            memory_location = datalist[-1][0] + 4
            datalist.append([memory_location] + [0])
        datalist[datalistindex][1] = registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data']

    def LWmem(self, pc):
        regsourcedata = registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data']
        offset = registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data']
        datalistindex = (int(assembledlist[pc][3]) - datalist[0][0] + regsourcedata + offset) / 4
        if int(datalistindex < len(datalist)):
            registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data'] = datalist[datalistindex][1]

    def MOVZmem(self, pc):
        if(registers[int(filter(str.isdigit,assembledlist[pc][3]))]['data'] == 0):
            registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data'] = registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data']

    def SLLmem(self, pc):
        shifted = registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data'] << int(assembledlist[pc][3])
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = shifted

    def SRLmem(self, pc):
        shifted = registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data'] >> int(assembledlist[pc][3])
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = shifted


    def MULmem(self, pc):
        mulvalue = registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data'] * registers[int(filter(str.isdigit,assembledlist[pc][3]))]['data']
        mulvalue = mulvalue % 32
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = mulvalue


    def ANDmem(self, pc):
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = int(registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data']) & \
                                                          int(registers[int(filter(str.isdigit,assembledlist[pc][3]))]['data'])

    def ORmem(self, pc):
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = int(registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data']) | \
                                                          int(registers[int(filter(str.isdigit,assembledlist[pc][3]))]['data'])

    def XORmem(self, pc):
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = int(registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data']) ^ \
                                                          int(registers[int(filter(str.isdigit,assembledlist[pc][3]))]['data'])

    def MOVmem(self, pc):
        pass

    def NOPmem(self, pc):
        pass

    def BNEmem(self, pc):
        pass

    def BLEZmem(self, pc):
        pass

    def Jmem(self, pc):
        pass

    def JRmem(self, pc):
        pass

    def SUBmem(self, pc):
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = \
            registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data'] - \
            registers[int(filter(str.isdigit,assembledlist[pc][3]))]['data']

    def BREAKmem(self, pc):
        pass

    def ADDmem(self, pc):
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = \
            registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data'] + \
            registers[int(filter(str.isdigit,assembledlist[pc][3]))]['data']

    def ADDImem(self, pc):
        registers[int(filter(str.isdigit,assembledlist[pc][1]))]['data'] = \
            registers[int(filter(str.isdigit,assembledlist[pc][2]))]['data'] + \
            int(assembledlist[pc][3])


class Dissasembler(object):
    # initializer / instance attributes
    def _init_(self):
        pass

    # method that runs the dissasember
    def dirty_work(self, input_name, output_name):
        input_file = open(input_name, "r")
        output_file = open(output_name, "w")
        counter = 0

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
                    assembledlist.append(['NOP'])
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
                                output_file.write('\t' + rd + ', ' + rt + ', #' + str(sa))

                                assembledlist.append([function_name] + [rd] + [rt] + [str(sa)])
                        if subtype is 1:
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rs)

                            assembledlist.append([function_name] + [rs])
                        if subtype is 2:
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rd + ', ' + rs + ', ' + rt)

                            assembledlist.append([function_name] + [rd] + [rs] + [rt])
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

                                assembledlist.append([function_name] + [str(jumpCode)])
                            if subtype is 5:
                                rs = registers[int(group1, 2)]['name']
                                rt = registers[int(group2, 2)]['name']
                                offset = int(line[16:32], 2)
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rt + ', ' + str(offset) +"(" + rs + ')' )

                                assembledlist.append([function_name] + [rs] + [rt] + [str(offset)])
                            if subtype is 6:
                                rs = registers[int(group1, 2)]['name']
                                offset = int(line[16:32], 2)*4
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rs + ', #' + str(offset))

                                assembledlist.append([function_name] + [rs] + [str(offset)])
                            if subtype is 7:
                                rs = registers[int(group1, 2)]['name']
                                rt = registers[int(group2, 2)]['name']
                                rd = registers[int(group3, 2)]['name']
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rd + ', ' + rs + ', ' + rt)

                                assembledlist.append([function_name] + [rd] + [rs] + [rt])
                            if subtype is 8:
                                rs = registers[int(group1, 2)]['name']
                                rt = registers[int(group2, 2)]['name']
                                immediate = str(self.twos_comp(int(line[16:32], 2), len(line[16:32])))
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rt + ', ' + rs + ', #' + str(immediate))

                                assembledlist.append([function_name] + [rt] + [rs] + [str(immediate)])
            else:#Output after Break
                output_file.write('%s' % (line[0:32]))
                output_file.write('\t' + (str(memory_location) + '\t' + str(self.twos_comp(int(line[0:32], 2), len(line[0:32])))))
                datalist.append([memory_location] + [self.twos_comp(int(line[0:32], 2), len(line[0:32]))])
            output_file.write("\n")
            memory_location += 4 # iterate memory location
            counter += 1

        #close out files
        input_file.close()
        output_file.close()

        #debug list
#        for i in range(len(assembledlist)):
#            for j in range(len(assembledlist[i])):
#               print(assembledlist[i][j])

    # method used to compute the 2's compliment
    def twos_comp(self, number, bitlength):
        if (number & (1 << (bitlength - 1))) != 0:#check first digit
            number = number - (1 << bitlength)
        return number


# driver for program
def run():
    dissasembler1 = Dissasembler()
    simulator1 = simulator()
    inputfilename = ""
    outputfilename = ""
    for i in range(len(sys.argv)):
        if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):#check for input file name
            inputfilename = sys.argv[i + 1]
        elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):#check for output file name
            outputfilename = sys.argv[i + 1]
            outputfilename = outputfilename + "_dis.txt"
    if not inputfilename:#default file names if not given
        inputfilename = "test2_bin.txt"
    if not outputfilename:
        outputfilename = "team2_out_dis.txt"
    dissasembler1.dirty_work(inputfilename, outputfilename)

    simulator1.tycoon()

    return


run()
