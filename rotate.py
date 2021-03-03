initString = input("Please enter the initial string\n") # initial string to be rotated
rotate = int(input("How many characters would you like to rotate?\n"))  # number of characters user wants to rotate 
overflow = initString[-rotate:] # finding the characters that will be placed in the beginning of the string
strlen = len(initString)    # obtaining length of string to know where to subtract the inital string
string = initString[:(strlen-rotate)]   # leftover after removing the overflow characters
print(overflow+string)  # placing the overflow characters in the beginning of the string followed by the non-overflowed characters 
