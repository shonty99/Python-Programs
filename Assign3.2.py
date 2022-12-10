#Accepts Number from user and print  Factors of that number

#Business Logic
def Factors(No):
    for i in range(1,No,1):
        if(No%i==0):
            print(i,end=" ")

#Main Function
def main():
    print("Enter the Number :")
    Num = int(input())

    Factors(Num)

if __name__ == "__main__":
    main()

"""
Input - 24
Output - 1 2 3 4 6 8 12 
"""