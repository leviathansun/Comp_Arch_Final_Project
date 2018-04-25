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

datalist = []
instruction = []
opcodelist = []
instrName = []
address = []
validInstr = []
arg1 = []
arg2 = []
arg3 = []
destReg = []
src1Reg = []
src2Reg = []
invalid = -1
numInstrs = 0


class Dissasembler(object):
    # initializer / instance attributes
    def _init_(self):
        pass

    # method that runs the dissasember
    def dirty_work(self, input_name, output_name):
        global invalid
        global numInstrs
        PC = 96
        input_file = open(input_name, "r")
        output_file = open(output_name, "w")
        counter = 0

        memory_location = 96
        break_found = False
        for line in input_file:#iterate through every line in file
            if break_found is False:
                validbit = line[0] #parse out the bits
                opcode = line[1:6]
                opcodelist.append(int(opcode, 2))
                validInstr.append(int(validbit))
                instruction.append(line[0:32])
                group1 = line[6:11]
                group2 = line[11:16]
                group3 = line[16:21]
                group4 = line[21:26]
                group5 = line[26:32]
                output_file.write(validbit + ' ' + opcode + ' ' + group1 + ' ' + group2 + ' ' + group3 + ' ' + group4
                                  + ' ' + group5 + '\t' + str(memory_location) + '\t') #space output
                if int(validbit) is 0:#check for invalid instruction
                    output_file.write("Invalid Instruction")

                    instrName.append('Invalid Instruction')
                    address.append(PC + (counter * 4))
                    arg1.append(int(group1, 2))
                    arg2.append(int(group2, 2))
                    arg3.append(' ')
                    destReg.append(invalid)
                    invalid -= 1
                    src1Reg.append(invalid)
                    invalid -= 1
                    src2Reg.append(invalid)
                    invalid -= 1
                    numInstrs += 1
                    counter += 1
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

                                instrName.append('NOP')
                                address.append(PC + (counter * 4))
                                arg1.append(int(group1, 2))
                                arg2.append(int(group2, 2))
                                arg3.append('')
                                destReg.append(invalid)
                                invalid -= 1
                                src1Reg.append(invalid)
                                invalid -= 1
                                src2Reg.append(invalid)
                                invalid -= 1
                                numInstrs += 1
                                counter += 1
                            else:
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rd + ', ' + rt + ', #' + str(sa))

                                instrName.append(function_name)
                                address.append(PC + (counter * 4))
                                arg1.append(int(group2, 2))
                                arg2.append(int(group3, 2))
                                arg3.append(int(group4, 2))
                                destReg.append(arg2[counter])
                                src1Reg.append(arg1[counter])
                                src2Reg.append(invalid)
                                invalid -= 1
                                numInstrs += 1
                                counter += 1

                        if subtype is 1:
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rs)

                            instrName.append(function_name)
                            address.append(PC + (counter * 4))
                            arg1.append(int(group1, 2))
                            arg2.append(0)
                            arg3.append(0)
                            destReg.append(invalid)
                            invalid -= 1
                            src1Reg.append(arg1[counter])
                            src2Reg.append(invalid)
                            invalid -= 1
                            numInstrs += 1
                            counter += 1

                        if subtype is 2:
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rd + ', ' + rs + ', ' + rt)

                            instrName.append(function_name)
                            address.append(PC + (counter * 4))
                            arg1.append(int(group1, 2))
                            arg2.append(int(group2, 2))
                            arg3.append(int(group3, 2))
                            destReg.append(arg3[counter])
                            src1Reg.append(arg1[counter])
                            src2Reg.append(arg2[counter])
                            numInstrs += 1
                            counter += 1

                        if subtype is 3:
                            output_file.write('%s' % (function_name))

                            instrName.append('BREAK')
                            address.append(PC + (counter * 4))
                            arg1.append(int(group1, 2))
                            arg2.append(int(group2, 2))
                            arg3.append(0)
                            destReg.append(invalid)
                            invalid -= 1
                            src1Reg.append(invalid)
                            invalid -= 1
                            src2Reg.append(invalid)
                            invalid -= 1
                            numInstrs += 1
                            counter += 1
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

                                instrName.append(function_name)
                                address.append(PC + (counter * 4))
                                arg1.append(jumpCode)
                                arg2.append(0)
                                arg3.append(0)
                                destReg.append(invalid)
                                invalid -= 1
                                src1Reg.append(invalid)
                                invalid -= 1
                                src2Reg.append(invalid)
                                invalid -= 1
                                numInstrs += 1
                                counter += 1

                        if subtype is 5:
                                rs = registers[int(group1, 2)]['name']
                                rt = registers[int(group2, 2)]['name']
                                offset = int(line[16:32], 2)
                                output_file.write('%s' % (function_name))
                                output_file.write('\t' + rt + ', ' + str(offset) +"(" + rs + ')' )

                                instrName.append(function_name)
                                address.append(PC + (counter * 4))
                                arg1.append(int(group1, 2))
                                arg2.append(int(group2, 2))
                                arg3.append(offset)
                                if funct == 11:
                                    destReg.append(invalid)
                                    invalid -= 1
                                    src1Reg.append(arg2[counter])
                                    src2Reg.append(arg1[counter])
                                elif funct == 3:
                                    destReg.append(arg2[counter])
                                    src1Reg.append(arg1[counter])
                                    src2Reg.append(invalid)
                                    invalid -= 1
                                elif funct == 5:
                                    destReg.append(invalid)
                                    invalid -= 1
                                    src1Reg.append(arg1[counter])
                                    src2Reg.append(arg2[counter])
                                numInstrs += 1
                                counter += 1
                        if subtype is 6:
                            rs = registers[int(group1, 2)]['name']
                            offset = int(line[16:32], 2)*4
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rs + ', #' + str(offset))

                            instrName.append(function_name)
                            address.append(PC + (counter * 4))
                            arg1.append(int(group1, 2))
                            arg2.append(int(group2, 2))
                            arg3.append(offset)
                            destReg.append(invalid)
                            invalid -= 1
                            src1Reg.append(arg1[counter])
                            src2Reg.append(invalid)
                            invalid -= 1
                            numInstrs += 1
                            counter += 1

                        if subtype is 7:
                            rs = registers[int(group1, 2)]['name']
                            rt = registers[int(group2, 2)]['name']
                            rd = registers[int(group3, 2)]['name']
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rd + ', ' + rs + ', ' + rt)

                            instrName.append(function_name)
                            address.append(PC + (counter * 4))
                            arg1.append(int(group1, 2))
                            arg2.append(int(group2, 2))
                            arg3.append(int(group3, 2))
                            destReg.append(arg3[counter])
                            src1Reg.append(arg1[counter])
                            src2Reg.append(arg2[counter])
                            numInstrs += 1
                            counter += 1

                        if subtype is 8:
                            rs = registers[int(group1, 2)]['name']
                            rt = registers[int(group2, 2)]['name']
                            immediate = str(self.twos_comp(int(line[16:32], 2), len(line[16:32])))
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rt + ', ' + rs + ', #' + str(immediate))

                            instrName.append('ADDI')
                            address.append(PC + (counter * 4))
                            arg1.append(int(group1, 2))
                            arg2.append(int(group2, 2))
                            arg3.append(int(group3, 2))
                            arg3[counter] = int(immediate)
                            destReg.append(arg2[counter])
                            src1Reg.append(arg1[counter])
                            src2Reg.append(invalid)
                            invalid -= 1
                            numInstrs += 1
                            counter += 1

            else:#Output after Break
                output_file.write('%s' % (line[0:32]))
                output_file.write('\t' + (str(memory_location) + '\t' + str(self.twos_comp(int(line[0:32], 2), len(line[0:32])))))
                datalist.append(self.twos_comp(int(line[0:32], 2), len(line[0:32])))
                address.append(PC + (counter * 4))
                counter += 1
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

