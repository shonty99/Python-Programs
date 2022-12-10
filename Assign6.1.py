#Accept a number and display its digits  in reverse order

#Business Logic
def Display(No):
   
    while(No>1):
        iDigit = No % 10
        No = No//10 
        print(iDigit)

#Main Function
def main():
    print("Please Enter the number :")
    Num = int(input())

    Display(Num)

if __name__ == "__main__":
    main()

"""
Input - 6921
Output - 
1
2
6
9

"""