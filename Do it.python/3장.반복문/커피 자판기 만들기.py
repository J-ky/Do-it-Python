#while 문 커피 자판기 만들기.
coffee=10
while True:
    money=int(input('돈을 넣어 주세요: '))
    if money==300:
        coffee=coffee-1
        print(f'커피 {coffee}잔 남았습니다.')
    elif money>300:
        coffee=coffee-1
        pay=money-300
        print(f'{money}원 받았습니다. {pay}거스름돈 입니다.\n커피 {coffee}잔 남았습니다.')
    else:
        print(f'돈이 부족합니다.\n커피가 {coffee}잔 남았습니다.')
    if coffee==0:
        print('커피가 모두 소진되었습니다.\n마감합니다!!')
        break
