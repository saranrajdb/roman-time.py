n=int(input())
v = [1000,900,500,400,100,90, 50,40,10, 9, 5, 4, 1] 
s= ["M","CM","D","CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
r=""
i=0
while n > 0:
    for a in range(n//v[i]): 
        r+=s[i]
        n-=v[i]
    i+=1
print(r)