class writeBack:
    def __init__(self):
        pass
    def run(self):
        if(pipline.postALUBuff[1] != -1):
            pipline.registers[pipline.destReg[pipline.postALUBuff[1]]] = pipline.postALUBuff[0]
            pipline.postALUBuff[0] = -1
            pipline.postALUBuff[1] = -1
        if(pipline.postMemBuff[1] != -1):
            pipline.registers[pipline.destReg[pipline.postMemBuff[1]]] = pipline.postMemBuff[0]
            pipline.postMemBuff[0] = -1
            pipline.postMemBuff[1] = -1

class arithmeticLogicUnit:

    def __init__(self):
        pass

    def run(self):
        if (pipline.preALUBuff[0] != -1):
            i = pipline.preALUBuff[0]
            pipline.postALUBuff[1] = i
            if (pipline.instrName[i] == 'SLL'):
                pipline.postALUBuff[0] = pipline.registers[pipline.src1Reg[i]] * pow(2, pipline.args3[i])
            elif (pipline.instrName[i] == 'SRL'):
                pipline.postALUBuff[0] = pipline.registers[pipline.src1Reg[i]] / pow(2, pipline.args3[i])
            elif (pipline.instrName[i] == 'ADDI'):
                pipline.postALUBuff[0] = int(pipline.registers[pipline.src1Reg[i]]) + pipline.args3[i]
            elif (pipline.instrName[i] == 'MUL'):
                pipline.postALUBuff[0] = pipline.registers[pipline.src1Reg[i] * pipline.registers[pipline.src2Reg[i]]]
            elif (pipline.instrName[i] == 'OR'):
                pipline.postALUBuff[0] = pipline.registers[pipline.src1Reg[i] | pipline.registers[pipline.src2Reg[i]]]
            elif (pipline.instrName[i] == 'AND'):
                pipline.postALUBuff[0] = pipline.registers[pipline.src1Reg[i] & pipline.registers[pipline.src2Reg[i]]]
            elif (pipline.instrName[i] == 'SUB'):
                pipline.postALUBuff[0] = pipline.registers[pipline.src1Reg[i] - pipline.registers[pipline.src2Reg[i]]]
            elif (pipline.instrName[i] == 'ADD'):
                pipline.postALUBuff[0] = pipline.registers[pipline.src1Reg[i]] + pipline.registers[pipline.src2Reg[i]]
            elif (pipline.instrName[i] == 'XOR'):
                pipline.postALUBuff[0] = pipline.registers[pipline.src1Reg[i]] ^ pipline.registers[pipline.src2Reg[i]]
            elif (pipline.instrName[i] == 'MOVZ'):
                if (pipline.src2Reg[i] == 0):
                    pipline.postALUBuff[0] = pipline.src1Reg[i]
            pipline.preALUBuff[0] = pipline.preALUBuff[1]
            pipline.preALUBuff[1] = -1
        else:
            pass

