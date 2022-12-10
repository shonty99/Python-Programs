
"""
/////////////////////////////////////////////////////////////////////
//
//  Function Name:  Div
//  Description :      Used to perform Division of 2 numbers
//  Input :              Integer, Integer
//  Output :            Integer
//  Date :               03/12/2022
//  Author :            Shantanu Vijaykumar Sawalkar
//
/////////////////////////////////////////////////////////////////////
"""
def Div(Num1,Num2):
    Division = 0
    Division = Num1 / Num2
    return Division

"""
/////////////////////////////////////////////////////////////////////
// Write a program to perform Division of 2 numbers
/////////////////////////////////////////////////////////////////////
"""

def main():

    print("Enter the First Number: ")
    No1 = int(input())
    print("Enter the Second Number: ")
    No2 = int(input())

    Result = Div(No1,No2)
    print("Division Of Two numbers are :",Result)

if __name__ == "__main__":
    main()

"""
/////////////////////////////////////////////////////////////////////
//
//  Input :         30      10
//  Output :       3.0
//
/////////////////////////////////////////////////////////////////////
"""