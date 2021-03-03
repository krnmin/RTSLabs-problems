#array = [1,5,2,1,10]
array = [int(num) for num in input("Enter numbers separated by spaces to create array\n").split()]  # userinput array
target = int(input("What is the target number?\n")) # userinput for the target number
#initializing variables for below and above counts
above = 0   
below = 0
# looping around the user given array to start counting how many is above or below
for x in array:
    if x > target:
        above = above +1
    if x < target:
        below = below +1
print('above = {:d}, below = {:d}'.format(above,below)) # python print format
