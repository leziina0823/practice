f=open('input4.txt','r')
total=0
for line in f:
    num=int(line.strip())
    total += num
f.close()
print('합계:',total)