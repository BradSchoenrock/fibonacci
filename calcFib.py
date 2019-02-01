
import sys
import datetime



# calculates first inNum fib numbers
# returns [0,1] for integers <=1
def calcFibNums(inNum):
    ans = [0,1]
    if inNum ==0:
        return []
    elif inNum ==1:
        return [0]
    nex = ans[-1] + ans[-2]
    for i in range(2,inNum):
        ans.append(nex)
        nex = ans[-1] + ans[-2]
    return ans



def main():
    print ("Hello World: Current time:",datetime.datetime.now())

    # take input from command line for number to check, checks if integer number
    try:
        inNum = int(sys.argv[1])           
    except:
        print ("please provide positive integer number for calculation") 
        print ("Goodnight World: Current time:",datetime.datetime.now())
        exit(0)
    # check if number provided is positive
    if inNum < 0:
        print ("please provide positive integer number for calculation") 
        print ("Goodnight World: Current time:",datetime.datetime.now())
        exit(0)

    # calculate first inNum fib numbers
    fibArray = calcFibNums(inNum)
    
    # print results
    if inNum ==0:
        print ("Don't ask for zero entries of the fibonacci sequence. Smartass...")
    elif inNum ==1:
        print ("First fibonacci number is 0 - \n")
    elif inNum > 1:
        print ("First",inNum,"fibonacci numbers - \n",fibArray)

    print ("Goodnight World: Current time:",datetime.datetime.now())



if __name__ == '__main__':
    main()
