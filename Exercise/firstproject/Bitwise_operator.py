a,b=5,4              #  5=0101;   4=0100
print(a&b)           #0101 & 0100 =0100;  the output is-- 4 (0100)
print(a|b)           #0101 | 0100 =0101;  the output is-- 5 (0101)
print(a^b)           #0101 ^ 0100 =0001;  the output is-- 1 (0001)
print(~a)            # ~5= -(5+1);  the output is= -6
print(~b)            # ~4= -(4+1);  the output is= -5
print(a << 2)        # a<<n=a*2^n; 5*2^2=5*2*2= 20
print(a >> 2)        # a>>n=a/2^n= 5/2*2 =1
print(b << 2)
print(b >> 2)