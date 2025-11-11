f=open('input2.txt','r')
text=f.read()
f.close()

words=text.split()
print('단어의 개수:',len(words))