class memWrite:
    def __init__(self):
        pass
    def run(self):
        if(pipline.preMemBuff[0] != -1):
            i = pipline.preMemBuff[0]
            hit = False
            if(pipline.instrName[i] == 'LW'):
                address = pipline.args3[i] + pipline.registers[pipline.src1Reg[i]]
                hit, data = pipline.cache.accessMemory(pipline.getIndexOfMemAddress(address),-1,False,0)

            elif(pipline.instrName[i] == 'SW'):
                address = pipline.args3[i] + pipline.registers[pipline.src2Reg[i]]
                hit, data = pipline.cache.accessMemory(pipline.getIndexOfMemAddress(address), -1, True, pipline.registers[pipline.src1Reg[i]])

            if(hit):

                if pipline.instrName[i] == 'LW':
                    pipline.postMemBuff[0] = int(data)
                    pipline.postMemBuff[1] = i

                pipline.preMemBuff[0] = pipline.preMemBuff[1]
                pipline.preMemBuff[1] = -1


class issueUnit:
    def __init__(self):
        pass

    def run(self):
        issueMe = True
        numIssued = 0
        numInPreIssueBuff = 0
        currIndex = -1
        current = 0

        for i in range(4):
            if (pipline.preIssueBuff[i] != -1):
                numInPreIssueBuff += 1

        ##WAR CHECK
        while (numIssued < 2 and numInPreIssueBuff > 0 and current < numInPreIssueBuff):
            issueMe = True
            currIndex = pipline.preIssueBuff[current]
            ## CHECK FOR ROOM IN BUFFERS
            if pipline.isMemOp(currIndex) and not -1 in pipline.preMemBuff:
                issueMe = False
            elif not pipline.isMemOp(currIndex) and not -1 in pipline.preALUBuff:
                issueMe = False

            ## WAR CHECK
            if current > 0:
                for i in range(0, current):
                    if (pipline.destReg[currIndex] == pipline.src1Reg[pipline.preIssueBuff[i]] or pipline.destReg[
                        currIndex] == pipline.src2Reg[pipline.preIssueBuff[i]]):
                        issueMe = False
                        # break
            if pipline.isMemOp(currIndex):
                for i in range(0, len(pipline.preMemBuff)):
                    if pipline.preMemBuff[i] != -1:
                        if pipline.destReg[currIndex] == pipline.src1Reg[pipline.preMemBuff[i]] or pipline.destReg[
                            currIndex] == pipline.src2Reg[pipline.preMemBuff[i]]:
                            issueMe = False
                            # break
            else:  # is ALU op
                for i in range(0, len(pipline.preALUBuff)):
                    if pipline.preALUBuff[i] != -1:
                        if pipline.destReg[currIndex] == pipline.src1Reg[pipline.preALUBuff[i]] or pipline.destReg[
                            currIndex] == pipline.src2Reg[pipline.preALUBuff[i]]:
                            issueMe = False
                            # break
            ## RAW CHECK
            if current > 0:
                for i in range(0, current):
                    if (pipline.src1Reg[currIndex] == pipline.destReg[pipline.preIssueBuff[i]] or pipline.src2Reg[
                        currIndex] == pipline.destReg[pipline.preIssueBuff[i]]):
                        issueMe = False
                        # break

            for i in range(0, len(pipline.preMemBuff)):
                if pipline.preMemBuff[i] != -1:
                    if pipline.src1Reg[currIndex] == pipline.destReg[pipline.preMemBuff[i]] or pipline.src2Reg[
                        currIndex] == pipline.destReg[pipline.preMemBuff[i]]:
                        issueMe = False
                        # break
            for i in range(0, len(pipline.preALUBuff)):
                if pipline.preALUBuff[i] != -1:
                    if pipline.src1Reg[currIndex] == pipline.destReg[pipline.preALUBuff[i]] or pipline.src2Reg[
                        currIndex] == pipline.destReg[pipline.preALUBuff[i]]:
                        issueMe = False
                        # break

            if pipline.postALUBuff[1] != -1:
                if pipline.src1Reg[currIndex] == pipline.destReg[pipline.postALUBuff[1]] or pipline.src2Reg[
                    currIndex] == pipline.destReg[pipline.postALUBuff[1]]:
                    issueMe = False
            if pipline.postMemBuff[1] != -1:
                if pipline.src1Reg[currIndex] == pipline.destReg[pipline.postMemBuff[1]] or pipline.src2Reg[
                    currIndex] == pipline.destReg[pipline.postMemBuff[1]]:
                    issueMe = False

            ## WAW CHECK
            for i in range(0, current):
                if pipline.destReg[currIndex] == pipline.destReg[pipline.preIssueBuff[i]]:
                    issueMe = False

            for i in range(0, len(pipline.preMemBuff)):
                if pipline.preMemBuff[i] != -1:
                    if pipline.destReg[currIndex] == pipline.destReg[pipline.preMemBuff[i]]:
                        issueMe = False
            for i in range(0, len(pipline.preALUBuff)):
                if pipline.preALUBuff[i] != -1:
                    if pipline.destReg[currIndex] == pipline.destReg[pipline.preALUBuff[i]]:
                        issueMe = False
            if pipline.postALUBuff[1] != -1:
                if pipline.destReg[currIndex] == pipline.destReg[pipline.postALUBuff[1]]:
                    issueMe = False
            if pipline.postMemBuff[1] != -1:
                if pipline.destReg[currIndex] == pipline.destReg[pipline.postMemBuff[1]]:
                    issueMe = False

            if (pipline.instrName[currIndex] == 'LW'):
                for i in range(0, current):
                    if pipline.instrName[pipline.preIssueBuff[i]] == 'SW':
                        issueMe = False

            if issueMe:
                numIssued += 1
                if pipline.isMemOp(currIndex):
                    pipline.preMemBuff[pipline.preMemBuff.index(-1)] = currIndex
                else:
                    pipline.preALUBuff[pipline.preALUBuff.index(-1)] = currIndex

                pipline.preIssueBuff[current:3] = pipline.preIssueBuff[current + 1:]
                pipline.preIssueBuff[3] = -1
                numInPreIssueBuff -= 1
            else:
                current += 1


