a = list(map(int,input().split()))
number = 0
for digit in a:
    number = number * 10 + digit
if(number%3=='0'):
    print(1)
else:
    print(0)
