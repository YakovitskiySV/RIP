from math import sqrt
import sys
    
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
        
except:
    print('Bad arguments, try to input them again\n')
        
    try:
        if len(sys.argv) == 1:
            a = float(input('input a: '))
            b = float(input('input b: '))
            c = float(input('input c: '))
            
        if len(sys.argv) == 2:
            a = float(sys.argv[1])
            b = float(input('input b: '))
            c = float(input('input c: '))
            
        if len(sys.argv) == 3:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(input('input c: '))
            
    except:
        print("clown\n")
        exit()

if a == 0 and b == 0 and c == 0:
    print("Infinite number of solutions\n")
    exit()

d = b*b - 4 * a * c

if d < 0:
    print("The discriminant is: %s\nThis equation has no solutions" %d)
    
elif a != 0: 
    x1 = (-b + sqrt(d) / (2*a))
    x2 = (-b - sqrt(d) / (2*a))
    
    if x1 >= 0 or x2 >= 0:
        print("Solution:")
        
    else:
        print("There is no solution for this equation")
    
    if x1 >= 0:
        x11 = sqrt(x1)
        x12 = -sqrt(x1)
        print("%s, %s" %(x11, x12))
        
    if x2 >= 0: 
        x21 = sqrt(x2)
        x22 = -sqrt(x2)
        print("%s, %s\n" %(x21, x22))

else:
    try:
        x11 = sqrt(-c/b)
        x12 = -sqrt(-c/b)
        print("Solution:\n%s, %s\n" %(x11, x12))
        
    except:
        print("There is no solution for this equation")