class instructionFetch:
    cleanup = False
    noHazards = True
    wait = -1
    def __init__(self):
        pass

    def checkForBranchHazards(self, index):
        for i in range(4):
            if pipline.preIssueBuff[i] != -1:
                if pipline.src1Reg[index] == pipline.destReg[pipline.preIssueBuff[i]]:
                    self.noHazards = False
        if (pipline.preMemBuff[0] != -1):
            if pipline.src1Reg[index] == pipline.destReg[pipline.preMemBuff[0]]:
                self.noHazards = False
        if (pipline.preMemBuff[1] != -1):
            if pipline.src1Reg[index] == pipline.destReg[pipline.preMemBuff[1]]:
                self.noHazards = False
        if (pipline.preALUBuff[0] != -1):
            if pipline.src1Reg[index] == pipline.destReg[pipline.preALUBuff[0]]:
                self.noHazards = False
        if (pipline.preALUBuff[1] != -1):
            if pipline.src1Reg[index] == pipline.destReg[pipline.preALUBuff[1]]:
                self.noHazards = False
        if (pipline.postALUBuff[1] != -1):
            if pipline.src1Reg[index] == pipline.destReg[pipline.postALUBuff[1]]:
                self.noHazards = False
        if (pipline.postMemBuff[1] != -1):

            if pipline.src1Reg[index] == pipline.destReg[pipline.postMemBuff[1]]:
                self.noHazards = False

        if self.noHazards:
            pass
        if pipline.instrName[index] == 'BLEZ':
            if self.noHazards:
                if pipline.registers[pipline.src1Reg[index]] <= 0:
                    pipline.PC += (pipline.args3[index])
                    pipline.PC += 4
                else:
                    pipline.PC += 4
        if pipline.instrName[index] == 'BNE':
            if pipline.src2Reg[index] in [pipline.destReg[pipline.preALUBuff[0]],
                                          pipline.destReg[pipline.preMemBuff[0]],
                                          pipline.destReg[pipline.preMemBuff[1]],
                                          pipline.destReg[pipline.preALUBuff[1]]]:
                self.noHazards = False
            if self.noHazards:
                if (pipline.registers[pipline.src1Reg[index]] != pipline.registers[pipline.src2Reg[index]]):
                    pipline.PC += pipline.args3[index]
                    pipline.PC += 4
                    return True
                else:
                    pipline.PC += 4

    def run(self):
        index = (pipline.PC - 96) / 4
        index1 = index
        numInPre = 0
        numIssued = 0

        for i in range(len(pipline.preIssueBuff)):
            if pipline.preIssueBuff[i] != -1:
                numInPre += 1

        if (pipline.instrName[index] == 'BREAK'):
            self.cleanup = True
            self.wait = 1
        elif not self.cleanup and numInPre < 4:  # 1
            hit, data1 = pipline.cache.accessMemory(-1, index, 0, 0)

            if hit and (pipline.PC % 8 == 0) and not self.cleanup and numInPre < 4:
                self.noHazards = True
                if (pipline.instrName[index] in ['BNE', 'BLEZ']):
                    self.checkForBranchHazards(index)
                elif (pipline.instrName[index] == 'J'):
                    pipline.PC = pipline.args1[index]
                    numIssued += 1
                elif (pipline.instrName[index] == 'JR'):
                    pipline.PC = pipline.registers[pipline.src1Reg[index]]
                elif (pipline.instrName[index] == 'Invalid Instruction'):
                    pipline.PC += 4
                elif (pipline.instrName[index] == 'BREAK'):
                    self.cleanup = True
                    self.wait = 1
                elif (pipline.instrName[index] == 'SW'):
                    address = pipline.args3[index] + pipline.registers[pipline.src2Reg[index]]
                    self.memoryoverflow(address)
                    pipline.preIssueBuff[numInPre] = index
                    pipline.PC += 4
                    numInPre += 1
                else:
                    pipline.preIssueBuff[numInPre] = index
                    pipline.PC += 4
                    numInPre += 1

                if (((pipline.PC - 96) / 4) == index + 1) and numInPre < 4:
                    index = index + 1
                    if (pipline.instrName[index] in ['BNE', 'BLEZ']):
                        self.checkForBranchHazards(index)
                    elif (pipline.instrName[index] == 'J'):
                        pipline.PC = pipline.args1[index]
                        numIssued += 1
                    elif (pipline.instrName[index] == 'JR'):
                        pipline.PC = pipline.registers[pipline.src1Reg[index]]
                    elif (pipline.instrName[index] == 'Invalid Instruction'):
                        pipline.PC += 4
                    elif (pipline.instrName[index] == 'BREAK'):
                        self.cleanup = True
                        self.wait = 1
                    elif (pipline.instrName[index] == 'SW'):
                        address = pipline.args3[index] + pipline.registers[pipline.src2Reg[index]]
                        self.memoryoverflow(address)
                        pipline.preIssueBuff[numInPre] = index
                        pipline.PC += 4
                        numInPre += 1
                    else:

                        pipline.preIssueBuff[numInPre] = index
                        pipline.PC += 4
                        numInPre += 1

            elif hit and not self.cleanup and numInPre < 4:
                self.noHazards = True
                if (pipline.instrName[index] in ['BNE', 'BLEZ']):
                    self.checkForBranchHazards(index)
                elif (pipline.instrName[index] == 'J'):
                    pipline.PC = pipline.args1[index]
                    numIssued += 1
                elif (pipline.instrName[index] == 'JR'):
                    pipline.PC = pipline.registers[pipline.src1Reg[index]]
                elif (pipline.instrName[index] == 'Invalid Instruction'):
                    pipline.PC += 4
                elif (pipline.instrName[index] == 'BREAK'):
                    self.cleanup = True
                    self.wait = 1
                elif (pipline.instrName[index] == 'SW'):
                    address = pipline.args3[index] + pipline.registers[pipline.src2Reg[index]]
                    self.memoryoverflow(address)
                    pipline.preIssueBuff[numInPre] = index
                    pipline.PC += 4
                    numInPre += 1
                else:
                    pipline.preIssueBuff[numInPre] = index
                    pipline.PC += 4
                    numInPre += 1

        if (self.cleanup):
            for i in range(4):
                if pipline.preIssueBuff[i] != -1:
                    return True
            if (pipline.preMemBuff[0] != -1) or (pipline.preMemBuff[1] != -1) or (pipline.preALUBuff[0] != -1) or (
                    pipline.preALUBuff[1] != -1):
                self.wait = 1
                return True
            elif (pipline.postMemBuff[1] != -1 or pipline.postALUBuff[1] != -1):
                self.wait = 1
                return True
            elif (pipline.instrName[index1] not in ['BNE', 'BLEZ', 'J', 'JR']):
                self.wait -= 1
            if (self.wait == 1):
                self.wait -= 1
                return True
            elif (pipline.instrName[index] == 'SW'):
                address = pipline.args3[index] + pipline.registers[pipline.src2Reg[index]]
                self.memoryoverflow(address)
                pipline.preIssueBuff[numInPre] = index
                pipline.PC += 4
                numInPre += 1
            else:
                return False
            if (self.wait == 0):
                return False
        if (pipline.cycle > 100):
            return False
        return True

    def memoryoverflow(self, memcheck):
     while memcheck >= len(pipline.memory):
         pipline.address.append(96 + (len(pipline.address) * 4))
         for x in range(0, 7):
             pipline.memory.append(0)


