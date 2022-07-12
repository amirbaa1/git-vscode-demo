
def is_prime(x, y):
    c=0
    for i in range(x, y+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            if i>1:
                c=i
                display_fristnumber(c)
def display_fristnumber(c):
    print(c)

a=input()
a=int(a)
b=input()
b=int(b)

is_prime(a, b)
