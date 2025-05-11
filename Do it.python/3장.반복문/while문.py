#10번찍어 나무 넘어뜨리기기
treeHit=0
while treeHit <10:
    treeHit=treeHit+1
    print(f'나무를 {treeHit}번 찍었습니다.')
    if treeHit==10:     #treeHit=10 은 같다라고 표현하는게 아니라 변수를 만들어주는 표현이다. ~와 같다의 표현은 == 사용해야 한다
        print('나무가 넘어갔습니다')

prompt='''
1.Add
2.Del
3.List
4.tuple

Enter number= '''
number=0
while number !=4:
    print(prompt)
    number=int(input())
    if number==4:
        print('정답입니다')

#무한 루프에서 빠져나가려면 <Ctrl+C>
