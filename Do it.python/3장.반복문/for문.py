#while은 무한 반복. for는 뭔가를 뽑아서 반복한다. 라는 느낌


#.총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 
a=[90,25,67,45,80]
number=0
for i in a:
    if i>=60:
        number=number+1
        print(f'{number}번 학생 합격')
    else:
        number=number+1
        print(f'{number}번 학생 불합격')

#합격통보 학생의 번호를 range를 사용하여 표현하기.
a=[90,25,67,45,80]
for number in range(len(a)):        #len(a)=5,range(5):0~4를 지칭한다. =>각 숫자에 넘버를 부여함.
    if a[number]<=60:                                                #=>인덱싱을 통해서 숫자를 가져와서 if 사용.
        continue
    print(f'{number+1}번 학생 합격입니다.')

##for와 rnage를 이용한 구구단.
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')  #print는 기본적으로 enter이 들어가 있는데 end=''이게 enter을 지워주는 역할(쭉 enter없이 값을 출력력)
    print('')                #한 줄이 끝나면(2단이 끝나면) enter을 삽입 시켜서 출력한다. 

#평균점수 구하기. for문을 이용해서 평균구하기 and range를 이용해서 평균보다 낮은 친구들에게 문자 보내기.
a=[70,60,55,75,95,90,80,80,85,100]
add=0
for i in a:
    add=i+add
aver= add/len(a)
for y in range(len(a)):
    num=y+1
    if a[y]<aver:
        print(f'{num}번 학생 평균보다 낮습니다.')
