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

dataList = []
instruction = []
opList = []
iName = []
address = []
validi = []
firstArg = []
secondArg = []
thirdArg = []
destReg = []
src1Reg = []
src2Reg = []
invalid = -5
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
                opList.append(int(opcode, 2))
                validi.append(int(validbit))
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

                    iName.append('Invalid Instruction')
                    address.append(PC + (counter * 4))
                    firstArg.append(int(group1, 2))
                    secondArg.append(int(group2, 2))
                    thirdArg.append(' ')
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

                                iName.append('NOP')
                                address.append(PC + (counter * 4))
                                firstArg.append(int(group1, 2))
                                secondArg.append(int(group2, 2))
                                thirdArg.append('')
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

                                iName.append(function_name)
                                address.append(PC + (counter * 4))
                                firstArg.append(int(group2, 2))
                                secondArg.append(int(group3, 2))
                                thirdArg.append(int(group4, 2))
                                destReg.append(secondArg[counter])
                                src1Reg.append(firstArg[counter])
                                src2Reg.append(invalid)
                                invalid -= 1
                                numInstrs += 1
                                counter += 1

                        if subtype is 1:
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rs)

                            iName.append(function_name)
                            address.append(PC + (counter * 4))
                            firstArg.append(int(group1, 2))
                            secondArg.append(0)
                            thirdArg.append(0)
                            destReg.append(invalid)
                            invalid -= 1
                            src1Reg.append(firstArg[counter])
                            src2Reg.append(invalid)
                            invalid -= 1
                            numInstrs += 1
                            counter += 1

                        if subtype is 2:
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rd + ', ' + rs + ', ' + rt)

                            iName.append(function_name)
                            address.append(PC + (counter * 4))
                            firstArg.append(int(group1, 2))
                            secondArg.append(int(group2, 2))
                            thirdArg.append(int(group3, 2))
                            destReg.append(thirdArg[counter])
                            src1Reg.append(firstArg[counter])
                            src2Reg.append(secondArg[counter])
                            numInstrs += 1
                            counter += 1

                        if subtype is 3:
                            output_file.write('%s' % (function_name))

                            iName.append('BREAK')
                            address.append(PC + (counter * 4))
                            firstArg.append(int(group1, 2))
                            secondArg.append(int(group2, 2))
                            thirdArg.append(0)
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

                                iName.append(function_name)
                                address.append(PC + (counter * 4))
                                firstArg.append(jumpCode)
                                secondArg.append(0)
                                thirdArg.append(0)
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

                                iName.append(function_name)
                                address.append(PC + (counter * 4))
                                firstArg.append(int(group1, 2))
                                secondArg.append(int(group2, 2))
                                thirdArg.append(offset)
                                if funct == 11:
                                    destReg.append(-2)
                                    invalid -= 1
                                    src1Reg.append(secondArg[counter])
                                    src2Reg.append(firstArg[counter])
                                elif funct == 3:
                                    destReg.append(secondArg[counter])
                                    src1Reg.append(firstArg[counter])
                                    src2Reg.append(invalid)
                                    invalid -= 1
                                elif funct == 5:
                                    destReg.append(-3)
                                    invalid -= 1
                                    src1Reg.append(firstArg[counter])
                                    src2Reg.append(secondArg[counter])
                                numInstrs += 1
                                counter += 1
                        if subtype is 6:
                            rs = registers[int(group1, 2)]['name']
                            offset = int(line[16:32], 2)*4
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rs + ', #' + str(offset))

                            iName.append(function_name)
                            address.append(PC + (counter * 4))
                            firstArg.append(int(group1, 2))
                            secondArg.append(int(group2, 2))
                            thirdArg.append(offset)
                            destReg.append(invalid)
                            invalid -= 1
                            src1Reg.append(firstArg[counter])
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

                            iName.append(function_name)
                            address.append(PC + (counter * 4))
                            firstArg.append(int(group1, 2))
                            secondArg.append(int(group2, 2))
                            thirdArg.append(int(group3, 2))
                            destReg.append(thirdArg[counter])
                            src1Reg.append(firstArg[counter])
                            src2Reg.append(secondArg[counter])
                            numInstrs += 1
                            counter += 1

                        if subtype is 8:
                            rs = registers[int(group1, 2)]['name']
                            rt = registers[int(group2, 2)]['name']
                            immediate = str(self.twos_comp(int(line[16:32], 2), len(line[16:32])))
                            output_file.write('%s' % (function_name))
                            output_file.write('\t' + rt + ', ' + rs + ', #' + str(immediate))

                            iName.append('ADDI')
                            address.append(PC + (counter * 4))
                            firstArg.append(int(group1, 2))
                            secondArg.append(int(group2, 2))
                            thirdArg.append(int(group3, 2))
                            thirdArg[counter] = int(immediate)
                            destReg.append(secondArg[counter])
                            src1Reg.append(firstArg[counter])
                            src2Reg.append(invalid)
                            invalid -= 1
                            numInstrs += 1
                            counter += 1

            else:#Output after Break
                output_file.write('%s' % (line[0:32]))
                output_file.write('\t' + (str(memory_location) + '\t' + str(self.twos_comp(int(line[0:32], 2), len(line[0:32])))))
                dataList.append(self.twos_comp(int(line[0:32], 2), len(line[0:32])))
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