class cacheUnit:
    cacheSet = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]
    lruBit = [0, 0, 0, 0]
    tagMask = int('00000000000000000000000011111111', 2)
    setMask = int('0011111', 2)
    justMissedList = [-1, -1]

    def __init__(self):
        pass


    def finalFlush(self):
        for s in range(4):
            if (self.cacheSet[s][0][2] == 1):
                wbAddr = self.cacheSet[s][0][2]  # tag of mem
                wbAddr = (wbAddr << 5) + (s << 3)  # converted to address with s
                index = (wbAddr - 96 - (4 * pipline.numInstructions)) / 4  # index of mem
                self.cacheSet[s][0][1] = 0  # reset dirty bit
                pipline.memory[index] = self.cacheSet[s][0][3]  # change value in memory 1st word
                pipline.memory[index + 1] = self.cacheSet[s][0][4]  # change value in memory 2nd word
            elif (self.cacheSet[s][1][1] == 1):
                wbAddr = self.cacheSet[s][1][2]
                wbAddr = (wbAddr << 5) + (s << 3)
                index = (wbAddr - 96 - (4 * pipline.numInstructions)) / 4
                self.cacheSet[s][1][1] = 0  # reset dirty bit
                self.memoryoverflow(index + 1)
                pipline.memory[index] = self.cacheSet[s][1][3]  # change value in memory 1st word
                pipline.memory[index + 1] = self.cacheSet[s][1][4]  # change value in memory 2nd word
                self.cacheSet[s][1][1] = 0

    def accessMemory(self, memIndex, instrIndex, isWriteTomem, dataToWrite):
        # figure out the alignment
        if (instrIndex != -1):
            address = (instrIndex * 4) + 96
            if (address % 8 == 0):  # address 96+n8
                dataword = 0  # block 0 was the address
                address1 = address
                address2 = address + 4
            else:  # address != 96+n8
                dataword = 1  # block 1 was the address
                address1 = address - 4
                address2 = address
            #print instrIndex
            data1 = pipline.instruction[(address1 - 96) / 4]
            data2 = pipline.instruction[(address2 - 96) / 4]
        else:
            address = (memIndex * 4) + 96 + (4 * pipline.numInstructions)
            if (address % 8 == 0):  # address 96+n8
                dataword = 0  # block 0 was the address
                address1 = address
                address2 = address + 4
            else:  # address != 96+n8
                dataword = 1  # block 1 was the address
                address1 = address - 4
                address2 = address
            addresscheck1 = (address1 - (96 + (4 * pipline.numInstructions))) / 4
            addresscheck2 = (address2 - (96 + (4 * pipline.numInstructions))) / 4
            self.memoryoverflow(max(addresscheck1, addresscheck2))
            data1 = pipline.memory[addresscheck1]
            data2 = pipline.memory[addresscheck2]

        # 4
        if (isWriteTomem and dataword == 0):
            data1 = dataToWrite
        elif (isWriteTomem and dataword == 1):
            data2 = dataToWrite

        # 5. decode the address of word 0 into cache address
        tag = (address1 & self.tagMask)
        setNum = (tag & self.setMask) >> 3
        tag = tag >> 5

        hit = False

        if (self.cacheSet[setNum][0][2] == tag):
            assocblock = 0
            hit = True
        elif (self.cacheSet[setNum][1][2] == tag):
            assocblock = 1
            hit = True
        if (hit and isWriteTomem):
            # update dirty bit
            self.cacheSet[setNum][assocblock][1] = 1
            # update set lru bit
            self.lruBit[setNum] = (assocblock + 1) % 2
            # write data to cache
            self.cacheSet[setNum][assocblock][dataword + 3] = dataToWrite
            return True, self.cacheSet[setNum][assocblock][dataword + 3]
        # 8.
        elif (hit and not isWriteTomem):
            self.lruBit[setNum] = (assocblock + 1) % 2
            return True, self.cacheSet[setNum][assocblock][dataword + 3]
        # 9.
        elif (not hit):
            if (address1 not in self.justMissedList):
                if (memIndex != -1):
                    self.justMissedList[1] = address1
                else:
                    self.justMissedList[0] = address1
                return False, 0
            else:  # second miss
                if self.cacheSet[setNum][self.lruBit[setNum]][1] == 1:
                    # write back the memory address asociated with the block
                    wbAddr = self.cacheSet[setNum][self.lruBit[setNum]][2]  # tag

                    wbAddr = (wbAddr << 5) + (setNum << 3)

                    if (wbAddr >= (pipline.numInstructions * 4) + 96):
                        pipline.memory[pipline.getIndexOfMemAddress(wbAddr)] = \
                        self.cacheSet[setNum][self.lruBit[setNum]][3]
                    if (wbAddr + 4 >= (pipline.numInstructions * 4) + 96):
                        pipline.memory[pipline.getIndexOfMemAddress(wbAddr + 4)] = \
                        self.cacheSet[setNum][self.lruBit[setNum]][4]
                    # now update the cache flag bits
                self.cacheSet[setNum][self.lruBit[setNum]][0] = 1  # valid  we are writing a block
                self.cacheSet[setNum][self.lruBit[setNum]][1] = 0  # reset the dirty bit
                if (isWriteTomem):
                    self.cacheSet[setNum][self.lruBit[setNum]][
                        1] = 1  # dirty if is data mem is dirty again, intruction mem never dirty
                # update both words in the actual cache block in set
                self.cacheSet[setNum][self.lruBit[setNum]][2] = tag  # tag
                self.cacheSet[setNum][self.lruBit[setNum]][3] = data1  # data
                self.cacheSet[setNum][self.lruBit[setNum]][4] = data2  # nextData

                if (memIndex != -1):
                    if type(data1) == str and type(data2) == str:
                        if data1[0] == '1':  # if pipline.registers[pipline.src1Reg[i]] < 0:
                            intdata1 = ((int(data1, 2) ^ 0b11111111111111111111111111111111) + 1) * -1
                        else:
                            intdata1 = int(data1, 2)

                        if data2[0] == '1':
                            intdata2 = ((int(data2, 2) ^ 0b11111111111111111111111111111111) + 1) * -1
                        else:
                            intdata2 = int(data2, 2)
                        self.cacheSet[setNum][self.lruBit[setNum]][3] = intdata1  # nextData
                        self.cacheSet[setNum][self.lruBit[setNum]][4] = intdata2  # nextData
                    else:
                        self.cacheSet[setNum][self.lruBit[setNum]][3] = data1  # nextData
                        self.cacheSet[setNum][self.lruBit[setNum]][4] = data2
                self.lruBit[setNum] = (self.lruBit[setNum] + 1) % 2  # set lru to show block is recently used
                return [True, self.cacheSet[setNum][(self.lruBit[setNum] + 1) % 2][
                    dataword + 3]]  # dataword was the actual word thatgenerated the hit

    def memoryoverflow(self, memcheck):
     while memcheck >= len(pipline.memory):
         pipline.address.append(96 + (len(pipline.address) * 4))
         for x in range(0, 7):
             datalist.append(0)

