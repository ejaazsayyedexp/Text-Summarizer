import sys
n=10
result=1
if(n%2==0):
    for i in range((n//2)-1):
        result*=3
else:
    for i in range(n//2):
        result*=2
print(result)
sys.stdout.flush()