print("We are going to write a loop that calculates the sume of 1/30 + 2/29 + 3/28 + ... + 30/1")
sum = 0
for i in range(1, 31):
    sum += i / (31 - i)
    print(sum)
print("The sum is", sum)