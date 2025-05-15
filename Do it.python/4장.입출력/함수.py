#매개변수:parameter,인수:arguments

#여러 개의 입력값을 모두 더하는 함수 만들기1
def add_many(*args):
    result=0
    for i in args:
        result=i+result
    return result

#여러 개의 입력값을 모두 더하는 함수 만들기2
def add_mul(choice,*args):
    if choice=="add":
        result=0
        for i in args:
            result=i+result
        return result
    elif choice=='mul':
        result=1
        for i in args:
            result=i*result
        return result
    
print(add_mul('add',2,3,4))
print(add_mul('mul',2,3,4))

#kwargs매개변수> 모든 매개변수 kwrags는 dictionary로 저장이 된다. 
def print_kwargs(**kwargs):
    print(kwargs)

###
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Unknown')
        self.age = kwargs.get('age', 0)

person = Person(name="Hong", age=25)
print(person.name)  # Hong
print(person.age)   # 25
###

#리턴값은 하나이다. 
def add_mul(a,b):
    return a+b,a*b

a=add_mul(2,3)
print(a)
print(add_mul(2,3))
#>(5, 6)

#분리해서 리턴값을 보고 싶다.
return1,return2=add_mul(2,3)
print(return1)
print(return2)

#매개변수에 초기값 설정(*순서를 잘 지켜주어야 함. 초기화하고 싶은 매개변수는 항상 뒤에 존재해야 한다.*)
def say_myself(name,age,man=True):
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}입니다.')
    if man:
        print('나는 남자입니다.')
    else:
        print('나는 여자입니다.')
    

say_myself('정근','25',True)
