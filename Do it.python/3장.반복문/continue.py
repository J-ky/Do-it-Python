#while 문 빠져나가지 않고 조건문으로 돌아가기 : continue

#0~10 홀수 출력
a=0
while a<10:
    a=a+1
    if a%2==0:
        continue
    print(a)

#1~10까지 3의 배수를 뺀 나머지 출력
a=0
while a<10:
    a=a+1
    if a%3==0:
        continue
    print(a)
