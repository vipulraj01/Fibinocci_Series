last_number = int(input("number of terms : "))
a = 0
b = 1
sums = 0
while sums < last_number:
    print(a)
    nth = a + b
    a = b
    b = nth
    sums += 1