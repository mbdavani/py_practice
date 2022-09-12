## The first two lines are negligable
a = 9119
z = str()




def square_digits(num):
    num = [int(x) for x in str(num)]
    z = str()

    for i in num:
        b = int(i*i)
        z += str(b)    


    q = ''.join( _ for _ in z)
#    print(q)
    return int(q)

q = square_digits(a)
print(q)