# Writeback
class WBstage:
    def __init__(self):
        pass
    def run(self):
        if(piplup.BUFFpostALU[1] != -1):
            piplup.registers[piplup.destReg[piplup.BUFFpostALU[1]]] = piplup.BUFFpostALU[0]
            piplup.BUFFpostALU[0] = -1
            piplup.BUFFpostALU[1] = -1
        if(piplup.BUFFpostMEM[1] != -1):
            piplup.registers[piplup.destReg[piplup.BUFFpostMEM[1]]] = piplup.BUFFpostMEM[0]
            piplup.BUFFpostMEM[0] = -1
            piplup.BUFFpostMEM[1] = -1


# memory unit
class MEMstage:
    def __init__(self):
        pass
    def run(self):
        if(piplup.BUFFpreMem[0] != -1):
            i = piplup.BUFFpreMem[0]
            hit = False
            if(piplup.iName[i] == 'LW'):
                address = piplup.args3[i] + piplup.registers[piplup.src1Reg[i]]
                hit, data = piplup.cache.accessMemory(piplup.getMEMI(address),-1,False,0)

            elif(piplup.iName[i] == 'SW'):
                address = piplup.args3[i] + piplup.registers[piplup.src2Reg[i]]
                hit, data = piplup.cache.accessMemory(piplup.getMEMI(address), -1, True, piplup.registers[piplup.src1Reg[i]])

            if(hit):

                if piplup.iName[i] == 'LW':
                    piplup.BUFFpostMEM[0] = int(data)
                    piplup.BUFFpostMEM[1] = i

                piplup.BUFFpreMem[0] = piplup.BUFFpreMem[1]
                piplup.BUFFpreMem[1] = -1


# arithmetic logic unit
class ALUstage:

    def __init__(self):
        pass

    def run(self):
        if (piplup.BUFFpreALU[0] != -1):
            i = piplup.BUFFpreALU[0]
            piplup.BUFFpostALU[1] = i
            if (piplup.iName[i] == 'SLL'):
                piplup.BUFFpostALU[0] = piplup.registers[piplup.src1Reg[i]] * pow(2, piplup.args3[i])
            elif (piplup.iName[i] == 'SRL'):
                piplup.BUFFpostALU[0] = piplup.registers[piplup.src1Reg[i]] / pow(2, piplup.args3[i])
            elif (piplup.iName[i] == 'ADD'):
                piplup.BUFFpostALU[0] = piplup.registers[piplup.src1Reg[i]] + piplup.registers[piplup.src2Reg[i]]
            elif (piplup.iName[i] == 'SUB'):
                piplup.BUFFpostALU[0] = piplup.registers[piplup.src1Reg[i] - piplup.registers[piplup.src2Reg[i]]]
            elif (piplup.iName[i] == 'AND'):
                piplup.BUFFpostALU[0] = piplup.registers[piplup.src1Reg[i] & piplup.registers[piplup.src2Reg[i]]]
            elif (piplup.iName[i] == 'OR'):
                piplup.BUFFpostALU[0] = piplup.registers[piplup.src1Reg[i] | piplup.registers[piplup.src2Reg[i]]]
            elif (piplup.iName[i] == 'XOR'):
                piplup.BUFFpostALU[0] = piplup.registers[piplup.src1Reg[i]] ^ piplup.registers[piplup.src2Reg[i]]
            elif (piplup.iName[i] == 'MOVZ'):
                if (piplup.src2Reg[i] == 0):
                    piplup.BUFFpostALU[0] = piplup.src1Reg[i]
            elif (piplup.iName[i] == 'ADDI'):
                piplup.BUFFpostALU[0] = int(piplup.registers[piplup.src1Reg[i]]) + piplup.args3[i]
            elif (piplup.iName[i] == 'MUL'):
                piplup.BUFFpostALU[0] = piplup.registers[piplup.src1Reg[i] * piplup.registers[piplup.src2Reg[i]]]
            piplup.BUFFpreALU[0] = piplup.BUFFpreALU[1]
            piplup.BUFFpreALU[1] = -1
        else:
            pass


