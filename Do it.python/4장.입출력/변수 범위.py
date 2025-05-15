#변수의 효력 범위
a=1
def vartest(a):
    a=a+1

vartest(a)
print(a)
#내 예상: 2 실제 값:1
#밖에 있는 a와 vartest에 있는 a와 다른 친구임

a=1
def vartest(a):
    a=a+1

print(vartest(3)) #None값 출력: 함수에 return이 없기 때문문
print(a) #1출력

a=1
def vartest(a):
    a=a+1
    return a

a=vartest(a)
print(a)
#vartst(a)에서 a는 밖에 있는 1을 지칭 함수를 실행하면 이 식에서는 return이 있어 2가 리턴받고 다시 변수 a에 값을 담음
#그리고 그 담은 a값을 출력 출력값:2

#sol1) global 명령어(사용 권장X)
a=1
def vartest():
    global a
    a=a+1

vartest()
print(a)

#sol2) 그냥 변수이름을 다르게 사용하면 헷갈리지 않고 사용가능.
