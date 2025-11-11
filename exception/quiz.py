try:
    name=input('열 파일 이름을 입력하세요: ')
    f=open(name,'r')
    text=f.read()
    print(text)
    f.close()
except FileNotFoundError:
    print('진짜진짜 중요한 파일 이름 잘못 씀')
    