# Instruction Decode
class IDstage:
    def __init__(self):
        pass

    def run(self):
        IDMe = True
        numIssued = 0
        numInPreIssueBuff = 0
        currIndex = -1
        current = 0

        for i in range(4):
            if (piplup.BUFFpreIssue[i] != -1):
                numInPreIssueBuff += 1

        while (numIssued < 2 and numInPreIssueBuff > 0 and current < 4):
            IDMe = True
            currIndex = piplup.BUFFpreIssue[current]
            if piplup.isMemOp(currIndex) and not -1 in piplup.BUFFpreMem:
                IDMe = False
            elif not piplup.isMemOp(currIndex) and not -1 in piplup.BUFFpreALU:
                IDMe = False
            if currIndex == -1:
                break

            if current > 0:
                for i in range(0, current):
                    if (piplup.destReg[currIndex] == piplup.src1Reg[piplup.BUFFpreIssue[i]] or piplup.destReg[
                        currIndex] == piplup.src2Reg[piplup.BUFFpreIssue[i]]):
                        IDMe = False
            if piplup.isMemOp(currIndex):
                for i in range(0, len(piplup.BUFFpreMem)):
                    if piplup.BUFFpreMem[i] != -1:
                        if piplup.destReg[currIndex] == piplup.src1Reg[piplup.BUFFpreMem[i]] or piplup.destReg[
                            currIndex] == piplup.src2Reg[piplup.BUFFpreMem[i]]:
                            IDMe = False
            if not piplup.isMemOp(currIndex):
                for i in range(0, len(piplup.BUFFpreALU)):
                    if piplup.BUFFpreALU[i] != -1:
                        if piplup.destReg[currIndex] == piplup.src1Reg[piplup.BUFFpreALU[i]] or piplup.destReg[
                            currIndex] == piplup.src2Reg[piplup.BUFFpreALU[i]]:
                            IDMe = False

            if current > 0:
                for i in range(0, current):
                    if (piplup.src1Reg[currIndex] == piplup.destReg[piplup.BUFFpreIssue[i]] or piplup.src2Reg[
                        currIndex] == piplup.destReg[piplup.BUFFpreIssue[i]]):
                        IDMe = False

            for i in range(0, len(piplup.BUFFpreMem)):
                if piplup.BUFFpreMem[i] != -1:
                    if piplup.src1Reg[currIndex] == piplup.destReg[piplup.BUFFpreMem[i]] or piplup.src2Reg[
                        currIndex] == piplup.destReg[piplup.BUFFpreMem[i]]:
                        IDMe = False
            for i in range(0, len(piplup.BUFFpreALU)):
                if piplup.BUFFpreALU[i] != -1:
                    if piplup.src1Reg[currIndex] == piplup.destReg[piplup.BUFFpreALU[i]] or piplup.src2Reg[
                        currIndex] == piplup.destReg[piplup.BUFFpreALU[i]]:
                        IDMe = False

            if piplup.BUFFpostALU[1] != -1:
                if piplup.src1Reg[currIndex] == piplup.destReg[piplup.BUFFpostALU[1]] or piplup.src2Reg[
                    currIndex] == piplup.destReg[piplup.BUFFpostALU[1]]:
                    IDMe = False
            if piplup.BUFFpostMEM[1] != -1:
                if piplup.src1Reg[currIndex] == piplup.destReg[piplup.BUFFpostMEM[1]] or piplup.src2Reg[
                    currIndex] == piplup.destReg[piplup.BUFFpostMEM[1]]:
                    IDMe = False

            for i in range(0, current):
                if piplup.destReg[currIndex] == piplup.destReg[piplup.BUFFpreIssue[i]]:
                    IDMe = False

            for i in range(0, len(piplup.BUFFpreMem)):
                if piplup.BUFFpreMem[i] != -1:
                    if piplup.destReg[currIndex] == piplup.destReg[piplup.BUFFpreMem[i]]:
                        IDMe = False
            for i in range(0, len(piplup.BUFFpreALU)):
                if piplup.BUFFpreALU[i] != -1:
                    if piplup.destReg[currIndex] == piplup.destReg[piplup.BUFFpreALU[i]]:
                        IDMe = False
            if piplup.BUFFpostALU[1] != -1:
                if piplup.destReg[currIndex] == piplup.destReg[piplup.BUFFpostALU[1]]:
                    IDMe = False
            if piplup.BUFFpostMEM[1] != -1:
                if piplup.destReg[currIndex] == piplup.destReg[piplup.BUFFpostMEM[1]]:
                    IDMe = False

            if (piplup.iName[currIndex] == 'LW'):
                for i in range( 0, current ):
                    if piplup.iName[piplup.BUFFpreIssue[i]] == 'SW':
                        IDMe = False

            if (piplup.iName[currIndex] == 'SW'):
                for i in range( 0, current ):
                    if piplup.iName[piplup.BUFFpreIssue[i]] == 'SW':
                        IDMe = False

            if IDMe:
                numIssued += 1
                if piplup.isMemOp(currIndex):
                    piplup.BUFFpreMem[piplup.BUFFpreMem.index(-1)] = currIndex
                else:
                    piplup.BUFFpreALU[piplup.BUFFpreALU.index(-1)] = currIndex

                piplup.BUFFpreIssue[0:current] = piplup.BUFFpreIssue[0:current]
                piplup.BUFFpreIssue[current:3] = piplup.BUFFpreIssue[current + 1:]
                piplup.BUFFpreIssue[3] = -1
                numInPreIssueBuff -= 1
            else:
                current += 1



