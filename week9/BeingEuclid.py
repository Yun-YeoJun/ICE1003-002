a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

def is_triangle(a,b,c):
    if (a >= b + c) or (b >= c + a) or (c >= a + b):
        return False
    else:
        return True

if is_triangle(a,b,c):
    print("YES")
else:
    print("NO")