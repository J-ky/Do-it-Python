#if문에서 '조건문'이란 참과 거짓을 판단하는 문장을 말한다. 

#돈이 있으면 택시를 타고 가고, 돈이 없으면 걸어간다. (여기서 조건문은 'money'가 된다. )
money=True
if money:
    print('택시를 타고 가라')
else:
    print('걸어가라.')

#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money=2000  #돈을 2000원 있다고 가정.
if money>=3000:
    print('택시를 타라')
else:
    print('걸어가라')

#돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라. 
money=2000
card=True
if money>=3000 or card:
    print('택시를 타고 가라')
else:
    print('걸어가라')


'not x  :  x가 거짓이면 참이다.'

#만약 주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라.
pocket=['money','card','key']
if 'card' not in pocket:
    print('걸어가라')
else:
    print('버스를 타고 가라')

#주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라. 
pocket=['paper','cell phone']
if 'money' in pocket:
    print('택시를 타라')
elif 'card' in pocket:  #elif card: 도 가능하다.
    print('택시를 타라')
else:                   #마지막은 else로 마무리
    print('걸어가라')

##조건부 표현식  :  (변수=조건문이 참인 경우 if조건문 else조건문이 거짓인 경우)
score=70
if score >=60:
    message='success'
    print(message)
else:
    message='failure'
    print(message)

score=40
message='success' if score>=60 else 'failure'
print(message)

