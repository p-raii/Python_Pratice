import re
file=open('pythonhw.txt')
sum=0
for line in file:
    line =line.rstrip()
    x= re.findall('[0-9]+',line)
    for i in x:
        y= int(i)
        sum = sum + y
print(sum)