class simClass(object):
    instruction = []
    opcode = []
    memory = []
    validInstr = []
    address = []
    numInstructions = 0
    instrName = []
    arg1 = []
    arg2 = []
    arg3 = []
    destReg = []
    src1Reg = []
    src2Reg = []
    cycle = 1
    registers = []
    preMemBuff = [-1, -1]  # first number is index, second is index
    postMemBuff = [-1, -1]  # first number is value, scond is instruction index
    preALUBuff = [-1, -1]  # first number is index, second is index, 2 instructions
    postALUBuff = [-1, -1]  # first number is value, second is instr index
    preIssueBuff = [-1, -1, -1, -1]  # list of 4 instruction indices
    WB = writeBack()
    ALU = arithmeticLogicUnit()
    MEM = memWrite()
    issue = issueUnit()
    fetch = instructionFetch()
    cache = cacheUnit()
    PC = 96

    def __init__(self, instrs, opcodes, mem, valids, addrs, args1, args2, args3, numInstrs, dest, src1, src2, instrName, pipelineoutput):
        self.instruction = instrs
        self.opcode = opcodes
        self.memory = mem
        self.validInstr = valids
        self.address = addrs
        self.numInstructions = numInstrs
        self.args1 = args1
        self.args2 = args2
        self.args3 = args3
        self.destReg = dest
        self.src1Reg = src1
        self.src2Reg = src2
        self.instrName = instrName
        self.pipelineoutput = pipelineoutput

    def getIndexOfMemAddress(self, bin_addr):
        return ((bin_addr - (96 + (4 * self.numInstructions))) / 4)

    def isMemOp(self, index):
        if self.instrName[index] in ['LW', 'SW']:
            return True
        return False

    def run( self):
        for x in range(0,32):
            self.registers.append(0)
        go = True
        while go:
            self.WB.run()
            self.ALU.run()
            self.MEM.run()
            self.issue.run()
            go = self.fetch.run()

            if not go:
                self.cache.finalFlush()
            self.printState()
            self.cycle+=1
    def printState(self):
        global pipelineoutput
        formattedInstr = ['', '', '', '', '', '', '', '', '', '']
        indices = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        for i in range(4):
            indices[i] = (self.preIssueBuff[i])

        indices[4] = self.preALUBuff[0]
        indices[5] = self.preALUBuff[1]
        indices[6] = self.postALUBuff[1]
        indices[7] = self.preMemBuff[0]
        indices[8] = self.preMemBuff[1]
        indices[9] = self.postMemBuff[1]

        for i in range(0, 10):
            #print instrName[i]
            if indices[i] > -1:
                if instrName[indices[i]] in ['MOVZ', 'ADD', 'SUB', 'AND', 'OR','XOR' 'MUL']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + '\tR' + str(
                        self.args3[indices[i]]) + ', R' + str(self.args1[indices[i]]) + ', R' + str(
                        self.args2[indices[i]]) + ']'
                elif instrName[indices[i]] in ['SLL', 'SRL']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + '\tR' + str(
                        self.args1[indices[i]]) + ', R' + str(self.args2[indices[i]]) + ', #' + str(
                        self.args3[indices[i]]) + ']'
                elif instrName[indices[i]] in ['BNE', 'ADDI']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + '\tR' + str(
                        self.args2[indices[i]]) + ', R' + str(self.args1[indices[i]]) + ', #' + str(
                        self.args3[indices[i]]) + ']'
                elif instrName[indices[i]] in ['SW', 'LW']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + '\tR' + str(
                        self.args2[indices[i]]) + ', ' + str(self.args3[indices[i]]) + '(R' + str(
                        self.args1[indices[i]]) + ')' + ']'
                elif instrName[indices[i]] == 'BLEZ':
                    formattedInstr[i] = '\t[' + 'BLEZ\tR' + str(self.args1[indices[i]]) + ', #' + str(
                        self.args3[indices[i]]) + ']'
                elif instrName[indices[i]] == 'J':
                    formattedInstr[i] = '\t[' + 'J\t#' + str(self.args1[indices[i]]) + ']'
                elif instrName[indices[i]] == 'JR':
                    formattedInstr[i] = '\t[' + 'JR\tR' + str(self.args1[indices[i]]) + ']'
                elif instrName[indices[i]] in ['NOP', 'BREAK', 'Invalid Instruction']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + ']'
            else:
                formattedInstr[i] = ''

        pipelineoutput.write('--------------------\n'
                             + 'Cycle:' + str(self.cycle)
                             + '\n\nPre-Issue Buffer:\n'
                             + '\tEntry 0:' + formattedInstr[0] + '\n'
                             + '\tEntry 1:' + formattedInstr[1] + '\n'
                             + '\tEntry 2:' + formattedInstr[2] + '\n'
                             + '\tEntry 3:' + formattedInstr[3] + '\n'
                             + 'Pre_ALU Queue:\n'
                             + '\tEntry 0:' + formattedInstr[4] + '\n'
                             + '\tEntry 1:' + formattedInstr[5] + '\n'
                             + 'Post_ALU Queue:\n'
                             + '\tEntry 0:' + formattedInstr[6] + '\n'
                             + 'Pre_MEM Queue:\n'
                             + '\tEntry 0:' + formattedInstr[7] + '\n'
                             + '\tEntry 1:' + formattedInstr[8] + '\n'
                             + 'Post_MEM Queue:\n'
                             + '\tEntry 0:' + formattedInstr[9] + '\n')

        pipelineoutput.write('\nRegisters'
                             + '\nR00:\t' + str(self.registers[0]) + '\t' + str(self.registers[1]) + '\t' + str(self.registers[2]) + '\t' + str(
            self.registers[3])
                             + '\t' + str(self.registers[4]) + '\t' + str(self.registers[5]) + '\t' + str(self.registers[6]) + '\t' + str(
            self.registers[7])
                             + '\nR08:\t' + str(self.registers[8]) + '\t' + str(self.registers[9]) + '\t' + str(
            self.registers[10]) + '\t' + str(self.registers[11])
                             + '\t' + str(self.registers[12]) + '\t' + str(self.registers[13]) + '\t' + str(self.registers[14]) + '\t' + str(
            self.registers[15])
                             + '\nR16:\t' + str(self.registers[16]) + '\t' + str(self.registers[17]) + '\t' + str(
            self.registers[18]) + '\t' + str(self.registers[19])
                             + '\t' + str(self.registers[20]) + '\t' + str(self.registers[21]) + '\t' + str(self.registers[22]) + '\t' + str(
            self.registers[23])
                             + '\nR24:\t' + str(self.registers[24]) + '\t' + str(self.registers[25]) + '\t' + str(
            self.registers[26]) + '\t' + str(self.registers[27])
                             + '\t' + str(self.registers[28]) + '\t' + str(self.registers[29]) + '\t' + str(self.registers[30]) + '\t' + str(
            self.registers[31])
                             + '\n')

        pipelineoutput.write('\nCache\n')

        for i in range(4):
            pipelineoutput.write('Set ' + str(i) + ': LRU=' + str(self.cache.lruBit[i]) + '\n')

            for j in range(2):
                pipelineoutput.write('\tEntry ' + str(j) + ':[(' + str(self.cache.cacheSet[i][j][0]) + ','
                                     + str(self.cache.cacheSet[i][j][1]) + ',' + str(self.cache.cacheSet[i][j][2])
                                     + ')<' + str(self.cache.cacheSet[i][j][3]) + ',' + str(
                    self.cache.cacheSet[i][j][4])
                                     + '>]\n')

        pipelineoutput.write('\nData')
        dataAddress = 96 + (self.numInstructions * 4)
        i = 0

        while i < len(self.memory):
            if (i % 8 == 0 and i == 0):
                pipelineoutput.write('\n' + str(dataAddress) + ':' + str(self.memory[i])),
            elif (i % 8 == 0 and not i == 0):
                pipelineoutput.write('\n' + str(dataAddress) + ':' + str(self.memory[i])),
            else:  # not a multiple of 8
                pipelineoutput.write('\t' + str(self.memory[i])),
            i += 1
            dataAddress += 4
        pipelineoutput.write('\n')

dissasembler1 = Dissasembler()
inputfilename = ""
outputfilename = ""
for i in range(len(sys.argv)):
    if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):#check for input file name
        inputfilename = sys.argv[i + 1]
    elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):#check for output file name
        outputfilename = sys.argv[i + 1]
        outputfilename2 = outputfilename + "_pipeline.txt"
        outputfilename = outputfilename + "_dis.txt"
if not inputfilename:#default file names if not given
    inputfilename = "test3_bin.txt"
if not outputfilename:
    outputfilename = "team2_out_dis.txt"
    outputfilename2 = "team2_out_pipeline.txt"
dissasembler1.dirty_work(inputfilename, outputfilename)
pipelineoutput = open(outputfilename2, 'w')
pipline = simClass(instruction, opcodelist, datalist, validInstr, address, arg1, arg2, arg3, numInstrs,
destReg, src1Reg, src2Reg, instrName, pipelineoutput)
pipline.run()
