'''
There are 3 functions: inv, and2 or2 which are equivalent to bitwise operators "NOT", "AND", and "OR". The functions are applied to given inputs resulting an output.
The program has two input files:
input.txt: Contains a seried of input variables. Each input is a list of binary values. Each line contains one input.

circuit.txt: Contains a series of defined funtions. In each line one function (operator) is applied to two operands.

The program is should implement the functions existed in circuit.txt and show the function output in the stdoutput.
Pseudocode:
1- Open input file.
2- Read each line of the file and add the line to the inputDic dictionary: {inputName: valueList}
3- Open the function (circute) file
4- Read each line of the file and add the function defined in each line to the circDic dictionary: { outputName : function(operand 1, operand 2) }
5- while (circDic.keys() != outputDic.keys()) do the following in a recursive loop
6- For each key (output) in the circDic dictionary, call the method operatorExecuter() to implement the function related to that key.
    6.1- Find the equivalend bitwise operator of the function (method executer())
    6.2- If operand is a key in the inputDic, then: Add inputDic[operand] to operandVals list: (operandVals.append(inputDic[operand])).
    6.3- Otherwise if the oeprand is a key in circDic, then: check if the value of this key is calculated (check if this key exists in outputDic)?
    6.4- If the key is in outputDic.keys(): add its value (outputDic[operand]) to operandVals list (operandVals.append(outputDic[operand]))
    6.5- If the operand is neither a given input nor is it in the outputDic dictionary: return an empty list as the value list of this operand (operandVals.append([]))
    6.6- Extract the operands list
    6.7- If any item in operandVals[] list is an empty list (len(item) == 0), it means there is no value defined for that operand and the bitwise peration cannot be implemented on this operand, therefore return an empty list as the result of operation execution: result = []
    6.8- Otherwise execute the operators on valid operands: result = executer(operand, opernadVal1, opernadVal2) and add the result to outputDic dictionary: outputDic[key] = output
7- Show each key and its value into the stdoutPut.

'''
import argparse
import sys

