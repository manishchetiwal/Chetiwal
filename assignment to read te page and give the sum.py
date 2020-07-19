import re
fhandle = open('new.txt')
content = fhandle.read()
nu = re.findall('[0-9]+', content)
count=0
s=0
for i in nu:
    count+=1
    s=s+ int(i)
    print('count=\n',count,'sum=',s, end='') 

