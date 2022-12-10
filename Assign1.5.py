#Program to take input number from user and print that number of *
#Business Logic
def Accept(Num):
    for i in range(0,Num,1):
        print("*")

#Main Function
def main():
    print("Enter the number :")
    No = int(input())

    Accept(No)

if __name__ == "__main__":
    main()

"""
Input -  5
Output - 
*
*
*
*
*
"""