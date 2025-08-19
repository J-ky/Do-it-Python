#포매팅 (d: 숫자만, s: 숫자, 문자 둘다 가능)
#                                       (d는 int를 받는 인자이기 때문에 float을 주면 Error가 뜬다.)
a='I eate %d apples.'%3
print(a)

b='I eate %s apples.' %'Three'
print(b)

c='I ate {0}apples. so I was sick for {day} days.' .format('five',day=3)
print(c)

#Error : 'I ate {0}apples. so I was sick for {day} days.' .format(0='five',day=3)
#                                                               .format은 위치 인자와 키워드 인자를 받는 방식이 있는데 0,1..과 같이 숫자들은 위치 인자로 인식
#                                                                그래서 키워드 인자를 받는 방식으로 받아버리면 오류가 난다. 

#f문자열 포맷팅
name='Python'
print(f'{{Hello,{name}}}')

print(f'Hello,{{{name}}}')

nick='홍길동'
age=15
print(f'나의 이름은 {nick}입니다. 나이는 {age}입니다.')

#format 함수 또는 f열 문자열 포매팅을 사용해 !!!python!!! 문자열을 출력하라.    
#                                                                       f'{A:표현}' > A를 표현해라.
print(f'{"python":!^12}')
