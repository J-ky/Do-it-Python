f=open('새파일.txt','w')#위치 지정을 하지 않으면 명령한 위치에서 파일이 생성된다. 
f.close

f=open('c:/python/Github sum/연습장.txt','w')
for i in range(1,11):
    data=f'{i}번째 줄 입니다.\n'    #'%s번째 줄입니다.\n'%i
    f.write(data)
f.close

#readline 함수: 한 줄씩 가져오는 것.
f=open('c:/python/Github sum/연습장.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close

#readlines 함수 : 한번에 다 가져오는 것.
f=open('c:/python/Github sum/연습장.txt','r')
lines=f.readlines()
for line in lines:
    print(line)
f.close

#줄 바꿈 문자 없애기.
f=open('c:/python/Github sum/연습장.txt','r')
lines=f.readlines()
for line in lines:
    line=line.replace('\n','')  #line=line.strip()   
    print(line)
f.close

#read : 파일 전체 가져오기.
f=open('c:/python/Github sum/연습장.txt','r')
data=f.read()
print(data)
f.close

#'a' : 새로운 내용 추가하기.(원래 덮어 씌우게 되면 기존의 기록은 삭제 되지만 'a'를 쓰면 추가가 된다.)
f=open('c:/python/Github sum/연습장.txt','a')
for i in range(11,21):
    data=f'{i}번째 줄 추가\n'
    f.write(data)
f.close

#with문 : open을 해주면 항상 close를 해주어야 하는데 with문을 사용 하면 자동으로 닫힌다. 
with open('c:/python/Github sum/연습장.txt','r')as f:
    data=f.read()
    print(data)
