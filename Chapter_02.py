

#헷갈리는 것 정리


#포멧코드에서의 정렬
#'%표현'% a  :  a를 표현해줘
print('%0.4f'% 3.1324345)   #%0.4는 칸 제한 없이 소수점 4자리까지 표현을 뜻한다. 0이 칸 제한 없음을 뜻 함. 만약 10.4라고 하면 
                            #10내에 오른쪽을 기준으로 소수점 4자리까지 표현을 한다.

print('%10.4f'%3.1324345)   #    3.1324
print('{0:>10.4f}'.format(3.1324345))
print(f'{3.1324345:>10.4f}')


#dictionary에서 get 함수  :  없는 값을 내가 원하는 값으로 출력 가능하게 하는 기능을 만들 수 있다. 

a={'name':'Hong','num':2020}
print(a.get('car'))#None
print(a.get('car','no key'))#no key



#주소
a=[1,2,3]
b=a
a[1]=4
print(b)  #[1, 4, 3]
#a와 b의 주소가 동일 하기 때문에 a메모리를 변경을 해도 b의 메모리도 같이 변경 된다. 
#주소가 다른 경우
s1=[1,2,3]
s2=s1[:]
s1[1]=4
print(s1)  #[1, 4, 3]
print(s2)  #[1, 2, 3]
#s2는 s1의 메모리를 인덱싱하여 가져온 거기 때문에 새로운 주소를 받은 새로운 메모리로 취급되어서 s1=s2(X)이다. 


#[1,3,5,4,2]리스트를 [5,4,3,2,1]로 만들어 보자.
a=[1,3,5,4,2]
b=list(set(a))
print(b)
#c=b.reverse()
#print(c)            #이렇게하면 .reverse는 리턴 값이 없기때문에 c는 None값을 받아서 None이 출력된다.
b.reverse()
print(b) 


#['Life','is','too','short']를 Life is too short의 문자열로 바꾸기(.join에 대한 이해 부족.)
a=['Life','is','too','short']
result=' '.join(a)
print(result)
#'(결합 문자)'.join(변수)
