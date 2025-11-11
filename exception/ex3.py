#1
scr=open('input3.txt','r',encoding='utf-8')
#2
dst=open('copy.txt','w',encoding='utf-8')
#3
for line in src:
    dst.write(line)
src.close()
dst.close()
print('파일 복사가 완료되었습니다.')
