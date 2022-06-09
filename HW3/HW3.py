dic = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def radix_to_radix(n, radix1, radix2):
    nToDec = 0
    idx = len(n) - 1
    for i in n:
        nToDec += int(i) * (radix1 ** idx)
        idx -= 1

    quotient, remainder = nToDec // radix2, nToDec % radix2

    result = []

    while quotient != 0:
        result.append(dic[remainder])
        quotient, remainder = quotient // radix2, quotient % radix2
    result.append(dic[remainder])
    result = list(reversed(result))
    return ''.join(result)

        

print("Enter a number : ",end="")
num = input().rstrip()
print("Enter a radix1, radix2: ",end="")
radix1, radix2 = map(int,input().split())

if num[0] != '-' and 2 <= radix1 <= 16 and 2 <= radix2 <= 16:
    result = radix_to_radix(num,radix1,radix2)
    print("[radix_to_radix] %s in based %d is %s in base %d" %(num,radix1,result,radix2))
else:
    print("Wrong Input !!!")