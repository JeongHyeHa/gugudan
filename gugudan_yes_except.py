while True:
    user_row = input("한 행에 출력할 구구단의 개수를 입력하세요: ")
    user_stage = input("최대 출력할 단 수를 입력하세요: ")

    try: 
        row = int(user_row) 
        stage = int(user_stage)

        if row < 1:
            print("한 행에 출력할 구구단의 개수가 1보다 작아서 실행이 불가능합니다.\n")
            continue
        elif stage < 1:
            print("최대 출력할 단 수가 1보다 작아서 실행이 불가능합니다.\n")
            continue
        elif row > stage:
            print("최대 출력할 단 수는 한 행에 출력할 개수보다 커야 합니다.\n")
            continue
        
        print(f"{stage}단까지 구구단을 {row}개씩 한 행에 출력합니다:\n")
        n = (stage + row - 1) // row  # stage를 row로 나눈 후 올림 계산

        for start in range(1, stage+1, row):   
            end = min(start+row, stage+1)
            for i in range(1,10):
                for j in range(start, end):
                    print(f"{j} x {i} = {j*i:2}", end="\t")
                print("")
            print("")
        break

    except ValueError:
        print("유효한 숫자를 입력해주세요.\n")
