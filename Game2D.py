# 1  1  1  X  1  1  1
# 1  1  X  X  1  1  1
# 1  X  X  X  X  X  X
# X  X  X  X  X  X  1
# X  X  X  X  X  1  1
# X  X  X  X  1  1  1

# Enter your code here:

nOfValues = int(input()) 
sum = 0 
count = 0 

for i in range(nOfValues):
    number = int(input())
    sum = sum + number
    count = count + 1 
calAverage = sum / count

good = calAverage >= 80 and calAverage <= 100 
middle = calAverage >= 50 and calAverage < 80 
low = calAverage >= 0 and calAverage < 50

if good:
    print('GOOD') 
elif middle:
    print('MIDDLE') 
elif low:
    print('LOW') 
else:
    print('ERROR')