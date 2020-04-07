# serial number of starts per row, i;e 1,2,3,4,5 etc..
""" here i loop for no of rows and j loop is for each row printing"""

t = int(input("enter the no of line/rows -) "))

for i in range(1, t+1):
    for j in range(1, i+1):
        print("*", end=" ")

    print()

