#Creating two functions to check whether the received values meets the required criteria
def check1():
    while True:
        try:
            n=input("Enter an integer: ")
            if int(n)<0 or int(n)>255:
                print("Please enter value between 0 and 255.")
            else:
                break
        except:
            print("Please enter a whole integer value.")
            pass
    return int(n)

def check2():
    #Different functions were created just to display different queries to the user
    while True:
        try:
            n=input("Enter another integer: ")
            if int(n)<0 or int(n)>255:
                print("Please enter value between 0 and 255.")
            else:
                break
        except:
            print("Please enter a whole integer value.")
            pass
    return int(n)










        

        


    

    
