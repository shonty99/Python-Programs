#Accept N number from user and display numbers which are divsible by 5

#Business logic
def Div(Brr,n):
    for i in range(0,n):
        if(Brr[i]%5==0):
            print(Brr[i])

#Main function
def main():
    Arr = []
    print("Please enter the size :")
    N = int(input())

    print("Enter the Elements :")
    for i in range(0,N,1):
        ele = int(input())
        Arr.append(ele)

    Div(Arr,N)
    

if __name__ == "__main__":
    main()