# Instruction Fetch
class IFstage:
    cleanup = False
    noHazards = True
    wait = -1
    def __init__(self):
        pass

    def checkForBranchHazards(self, index):
        for i in range(4):
            if piplup.BUFFpreIssue[i] != -1:
                if piplup.src1Reg[index] == piplup.destReg[piplup.BUFFpreIssue[i]]:
                    self.noHazards = False
        if (piplup.BUFFpreMem[0] != -1):
            if piplup.src1Reg[index] == piplup.destReg[piplup.BUFFpreMem[0]]:
                self.noHazards = False
        if (piplup.BUFFpreMem[1] != -1):
            if piplup.src1Reg[index] == piplup.destReg[piplup.BUFFpreMem[1]]:
                self.noHazards = False
        if (piplup.BUFFpreALU[0] != -1):
            if piplup.src1Reg[index] == piplup.destReg[piplup.BUFFpreALU[0]]:
                self.noHazards = False
        if (piplup.BUFFpreALU[1] != -1):
            if piplup.src1Reg[index] == piplup.destReg[piplup.BUFFpreALU[1]]:
                self.noHazards = False
        if (piplup.BUFFpostALU[1] != -1):
            if piplup.src1Reg[index] == piplup.destReg[piplup.BUFFpostALU[1]]:
                self.noHazards = False
        if (piplup.BUFFpostMEM[1] != -1):

            if piplup.src1Reg[index] == piplup.destReg[piplup.BUFFpostMEM[1]]:
                self.noHazards = False

        if self.noHazards:
            pass
        if piplup.iName[index] == 'BLEZ':
            if self.noHazards:
                if piplup.registers[piplup.src1Reg[index]] <= 0:
                    piplup.PC += (piplup.args3[index])
                    piplup.PC += 4
                else:
                    piplup.PC += 4
        if piplup.iName[index] == 'BNE':
            if piplup.src2Reg[index] in [piplup.destReg[piplup.BUFFpreALU[0]],
                                          piplup.destReg[piplup.BUFFpreMem[0]],
                                          piplup.destReg[piplup.BUFFpreMem[1]],
                                          piplup.destReg[piplup.BUFFpreALU[1]]]:
                self.noHazards = False
            if self.noHazards:
                if (piplup.registers[piplup.src1Reg[index]] != piplup.registers[piplup.src2Reg[index]]):
                    piplup.PC += piplup.args3[index]
                    #piplup.PC += 4
                    return True
                else:
                    piplup.PC += 4

    def run(self):
        index = (piplup.PC - 96) / 4
        index1 = index
        numInPre = 0
        numIssued = 0

        for i in range(len(piplup.BUFFpreIssue)):
            if piplup.BUFFpreIssue[i] != -1:
                numInPre += 1

        if (piplup.iName[index] == 'BREAK'):
            self.cleanup = True
            self.wait = 1
        elif not self.cleanup and numInPre < 4:
            hit, data1 = piplup.cache.accessMemory(-1, index, 0, 0)

            if hit and (piplup.PC % 8 == 0) and not self.cleanup and numInPre < 4:
                self.noHazards = True
                if (piplup.iName[index] in ['BNE', 'BLEZ']):
                    self.checkForBranchHazards(index)
                elif (piplup.iName[index] == 'J'):
                    piplup.PC = piplup.args1[index]
                    numIssued += 1
                elif (piplup.iName[index] == 'JR'):
                    piplup.PC = piplup.registers[piplup.src1Reg[index]]
                elif (piplup.iName[index] == 'Invalid Instruction'):
                    piplup.PC += 4
                elif (piplup.iName[index] == 'BREAK'):
                    self.cleanup = True
                    self.wait = 1
                elif (piplup.iName[index] == 'SW'):
                    address = piplup.args3[index] + piplup.registers[piplup.src2Reg[index]]
                    self.memoryoverflow(address)
                    piplup.BUFFpreIssue[numInPre] = index
                    piplup.PC += 4
                    numInPre += 1
                else:
                    piplup.BUFFpreIssue[numInPre] = index
                    piplup.PC += 4
                    numInPre += 1

                if (((piplup.PC - 96) / 4) == index + 1) and numInPre < 4:
                    index = index + 1
                    if (piplup.iName[index] in ['BNE', 'BLEZ']):
                        self.checkForBranchHazards(index)
                    elif (piplup.iName[index] == 'J'):
                        piplup.PC = piplup.args1[index]
                        numIssued += 1
                    elif (piplup.iName[index] == 'JR'):
                        piplup.PC = piplup.registers[piplup.src1Reg[index]]
                    elif (piplup.iName[index] == 'Invalid Instruction'):
                        piplup.PC += 4
                    elif (piplup.iName[index] == 'SW'):
                        address = piplup.args3[index] + piplup.registers[piplup.src2Reg[index]]
                        self.memoryoverflow(address)
                        piplup.BUFFpreIssue[numInPre] = index
                        piplup.PC += 4
                        numInPre += 1
                    elif (piplup.iName[index] == 'BREAK'):
                        self.cleanup = True
                        self.wait = 1
                    else:

                        piplup.BUFFpreIssue[numInPre] = index
                        piplup.PC += 4
                        numInPre += 1

            elif hit and not self.cleanup and numInPre < 4:
                self.noHazards = True
                if (piplup.iName[index] in ['BNE', 'BLEZ']):
                    self.checkForBranchHazards(index)
                elif (piplup.iName[index] == 'J'):
                    piplup.PC = piplup.args1[index]
                    numIssued += 1
                elif (piplup.iName[index] == 'JR'):
                    piplup.PC = piplup.registers[piplup.src1Reg[index]]
                elif (piplup.iName[index] == 'Invalid Instruction'):
                    piplup.PC += 4
                elif (piplup.iName[index] == 'SW'):
                    address = piplup.args3[index] + piplup.registers[piplup.src2Reg[index]]
                    self.memoryoverflow(address)
                    piplup.BUFFpreIssue[numInPre] = index
                    piplup.PC += 4
                    numInPre += 1
                elif (piplup.iName[index] == 'BREAK'):
                    self.cleanup = True
                    self.wait = 1
                else:
                    piplup.BUFFpreIssue[numInPre] = index
                    piplup.PC += 4
                    numInPre += 1

        if (self.cleanup):
            for i in range(4):
                if piplup.BUFFpreIssue[i] != -1:
                    return True
            if (piplup.BUFFpreMem[0] != -1) or (piplup.BUFFpreMem[1] != -1) or (piplup.BUFFpreALU[0] != -1) or (
                    piplup.BUFFpreALU[1] != -1):
                self.wait = 1
                return True
            elif (piplup.BUFFpostMEM[1] != -1 or piplup.BUFFpostALU[1] != -1):
                self.wait = 1
                return True
            elif (piplup.iName[index1] not in ['BNE', 'BLEZ', 'J', 'JR']):
                self.wait -= 1
            if (self.wait == 1):
                self.wait -= 1
                return True
            elif (piplup.iName[index] == 'SW'):
                address = piplup.args3[index] + piplup.registers[piplup.src2Reg[index]]
                self.memoryoverflow(address)
                piplup.BUFFpreIssue[numInPre] = index
                piplup.PC += 4
                numInPre += 1
            else:
                return False
            if (self.wait == 0):
                return False
        if (piplup.cycle > 100):
            return False
        return True

    def memoryoverflow(self, memcheck):
        memcheck = (memcheck - (96 + (4 * piplup.numInstructions))) / 4
        while memcheck >= len(piplup.memory):
            piplup.address.append(96 + (len(piplup.address) * 4))
            piplup.memory.append(0)


