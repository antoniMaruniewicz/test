import sys
i = 0
j = 1
k = 0
fib = 0
print("Zmiana2")
print("print-function")
number = int(input("Hown many numbers do you want to display?"))
print("Fibonnaci sequance:")
while(i < number):
    print(fib)
    fib = j + k
    j = k
    k = fib
    i += 1
    # to do: format 
