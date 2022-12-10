#Accept number from user and display its factors in decreasing order

#Business Logic
def FactRev(No):
    for i in range(No-1,0,-1):
        if(No%i==0):
            print(i,end=" ")

#Main Function
def main():
    print("Please enter the number:")
    Num = int(input())

    FactRev(Num)

if __name__ == "__main__":
    main()