# Caching unit
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


    def cacheFlush(self):
        for s in range(4):
            if (self.cacheSet[s][0][2] == 1):
                wbAddr = self.cacheSet[s][0][2]
                wbAddr = (wbAddr << 5) + (s << 3)
                index = (wbAddr - 96 - (4 * piplup.numInstructions)) / 4
                self.cacheSet[s][0][1] = 0
                piplup.memory[index] = self.cacheSet[s][0][3]
                piplup.memory[index + 1] = self.cacheSet[s][0][4]
            elif (self.cacheSet[s][1][1] == 1):
                wbAddr = self.cacheSet[s][1][2]
                wbAddr = (wbAddr << 5) + (s << 3)
                index = (wbAddr - 96 - (4 * piplup.numInstructions)) / 4
                self.cacheSet[s][1][1] = 0
                piplup.memory[index] = self.cacheSet[s][1][3]
                piplup.memory[index + 1] = self.cacheSet[s][1][4]
                self.cacheSet[s][1][1] = 0

    def accessMemory(self, memIndex, instrIndex, isWriteTomem, dataToWrite):
        if (instrIndex != -1):
            address = (instrIndex * 4) + 96
            if (address % 8 == 0):
                dataword = 0
                address1 = address
                address2 = address + 4
            else:
                dataword = 1
                address1 = address - 4
                address2 = address
            data1 = piplup.instruction[(address1 - 96) / 4]
            data2 = piplup.instruction[(address2 - 96) / 4]
        else:
            address = (memIndex * 4) + 96 + (4 * piplup.numInstructions)
            if (address % 8 == 0):
                dataword = 0
                address1 = address
                address2 = address + 4
            else:
                dataword = 1
                address1 = address - 4
                address2 = address
            addresscheck1 = (address1 - (96 + (4 * piplup.numInstructions))) / 4
            addresscheck2 = (address2 - (96 + (4 * piplup.numInstructions))) / 4
            self.memoryoverflow(max(addresscheck1, addresscheck2))
            data1 = piplup.memory[addresscheck1]
            data2 = piplup.memory[addresscheck2]
        if (isWriteTomem and dataword == 0):
            data1 = dataToWrite
        elif (isWriteTomem and dataword == 1):
            data2 = dataToWrite

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
            self.cacheSet[setNum][assocblock][1] = 1
            self.lruBit[setNum] = (assocblock + 1) % 2
            self.cacheSet[setNum][assocblock][dataword + 3] = dataToWrite
            return True, self.cacheSet[setNum][assocblock][dataword + 3]
        elif (hit and not isWriteTomem):
            self.lruBit[setNum] = (assocblock + 1) % 2
            return True, self.cacheSet[setNum][assocblock][dataword + 3]
        elif (not hit):
            if (address1 not in self.justMissedList):
                if (memIndex != -1):
                    self.justMissedList[1] = address1
                else:
                    self.justMissedList[0] = address1
                return False, 0
            else:
                if self.cacheSet[setNum][self.lruBit[setNum]][1] == 1:
                    wbAddr = self.cacheSet[setNum][self.lruBit[setNum]][2]

                    wbAddr = (wbAddr << 5) + (setNum << 3)

                    if (wbAddr >= (piplup.numInstructions * 4) + 96):
                        piplup.memory[piplup.getMEMI(wbAddr)] = \
                        self.cacheSet[setNum][self.lruBit[setNum]][3]
                    if (wbAddr + 4 >= (piplup.numInstructions * 4) + 96):
                        piplup.memory[piplup.getMEMI(wbAddr + 4)] = \
                        self.cacheSet[setNum][self.lruBit[setNum]][4]
                self.cacheSet[setNum][self.lruBit[setNum]][0] = 1
                self.cacheSet[setNum][self.lruBit[setNum]][1] = 0
                if (isWriteTomem):
                    self.cacheSet[setNum][self.lruBit[setNum]][
                        1] = 1
                self.cacheSet[setNum][self.lruBit[setNum]][2] = tag
                self.cacheSet[setNum][self.lruBit[setNum]][3] = data1
                self.cacheSet[setNum][self.lruBit[setNum]][4] = data2

                if (memIndex != -1):
                    if type(data1) == str and type(data2) == str:
                        if data1[0] == '1':
                            intdata1 = ((int(data1, 2) ^ 0b11111111111111111111111111111111) + 1) * -1
                        else:
                            intdata1 = int(data1, 2)

                        if data2[0] == '1':
                            intdata2 = ((int(data2, 2) ^ 0b11111111111111111111111111111111) + 1) * -1
                        else:
                            intdata2 = int(data2, 2)
                        self.cacheSet[setNum][self.lruBit[setNum]][3] = intdata1
                        self.cacheSet[setNum][self.lruBit[setNum]][4] = intdata2
                    else:
                        self.cacheSet[setNum][self.lruBit[setNum]][3] = data1
                        self.cacheSet[setNum][self.lruBit[setNum]][4] = data2
                self.lruBit[setNum] = (self.lruBit[setNum] + 1) % 2
                return [True, self.cacheSet[setNum][(self.lruBit[setNum] + 1) % 2][
                    dataword + 3]]
    def memoryoverflow(self, memcheck):
        while memcheck >= len(piplup.memory):
            piplup.address.append(96 + (len(piplup.address) * 4))
            piplup.memory.append(0)


