# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

# Expected Output

# * * * * *  
# * * * *  
# * * *  
# * *  
# *

#Create a loop for the column pattern
for column in range(5):
#Create a loop for the row pattern
    for row in range(column + 1, 5):
#Print the output of row through asterisks
        print("*", end = " ")
#Print the output of column through asterisks
    print("*")

