#Creating a function to convert  whole integers into binaries
def changeToBinary(x):
    binaries=""
    while x!=0:
        y=x%2
        x=int(x/2)
        binaries=str(y)+binaries     
    l=8-len(binaries)    
    for i in range(l):
        binaries="0"+binaries
    return binaries



