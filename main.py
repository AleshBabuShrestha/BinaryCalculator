import conversion,greetings,inputValidation
#Importing various secondary modules containing functions to be used in the main module

greetings.initial()
#Calling initial() function present in greetings module

while True:
    m=inputValidation.check1()
    n=inputValidation.check2()
    #Calling check1() and check2() functions present in inputValidation module and storing the values within m and n respectively
    
    num1=""
    num1=conversion.changeToBinary(m)
    num2=""
    num2=conversion.changeToBinary(n)
    #Calling changeToBinary() function present in conversion module to convert m and n into binaries
    
    summation=""
    carryin=0
    for i in range(7,-1,-1):
        p=int(num1[i])
        q=int(num2[i])
        
        summation=str(p^q^carryin)+summation
        #Calculating sum of individual bits
        
        carryin=(carryin&(p^q))|(p&q)
        #Calculating carry in(/out) bit
        
    print("Binary Addition: "+summation)
    #Displaying binary addition of the provided integers
                                
    yn=input("Do you want to re-run the program?(y/n)")
    if yn=="y":
        pass
    elif yn=="n":
            break
    else:
        print("You entered an invalid command. Hence,the program has ended.")
        break
    #Asking user whether to re-run the program or close  it
    
greetings.final()
#Calling final() function present in greetings module
    
        
        

        
        
    
    
