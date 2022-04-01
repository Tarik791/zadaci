# Python program to print numbers from 1 to n

n = int(input("Unesite bilo koji broj: "))

print("Lista prirodnih brojeva iz 1", "do", n)

for i in range(1, n + 1):
    print(i, end='  ')