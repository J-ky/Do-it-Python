#외부 모듈을 끌어다가 사용하는 것.
import sys

args=sys.argv[1:]
for i in args:
    print(i)

#위를 실행하려면 TERMIMAL에서 이 파일 위치로 들어가야 함 cd '파일명'
                                                # cd .. : 후진
                                                # 그리고 python .\파일명 인수.. : 숫자는 파일명부터 0으로 센다.
