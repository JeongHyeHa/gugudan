#사용자가 입력한 값 검토: 1보다 큰 정수(o)
def input_check(str, max):
    while True:
        user_input = input(f"{str}를 입력하세요(~{max}): ")
        try:
            num = int(user_input)
            if num <= 0:
                print(f"{str}가 1보다 작아서 실행이 불가능합니다.\n")
                continue
            if num>max:
                print(f"값을 초과하셨습니다. 1~{max} 중 원하는 값을 택해주세요.\n")
                continue
            return num
        except ValueError:
            print("잘못된 입력입니다. 양의 10진수 정수를 입력하세요 (예: 1, 2, 3, ...)\n")

            

while True:
    row = input_check("한 행에 출력할 구구단의 개수", 10)
    stage = input_check("최대 출력할 단 수", 1000)

    if row > stage:
        print("최대 출력할 단 수는 한 행에 출력할 개수보다 커야 합니다.")
        print("구구단을 다시 시작합니다.\n")
        continue
    
    for start in range(1, stage+1, row):   
        end = min(start+row, stage+1)
        for i in range(1,10):
            for j in range(start, end):
                print(f"{j} x {i} = {j*i}", end="\t")
            print("")
        print("")
    break



#0일 때
#음수일 때
#실수일 때
#문자일 때
#2진수일 때
#16진수를 넣을 때
#엔터만 눌렀을 때
#입력한 수가 엄청 클 때