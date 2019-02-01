
import sys
import datetime



# returns -1 if inNum not in fib sequence, 
# otherwise returns position in sequence
def fibPos(inNum):
    # check for first few numbers
    if inNum <0:
        return -1
    if inNum ==0:
        return 1
    if inNum ==1:
        return 2
    # set variable initial values
    first=0
    second=1
    nex=1
    count = 3
    # keep calculating higher fib numbers until we are at or over inNum
    while nex <= inNum:
        ans=second+nex
        first = second
        second = nex
        nex = ans
        count = count +1
        # found it
        if nex == inNum:
            return count
    # didn't find it
    else:
        return -1



# calculates fib numbers up to inNum
def calcFibNums(inNum):
    # array holding fib values & append new values to it 
    # until we are over provided number
    ans = [0,1]
    nex = ans[-1] + ans[-2]
    while nex<=inNum:
        ans.append(nex)
        nex = ans[-1] + ans[-2]
    return ans



def main():
    print ("Hello World: Current time:",datetime.datetime.now())

    # take input from command line for number to check, checks if integer number
    try:
        inNum = int(sys.argv[1])
    except:
        print ("please provide integer number for calculation") 
        print ("Goodnight World: Current time:",datetime.datetime.now())
        exit(0)
        
    # find position of fib number in sequence (if in) and calculate fib numbers up to specified limit
    pos=fibPos(inNum)
    fibArray = calcFibNums(inNum)
    
    # print results
    print ("Fibonacci numbers up to the number provided - \n",fibArray)
    
    if pos > 0:
        print ("Position of given number in the fibbonacci sequence is ",pos,".")
    else:
        print ("Given number not in fibbonacci sequence.")

    print ("Goodnight World: Current time:",datetime.datetime.now())



if __name__ == '__main__':
    main()
