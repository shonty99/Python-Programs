#Accept Number from user and display its non factors

def NonFact(No):
    for i in range(1,No,1):
        if(No%i!=0):
            print(i,end=" ")

#Main Function
def main():
    Num =int(input("Please Enter the Number :"))

    NonFact(Num)

if __name__ == "__main__":
    main()