# Pipeline Simulator Class
class simClass(object):
    instruction = []
    opcode = []
    memory = []
    validi = []
    address = []
    iName = []
    firstArg = []
    secondArg = []
    thirdArg = []
    destReg = []
    src1Reg = []
    src2Reg = []
    registers = []
    BUFFpreMem = [-1, -1]
    BUFFpostMEM = [-1, -1]
    BUFFpreALU = [-1, -1]
    BUFFpostALU = [-1, -1]
    BUFFpreIssue = [-1, -1, -1, -1]
    WB = WBstage()
    ALU = ALUstage()
    MEM = MEMstage()
    ID = IDstage()
    IF = IFstage()
    cache = cacheUnit()
    numInstructions = 0
    cycle = 1
    PC = 96

    def __init__(self, instrs, opcodes, mem, valids, addrs, args1, args2, args3, numInstrs, dest, src1, src2, iName, pipelineoutput):
        self.instruction = instrs
        self.opcode = opcodes
        self.memory = mem
        self.validi = valids
        self.address = addrs
        self.numInstructions = numInstrs
        self.args1 = args1
        self.args2 = args2
        self.args3 = args3
        self.destReg = dest
        self.src1Reg = src1
        self.src2Reg = src2
        self.iName = iName
        self.pipelineoutput = pipelineoutput

    def getMEMI(self, bin_addr):
        return ((bin_addr - (96 + (4 * self.numInstructions))) / 4)

    def isMemOp(self, index):
        if self.iName[index] in ['LW', 'SW']:
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
            self.ID.run()
            go = self.IF.run()

            if not go:
                self.cache.cacheFlush()
            self.printState()
            self.cycle+=1


    def printState(self):
        global pipelineoutput
        formattedInstr = ['', '', '', '', '', '', '', '', '', '']
        indices = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        for i in range(4):
            indices[i] = (self.BUFFpreIssue[i])

        indices[4] = self.BUFFpreALU[0]
        indices[5] = self.BUFFpreALU[1]
        indices[6] = self.BUFFpostALU[1]
        indices[7] = self.BUFFpreMem[0]
        indices[8] = self.BUFFpreMem[1]
        indices[9] = self.BUFFpostMEM[1]

        for i in range(0, 10):
            if indices[i] > -1:
                if iName[indices[i]] in ['MOVZ', 'ADD', 'SUB', 'AND', 'OR','XOR' 'MUL']:
                    formattedInstr[i] = '\t[' + self.iName[indices[i]] + '\tR' + str(
                        self.args3[indices[i]]) + ', R' + str(self.args1[indices[i]]) + ', R' + str(
                        self.args2[indices[i]]) + ']'
                elif iName[indices[i]] in ['SLL', 'SRL']:
                    formattedInstr[i] = '\t[' + self.iName[indices[i]] + '\tR' + str(
                        self.args1[indices[i]]) + ', R' + str(self.args2[indices[i]]) + ', #' + str(
                        self.args3[indices[i]]) + ']'
                elif iName[indices[i]] in ['BNE', 'ADDI']:
                    formattedInstr[i] = '\t[' + self.iName[indices[i]] + '\tR' + str(
                        self.args2[indices[i]]) + ', R' + str(self.args1[indices[i]]) + ', #' + str(
                        self.args3[indices[i]]) + ']'
                elif iName[indices[i]] in ['SW', 'LW']:
                    formattedInstr[i] = '\t[' + self.iName[indices[i]] + '\tR' + str(
                        self.args2[indices[i]]) + ', ' + str(self.args3[indices[i]]) + '(R' + str(
                        self.args1[indices[i]]) + ')' + ']'
                elif iName[indices[i]] == 'BLEZ':
                    formattedInstr[i] = '\t[' + 'BLEZ\tR' + str(self.args1[indices[i]]) + ', #' + str(
                        self.args3[indices[i]]) + ']'
                elif iName[indices[i]] == 'J':
                    formattedInstr[i] = '\t[' + 'J\t#' + str(self.args1[indices[i]]) + ']'
                elif iName[indices[i]] == 'JR':
                    formattedInstr[i] = '\t[' + 'JR\tR' + str(self.args1[indices[i]]) + ']'
                elif iName[indices[i]] in ['NOP', 'BREAK', 'Invalid Instruction']:
                    formattedInstr[i] = '\t[' + self.iName[indices[i]] + ']'
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
            else:
                pipelineoutput.write('\t' + str(self.memory[i])),
            i += 1
            dataAddress += 4
        pipelineoutput.write('\n')

dissasembler1 = Dissasembler()
inputfilename = ""
outputfilename = ""
for i in range(len(sys.argv)):
    if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):  # check for input file name
        inputfilename = sys.argv[i + 1]
    elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):  # check for output file name
        outputfilename = sys.argv[i + 1]
        outputfilename2 = outputfilename + "_pipeline.txt"
        outputfilename = outputfilename + "_dis.txt"
if not inputfilename:  # default file names if not given
    inputfilename = "test1_bin.txt"
if not outputfilename:
    outputfilename = "team2_out_dis.txt"
    outputfilename2 = "team2_out_pipeline.txt"
dissasembler1.dirty_work(inputfilename, outputfilename)
pipelineoutput = open(outputfilename2, 'w')
piplup = simClass(instruction, opList, dataList, validi, address, firstArg, secondArg, thirdArg, numInstrs,
destReg, src1Reg, src2Reg, iName, pipelineoutput)
piplup.run()
