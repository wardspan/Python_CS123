print("The command print “###” prints the sequence of hash symbols once. Use the loop to print this “###” five times.")
for j in range(5):
    print("###")

print("Print a patterns using the while loop")
i = 1
while i < 6:
    print("#" * i)
    i += 1

print('Print a reverse pattern using a while loop.')
k = 1
while k < 6:
    print("#" * (6 - k))
    k += 1
    
print("Please input 5 test scores and we will calculate the average.")
total = 0
counter = 1

while (counter <=5):
    input1 = int(input("Enter test score: "))
    total = total + input1
    average = total / counter
    print("Score: ", input1, '\t', "Total:", total, '\t', "Average:", average, '\t', "Counter:", counter )
    counter = counter + 1