class SimulateLogic:
    def __init__(self, inputFile, functionFile):
        print("inside init: ")
        self.inFile = inputFile
        self.funcFile = functionFile
        print("inside init: ", self.inFile + " " + self.funcFile)
        self.inputDic = {}
        self.circDic = {}
        
    
    '''
    simulate(): The main function in which reads the input files and executes the functions given in the circuit.txt file.
    Output:
        outputDic: A dictionary of output function names as keys and the a list containgn the result of the function execution as he value of the key
    '''
    def simulate(self):
        self.readFile(self.inFile, self.inputDic)
        self.readFile(self.funcFile, self.circDic)
        print(f'Dic of input operands: {self.inputDic}')
        print(f'Dic of circuit file: {self.circDic}')
        
        outputDic = {}
        outputDic = self.circuitImple(outputDic)
        return outputDic
        #print (f'final result is: {outputDic}')
    
    '''
    readFile(): read the input file and put the lines in its relevant dictionary
    Inputs:
        fileName: A text file to read its content
        dicName: A dictinary to add the file content into it
    Output:
        None
    '''
    def readFile(self, fileName, dicName):
        try:
            with open(fileName, 'r') as f:
                for line in f:
                    key = line.split("=")[0].strip()
                    dicName[key] = line.split("=")[1].strip()
                    
        except FileNotFoundError:
            print('File is not accessible.')
            

    '''
    circuitImple(): Implements the function given in the circuite.txt file and retunrs the output results.
                    The method executes recursively till all the functions (keys in the circDic) is executed.
    Input: outputDic: An empty dictionary which is filled when ever a function of the circDic dictionary is implemented.
    Output: outputDic: The input dictionary containing all the functions execution results.
    '''
    def circuitImple(self, outputDic):
        if self.circDic.keys() == outputDic.keys():
            return outputDic
            
        result = []
        for key in self.circDic:
            print(f'key is: {key}')
            result = self.operatorExecuter(self.circDic[key], outputDic)
            if len(result) > 0:
                outputDic[key] = str(result)
            print (f'outputDic is: {outputDic}')
        return self.circuitImple(outputDic)


    '''
    operatorExecuter(): Executes a function(operator) provided in circuit.txt file
    Input:
        function: function to execute
        funcResultsDic: This is the output result dictinary. It contains the name of each function as key and the result of the execution of that function as value.
    Output:
        result of the executed function.
    '''
    def operatorExecuter(self, function, funcResultsDic):
        funcName = function.split("(")[0]
        print(f'function Name: {funcName}')
        operands = function.split("(")[1][:-1]
        print(f'operands are: {operands}. Extract operands values...')

        operandVals = self.extractOpernadsVal(operands, funcResultsDic)  #extract list of operand values
        print(f'list of operand values: {operandVals}')
        for valList in operandVals:
            if len(valList) == 0:   #operand has no value to be used in function execution ===> return an emply list as the result of operator exexuter
                print(f'operand has not value: return an empty list as result of operatorExecuter()')
                return []

        result = self.executer(funcName, operandVals)
        return result


    '''
    executer(): Selects which bitwise operator to execute and executes the selected one.
    Input:
        funcName: A string stating the name of the function as it is stated in circuit.txt file
        operands: A list of string lists: each inner list is an input argument of the function to be implemented
    Output:
        result: A list as the result of the bitwise operator execution
    '''
    def executer(self, funcName, operands):
        print(f'execute function {funcName} on operands {operands}')
        if funcName.lower() == "inv":
            result = self.invert(operands)

        elif funcName.lower() == "and2":
            result = self.bitwiseAnd(operands)

        elif funcName.lower() == "or2":
            result = self.bitwiseOr(operands)

        return result
    
    '''
    invert(): Implements bitwise inversion.
    Input:
        operands: A list of string lists: each inner list is an operand to be inverted
        
    Output:
        invertedList: The inverted operand list
    '''
    def invert(self, operands):
        invertedList = []
        #check if item is a string or an integer?
        print(f'operands list is: {operands}')
        for item in operands:
            print(f'item is: {item}')
            for value in item[1:-1].split(","):
                if int(value) == 0:
                    invertedList.append(1)
                    
                else:
                    invertedList.append(0)
        print(f'invert result: {invertedList}')
        return invertedList
            
    
    
    '''
    bitwiseAnd(): Implements bitwise AND (&).
    Input:
        operands: A list of string lists: each inner list is an operand.
        
    Output:
        invertedList: The result of bitwise AND on the input operands
    '''
    def bitwiseAnd(self, operands):
        bitwiseAnd = []
        firstOperand = operands[0][1:-1].split(",")
        secondOperand = operands[1][1:-1].split(",")
        
        for i in range(len(firstOperand)):
            bitwiseAnd.append(int(firstOperand[i]) & int(secondOperand[i]))
            
        print(f'firstOperand: {firstOperand}, secondOperand: {secondOperand}, bitwiseAnd: {bitwiseAnd}')
        return bitwiseAnd
   
   
    '''
    bitwiseOr(): Implements bitwise OR (|).
    Input:
        operands: A list of string lists: each inner list is an operand.
        
    Output:
        invertedList: The result of bitwise OR on the input operands
    '''
    def bitwiseOr(self, operands):
        bitwiseOr = []
        firstOperand = operands[0][1:-1].split(",")
        secondOperand = operands[1][1:-1].split(",")

        for i in range(len(firstOperand)):
            bitwiseOr.append(int(firstOperand[i]) | int(secondOperand[i]))
            
        print(f'firstOperand: {firstOperand}, secondOperand: {secondOperand}, bitwiseOr: {bitwiseOr}')
        return bitwiseOr
        

    '''
    extractOpernadsVal(): Extracs the values of the operands
    Input:
        operands: A sting containing the name of the operands
        funcResultsDic: This is the output result dictinary. It contains the name of each function as key and the result of the execution of that function as value.
    Output:
        operandVals list: Each item of the list is a list of 0 and 1: item = [1, 0, 1]
    '''
    def extractOpernadsVal(self, operands, funcResultsDic):
        operandVals = []
        for item in operands.split(","):
            item = item.strip()
            
            if item in self.inputDic.keys(): #operand is an input given in input file
                print(f'Operand is an input given in input file: Add the given input to operandVals list...')
                operandVals.append(self.inputDic[item])

            elif item in self.circDic.keys():    #operand is also an output of the system
                #print("Check keys in circDic...")
                if item in funcResultsDic.keys():    #the value of this output is already calculated ===> return its value
                    print(f'Operand is an already calculated output: Add  its value to operandVals list...')
                    operandVals.append(funcResultsDic[item])
                
                else:   #operand is an output of the system in which its value is not yet calculated ===> return an empty list
                    #print("just add an empty list...")
                    print(f'Operand is an un executed output: Add  empty list to operandVals list...')
                    operandVals.append([])

        return operandVals
#
        
def main():
    args = sys.argv[1:]
    try:
        if not args:
            print('inputFile and circuitFile are not provided')
    
        if args[0] == '-h':
            print(f'Run this command: python[versin] file.py input.txt circuit.txt')
            sys.exit(1)
            
        if len(args) < 2 and args[0] != '-h':
            print('2 files is needed as input...')
            sys.exit(1)
    
        inputFile = args[0]
        
        circuitFile = args[1]
        
        simulator = SimulateLogic(inputFile, circuitFile)
        finalResult = simulator.simulate()
        for key in finalResult:
            print(f'{key}: {finalResult[key]}')
        
    except IndexError:
        print('Run [-h] to see an example')
        sys.exit(1)
    
    
if __name__ == '__main__':
    main()


