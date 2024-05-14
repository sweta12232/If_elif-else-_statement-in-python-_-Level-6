# Nested loop means a loop statement inside another loop statement.

def prime(a):
    for j in range(1, 100):
        for i in range(2,j):
            if j % i == 0:
                print("It is not prime ")
            break
    else:
        print("It is a prime number")

prime(7)
            
